import json

days = [
    {
        "day": 1,
        "title_fr": "La Miséricorde par le Coran",
        "title_en": "Mercy through the Quran",
        "category": "Miséricorde & Guidance",
        "ar_sing": "اللَّهُمَّ ارْحَمْنِي بِالقُرْآنِ",
        "ar_plur": "اللَّهُمَّ ارْحَمْنَا بِالقُرْآنِ",
        "phon_sing": "Allāhumma-rhamnī bil-Qur'ān",
        "phon_plur": "Allāhumma-rhamnā bil-Qur'ān",
        "fr_sing": "Ô Allah, fais-moi miséricorde par le Coran",
        "fr_plur": "Ô Allah, fais-nous miséricorde par le Coran",
        "en_sing": "O Allah, have mercy upon me through the Quran",
        "en_plur": "O Allah, have mercy upon us through the Quran",
        "vocab": [
            {"ar": "اللَّهُمَّ", "phon": "Allāhumma", "fr": "Ô Allah", "en": "O Allah"},
            {"ar": "ارْحَمْنِي / ارْحَمْنَا", "phon": "irhamnī / irhamnā", "fr": "fais-moi / fais-nous miséricorde", "en": "have mercy on me / us"},
            {"ar": "بِالقُرْآنِ", "phon": "bil-Qur'ān", "fr": "par le Noble Coran", "en": "through the Quran"}
        ],
        "reflection_fr": "Le Coran est une source infinie de miséricorde divine. En demandant la miséricorde par le Coran, on demande qu'il apaise nos cœurs et éclaire notre vie.",
        "reflection_en": "The Quran is an infinite spring of divine mercy. Asking for mercy through the Quran brings peace to the heart and guidance to daily life."
    },
    {
        "day": 2,
        "title_fr": "Un Guide, Lumière et Bénédiction",
        "title_en": "A Guide, Light and Blessing",
        "category": "Miséricorde & Guidance",
        "ar_sing": "وَاجْعَلْهُ لِي إِمَامًا وَنُورًا وَهُدًى وَرَحْمَةً",
        "ar_plur": "وَاجْعَلْهُ لَنَا إِمَامًا وَنُورًا وَهُدًى وَرَحْمَةً",
        "phon_sing": "Wa-j'alhu lī imāman wa nūran wa hudan wa rahmah",
        "phon_plur": "Wa-j'alhu lanā imāman wa nūran wa hudan wa rahmah",
        "fr_sing": "Et fais qu'il soit pour moi un guide (imam), une lumière, une bonne direction et une miséricorde",
        "fr_plur": "Et fais qu'il soit pour nous un guide (imam), une lumière, une bonne direction et une miséricorde",
        "en_sing": "And make it for me a guide (leader), a light, guidance, and mercy",
        "en_plur": "And make it for us a guide (leader), a light, guidance, and mercy",
        "vocab": [
            {"ar": "وَاجْعَلْهُ", "phon": "wa-j'alhu", "fr": "et fais qu'il soit", "en": "and make it"},
            {"ar": "لِي / لَنَا", "phon": "lī / lanā", "fr": "pour moi / pour nous", "en": "for me / for us"},
            {"ar": "إِمَامًا", "phon": "imāman", "fr": "un modèle / un guide", "en": "a leader / guide"},
            {"ar": "وَنُورًا", "phon": "wa nūran", "fr": "et une lumière", "en": "and a light"},
            {"ar": "وَهُدًى", "phon": "wa hudan", "fr": "et une guidée", "en": "and a guidance"},
            {"ar": "وَرَحْمَةً", "phon": "wa rahmah", "fr": "et une miséricorde", "en": "and a mercy"}
        ],
        "reflection_fr": "L'Imam est celui que l'on suit dans chaque pas. Faire du Coran son imam, c'est aligner ses choix, ses pensées et ses actes sur la parole d'Allah.",
        "reflection_en": "An Imam is one whom we follow steadfastly. Taking the Quran as your guide means aligning every step, thought, and deed with Allah's words."
    },
    {
        "day": 3,
        "title_fr": "Le Rappel de ce qui a été oublié",
        "title_en": "Remembering What Was Forgotten",
        "category": "Science & Compréhension",
        "ar_sing": "اللَّهُمَّ ذَكِّرْنِي مِنْهُ مَا نَسِيتُ",
        "ar_plur": "اللَّهُمَّ ذَكِّرْنَا مِنْهُ مَا نَسِينَا",
        "phon_sing": "Allāhumma dhakkirnī minhu mā nasītu",
        "phon_plur": "Allāhumma dhakkirnā minhu mā nasīnā",
        "fr_sing": "Ô Allah, rappelle-moi de ce que j'en ai oublié",
        "fr_plur": "Ô Allah, rappelle-nous de ce que nous en avons oublié",
        "en_sing": "O Allah, remind me of what I have forgotten of it",
        "en_plur": "O Allah, remind us of what we have forgotten of it",
        "vocab": [
            {"ar": "ذَكِّرْنِي / ذَكِّرْنَا", "phon": "dhakkirnī / dhakkirnā", "fr": "rappelle-moi / rappelle-nous", "en": "remind me / remind us"},
            {"ar": "مِنْهُ", "phon": "minhu", "fr": "de celui-ci (du Coran)", "en": "from it (the Quran)"},
            {"ar": "مَا نَسِيتُ / نَسِينَا", "phon": "mā nasītu / nasīnā", "fr": "ce que j'ai oublié / nous avons oublié", "en": "what I / we forgot"}
        ],
        "reflection_fr": "L'oubli est humain. Cette invocation demande à Allah de réactiver dans notre mémoire les versets et les enseignements sacrés.",
        "reflection_en": "Forgetfulness is part of human nature. This prayer asks Allah to revive the sacred verses and meanings within our hearts."
    },
    {
        "day": 4,
        "title_fr": "L'Enseignement de ce qu'on ignore",
        "title_en": "Teaching What We Do Not Know",
        "category": "Science & Compréhension",
        "ar_sing": "وَعَلِّمْنِي مِنْهُ مَا جَهِلْتُ",
        "ar_plur": "وَعَلِّمْنَا مِنْهُ مَا جَهِلْنَا",
        "phon_sing": "Wa 'allimnī minhu mā jahiltu",
        "phon_plur": "Wa 'allimnā minhu mā jahilnā",
        "fr_sing": "Et enseigne-moi de ce que j'en ignore",
        "fr_plur": "Et enseigne-nous de ce que nous en ignorons",
        "en_sing": "And teach me from it that which I do not know",
        "en_plur": "And teach us from it that which we do not know",
        "vocab": [
            {"ar": "وَعَلِّمْنِي / وَعَلِّمْنَا", "phon": "wa 'allimnī / wa 'allimnā", "fr": "et enseigne-moi / enseigne-nous", "en": "and teach me / teach us"},
            {"ar": "مِنْهُ", "phon": "minhu", "fr": "de celui-ci", "en": "from it"},
            {"ar": "مَا جَهِلْتُ / جَهِلْنَا", "phon": "mā jahiltu / jahilnā", "fr": "ce que j'ignorais / nous ignorions", "en": "what I / we were ignorant of"}
        ],
        "reflection_fr": "Le Coran recèle des profondeurs inépuisables. Demander la science à Allah ouvre les portes de la méditation profonde (Tadabbur).",
        "reflection_en": "The Quran possesses inexhaustible depths of wisdom. Seeking knowledge directly from Allah unlocks true contemplation (Tadabbur)."
    },
    {
        "day": 5,
        "title_fr": "La Récitation Jour et Nuit",
        "title_en": "Recitation by Night and Day",
        "category": "Adoration & Constance",
        "ar_sing": "وَارْزُقْنِي تِلَاوَتَهُ آنَاءَ اللَّيْلِ وَأَطْرَافَ النَّهَارِ",
        "ar_plur": "وَارْزُقْنَا تِلَاوَتَهُ آنَاءَ اللَّيْلِ وَأَطْرَافَ النَّهَارِ",
        "phon_sing": "Wa-rzuqnī tilāwatahu ānā'a-l-layli wa atrōfa-n-nahār",
        "phon_plur": "Wa-rzuqnā tilāwatahu ānā'a-l-layli wa atrōfa-n-nahār",
        "fr_sing": "Et accorde-moi sa récitation aux heures de la nuit et aux extrémités du jour",
        "fr_plur": "Et accorde-nous sa récitation aux heures de la nuit et aux extrémités du jour",
        "en_sing": "And grant me its recitation throughout the night and at the ends of the day",
        "en_plur": "And grant us its recitation throughout the night and at the ends of the day",
        "vocab": [
            {"ar": "وَارْزُقْنِي / وَارْزُقْنَا", "phon": "wa-rzuqnī / wa-rzuqnā", "fr": "et accorde-moi / accorde-nous", "en": "and grant me / grant us"},
            {"ar": "تِلَاوَتَهُ", "phon": "tilāwatahu", "fr": "sa récitation", "en": "its recitation"},
            {"ar": "آنَاءَ اللَّيْلِ", "phon": "ānā'a-l-layl", "fr": "aux heures de la nuit", "en": "hours of the night"},
            {"ar": "وَأَطْرَافَ النَّهَارِ", "phon": "wa atrōfa-n-nahār", "fr": "et aux extrémités du jour", "en": "and ends of the day"}
        ],
        "reflection_fr": "La récitation nocturne (Qiyam al-Layl) apaise l'esprit et fortifie l'âme face aux défis du quotidien.",
        "reflection_en": "Reciting at night (Qiyam al-Layl) brings tranquility to the soul and anchors strength for daytime endeavors."
    },
    {
        "day": 6,
        "title_fr": "Un Argument en notre Faveur",
        "title_en": "A Proof in Our Favor",
        "category": "Jour Dernier",
        "ar_sing": "وَاجْعَلْهُ لِي حُجَّةً يَا رَبَّ العَالَمِينَ",
        "ar_plur": "وَاجْعَلْهُ لَنَا حُجَّةً يَا رَبَّ العَالَمِينَ",
        "phon_sing": "Wa-j'alhu lī hujjatan yā Rabba-l-'ālamīn",
        "phon_plur": "Wa-j'alhu lanā hujjatan yā Rabba-l-'ālamīn",
        "fr_sing": "Et fais qu'il soit pour moi un argument en ma faveur, Ô Seigneur de l'univers",
        "fr_plur": "Et fais qu'il soit pour nous un argument en notre faveur, Ô Seigneur de l'univers",
        "en_sing": "And make it an argument in my favor, O Lord of all worlds",
        "en_plur": "And make it an argument in our favor, O Lord of all worlds",
        "vocab": [
            {"ar": "حُجَّةً", "phon": "hujjatan", "fr": "un argument / une preuve (favorable)", "en": "a proof / evidence"},
            {"ar": "لِي / لَنَا", "phon": "lī / lanā", "fr": "pour moi / pour nous", "en": "for me / for us"},
            {"ar": "يَا رَبَّ العَالَمِينَ", "phon": "yā Rabba-l-'ālamīn", "fr": "Ô Seigneur des mondes", "en": "O Lord of the worlds"}
        ],
        "reflection_fr": "Le Prophète ﷺ a dit : « Le Coran est un argument en ta faveur ou contre toi. » Nous implorons Allah qu'il témoigne pour nous le Jour du Jugement.",
        "reflection_en": "The Prophet ﷺ said: 'The Quran is a proof for you or against you.' We pray that it will intercede on our behalf on the Day of Judgment."
    },
    {
        "day": 7,
        "title_fr": "La Préservation de la Religion",
        "title_en": "Rectification of Our Faith",
        "category": "Équilibre Spirituel",
        "ar_sing": "اللَّهُمَّ أَصْلِحْ لِي دِينِي الَّذِي هُوَ عِصْمَةُ أَمْرِي",
        "ar_plur": "اللَّهُمَّ أَصْلِحْ لَنَا دِينَنَا الَّذِي هُوَ عِصْمَةُ أَمْرِنَا",
        "phon_sing": "Allāhumma aslih lī dīnī alladhī huwa 'ismatu amrī",
        "phon_plur": "Allāhumma aslih lanā dīnanā alladhī huwa 'ismatu amrinā",
        "fr_sing": "Ô Allah, rectifie pour moi ma religion qui est la sauvegarde de toutes mes affaires",
        "fr_plur": "Ô Allah, rectifie pour nous notre religion qui est la sauvegarde de toutes nos affaires",
        "en_sing": "O Allah, rectify for me my religion which is the safeguard of all my affairs",
        "en_plur": "O Allah, rectify for us our religion which is the safeguard of all our affairs",
        "vocab": [
            {"ar": "أَصْلِحْ", "phon": "aslih", "fr": "réforme / rectifie / améliore", "en": "rectify / reform / mend"},
            {"ar": "دِينِي / دِينَنَا", "phon": "dīnī / dīnanā", "fr": "ma religion / notre religion", "en": "my religion / our religion"},
            {"ar": "عِصْمَةُ أَمْرِي", "phon": "'ismatu amrī", "fr": "la protection de mes affaires", "en": "the shield of my matters"}
        ],
        "reflection_fr": "Si la foi d'un croyant est intacte, toutes les autres épreuves deviennent surmontables. Elle est la boussole suprême.",
        "reflection_en": "When faith is sound and safeguarded, all other earthly tribulations become bearable. It is the ultimate anchor."
    },
    {
        "day": 8,
        "title_fr": "La Rectitude de la Vie Terrestre",
        "title_en": "Righteousness in Earthly Life",
        "category": "Équilibre Spirituel",
        "ar_sing": "وَأَصْلِحْ لِي دُنْيَايَ الَّتِي فِيهَا مَعَاشِي",
        "ar_plur": "وَأَصْلِحْ لَنَا دُنْيَانَا الَّتِي فِيهَا مَعَاشُنَا",
        "phon_sing": "Wa aslih lī dunyāya-llatī fīhā ma'āshī",
        "phon_plur": "Wa aslih lanā dunyānā-llatī fīhā ma'āshunā",
        "fr_sing": "Et rectifie pour moi ce bas-monde dans lequel se trouve ma subsistance",
        "fr_plur": "Et rectifie pour nous ce bas-monde dans lequel se trouve notre subsistance",
        "en_sing": "And rectify for me my worldly life wherein is my livelihood",
        "en_plur": "And rectify for us our worldly life wherein is our livelihood",
        "vocab": [
            {"ar": "دُنْيَايَ / دُنْيَانَا", "phon": "dunyāya / dunyānā", "fr": "mon bas-monde / notre bas-monde", "en": "my earthly life / our world"},
            {"ar": "فِيهَا مَعَاشِي / مَعَاشُنَا", "phon": "fīhā ma'āshī / ma'āshunā", "fr": "où se trouve ma / notre subsistance", "en": "wherein is my / our sustenance"}
        ],
        "reflection_fr": "L'Islam enseigne l'équilibre : rechercher le bien dans ce monde (travail licite, famille, santé) comme moyen d'atteindre l'agrément divin.",
        "reflection_en": "Islam emphasizes harmony: seeking goodness and lawful provision in this world as a means to earn Allah's pleasure."
    },
    {
        "day": 9,
        "title_fr": "La Préparation de l'Au-delà",
        "title_en": "Readiness for the Hereafter",
        "category": "Équilibre Spirituel",
        "ar_sing": "وَأَصْلِحْ لِي آخِرَتِي الَّتِي فِيهَا مَعَادِي",
        "ar_plur": "وَأَصْلِحْ لَنَا آخِرَتَنَا الَّتِي فِيهَا مَعَادُنَا",
        "phon_sing": "Wa aslih lī ākhiratī-llatī fīhā ma'ādī",
        "phon_plur": "Wa aslih lanā ākhiratanā-llatī fīhā ma'ādunā",
        "fr_sing": "Et rectifie pour moi mon au-delà vers lequel se fera mon retour",
        "fr_plur": "Et rectifie pour nous notre au-delà vers lequel se fera notre retour",
        "en_sing": "And rectify for me my hereafter wherein is my ultimate return",
        "en_plur": "And rectify for us our hereafter wherein is our ultimate return",
        "vocab": [
            {"ar": "آخِرَتِي / آخِرَتَنَا", "phon": "ākhiratī / ākhiratanā", "fr": "mon au-delà / notre au-delà", "en": "my hereafter / our hereafter"},
            {"ar": "مَعَادِي / مَعَادُنَا", "phon": "ma'ādī / ma'ādunā", "fr": "mon retour / notre retour éternel", "en": "my return / our final destination"}
        ],
        "reflection_fr": "L'au-delà est la demeure véritable et éternelle. Demander sa droiture, c'est prier pour le pardon, les bonnes actions et le Paradis.",
        "reflection_en": "The Hereafter is the true, everlasting abode. Praying for its righteousness means seeking forgiveness, purity, and Paradise."
    },
    {
        "day": 10,
        "title_fr": "La Vie comme Accroissement en Bien",
        "title_en": "Life as an Increase in Good",
        "category": "Vision de la Vie",
        "ar_sing": "وَاجْعَلِ الحَيَاةَ زِيَادَةً لِي فِي كُلِّ خَيْرٍ",
        "ar_plur": "وَاجْعَلِ الحَيَاةَ زِيَادَةً لَنَا فِي كُلِّ خَيْرٍ",
        "phon_sing": "Wa-j'ali-l-hayāta ziyādatan lī fī kulli khayr",
        "phon_plur": "Wa-j'ali-l-hayāta ziyādatan lanā fī kulli khayr",
        "fr_sing": "Et fais de la vie un accroissement pour moi en tout bien",
        "fr_plur": "Et fais de la vie un accroissement pour nous en tout bien",
        "en_sing": "And make life an increase for me in every good",
        "en_plur": "And make life an increase for us in every good",
        "vocab": [
            {"ar": "الحَيَاةَ", "phon": "al-hayāh", "fr": "la vie", "en": "life"},
            {"ar": "زِيَادَةً", "phon": "ziyādatan", "fr": "une abondance / un accroissement", "en": "an increase / growth"},
            {"ar": "فِي كُلِّ خَيْرٍ", "phon": "fī kulli khayr", "fr": "en toute bonne œuvre", "en": "in all goodness"}
        ],
        "reflection_fr": "Chaque jour supplémentaire accordé sur cette Terre est une opportunité en or d'adorer Allah, de faire le bien et d'aider les autres.",
        "reflection_en": "Every additional sunrise on Earth is a golden gift to draw closer to Allah, perform good deeds, and serve humanity."
    },
    {
        "day": 11,
        "title_fr": "Le Repos Face à Tout Mal",
        "title_en": "Peaceful Relief from Evil",
        "category": "Vision de la Vie",
        "ar_sing": "وَاجْعَلِ المَوْتَ رَاحَةً لِي مِنْ كُلِّ شَرٍّ",
        "ar_plur": "وَاجْعَلِ المَوْتَ رَاحَةً لَنَا مِنْ كُلِّ شَرٍّ",
        "phon_sing": "Wa-j'ali-l-mawta rāhatan lī min kulli sharr",
        "phon_plur": "Wa-j'ali-l-mawta rāhatan lanā min kulli sharr",
        "fr_sing": "Et fais de la mort un soulagement pour moi de tout mal",
        "fr_plur": "Et fais de la mort un soulagement pour nous de tout mal",
        "en_sing": "And make death a relief for me from every evil",
        "en_plur": "And make death a relief for us from every evil",
        "vocab": [
            {"ar": "المَوْتَ", "phon": "al-mawt", "fr": "la mort", "en": "death"},
            {"ar": "رَاحَةً", "phon": "rāhatan", "fr": "un repos / soulagement", "en": "a rest / peaceful relief"},
            {"ar": "مِنْ كُلِّ شَرٍّ", "phon": "min kulli sharr", "fr": "de tout mal / épreuve", "en": "from every evil / hardship"}
        ],
        "reflection_fr": "Pour le croyant vertueux, la mort marque la fin des tourments terrestres et le début de la paix et de la félicité auprès de son Créateur.",
        "reflection_en": "For the believer, transition from this world is liberation from trials into the embrace of divine peace and light."
    },
    {
        "day": 12,
        "title_fr": "La Meilleure Fin de Vie",
        "title_en": "The Best Conclusion of Life",
        "category": "Bonne Fin (Husn al-Khatima)",
        "ar_sing": "اللَّهُمَّ اجْعَلْ خَيْرَ عُمْرِي آخِرَهُ",
        "ar_plur": "اللَّهُمَّ اجْعَلْ خَيْرَ أَعْمَارِنَا أَوَاخِرَهَا",
        "phon_sing": "Allāhumma-j'al khayra 'umrī ākhirahu",
        "phon_plur": "Allāhumma-j'al khayra a'mārinā awākhirahā",
        "fr_sing": "Ô Allah, fais que la meilleure partie de ma vie soit sa fin",
        "fr_plur": "Ô Allah, fais que la meilleure partie de nos vies soit leur fin",
        "en_sing": "O Allah, make the best part of my life its end",
        "en_plur": "O Allah, make the best part of our lives their end",
        "vocab": [
            {"ar": "خَيْرَ", "phon": "khayr", "fr": "le meilleur de", "en": "the best of"},
            {"ar": "عُمْرِي / أَعْمَارِنَا", "phon": "'umrī / a'mārinā", "fr": "ma vie / nos vies", "en": "my life / our lifespans"},
            {"ar": "آخِرَهُ / أَوَاخِرَهَا", "phon": "ākhirahu / awākhirahā", "fr": "sa fin / leurs fins", "en": "its end / their ends"}
        ],
        "reflection_fr": "Ce qui compte le plus, c'est la façon dont on conclut son parcours. On demande à Allah que nos derniers jours soient les plus dévoués.",
        "reflection_en": "What matters most is how we finish the race of life. We ask that our final chapters be filled with the deepest devotion."
    },
    {
        "day": 13,
        "title_fr": "Les Dernières Actions Réussies",
        "title_en": "Blessed Final Deeds",
        "category": "Bonne Fin (Husn al-Khatima)",
        "ar_sing": "وَخَيْرَ عَمَلِي خَوَاتِمَهُ",
        "ar_plur": "وَخَيْرَ أَعْمَالِنَا خَوَاتِمَهَا",
        "phon_sing": "Wa khayra 'amalī khawātimahu",
        "phon_plur": "Wa khayra a'mālinā khawātimahā",
        "fr_sing": "Et la meilleure de mes actions son scellement (sa conclusion)",
        "fr_plur": "Et la meilleure de nos actions leur scellement (leur conclusion)",
        "en_sing": "And the best of my deeds its final ones",
        "en_plur": "And the best of our deeds their final ones",
        "vocab": [
            {"ar": "عَمَلِي / أَعْمَالِنَا", "phon": "'amalī / a'mālinā", "fr": "mon œuvre / nos œuvres", "en": "my deeds / our actions"},
            {"ar": "خَوَاتِمَهُ / خَوَاتِمَهَا", "phon": "khawātimahu / khawātimahā", "fr": "ses conclusions / sceaux", "en": "their conclusions / seals"}
        ],
        "reflection_fr": "« Les actes ne valent que par leur fin » enseignait le Messager d'Allah ﷺ. Mourir en état de prière ou de dhikr est une grâce suprême.",
        "reflection_en": "«Actions are judged by their seals» taught the Prophet ﷺ. Returning to Allah in a state of worship is the highest blessing."
    },
    {
        "day": 14,
        "title_fr": "Le Plus Beau des Jours : La Rencontre",
        "title_en": "The Day of Meeting the Beloved",
        "category": "Bonne Fin (Husn al-Khatima)",
        "ar_sing": "وَخَيْرَ أَيَّامِي يَوْمَ أَلْقَاكَ فِيهِ",
        "ar_plur": "وَخَيْرَ أَيَّامِنَا يَوْمَ نَلْقَاكَ فِيهِ",
        "phon_sing": "Wa khayra ayyāmī yawma alqāka fīh",
        "phon_plur": "Wa khayra ayyāminā yawma nalqāka fīh",
        "fr_sing": "Et le meilleur de mes jours le jour où je Te rencontrerai",
        "fr_plur": "Et le meilleur de nos jours le jour où nous Te rencontrerons",
        "en_sing": "And the best of my days the day on which I meet You",
        "en_plur": "And the best of our days the day on which we meet You",
        "vocab": [
            {"ar": "خَيْرَ أَيَّامِي / أَيَّامِنَا", "phon": "khayra ayyāmī / ayyāminā", "fr": "le meilleur de mes / nos jours", "en": "the best of my / our days"},
            {"ar": "يَوْمَ", "phon": "yawma", "fr": "le jour où", "en": "the day when"},
            {"ar": "أَلْقَاكَ / نَلْقَاكَ", "phon": "alqāka / nalqāka", "fr": "je Te rencontrerai / nous Te rencontrerons", "en": "I meet You / we meet You"}
        ],
        "reflection_fr": "La rencontre avec Allah est le but suprême de chaque croyant. Que ce jour soit un jour de joie, d'agrément et d'amour.",
        "reflection_en": "Meeting the Divine Creator is the pinnacle longing of the faithful. We pray it will be a day of serene joy and welcome."
    },
    {
        "day": 15,
        "title_fr": "Vie Paisible et Mort Digne",
        "title_en": "A Blissful Life and Upright Death",
        "category": "Dignité & Sérénité",
        "ar_sing": "اللَّهُمَّ إِنِّي أَسْأَلُكَ عِيشَةً هَنِيَّةً وَمِيتَةً سَوِيَّةً",
        "ar_plur": "اللَّهُمَّ إِنَّا نَسْأَلُكَ عِيشَةً هَنِيَّةً وَمِيتَةً سَوِيَّةً",
        "phon_sing": "Allāhumma innī as'aluka 'īshatan haniyyah, wa mītatan sawiyyah",
        "phon_plur": "Allāhumma innā nas'aluka 'īshatan haniyyah, wa mītatan sawiyyah",
        "fr_sing": "Ô Allah, je Te demande une vie paisible et sereine, et une mort droite et digne",
        "fr_plur": "Ô Allah, nous Te demandons une vie paisible et sereine, et une mort droite et digne",
        "en_sing": "O Allah, I ask You for a pleasant, tranquil life and an upright, noble death",
        "en_plur": "O Allah, we ask You for a pleasant, tranquil life and an upright, noble death",
        "vocab": [
            {"ar": "عِيشَةً هَنِيَّةً", "phon": "'īshatan haniyyah", "fr": "une existence douce et paisible", "en": "a serene and peaceful living"},
            {"ar": "مِيتَةً سَوِيَّةً", "phon": "mītatan sawiyyah", "fr": "une fin digne, droite et paisible", "en": "an upright and honorable passing"}
        ],
        "reflection_fr": "La vie 'haniyyah' est exempte de tourments intérieurs et de culpabilité ; la mort 'sawiyyah' est vécue avec dignité sans humiliation.",
        "reflection_en": "A 'haniyyah' life is free from spiritual agony, while a 'sawiyyah' death is marked with grace, dignity, and faith."
    },
    {
        "day": 16,
        "title_fr": "Un Retour Sans Humiliation",
        "title_en": "A Return Free of Disgrace",
        "category": "Dignité & Sérénité",
        "ar_sing": "وَمَرَدًّا غَيْرَ مُخْزٍ وَلَا فَاضِحٍ",
        "ar_plur": "وَمَرَدًّا غَيْرَ مُخْزٍ وَلَا فَاضِحٍ",
        "phon_sing": "Wa maraddan ghayra mukhzin wa lā fādih",
        "phon_plur": "Wa maraddan ghayra mukhzin wa lā fādih",
        "fr_sing": "Et un retour (vers Toi) sans humiliation ni déshonneur",
        "fr_plur": "Et un retour (vers Toi) sans humiliation ni déshonneur",
        "en_sing": "And an ultimate return unto You neither humiliating nor disgraceful",
        "en_plur": "And an ultimate return unto You neither humiliating nor disgraceful",
        "vocab": [
            {"ar": "مَرَدًّا", "phon": "maraddan", "fr": "un retour final", "en": "a return / outcome"},
            {"ar": "غَيْرَ مُخْزٍ", "phon": "ghayra mukhzin", "fr": "sans honte ni bassesse", "en": "without shame or humiliation"},
            {"ar": "وَلَا فَاضِحٍ", "phon": "wa lā fādih", "fr": "ni exposition publique de nos péchés", "en": "nor exposure of faults"}
        ],
        "reflection_fr": "Nous demandons à Allah de couvrir nos manquements sous le voile de Sa bonté (Satr) afin de ne jamais être exposés à la honte.",
        "reflection_en": "We ask the Lord of the Throne to cover our flaws with His protective veil (Satr) so we may stand with honor."
    },
    {
        "day": 17,
        "title_fr": "L'Excellence dans l'Invocation et le Succès",
        "title_en": "The Best in Supplication and Success",
        "category": "Excellence & Réussite",
        "ar_sing": "اللَّهُمَّ إِنِّي أَسْأَلُكَ خَيْرَ المَسْأَلَةِ وَخَيْرَ الدُّعَاءِ وَخَيْرَ النَّجَاحِ",
        "ar_plur": "اللَّهُمَّ إِنَّا نَسْأَلُكَ خَيْرَ المَسْأَلَةِ وَخَيْرَ الدُّعَاءِ وَخَيْرَ النَّجَاحِ",
        "phon_sing": "Allāhumma innī as'aluka khayra-l-mas'alati wa khayra-d-du'ā'i wa khayra-n-najāh",
        "phon_plur": "Allāhumma innā nas'aluka khayra-l-mas'alati wa khayra-d-du'ā'i wa khayra-n-najāh",
        "fr_sing": "Ô Allah, je Te demande la meilleure requête, la meilleure invocation et la plus belle réussite",
        "fr_plur": "Ô Allah, nous Te demandons la meilleure requête, la meilleure invocation et la plus belle réussite",
        "en_sing": "O Allah, I ask You for the best petition, the best supplication, and the best success",
        "en_plur": "O Allah, we ask You for the best petition, the best supplication, and the best success",
        "vocab": [
            {"ar": "خَيْرَ المَسْأَلَةِ", "phon": "khayra-l-mas'alah", "fr": "la plus noble des demandes", "en": "the highest petition"},
            {"ar": "خَيْرَ الدُّعَاءِ", "phon": "khayra-d-du'ā'", "fr": "la meilleure des invocations", "en": "the best supplication"},
            {"ar": "خَيْرَ النَّجَاحِ", "phon": "khayra-n-najāh", "fr": "la vraie réussite complète", "en": "the true and wholesome success"}
        ],
        "reflection_fr": "Le succès véritable englobe le bien dans ce monde et le triomphe au Paradis. Cette formule résume toutes les aspirations nobles.",
        "reflection_en": "Real success is multifaceted: inner clarity in this world and glorious safety in the eternal realm."
    },
    {
        "day": 18,
        "title_fr": "Le Savoir, l'Action et la Récompense",
        "title_en": "Knowledge, Deeds and Rewards",
        "category": "Excellence & Réussite",
        "ar_sing": "وَخَيْرَ العِلْمِ وَخَيْرَ العَمَلِ وَخَيْرَ الثَّوَابِ وَخَيْرَ الحَيَاةِ وَخَيْرَ المَمَاتِ",
        "ar_plur": "وَخَيْرَ العِلْمِ وَخَيْرَ العَمَلِ وَخَيْرَ الثَّوَابِ وَخَيْرَ الحَيَاةِ وَخَيْرَ المَمَاتِ",
        "phon_sing": "Wa khayra-l-'ilmi wa khayra-l-'amali wa khayra-th-thawābi wa khayra-l-hayāti wa khayra-l-mamāt",
        "phon_plur": "Wa khayra-l-'ilmi wa khayra-l-'amali wa khayra-th-thawābi wa khayra-l-hayāti wa khayra-l-mamāt",
        "fr_sing": "Et le meilleur savoir, la meilleure œuvre, la plus belle récompense, la meilleure vie et la meilleure fin",
        "fr_plur": "Et le meilleur savoir, la meilleure œuvre, la plus belle récompense, la meilleure vie et la meilleure fin",
        "en_sing": "And the best knowledge, the best deed, the best reward, the best life, and the best death",
        "en_plur": "And the best knowledge, the best deed, the best reward, the best life, and the best death",
        "vocab": [
            {"ar": "خَيْرَ العِلْمِ", "phon": "khayra-l-'ilm", "fr": "le savoir bénéfique", "en": "beneficial knowledge"},
            {"ar": "خَيْرَ العَمَلِ", "phon": "khayra-l-'amal", "fr": "l'action pieuse et acceptée", "en": "righteous, accepted deed"},
            {"ar": "خَيْرَ الثَّوَابِ", "phon": "khayra-th-thawāb", "fr": "la récompense généreuse", "en": "bountiful recompense"}
        ],
        "reflection_fr": "La trilogie du croyant : apprendre la vérité, la mettre en pratique avec sincérité, et espérer la récompense d'Allah.",
        "reflection_en": "The believers' trilogy: acquiring useful knowledge, practicing it with sincerity, and trusting Allah's recompense."
    },
    {
        "day": 19,
        "title_fr": "Constance, Foi et Balance Lourde",
        "title_en": "Steadfastness, Faith and Heavy Scales",
        "category": "Progression Spirituelle",
        "ar_sing": "وَثَبِّتْنِي وَثَقِّلْ مَوَازِينِي وَحَقِّقْ إِيمَانِي وَارْفَعْ دَرَجَتِي",
        "ar_plur": "وَثَبِّتْنَا وَثَقِّلْ مَوَازِينَنَا وَحَقِّقْ إِيمَانَنَا وَارْفَعْ دَرَجَاتِنَا",
        "phon_sing": "Wa thabbitnī wa thaqqil mawāzīnī wa haqqiq īmānī wa-rfa' darajatī",
        "phon_plur": "Wa thabbitnā wa thaqqil mawāzīnanā wa haqqiq īmānanā wa-rfa' darajātinā",
        "fr_sing": "Et affermis-moi, alourdis mes balances, concrétise ma foi et élève mon rang",
        "fr_plur": "Et affermis-nous, alourdis nos balances, concrétise notre foi et élève nos rangs",
        "en_sing": "And make me steadfast, make heavy my scales, realize my faith, and elevate my rank",
        "en_plur": "And make us steadfast, make heavy our scales, realize our faith, and elevate our ranks",
        "vocab": [
            {"ar": "ثَبِّتْنِي / ثَبِّتْنَا", "phon": "thabbitnī / thabbitnā", "fr": "affermis-moi / nous", "en": "grant me / us firmness"},
            {"ar": "ثَقِّلْ مَوَازِينِي", "phon": "thaqqil mawāzīnī", "fr": "alourdis mes balances", "en": "make heavy my scales"},
            {"ar": "حَقِّقْ إِيمَانِي", "phon": "haqqiq īmānī", "fr": "concrétise / purifie ma foi", "en": "actualize my faith"},
            {"ar": "ارْفَعْ دَرَجَتِي", "phon": "irfa' darajatī", "fr": "élève mon degré", "en": "raise my station"}
        ],
        "reflection_fr": "La balance alourdie par les bonnes actions est le gage du salut éternel (Al-Mawāzīn).",
        "reflection_en": "The weighing of deeds (Al-Mawāzīn) determines the eternal outcome; we ask that our good deeds outweigh our faults."
    },
    {
        "day": 20,
        "title_fr": "Pardon, Prière et Hauts Degrés",
        "title_en": "Prayer Accepted and Highest Heavens",
        "category": "Progression Spirituelle",
        "ar_sing": "وَتَقَبَّلْ صَلَاتِي وَاغْفِرْ خَطِيئَاتِي وَأَسْأَلُكَ العُلَا مِنَ الجَنَّةِ",
        "ar_plur": "وَتَقَبَّلْ صَلَاتَنَا وَاغْفِرْ خَطِيئَاتِنَا وَنَسْأَلُكَ العُلَا مِنَ الجَنَّةِ",
        "phon_sing": "Wa taqabbal salātī wa-ghfir khatī'ātī wa as'aluka-l-'ulā mina-l-jannah",
        "phon_plur": "Wa taqabbal salātanā wa-ghfir khatī'ātinā wa nas'aluka-l-'ulā mina-l-jannah",
        "fr_sing": "Et accepte ma prière, pardonne mes fautes, et je Te demande les plus hauts rangs du Paradis",
        "fr_plur": "Et accepte notre prière, pardonne nos fautes, et nous Te demandons les plus hauts rangs du Paradis",
        "en_sing": "And accept my prayer, forgive my sins, and I ask You for the highest stations of Paradise",
        "en_plur": "And accept our prayer, forgive our sins, and we ask You for the highest stations of Paradise",
        "vocab": [
            {"ar": "تَقَبَّلْ صَلَاتِي", "phon": "taqabbal salātī", "fr": "accepte ma prière", "en": "accept my prayer"},
            {"ar": "اغْفِرْ خَطِيئَاتِي", "phon": "ighfir khatī'ātī", "fr": "efface mes péchés", "en": "pardon my misdeeds"},
            {"ar": "العُلَا مِنَ الجَنَّةِ", "phon": "al-'ulā mina-l-jannah", "fr": "les plus hauts sommets du Paradis", "en": "the highest abodes of Paradise"}
        ],
        "reflection_fr": "Ne te contente jamais du minimum dans tes invocations : le Prophète ﷺ nous a enseigné de demander le Firdaws, le plus haut niveau du Paradis.",
        "reflection_en": "Never hesitate to aim high in du'a: the Prophet ﷺ instructed us to ask for Al-Firdaws, the highest pinnacle of Paradise."
    },
    {
        "day": 21,
        "title_fr": "Les Clés de la Miséricorde et du Pardon",
        "title_en": "The Requisites of Divine Mercy",
        "category": "Clés du Pardon",
        "ar_sing": "اللَّهُمَّ إِنِّي أَسْأَلُكَ مُوجِبَاتِ رَحْمَتِكَ وَعَزَائِمَ مَغْفِرَتِكَ",
        "ar_plur": "اللَّهُمَّ إِنَّا نَسْأَلُكَ مُوجِبَاتِ رَحْمَتِكَ وَعَزَائِمَ مَغْفِرَتِكَ",
        "phon_sing": "Allāhumma innī as'aluka mūjibāti rahmatika wa 'azā'ima maghfiratik",
        "phon_plur": "Allāhumma innā nas'aluka mūjibāti rahmatika wa 'azā'ima maghfiratik",
        "fr_sing": "Ô Allah, je Te demande les causes certaines de Ta miséricorde et les moyens décisifs de Ton pardon",
        "fr_plur": "Ô Allah, nous Te demandons les causes certaines de Ta miséricorde et les moyens décisifs de Ton pardon",
        "en_sing": "O Allah, I ask You for that which guarantees Your mercy and causes Your forgiveness",
        "en_plur": "O Allah, we ask You for that which guarantees Your mercy and causes Your forgiveness",
        "vocab": [
            {"ar": "مُوجِبَاتِ رَحْمَتِكَ", "phon": "mūjibāti rahmatik", "fr": "les actes qui attirent Ta miséricorde", "en": "deeds that necessitate Your mercy"},
            {"ar": "عَزَائِمَ مَغْفِرَتِكَ", "phon": "'azā'ima maghfiratik", "fr": "les moyens inébranlables de Ton pardon", "en": "resolute means of Your forgiveness"}
        ],
        "reflection_fr": "Nous demandons à Allah de nous guider vers les paroles et les actions concrètes qui rendent Sa miséricorde inévitable pour nous.",
        "reflection_en": "We plead with Allah to inspire us toward the sincere deeds that unconditionally unlock His boundless mercy."
    },
    {
        "day": 22,
        "title_fr": "Le Paradis et le Salut du Feu",
        "title_en": "Triumph in Paradise and Refuge from Fire",
        "category": "Clés du Pardon",
        "ar_sing": "وَالسَّلَامَةَ مِنْ كُلِّ إِثْمٍ وَالغَنِيمَةَ مِنْ كُلِّ بِرٍّ وَالفَوْزَ بِالجَنَّةِ وَالنَّجَاةَ مِنَ النَّارِ",
        "ar_plur": "وَالسَّلَامَةَ مِنْ كُلِّ إِثْمٍ وَالغَنِيمَةَ مِنْ كُلِّ بِرٍّ وَالفَوْزَ بِالجَنَّةِ وَالنَّجَاةَ مِنَ النَّارِ",
        "phon_sing": "Wa-s-salāmata min kulli ithm, wal-ghanīmata min kulli birr, wal-fawza bil-jannati wan-najāta mina-n-nār",
        "phon_plur": "Wa-s-salāmata min kulli ithm, wal-ghanīmata min kulli birr, wal-fawza bil-jannati wan-najāta mina-n-nār",
        "fr_sing": "Et la préservation de tout péché, le plein profit de toute piété, le triomphe par le Paradis et la délivrance du Feu",
        "fr_plur": "Et la préservation de tout péché, le plein profit de toute piété, le triomphe par le Paradis et la délivrance du Feu",
        "en_sing": "And safety from every sin, the gain of every righteousness, triumph with Paradise, and deliverance from the Fire",
        "en_plur": "And safety from every sin, the gain of every righteousness, triumph with Paradise, and deliverance from the Fire",
        "vocab": [
            {"ar": "السَّلَامَةَ مِنْ كُلِّ إِثْمٍ", "phon": "as-salāmata min kulli ithm", "fr": "être indemne de tout péché", "en": "immunity from all sin"},
            {"ar": "الغَنِيمَةَ مِنْ كُلِّ بِرٍّ", "phon": "al-ghanīmata min kulli birr", "fr": "le butin de chaque bonne action", "en": "harvesting every righteousness"},
            {"ar": "الفَوْزَ بِالجَنَّةِ", "phon": "al-fawza bil-jannah", "fr": "la victoire du Paradis", "en": "victory of entering Paradise"},
            {"ar": "النَّجَاةَ مِنَ النَّارِ", "phon": "an-najāta mina-n-nār", "fr": "le sauvetage du brasier", "en": "salvation from Hellfire"}
        ],
        "reflection_fr": "Cette formule magistrale embrasse tout ce qu'un être humain peut désirer : s'éloigner du mal, embrasser le bien, goûter au Paradis.",
        "reflection_en": "This comprehensive phrase covers every desire: fleeing from harm, reaping virtues, and dwelling in eternal gardens."
    },
    {
        "day": 23,
        "title_fr": "Le Bon Dénouement de Tout",
        "title_en": "Gracious Outcomes in All Matters",
        "category": "Protection & Sérénité",
        "ar_sing": "اللَّهُمَّ أَحْسِنْ عَاقِبَتِي فِي الأُمُورِ كُلِّهَا وَأَجِرْنِي مِنْ خِزْيِ الدُّنْيَا وَعَذَابِ الآخِرَةِ",
        "ar_plur": "اللَّهُمَّ أَحْسِنْ عَاقِبَتَنَا فِي الأُمُورِ كُلِّهَا وَأَجِرْنَا مِنْ خِزْيِ الدُّنْيَا وَعَذَابِ الآخِرَةِ",
        "phon_sing": "Allāhumma ahsin 'āqibatī fī-l-umūri kullihā wa ajirnī min khizyi-d-dunyā wa 'adhābi-l-ākhirah",
        "phon_plur": "Allāhumma ahsin 'āqibatanā fī-l-umūri kullihā wa ajirnā min khizyi-d-dunyā wa 'adhābi-l-ākhirah",
        "fr_sing": "Ô Allah, parfait l'issue de toutes mes affaires et préserve-moi de l'opprobre d'ici-bas et du châtiment de l'au-delà",
        "fr_plur": "Ô Allah, parfait l'issue de toutes nos affaires et préserve-nous de l'opprobre d'ici-bas et du châtiment de l'au-delà",
        "en_sing": "O Allah, make noble the outcome of all my affairs and save me from the shame of this world and penalty of the hereafter",
        "en_plur": "O Allah, make noble the outcome of all our affairs and save us from the shame of this world and penalty of the hereafter",
        "vocab": [
            {"ar": "أَحْسِنْ عَاقِبَتَنَا", "phon": "ahsin 'āqibatanā", "fr": "embellis et perfectionne notre fin", "en": "make blessed our end"},
            {"ar": "فِي الأُمُورِ كُلِّهَا", "phon": "fī-l-umūri kullihā", "fr": "dans chaque projet et circonstance", "en": "in all affairs and choices"},
            {"ar": "خِزْيِ الدُّنْيَا", "phon": "khizyi-d-dunyā", "fr": "l'humiliation dans ce monde", "en": "the humiliation of this life"}
        ],
        "reflection_fr": "Que de projets semblent prometteurs mais finissent mal ! Nous remettons le dénouement de chaque épreuve entre les mains d'Allah.",
        "reflection_en": "Many pursuits appear tempting but turn bitter. We entrust the outcome of each life endeavor to Allah's wise decree."
    },
    {
        "day": 24,
        "title_fr": "La Crainte Vénérée d'Allah",
        "title_en": "A Shield of Reverence",
        "category": "Crainte & Obéissance",
        "ar_sing": "اللَّهُمَّ اقْسِمْ لِي مِنْ خَشْيَتِكَ مَا تَحُولُ بِهِ بَيْنِي وَبَيْنَ مَعْصِيَتِكَ",
        "ar_plur": "اللَّهُمَّ اقْسِمْ لَنَا مِنْ خَشْيَتِكَ مَا تَحُولُ بِهِ بَيْنَنَا وَبَيْنَ مَعْصِيَتِكَ",
        "phon_sing": "Allāhumma-qsim lī min khashyatika mā tahūlu bihī baynī wa bayna ma'siyatik",
        "phon_plur": "Allāhumma-qsim lanā min khashyatika mā tahūlu bihī baynanā wa bayna ma'siyatik",
        "fr_sing": "Ô Allah, accorde-moi une part de Ta crainte qui s'interpose entre moi et Ta désobéissance",
        "fr_plur": "Ô Allah, accorde-nous une part de Ta crainte qui s'interpose entre nous et Ta désobéissance",
        "en_sing": "O Allah, apportion to me such fear of You as will come between me and disobeying You",
        "en_plur": "O Allah, apportion to us such fear of You as will come between us and disobeying You",
        "vocab": [
            {"ar": "اقْسِمْ لَنَا", "phon": "iqsim lanā", "fr": "octroie-nous une part bénie", "en": "apportion unto us a share"},
            {"ar": "مِنْ خَشْيَتِكَ", "phon": "min khashyatik", "fr": "de Ta crainte révérencielle", "en": "of reverence/awe of You"},
            {"ar": "تَحُولُ بِهِ", "phon": "tahūlu bihī", "fr": "qui forme une barrière", "en": "that acts as a barrier"}
        ],
        "reflection_fr": "La crainte d'Allah ('Khashya') n'est pas une peur paralysante, mais un respect profond et un amour qui retient le croyant de blesser son âme.",
        "reflection_en": "'Khashya' is not terrifying panic, but awe, love, and sacred respect that gently holds the soul back from falling into transgression."
    },
    {
        "day": 25,
        "title_fr": "L'Obéissance vers le Paradis",
        "title_en": "Obedience that Leads to Paradise",
        "category": "Crainte & Obéissance",
        "ar_sing": "وَمِنْ طَاعَتِكَ مَا تُبَلِّغُنِي بِهِ جَنَّتَكَ",
        "ar_plur": "وَمِنْ طَاعَتِكَ مَا تُبَلِّغُنَا بِهِ جَنَّتَكَ",
        "phon_sing": "Wa min tā'atika mā tuballighunī bihī jannatak",
        "phon_plur": "Wa min tā'atika mā tuballighunā bihī jannatak",
        "fr_sing": "Et une part de Ton obéissance par laquelle Tu me feras atteindre Ton Paradis",
        "fr_plur": "Et une part de Ton obéissance par laquelle Tu nous feras atteindre Ton Paradis",
        "en_sing": "And of obedience to You that which will convey me to Your Paradise",
        "en_plur": "And of obedience to You that which will convey us to Your Paradise",
        "vocab": [
            {"ar": "مِنْ طَاعَتِكَ", "phon": "min tā'atik", "fr": "de Ton obéissance dévouée", "en": "of devotion and obedience to You"},
            {"ar": "تُبَلِّغُنَا بِهِ", "phon": "tuballighunā bihī", "fr": "Tu nous feras parvenir grâce à elle", "en": "You convey us through it"},
            {"ar": "جَنَّتَكَ", "phon": "jannatak", "fr": "Ton vaste Paradis", "en": "Your Paradise"}
        ],
        "reflection_fr": "L'obéissance aux préceptes divins n'est pas un fardeau, c'est l'échelle de lumière qui élève le serviteur vers la béatitude éternelle.",
        "reflection_en": "Obeying divine guidance is never a burden; it is the luminous stairway that elevates the sincere heart into eternal joy."
    },
    {
        "day": 26,
        "title_fr": "La Certitude face aux Épreuves",
        "title_en": "Firm Certainty Overcoming Hardship",
        "category": "Épreuves & Patience",
        "ar_sing": "وَمِنَ اليَقِينِ مَا تُهَوِّنُ بِهِ عَلَيَّ مَصَائِبَ الدُّنْيَا",
        "ar_plur": "وَمِنَ اليَقِينِ مَا تُهَوِّنُ بِهِ عَلَيْنَا مَصَائِبَ الدُّنْيَا",
        "phon_sing": "Wa mina-l-yaqīni mā tuhawwinu bihī 'alayya masā'iba-d-dunyā",
        "phon_plur": "Wa mina-l-yaqīni mā tuhawwinu bihī 'alaynā masā'iba-d-dunyā",
        "fr_sing": "Et une certitude par laquelle Tu rendras légères pour moi les épreuves de ce bas-monde",
        "fr_plur": "Et une certitude par laquelle Tu rendras légères pour nous les épreuves de ce bas-monde",
        "en_sing": "And of conviction that will make easy for me the misfortunes of this world",
        "en_plur": "And of conviction that will make easy for us the misfortunes of this world",
        "vocab": [
            {"ar": "اليَقِينِ", "phon": "al-yaqīn", "fr": "la certitude inébranlable", "en": "unwavering certainty"},
            {"ar": "تُهَوِّنُ بِهِ", "phon": "tuhawwinu bihī", "fr": "Tu allèges / rends doux", "en": "You make light and easy"},
            {"ar": "مَصَائِبَ الدُّنْيَا", "phon": "masā'iba-d-dunyā", "fr": "les épreuves de cette vie", "en": "the calamities of this world"}
        ],
        "reflection_fr": "Lorsque la certitude (Yaqîn) habite le cœur, les tempêtes de la vie ne peuvent plus le briser, car il sait que tout est entre les mains d'Allah.",
        "reflection_en": "When divine certitude (Yaqin) fills the core, hardships transform into opportunities for patience, elevation, and strength."
    },
    {
        "day": 27,
        "title_fr": "La Santé et les Bienfaits Durables",
        "title_en": "Preserving Senses and Vitality",
        "category": "Santé & Bienfaits",
        "ar_sing": "وَمَتِّعْنِي بِسَمْعِي وَبَصَرِي وَقُوَّتِي مَا أَحْيَيْتَنِي وَاجْعَلْهُ الوَارِثَ مِنِّي",
        "ar_plur": "وَمَتِّعْنَا بِأَسْمَاعِنَا وَأَبْصَارِنَا وَقُوَّتِنَا مَا أَحْيَيْتَنَا وَاجْعَلْهُ الوَارِثَ مِنَّا",
        "phon_sing": "Wa matti'nī bi-sam'ī wa basarī wa quwwatī mā ahyaytanī wa-j'alhu-l-wāritha minnī",
        "phon_plur": "Wa matti'nā bi-asmā'inā wa absārinā wa quwwatinā mā ahyaytanā wa-j'alhu-l-wāritha minnā",
        "fr_sing": "Et fais-moi jouir de mon ouïe, de ma vue et de ma force tant que Tu me garderas en vie, et fais qu'elles demeurent jusqu'à ma mort",
        "fr_plur": "Et fais-nous jouir de nos facultés d'ouïe, de vue et de notre force tant que Tu nous garderas en vie, et fais qu'elles nous accompagnent jusqu'à notre mort",
        "en_sing": "And let me enjoy my hearing, my sight, and my strength as long as You keep me alive, and make them remain with me until the end",
        "en_plur": "And let us enjoy our hearing, our sight, and our strength as long as You keep us alive, and make them remain with us until the end",
        "vocab": [
            {"ar": "مَتِّعْنَا", "phon": "matti'nā", "fr": "fais-nous bénéficier pleinement", "en": "allow us to enjoy healthily"},
            {"ar": "بِأَسْمَاعِنَا وَأَبْصَارِنَا", "phon": "bi-asmā'inā wa absārinā", "fr": "de nos oreilles et nos yeux", "en": "our hearing and sights"},
            {"ar": "وَقُوَّتِنَا", "phon": "wa quwwatinā", "fr": "et de notre énergie vitale", "en": "and our vitality/strength"},
            {"ar": "الوَارِثَ مِنَّا", "phon": "al-wāritha minnā", "fr": "qui perdurent jusqu'au dernier souffle", "en": "lasting with us until death"}
        ],
        "reflection_fr": "Demander que la vue et l'ouïe 'héritent de nous' signifie rester lucide, autonome et capable d'adorer Allah jusqu'au tout dernier jour.",
        "reflection_en": "Praying that physical faculties 'inherit from us' means maintaining clarity of mind and body until our very last breath."
    },
    {
        "day": 28,
        "title_fr": "Justice et Secours Contre l'Injustice",
        "title_en": "Justice and Victory Over Tyranny",
        "category": "Justice & Protection",
        "ar_sing": "وَاجْعَلْ ثَأْرِي عَلَى مَنْ ظَلَمَنِي وَانْصُرْنِي عَلَى مَنْ عَادَانِي",
        "ar_plur": "وَاجْعَلْ ثَأْرَنَا عَلَى مَنْ ظَلَمَنَا وَانْصُرْنَا عَلَى مَنْ عَادَانَا",
        "phon_sing": "Wa-j'al tha'rī 'alā man zalamanī wan-surnī 'alā man 'ādānī",
        "phon_plur": "Wa-j'al tha'ranā 'alā man zalamanā wan-surnā 'alā man 'ādānā",
        "fr_sing": "Et fais que justice soit rendue uniquement contre celui qui m'a lésé, et secours-moi contre celui qui m'a pris pour ennemi",
        "fr_plur": "Et fais que justice soit rendue uniquement contre ceux qui nous ont lésés, et secours-nous contre ceux qui nous ont pris pour ennemis",
        "en_sing": "And let justice fall only upon those who wrong me, and grant me victory over those who show enmity towards me",
        "en_plur": "And let justice fall only upon those who wrong us, and grant us victory over those who show enmity towards us",
        "vocab": [
            {"ar": "ثَأْرَنَا عَلَى مَنْ ظَلَمَنَا", "phon": "tha'ranā 'alā man zalamanā", "fr": "notre justice contre les oppresseurs", "en": "justice upon our wrongdoers"},
            {"ar": "وَانْصُرْنَا", "phon": "wan-surnā", "fr": "et donne-nous la victoire", "en": "and grant us victory"},
            {"ar": "مَنْ عَادَانَا", "phon": "man 'ādānā", "fr": "ceux qui nous attaquent sans droit", "en": "those hostile towards us"}
        ],
        "reflection_fr": "L'Islam rejette l'injustice aveugle et la vengeance disproportionnée : nous demandons l'équité divine parfaite et la protection contre les oppresseurs.",
        "reflection_en": "Islam repudiates unchecked retribution: this prayer asks for pure divine justice and safety from malice and oppression."
    },
    {
        "day": 29,
        "title_fr": "Protéger la Foi et Libérer l'Esprit",
        "title_en": "Shielding Faith from Worldly Distractions",
        "category": "Sagesse & Priorités",
        "ar_sing": "وَلَا تَجْعَلْ مُصِيبَتِي فِي دِينِي وَلَا تَجْعَلِ الدُّنْيَا أَكْبَرَ هَمِّي وَلَا مَبْلَغَ عِلْمِي وَلَا تُسَلِّطْ عَلَيَّ مَنْ لَا يَرْحَمُنِي",
        "ar_plur": "وَلَا تَجْعَلْ مُصِيبَتَنَا فِي دِينِنَا وَلَا تَجْعَلِ الدُّنْيَا أَكْبَرَ هَمِّنَا وَلَا مَبْلَغَ عِلْمِنَا وَلَا تُسَلِّطْ عَلَيْنَا مَنْ لَا يَرْحَمُنَا",
        "phon_sing": "Wa lā taj'al musībatī fī dīnī wa lā taj'ali-d-dunyā akbara hammī wa lā mablagha 'ilmī wa lā tusallit 'alayya man lā yarhamunī",
        "phon_plur": "Wa lā taj'al musībatanā fī dīninā wa lā taj'ali-d-dunyā akbara hamminā wa lā mablagha 'ilminā wa lā tusallit 'alaynā man lā yarhamunā",
        "fr_sing": "Et ne mets pas l'épreuve dans ma religion, ne fais pas du monde mon souci suprême ni la limite de mon savoir, et ne m'impose personne sans compassion pour moi",
        "fr_plur": "Et ne mets pas l'épreuve dans notre religion, ne fais pas du monde notre souci suprême ni la limite de notre savoir, et ne nous impose personne sans compassion pour nous",
        "en_sing": "Do not let calamity afflict my religion, nor make the world my greatest grief or the limit of my knowledge, and do not place over me anyone lacking mercy towards me",
        "en_plur": "Do not let calamity afflict our religion, nor make the world our greatest grief or the limit of our knowledge, and do not place over us anyone lacking mercy towards us",
        "vocab": [
            {"ar": "مُصِيبَتَنَا فِي دِينِنَا", "phon": "musībatanā fī dīninā", "fr": "une calamité qui affaiblit notre foi", "en": "affliction touching our faith"},
            {"ar": "أَكْبَرَ هَمِّنَا", "phon": "akbara hamminā", "fr": "la préoccupation obsédante", "en": "our consuming worry"},
            {"ar": "مَبْلَغَ عِلْمِنَا", "phon": "mablagha 'ilminā", "fr": "l'horizon borné de notre esprit", "en": "the boundary of our intellect"},
            {"ar": "مَنْ لَا يَرْحَمُنَا", "phon": "man lā yarhamunā", "fr": "des dirigeants sans pitié", "en": "oppressors devoid of mercy"}
        ],
        "reflection_fr": "La pire des épreuves n'est pas financière ou physique, c'est de perdre la foi ou d'être esclave de l'illusion terrestre.",
        "reflection_en": "The gravest calamity is not losing material fortune, but losing religious moral compass or becoming imprisoned by worldly illusions."
    },
    {
        "day": 30,
        "title_fr": "L'Affranchissement Total et Clôture Céleste",
        "title_en": "The Grand Finale: Total Liberation and Peace",
        "category": "Apothéose & Clôture",
        "ar_sing": "اللَّهُمَّ لَا تَدَعْ لِي ذَنْبًا إِلَّا غَفَرْتَهُ وَلَا هَمًّا إِلَّا فَرَّجْتَهُ وَلَا دَيْنًا إِلَّا قَضَيْتَهُ وَلَا حَاجَةً مِنْ حَوَائِجِ الدُّنْيَا وَالآخِرَةِ إِلَّا قَضَيْتَهَا يَا أَرْحَمَ الرَّاحِمِينَ * رَبَّنَا آتِنَا فِي الدُّنْيَا حَسَنَةً وَفِي الآخِرَةِ حَسَنَةً وَقِنَا عَذَابَ النَّارِ * وَصَلَّى اللهُ عَلَى نَبِيِّنَا مُحَمَّدٍ وَعَلَى آلِهِ وَأَصْحَابِهِ الأَخْيَارِ وَسَلَّمَ تَسْلِيمًا كَثِيرًا",
        "ar_plur": "اللَّهُمَّ لَا تَدَعْ لَنَا ذَنْبًا إِلَّا غَفَرْتَهُ وَلَا هَمًّا إِلَّا فَرَّجْتَهُ وَلَا دَيْنًا إِلَّا قَضَيْتَهُ وَلَا حَاجَةً مِنْ حَوَائِجِ الدُّنْيَا وَالآخِرَةِ إِلَّا قَضَيْتَهَا يَا أَرْحَمَ الرَّاحِمِينَ * رَبَّنَا آتِنَا فِي الدُّنْيَا حَسَنَةً وَفِي الآخِرَةِ حَسَنَةً وَقِنَا عَذَابَ النَّارِ * وَصَلَّى اللهُ عَلَى نَبِيِّنَا مُحَمَّدٍ وَعَلَى آلِهِ وَأَصْحَابِهِ الأَخْيَارِ وَسَلَّمَ تَسْلِيمًا كَثِيرًا",
        "phon_sing": "Allāhumma lā tada' lī dhanban illā ghafartah, wa lā hamman illā farrajtah, wa lā daynan illā qadaytah, wa lā hājatan min hawā'iji-d-dunyā wal-ākhirati illā qadaytahā yā Arhama-r-Rāhimīn * Rabbanā ātinā fid-dunyā hasanatan wa fil-ākhirati hasanatan wa qinā 'adhāba-n-nār * Wa sallallāhu 'alā nabiyyinā Muhammadin wa 'alā ālihī wa ashābihi-l-akhyār, wa sallama taslīman kathīrā",
        "phon_plur": "Allāhumma lā tada' lanā dhanban illā ghafartah, wa lā hamman illā farrajtah, wa lā daynan illā qadaytah, wa lā hājatan min hawā'iji-d-dunyā wal-ākhirati illā qadaytahā yā Arhama-r-Rāhimīn * Rabbanā ātinā fid-dunyā hasanatan wa fil-ākhirati hasanatan wa qinā 'adhāba-n-nār * Wa sallallāhu 'alā nabiyyinā Muhammadin wa 'alā ālihī wa ashābihi-l-akhyār, wa sallama taslīman kathīrā",
        "fr_sing": "Ô Allah, ne me laisse aucun péché sans le pardonner, aucun souci sans le dissiper, aucune dette sans l'acquitter, ni aucun besoin d'ici-bas et de l'au-delà sans le combler, Ô le Plus Miséricordieux des miséricordieux ! Seigneur, accorde-nous le bien en ce monde et le bien dans l'au-delà, et protège-nous du châtiment du Feu. Et que la paix et la bénédiction d'Allah soient abondamment accordées à notre Prophète Muhammad, à sa famille et à ses nobles compagnons.",
        "fr_plur": "Ô Allah, ne nous laisse aucun péché sans le pardonner, aucun souci sans le dissiper, aucune dette sans l'acquitter, ni aucun besoin d'ici-bas et de l'au-delà sans le combler, Ô le Plus Miséricordieux des miséricordieux ! Seigneur, accorde-nous le bien en ce monde et le bien dans l'au-delà, et protège-nous du châtiment du Feu. Et que la paix et la bénédiction d'Allah soient abondamment accordées à notre Prophète Muhammad, à sa famille et à ses nobles compagnons.",
        "en_sing": "O Allah, leave me no sin unforgiven, no grief unrelieved, no debt unpaid, and no need of this world or the Hereafter unfulfilled, O Most Merciful of the merciful! Our Lord, give us in this world that which is good and in the Hereafter that which is good, and save us from the torment of the Fire. And may Allah shower abundant peace and blessings upon our Prophet Muhammad, his family, and his noble companions.",
        "en_plur": "O Allah, leave us no sin unforgiven, no grief unrelieved, no debt unpaid, and no need of this world or the Hereafter unfulfilled, O Most Merciful of the merciful! Our Lord, give us in this world that which is good and in the Hereafter that which is good, and save us from the torment of the Fire. And may Allah shower abundant peace and blessings upon our Prophet Muhammad, his family, and his noble companions.",
        "vocab": [
            {"ar": "لَا تَدَعْ لَنَا ذَنْبًا", "phon": "lā tada' lanā dhanban", "fr": "ne laisse aucun péché sans pardon", "en": "leave no sin unforgiven"},
            {"ar": "وَلَا هَمًّا إِلَّا فَرَّجْتَهُ", "phon": "wa lā hamman illā farrajtah", "fr": "aucun souci sans délivrance", "en": "no distress unrelieved"},
            {"ar": "وَلَا دَيْنًا إِلَّا قَضَيْتَهُ", "phon": "wa lā daynan illā qadaytah", "fr": "aucune dette sans acquittement", "en": "no debt unpaid"},
            {"ar": "يَا أَرْحَمَ الرَّاحِمِينَ", "phon": "yā Arhama-r-Rāhimīn", "fr": "Ô le Plus Miséricordieux", "en": "O Most Merciful"},
            {"ar": "حَسَنَةً", "phon": "hasanatan", "fr": "un bienfait durable", "en": "goodness / blessing"},
            {"ar": "صَلَّى اللهُ عَلَى نَبِيِّنَا", "phon": "sallallāhu 'alā nabiyyinā", "fr": "prières et saluts sur notre Prophète", "en": "blessings upon our Prophet"}
        ],
        "reflection_fr": "Le couronnement sublime de la récitation : l'absolution intégrale, la délivrance des dettes et peines, l'invocation coranique maîtresse et la salutation bénie sur le Bien-Aimé ﷺ.",
        "reflection_en": "The grand culmination: total absolution of sins, relief from anxieties, debt clearance, the paramount Quranic prayer, and exalted salutations upon the Prophet ﷺ."
    }
]

app_data = {
    "title_fr": "Dou'a Khatm al-Qur'an 30",
    "title_en": "Quran Completion Du'a 30",
    "description_fr": "Programme d'apprentissage immersif de 30 jours : Dou'a de clôture du Coran, phrase par phrase, en arabe vocalisé, phonétique, français et anglais, avec bascule instantanée Singulier (Seul) / Pluriel (En groupe).",
    "description_en": "30-Day Immersive Mastery: Quran Completion Supplication, sentence by sentence, with fully vocalized Arabic, phonetics, French and English translations, and instant 1-click Singular (Personal) / Plural (Group) toggle.",
    "days": days
}

output_path = "/home/dev-yokan/doua-khatm-30/data.js"
with open(output_path, "w", encoding="utf-8") as f:
    f.write("window.DOUA_DATA = " + json.dumps(app_data, ensure_ascii=False, indent=2) + ";\n")

print(f"data.js generated successfully at {output_path} with {len(days)} days.")
