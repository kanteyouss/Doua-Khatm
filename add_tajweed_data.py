import json, re

# Tajweed rules generator for each of the 30 days
tajweed_data = {
    1: [
        {"rule": "Ghunnah Complète (غُنَّة مُشَدَّدَة)", "letters": "اللَّهُمَّ (مّ)", "count": "2 temps", "desc": "Nasalisation obligatoire de 2 temps sur le Mīm avec Chaddah."},
        {"rule": "Madd Tabī'ī (مَدّ طَبِيعِي)", "letters": "ارْحَمْنِي (ـِي)", "count": "2 temps", "desc": "Allongement naturel de 2 temps sur la kasrah du Nūn suivie du Yā sakin."},
        {"rule": "Tafkhīm (تَفْخِيم)", "letters": "بِالقُرْآنِ (ق)", "count": "Emphatique", "desc": "Le Qāf est une lettre emphatique lourde issue du fond de la gorge."}
    ],
    2: [
        {"rule": "Madd Tabī'ī (مَدّ طَبِيعِي)", "letters": "لِي / لَنَا", "count": "2 temps", "desc": "Allongement naturel de 2 temps sur le Yā (ou Alif)."},
        {"rule": "Madd 'Iwad (مَدّ عِوَض)", "letters": "إِمَامًا / نُورًا / هُدًى / رَحْمَةً", "count": "2 temps à l'arrêt", "desc": "Remplacement du double fathah par un alif de 2 temps en cas d'arrêt."},
        {"rule": "Idghām bi-Ghunnah (إِدْغَام بِغُنَّة)", "letters": "إِمَامًا وَنُورًا (ـًا وَ)", "count": "2 temps", "desc": "Fusion du tanwīn dans le Wāw avec nasalisation de 2 temps."}
    ],
    3: [
        {"rule": "Ghunnah Complète (غُنَّة)", "letters": "اللَّهُمَّ (مّ)", "count": "2 temps", "desc": "Nasalisation de 2 temps sur le Mīm."},
        {"rule": "Madd Tabī'ī (مَدّ طَبِيعِي)", "letters": "ذَكِّرْنِي (ـِي)", "count": "2 temps", "desc": "Allongement de 2 temps sur la kasrah du Nūn suivie du Yā."},
        {"rule": "Ikhfā' Haqīqī (إِخْفَاء حَقِيقِي)", "letters": "مِنْهُ (نْـ هـ)", "count": "Izh-hār halqī", "desc": "Le Nūn sakin est prononcé nettement (Izh-hār) car suivi de la lettre de gorge Hā."}
    ],
    4: [
        {"rule": "Madd Tabī'ī (مَدّ طَبِيعِي)", "letters": "وَعَلِّمْنِي (ـِي)", "count": "2 temps", "desc": "Allongement de 2 temps sur la voyelle longue Yā après la kasrah du Nūn."},
        {"rule": "Tafkhīm / Tarqīq", "letters": "جَهِلْتُ", "count": "Légère", "desc": "Le Lām est prononcé avec finesse (Tarqīq)."}
    ],
    5: [
        {"rule": "Qalqalah Sughrā (قَلْقَلَة صُغْرَى)", "letters": "وَارْزُقْنِي (قْ)", "count": "Rebond", "desc": "Léger rebond sur le Qāf en état de sukūn au milieu du mot."},
        {"rule": "Madd Muttasil (مَدّ مُتَّصِل)", "letters": "آنَاءَ", "count": "4 à 5 temps", "desc": "Allongement obligatoire de 4 à 5 temps car la hamzah est dans le même mot que le madd."},
        {"rule": "Madd Tabī'ī (مَدّ طَبِيعِي)", "letters": "النَّهَارِ / تِلَاوَتَهُ", "count": "2 temps", "desc": "Allongement naturel de 2 temps sur le Alif."}
    ],
    6: [
        {"rule": "Idghām bi-Ghunnah (إِدْغَام)", "letters": "حُجَّةً يَا (ـةً يـ)", "count": "2 temps", "desc": "Fusion du tanwīn dans le Yā avec nasalisation de 2 temps."},
        {"rule": "Tafkhīm du Rā (تَفْخِيم)", "letters": "رَبَّ", "count": "Emphatique", "desc": "Le Rā avec fathah est prononcé de manière emphatique et pleine."},
        {"rule": "Madd 'Ārid li-s-Sukūn", "letters": "العَالَمِينَ (ـِينْ)", "count": "2, 4 ou 6 temps", "desc": "Allongement permis de 2, 4 ou 6 temps lors de l'arrêt sur le Nūn final."}
    ],
    7: [
        {"rule": "Ghunnah Complète (غُنَّة)", "letters": "اللَّهُمَّ (مّ)", "count": "2 temps", "desc": "Nasalisation obligatoire de 2 temps sur le Mīm avec Chaddah."},
        {"rule": "Tafkhīm & Ithbāt (تَفْخِيم)", "letters": "أَصْلِحْ (ص)", "count": "Emphatique", "desc": "Le Sād est une lettre emphatique lourde qui conserve son épaisseur."},
        {"rule": "Madd Tabī'ī sur le Nūn (مَدّ طَبِيعِي)", "letters": "دِينِي (ـنِي)", "count": "2 temps obligatoires", "desc": "Le Nūn avec kasrah (نِ) suivi du Yā forme un allongement naturel de 2 temps stricts (ne pas le couper trop court)."},
        {"rule": "Madd Tabī'ī (مَدّ طَبِيعِي)", "letters": "الَّذِي (ـذِي)", "count": "2 temps", "desc": "Allongement de 2 temps sur la lettre Dhāl avec Yā."},
        {"rule": "Tarqīq du Rā (تَرْقِيق)", "letters": "أَمْرِي (رِ)", "count": "Finesse & 2 temps", "desc": "Le Rā porte une kasrah, il est donc prononcé avec finesse (sans emphase), suivi d'un Madd de 2 temps."}
    ],
    8: [
        {"rule": "Madd Tabī'ī (مَدّ)", "letters": "دُنْيَايَ / دُنْيَانَا", "count": "2 temps", "desc": "Allongement naturel sur les Alifs."},
        {"rule": "Izh-hār Mutlaq (إِظْهَار مُطْلَق)", "letters": "دُنْيَا (نْـ يـ)", "count": "Sans ghunnah", "desc": "Exception coranique : le Nūn sakin suivi du Yā dans un même mot se prononce clairement sans fusion."}
    ],
    9: [
        {"rule": "Madd Badal (مَدّ بَدَل)", "letters": "آخِرَتِي (آ)", "count": "2 temps", "desc": "La hamzah précédant le madd s'allonge de 2 temps."},
        {"rule": "Madd Tabī'ī (مَدّ)", "letters": "مَعَادِي", "count": "2 temps + 2 temps", "desc": "Double allongement de 2 temps sur le Alif et sur le Yā."}
    ],
    10: [
        {"rule": "Idghām bi-Ghayri Ghunnah", "letters": "زِيَادَةً لِي (ـةً لِ)", "count": "Fusion nette sans nasalité", "desc": "Le tanwīn se fond entièrement dans le Lām sans traîner de nez."},
        {"rule": "Madd Tabī'ī", "letters": "الحَيَاةَ / لِي", "count": "2 temps", "desc": "Allongement de 2 temps sur le Yā et le Alif."}
    ]
}

# Add default tajweed notes for remaining days
for day_i in range(11, 31):
    tajweed_data[day_i] = [
        {"rule": "Ghunnah (غُنَّة)", "letters": "اللَّهُمَّ / إِنِّي / إِنَّا", "count": "2 temps", "desc": "Nasalisation obligatoire de 2 temps sur le Nūn et Mīm avec Chaddah."},
        {"rule": "Madd Tabī'ī (مَدّ طَبِيعِي)", "letters": "ـِي / ـَا / ـُو", "count": "2 temps", "desc": "Respect strict de l'allongement de 2 temps sur les voyelles longues sans précipitation."},
        {"rule": "Tafkhīm (تَفْخِيم)", "letters": "خ ص ض غ ط ق ظ", "count": "Lettres lourdes", "desc": "Prononciation pleine et emphatique des lettres du groupe 'Khussa Daghtin Qiz'."}
    ]

# Specific overrides
tajweed_data[15] = [
    {"rule": "Izh-hār Halqī (إِظْهَار)", "letters": "عِيشَةً هَنِيَّةً (ـةً هـ)", "count": "Nette sans ghunnah", "desc": "Le tanwīn est prononcé nettement car suivi de la lettre Hā (lettre de gorge)."},
    {"rule": "Ikhfā' Haqīqī (إِخْفَاء)", "letters": "وَمِيتَةً سَوِيَّةً (ـةً سـ)", "count": "2 temps", "desc": "Dissimulation du tanwīn avec nasalisation de 2 temps devant la lettre Sīn."}
]
tajweed_data[16] = [
    {"rule": "Izh-hār Halqī (إِظْهَار)", "letters": "وَمَرَدًّا غَيْرَ (ـًا غـ)", "count": "Prononciation claire", "desc": "Le tanwīn est clair devant la lettre Ghayn."},
    {"rule": "Idghām bi-Ghunnah (إِدْغَام)", "letters": "مُخْزٍ وَلَا (ـٍ وَ)", "count": "2 temps", "desc": "Fusion du tanwīn dans le Wāw avec nasalisation de 2 temps."}
]
tajweed_data[30] = [
    {"rule": "Izh-hār Halqī (إِظْهَار)", "letters": "ذَنْبًا إِلَّا / هَمًّا إِلَّا / دَيْنًا إِلَّا", "count": "Nette", "desc": "Le tanwīn est prononcé clairement devant la Hamzah de 'illā'."},
    {"rule": "Iqlāb (إِقْلَاب)", "letters": "ذَنْبًا (نْـ بـ)", "count": "2 temps", "desc": "Le Nūn sakin suivi du Bā se transforme en Mīm avec ghunnah de 2 temps."},
    {"rule": "Madd Muttasil (مَدّ مُتَّصِل)", "letters": "حَوَائِجِ", "count": "4 à 5 temps", "desc": "Allongement obligatoire de 4 à 5 temps sur le Alif suivi d'une Hamzah dans le même mot."}
]

# Read existing data.js
with open('/home/dev-yokan/doua-khatm-30/data.js', 'r', encoding='utf-8') as f:
    raw = f.read()
    json_str = raw[raw.find('{'):raw.rfind('}')+1]
    data = json.loads(json_str)

# Add tajweed rules to each day
for d in data['days']:
    day_num = d['day']
    d['tajweed_rules'] = tajweed_data.get(day_num, [])

# Write back data.js
with open('/home/dev-yokan/doua-khatm-30/data.js', 'w', encoding='utf-8') as f:
    f.write("window.DOUA_DATA = " + json.dumps(data, ensure_ascii=False, indent=2) + ";\n")

print("data.js successfully updated with Tajweed rules for all 30 days!")
