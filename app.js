(() => {
  const DATA = window.DOUA_DATA;
  if (!DATA || !DATA.days) {
    console.error("DOUA_DATA not loaded");
    return;
  }

  const STORAGE_KEY = "doua_khatm_30_state_v2";

  const defaultState = {
    currentDay: 1,
    currentStep: 1,
    completedDays: [],
    xp: 0,
    streak: 1,
    lastVisitDate: new Date().toISOString().slice(0, 10),
    grammMode: "sing", // "sing" (👤 Seul) or "plur" (👥 Groupe)
    langMode: "both",  // "fr", "en", or "both"
    theme: "light",
    fontSizeOffset: 0
  };

  let state = loadState();
  let currentView = "parcours";
  let drawerFilter = "all";
  let isPlayingAudio = false;
  let studioIsLooping = false;
  let fulltextAudioIndex = -1;
  let fulltextPlaying = false;
  let shadowingActive = false;

  // MediaRecorder variables
  let mediaRecorder = null;
  let audioChunks = [];
  let isRecording = false;

  function loadState() {
    try {
      const raw = localStorage.getItem(STORAGE_KEY);
      if (!raw) return { ...defaultState };
      const parsed = JSON.parse(raw);
      const today = new Date().toISOString().slice(0, 10);
      if (parsed.lastVisitDate && parsed.lastVisitDate !== today) {
        const prev = new Date(parsed.lastVisitDate);
        const curr = new Date(today);
        const diffDays = Math.round((curr - prev) / 86400000);
        if (diffDays === 1) parsed.streak = (parsed.streak || 1) + 1;
        else if (diffDays > 1) parsed.streak = 1;
        parsed.lastVisitDate = today;
      }
      return { ...defaultState, ...parsed };
    } catch {
      return { ...defaultState };
    }
  }

  function saveState() {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(state));
    renderTopStats();
  }

  function addXP(amount) {
    state.xp += amount;
    saveState();
  }

  // ==================== WEB AUDIO API (GENTLE CHIMES) ====================
  let audioCtx = null;
  function getAudioContext() {
    if (!audioCtx) {
      const AudioCtx = window.AudioContext || window.webkitAudioContext;
      if (AudioCtx) audioCtx = new AudioCtx();
    }
    return audioCtx;
  }

  function playChime(isSuccess = true) {
    try {
      const ctx = getAudioContext();
      if (!ctx) return;
      if (ctx.state === "suspended") ctx.resume();

      const osc = ctx.createOscillator();
      const gain = ctx.createGain();
      osc.connect(gain);
      gain.connect(ctx.destination);

      const now = ctx.currentTime;
      if (isSuccess) {
        osc.type = "sine";
        osc.frequency.setValueAtTime(523.25, now); // C5
        osc.frequency.exponentialRampToValueAtTime(659.25, now + 0.12); // E5
        osc.frequency.exponentialRampToValueAtTime(783.99, now + 0.25); // G5
        gain.gain.setValueAtTime(0.15, now);
        gain.gain.exponentialRampToValueAtTime(0.001, now + 0.7);
        osc.start(now);
        osc.stop(now + 0.7);
      } else {
        osc.type = "triangle";
        osc.frequency.setValueAtTime(280, now);
        osc.frequency.exponentialRampToValueAtTime(200, now + 0.2);
        gain.gain.setValueAtTime(0.12, now);
        gain.gain.exponentialRampToValueAtTime(0.001, now + 0.35);
        osc.start(now);
        osc.stop(now + 0.35);
      }
    } catch (e) {
      // Audio not permitted yet
    }
  }

  // ==================== THEME & STATS ====================
  function applyTheme() {
    document.documentElement.setAttribute("data-theme", state.theme || "light");
  }

  document.getElementById("btn-theme-toggle").addEventListener("click", () => {
    state.theme = state.theme === "dark" ? "light" : "dark";
    applyTheme();
    saveState();
  });

  function renderTopStats() {
    document.getElementById("stat-streak").textContent = state.streak;
    document.getElementById("stat-xp").textContent = state.xp;
    const completedCount = state.completedDays.length;
    document.getElementById("stat-progress-count").textContent = `${completedCount}/30`;
    document.getElementById("drawer-trigger-label").textContent = `Jour ${String(state.currentDay).padStart(2, "0")} / 30`;
    const pct = Math.round((completedCount / 30) * 100);
    document.getElementById("global-progress-fill").style.width = `${pct}%`;
  }

  // ==================== 1-CLICK GRAMMATICAL TOGGLE ====================
  const btnToggleGrammMode = document.getElementById("btn-toggle-gramm-mode");
  const grammModeIcon = document.getElementById("gramm-mode-icon");
  const grammModeText = document.getElementById("gramm-mode-text");
  const currentGrammLabel = document.getElementById("current-gramm-label");

  function updateGrammUI() {
    if (state.grammMode === "sing") {
      grammModeIcon.textContent = "👤";
      grammModeText.textContent = "Seul (Singulier)";
      currentGrammLabel.textContent = "Mode Singulier (Pour soi)";
      btnToggleGrammMode.style.borderColor = "var(--emerald)";
    } else {
      grammModeIcon.textContent = "👥";
      grammModeText.textContent = "Groupe (Pluriel)";
      currentGrammLabel.textContent = "Mode Pluriel (En groupe)";
      btnToggleGrammMode.style.borderColor = "var(--indigo)";
    }
  }

  btnToggleGrammMode.addEventListener("click", () => {
    state.grammMode = state.grammMode === "sing" ? "plur" : "sing";
    updateGrammUI();
    saveState();
    renderCurrentDay();
    initQuiz();
    renderStudio();
    renderFlashcard();
    renderFullText();
  });

  // ==================== LANGUAGE TOGGLE ====================
  const btnToggleLang = document.getElementById("btn-toggle-lang");
  const langIndicator = document.getElementById("lang-indicator");
  const frFieldBlock = document.getElementById("fr-field-block");
  const enFieldBlock = document.getElementById("en-field-block");

  function updateLangUI() {
    langIndicator.textContent = state.langMode.toUpperCase();
    if (state.langMode === "fr") {
      frFieldBlock.style.display = "block";
      enFieldBlock.style.display = "none";
    } else if (state.langMode === "en") {
      frFieldBlock.style.display = "none";
      enFieldBlock.style.display = "block";
    } else {
      frFieldBlock.style.display = "block";
      enFieldBlock.style.display = "block";
    }
  }

  btnToggleLang.addEventListener("click", () => {
    if (state.langMode === "both") state.langMode = "fr";
    else if (state.langMode === "fr") state.langMode = "en";
    else state.langMode = "both";
    updateLangUI();
    saveState();
    renderCurrentDay();
  });

  // ==================== TABS & VIEWS ====================
  const navPills = document.querySelectorAll(".segmented-nav .nav-pill");
  const views = document.querySelectorAll(".view");

  navPills.forEach(pill => {
    pill.addEventListener("click", () => {
      switchView(pill.getAttribute("data-view"));
    });
  });

  function switchView(viewName) {
    currentView = viewName;
    navPills.forEach(p => p.classList.toggle("active", p.getAttribute("data-view") === viewName));
    views.forEach(v => v.classList.toggle("active", v.id === `view-${viewName}`));
    stopAudio();

    if (viewName === "parcours") renderCurrentDay();
    else if (viewName === "studio") renderStudio();
    else if (viewName === "flashcards") renderFlashcard();
    else if (viewName === "plan") renderPlanGrid();
    else if (viewName === "fulltext") renderFullText();
  }

  // ==================== 4-STEP STEPPER LOGIC ====================
  const stepItems = document.querySelectorAll(".stepper-wrap .step-item");
  const stepPanels = document.querySelectorAll(".step-panel");

  function setStep(stepNum) {
    state.currentStep = stepNum;
    stepItems.forEach(item => {
      const s = parseInt(item.getAttribute("data-step"));
      item.classList.toggle("active", s === stepNum);
      if (s < stepNum) item.classList.add("completed");
      else item.classList.remove("completed");
    });
    stepPanels.forEach(panel => {
      panel.classList.toggle("active", panel.id === `step-panel-${stepNum}`);
    });
    window.scrollTo({ top: 0, behavior: "smooth" });
  }

  stepItems.forEach(item => {
    item.addEventListener("click", () => {
      setStep(parseInt(item.getAttribute("data-step")));
    });
  });

  document.querySelectorAll(".btn-go-step").forEach(btn => {
    btn.addEventListener("click", () => {
      const target = parseInt(btn.getAttribute("data-target"));
      setStep(target);
    });
  });

  // ==================== AUDIO MP3 & SPEECH SYNTHESIS ENGINE ====================
  const waveformBars = document.getElementById("audio-waveform");
  let currentAudioObj = null;

  function stopAudio() {
    if (currentAudioObj) {
      currentAudioObj.pause();
      currentAudioObj.currentTime = 0;
      currentAudioObj = null;
    }
    if ("speechSynthesis" in window) {
      window.speechSynthesis.cancel();
    }
    isPlayingAudio = false;
    fulltextPlaying = false;
    shadowingActive = false;
    waveformBars.classList.remove("playing");
    updatePlayButtonState(false);
    const hfBtn = document.getElementById("btn-handsfree-toggle");
    if (hfBtn) hfBtn.textContent = "▶ Lancer";
  }

  function playArabicDayAudio(dayNum, isSing, rate = 0.9, onEnd = null) {
    stopAudio();
    isPlayingAudio = true;
    waveformBars.classList.add("playing");

    const mode = isSing ? "sing" : "plur";
    const src = `audio/day_${dayNum}_${mode}.mp3`;

    currentAudioObj = new Audio(src);
    currentAudioObj.playbackRate = rate;

    currentAudioObj.onended = () => {
      isPlayingAudio = false;
      waveformBars.classList.remove("playing");
      currentAudioObj = null;
      if (onEnd) onEnd();
    };

    currentAudioObj.onerror = () => {
      console.warn("Local mp3 error, attempting online TTS stream");
      const cur = getDayData(dayNum);
      const text = isSing ? cur.ar_sing : cur.ar_plur;
      const url = `https://translate.google.com/translate_tts?ie=UTF-8&tl=ar&client=tw-ob&q=${encodeURIComponent(text)}`;
      currentAudioObj = new Audio(url);
      currentAudioObj.playbackRate = rate;
      currentAudioObj.onended = () => {
        isPlayingAudio = false;
        waveformBars.classList.remove("playing");
        currentAudioObj = null;
        if (onEnd) onEnd();
      };
      currentAudioObj.onerror = () => {
        speakArabicFallback(text, rate, onEnd);
      };
      currentAudioObj.play().catch(() => speakArabicFallback(text, rate, onEnd));
    };

    currentAudioObj.play().catch(e => {
      console.warn("Audio play blocked or error:", e);
      const cur = getDayData(dayNum);
      const text = isSing ? cur.ar_sing : cur.ar_plur;
      speakArabicFallback(text, rate, onEnd);
    });
  }

  function playVocabAudio(word) {
    stopAudio();
    const clean = word.replace(/[،.*]/g, "").trim();
    const url = `https://translate.google.com/translate_tts?ie=UTF-8&tl=ar&client=tw-ob&q=${encodeURIComponent(clean)}`;
    const a = new Audio(url);
    a.play().catch(() => speakArabicFallback(clean, 0.85));
  }

  function speakArabicFallback(text, rate = 0.9, onEnd = null) {
    if (!("speechSynthesis" in window)) {
      isPlayingAudio = false;
      waveformBars.classList.remove("playing");
      if (onEnd) onEnd();
      return;
    }
    window.speechSynthesis.cancel();
    isPlayingAudio = true;
    waveformBars.classList.add("playing");

    const utter = new SpeechSynthesisUtterance(text);
    utter.lang = "ar-SA";
    utter.rate = rate;

    const voices = window.speechSynthesis.getVoices();
    const arVoice = voices.find(v => v.lang.startsWith("ar"));
    if (arVoice) utter.voice = arVoice;

    utter.onend = () => {
      isPlayingAudio = false;
      waveformBars.classList.remove("playing");
      if (onEnd) onEnd();
    };
    utter.onerror = () => {
      isPlayingAudio = false;
      waveformBars.classList.remove("playing");
      if (onEnd) onEnd();
    };

    window.speechSynthesis.speak(utter);
  }

  if ("speechSynthesis" in window) {
    window.speechSynthesis.onvoiceschanged = () => {
      window.speechSynthesis.getVoices();
    };
  }

  // ==================== RENDER DAY (STEP 1 & 2) ====================
  const dayBadge = document.getElementById("day-badge");
  const categoryBadge = document.getElementById("category-badge");
  const dayTitle = document.getElementById("day-title");
  const prayerArabic = document.getElementById("prayer-arabic");
  const prayerPhonetic = document.getElementById("prayer-phonetic");
  const prayerFr = document.getElementById("prayer-fr");
  const prayerEn = document.getElementById("prayer-en");
  const vocabGrid = document.getElementById("vocab-grid");
  const reflectionText = document.getElementById("reflection-text");
  const reflectionHeading = document.getElementById("reflection-heading");
  const btnValidate = document.getElementById("btn-validate-day");
  const btnValidateLabel = document.getElementById("btn-validate-label");
  const btnPrevDay = document.getElementById("btn-prev-day");
  const btnNextDay = document.getElementById("btn-next-day");
  const btnPlayAudio = document.getElementById("btn-play-audio");
  const btnPlayLabel = document.getElementById("btn-play-label");
  const speedSelect = document.getElementById("audio-speed-select");
  const btnRepeatAudio = document.getElementById("btn-repeat-audio");
  const recorderPromptAr = document.getElementById("recorder-prompt-ar");

  function getDayData(dayNum) {
    return DATA.days.find(d => d.day === dayNum) || DATA.days[0];
  }

  function renderCurrentDay() {
    const cur = getDayData(state.currentDay);
    const isSing = state.grammMode === "sing";

    dayBadge.textContent = `Jour ${cur.day} sur 30`;
    categoryBadge.textContent = cur.category || "Invocations";
    dayTitle.textContent = state.langMode === "en" ? cur.title_en : cur.title_fr;

    // Main Arabic & Translations
    const activeArabic = isSing ? cur.ar_sing : cur.ar_plur;
    prayerArabic.textContent = activeArabic;
    prayerPhonetic.textContent = isSing ? cur.phon_sing : cur.phon_plur;
    prayerFr.textContent = isSing ? cur.fr_sing : cur.fr_plur;
    prayerEn.textContent = isSing ? cur.en_sing : cur.en_plur;
    recorderPromptAr.textContent = activeArabic;

    // Vocab Grid
    vocabGrid.innerHTML = "";
    (cur.vocab || []).forEach(v => {
      const card = document.createElement("div");
      card.className = "vocab-card";
      card.innerHTML = `
        <div class="vocab-ar">${v.ar}</div>
        <div class="vocab-phon">${v.phon}</div>
        <div class="vocab-meanings">
          <div style="font-weight: 600; color: var(--ink);">${v.fr}</div>
          <div style="color: var(--ink-muted); font-style: italic;">${v.en}</div>
        </div>
      `;
      card.addEventListener("click", () => {
        const wordToPlay = v.ar.split("/")[isSing ? 0 : (v.ar.includes("/") ? 1 : 0)].trim();
        playVocabAudio(wordToPlay);
      });
      vocabGrid.appendChild(card);
    });

    // Spiritual Reflection
    if (state.langMode === "en") {
      reflectionHeading.textContent = "Spiritual Wisdom & Inner Contemplation";
      reflectionText.textContent = cur.reflection_en;
    } else {
      reflectionHeading.textContent = "Méditation Spirituelle & Sagesse";
      reflectionText.textContent = cur.reflection_fr;
    }

    // Prev / Next button state
    btnPrevDay.disabled = state.currentDay <= 1;
    btnNextDay.disabled = state.currentDay >= 30;

    // Validation Status
    const isDone = state.completedDays.includes(state.currentDay);
    if (isDone) {
      btnValidate.classList.add("completed");
      btnValidateLabel.textContent = "✓ Jour validé (+25 XP acquis)";
    } else {
      btnValidate.classList.remove("completed");
      btnValidateLabel.textContent = "Valider ce jour (+25 XP)";
    }

    initQuiz();
    renderDrawerList();
    renderTopStats();
  }

  // Audio Play in Step 1
  function updatePlayButtonState(playing) {
    if (playing) {
      btnPlayAudio.classList.add("playing");
      btnPlayLabel.textContent = "Arrêter";
    } else {
      btnPlayAudio.classList.remove("playing");
      btnPlayLabel.textContent = "Écouter";
    }
  }

  btnPlayAudio.addEventListener("click", () => {
    if (isPlayingAudio) {
      stopAudio();
    } else {
      const isSing = state.grammMode === "sing";
      const rate = parseFloat(speedSelect.value) || 0.9;
      updatePlayButtonState(true);
      playArabicDayAudio(state.currentDay, isSing, rate, () => {
        updatePlayButtonState(false);
      });
    }
  });

  btnRepeatAudio.addEventListener("click", () => {
    stopAudio();
    const isSing = state.grammMode === "sing";
    const rate = parseFloat(speedSelect.value) || 0.9;
    let count = 0;

    function loopOnce() {
      if (count >= 3) {
        updatePlayButtonState(false);
        return;
      }
      count++;
      updatePlayButtonState(true);
      playArabicDayAudio(state.currentDay, isSing, rate, () => {
        setTimeout(loopOnce, 600);
      });
    }
    loopOnce();
  });

  // Hands-free Shadowing Coach
  const btnHandsfree = document.getElementById("btn-handsfree-toggle");
  const hfStatusText = document.getElementById("hf-status-text");

  btnHandsfree.addEventListener("click", () => {
    if (shadowingActive) {
      stopAudio();
      return;
    }

    shadowingActive = true;
    btnHandsfree.textContent = "⏸ Arrêter";
    const isSing = state.grammMode === "sing";

    // Phase 1: Slow listen
    hfStatusText.textContent = "🎧 Écoutez attentivement (0.75x)...";
    updatePlayButtonState(true);
    playArabicDayAudio(state.currentDay, isSing, 0.75, () => {
      if (!shadowingActive) return;
      playChime(true);
      hfStatusText.textContent = "🗣️ À vous de réciter à voix haute ! (Pause 4s)";
      waveformBars.classList.remove("playing");

      setTimeout(() => {
        if (!shadowingActive) return;
        hfStatusText.textContent = "🎧 Réécoute à vitesse normale (1.0x)...";
        updatePlayButtonState(true);
        playArabicDayAudio(state.currentDay, isSing, 1.0, () => {
          if (!shadowingActive) return;
          playChime(true);
          hfStatusText.textContent = "✓ Récitation terminée ! Prêt pour le vocabulaire.";
          shadowingActive = false;
          btnHandsfree.textContent = "▶ Relancer";
          updatePlayButtonState(false);
        });
      }, 4200);
    });
  });

  // Blurs & Font Size
  document.getElementById("btn-blur-ar").addEventListener("click", e => {
    prayerArabic.classList.toggle("field-blur");
    e.target.classList.toggle("active");
  });
  document.getElementById("btn-blur-phon").addEventListener("click", e => {
    prayerPhonetic.classList.toggle("field-blur");
    e.target.classList.toggle("active");
  });
  document.getElementById("btn-blur-tr").addEventListener("click", e => {
    prayerFr.classList.toggle("field-blur");
    prayerEn.classList.toggle("field-blur");
    e.target.classList.toggle("active");
  });

  document.getElementById("btn-font-bigger").addEventListener("click", () => {
    state.fontSizeOffset = Math.min(state.fontSizeOffset + 0.25, 1.25);
    prayerArabic.style.fontSize = `${2.5 + state.fontSizeOffset}rem`;
  });
  document.getElementById("btn-font-smaller").addEventListener("click", () => {
    state.fontSizeOffset = Math.max(state.fontSizeOffset - 0.25, -0.6);
    prayerArabic.style.fontSize = `${2.5 + state.fontSizeOffset}rem`;
  });

  // Day navigation Prev / Next
  btnPrevDay.addEventListener("click", () => {
    if (state.currentDay > 1) {
      stopAudio();
      state.currentDay--;
      state.currentStep = 1;
      saveState();
      renderCurrentDay();
      setStep(1);
    }
  });

  btnNextDay.addEventListener("click", () => {
    if (state.currentDay < 30) {
      stopAudio();
      state.currentDay++;
      state.currentStep = 1;
      saveState();
      renderCurrentDay();
      setStep(1);
    }
  });

  // ==================== STEP 3: INTERACTIVE QUIZ PUZZLE ====================
  const quizMeaning = document.getElementById("quiz-meaning");
  const quizSlots = document.getElementById("quiz-slots");
  const quizPool = document.getElementById("quiz-pool");
  const quizFeedback = document.getElementById("quiz-feedback");
  const btnQuizCheck = document.getElementById("btn-quiz-check");
  const btnQuizReset = document.getElementById("btn-quiz-reset");

  let quizWordsTarget = [];
  let quizWordsSelected = [];
  let quizWordsPool = [];

  function cleanWord(w) {
    return w.replace(/[،.*]/g, "").trim();
  }

  function initQuiz() {
    const cur = getDayData(state.currentDay);
    const isSing = state.grammMode === "sing";
    const rawArabic = isSing ? cur.ar_sing : cur.ar_plur;
    quizMeaning.textContent = `"${isSing ? cur.fr_sing : cur.fr_plur}"`;

    quizWordsTarget = rawArabic.split(/\s+/).map(cleanWord).filter(Boolean);
    quizWordsSelected = [];
    quizWordsPool = [...quizWordsTarget].sort(() => Math.random() - 0.5);

    quizFeedback.textContent = "";
    quizFeedback.className = "quiz-feedback";
    renderQuizBoard();
  }

  function renderQuizBoard() {
    quizSlots.innerHTML = "";
    quizPool.innerHTML = "";

    if (quizWordsSelected.length === 0) {
      quizSlots.innerHTML = `<span style="color: var(--ink-muted); font-size: 0.9rem; font-style: italic;">Touchez les mots ci-dessous pour reconstituer la phrase...</span>`;
    } else {
      quizWordsSelected.forEach((word, idx) => {
        const chip = document.createElement("button");
        chip.className = "quiz-word-chip";
        chip.style.borderColor = "var(--gold-light)";
        chip.textContent = word;
        chip.addEventListener("click", () => {
          quizWordsSelected.splice(idx, 1);
          quizWordsPool.push(word);
          renderQuizBoard();
        });
        quizSlots.appendChild(chip);
      });
    }

    quizWordsPool.forEach((word, idx) => {
      const chip = document.createElement("button");
      chip.className = "quiz-word-chip";
      chip.textContent = word;
      chip.addEventListener("click", () => {
        quizWordsPool.splice(idx, 1);
        quizWordsSelected.push(word);
        renderQuizBoard();
      });
      quizPool.appendChild(chip);
    });
  }

  btnQuizReset.addEventListener("click", initQuiz);

  btnQuizCheck.addEventListener("click", () => {
    if (quizWordsSelected.length !== quizWordsTarget.length) {
      quizFeedback.textContent = "⚠️ Veuillez placer tous les mots avant de vérifier.";
      quizFeedback.className = "quiz-feedback error";
      playChime(false);
      return;
    }

    const isCorrect = quizWordsSelected.every((w, i) => cleanWord(w) === cleanWord(quizWordsTarget[i]));
    if (isCorrect) {
      quizFeedback.textContent = "🎉 Excellent ! Vous avez parfaitement reconstitué la phrase (+15 XP) !";
      quizFeedback.className = "quiz-feedback success";
      playChime(true);
      addXP(15);
      triggerConfetti();
    } else {
      quizFeedback.textContent = "❌ L'ordre n'est pas tout à fait correct. Réessayez ou réinitialisez !";
      quizFeedback.className = "quiz-feedback error";
      playChime(false);
    }
  });

  // ==================== STEP 4: MICROPHONE VOICE RECORDER ====================
  const btnRecordMic = document.getElementById("btn-record-mic");
  const recordStatusLabel = document.getElementById("record-status-label");
  const userAudioPreview = document.getElementById("user-audio-preview");
  const recordedAudioEl = document.getElementById("recorded-audio-element");

  btnRecordMic.addEventListener("click", async () => {
    if (!isRecording) {
      try {
        const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
        mediaRecorder = new MediaRecorder(stream);
        audioChunks = [];

        mediaRecorder.ondataavailable = e => {
          if (e.data.size > 0) audioChunks.push(e.data);
        };

        mediaRecorder.onstop = () => {
          const audioBlob = new Blob(audioChunks, { type: "audio/webm" });
          const audioUrl = URL.createObjectURL(audioBlob);
          recordedAudioEl.src = audioUrl;
          userAudioPreview.style.display = "block";
          recordStatusLabel.textContent = "✓ Enregistrement prêt ! Écoutez votre voix ci-dessous.";
          stream.getTracks().forEach(t => t.stop());
        };

        mediaRecorder.start();
        isRecording = true;
        btnRecordMic.classList.add("recording");
        recordStatusLabel.textContent = "🔴 Enregistrement en cours... Récitez la phrase !";
      } catch (err) {
        alert("Impossible d'accéder au microphone. Veuillez autoriser l'accès micro dans votre navigateur.");
      }
    } else {
      if (mediaRecorder && mediaRecorder.state !== "inactive") {
        mediaRecorder.stop();
      }
      isRecording = false;
      btnRecordMic.classList.remove("recording");
    }
  });

  // Validate Day
  btnValidate.addEventListener("click", () => {
    const isDone = state.completedDays.includes(state.currentDay);
    if (!isDone) {
      state.completedDays.push(state.currentDay);
      addXP(25);
      playChime(true);
      triggerConfetti();
      renderCurrentDay();
    } else {
      state.completedDays = state.completedDays.filter(d => d !== state.currentDay);
      saveState();
      renderCurrentDay();
    }
  });

  // Copy buttons
  document.querySelectorAll(".copy-btn").forEach(btn => {
    btn.addEventListener("click", () => {
      const targetId = btn.getAttribute("data-target");
      const el = document.getElementById(targetId);
      if (el) {
        navigator.clipboard.writeText(el.textContent);
        playChime(true);
      }
    });
  });

  // ==================== DRAWER ====================
  const drawer = document.getElementById("blocks-drawer");
  const drawerBackdrop = document.getElementById("drawer-backdrop");
  const drawerList = document.getElementById("drawer-days-list");
  const blockSearch = document.getElementById("block-search");
  const filterPills = document.querySelectorAll(".drawer-search-area .filter-pill");

  function openDrawer() {
    drawer.classList.add("open");
    drawerBackdrop.classList.add("open");
  }
  function closeDrawer() {
    drawer.classList.remove("open");
    drawerBackdrop.classList.remove("open");
  }

  document.getElementById("btn-open-drawer").addEventListener("click", openDrawer);
  document.getElementById("btn-close-drawer").addEventListener("click", closeDrawer);
  drawerBackdrop.addEventListener("click", closeDrawer);

  filterPills.forEach(pill => {
    pill.addEventListener("click", () => {
      filterPills.forEach(p => p.classList.remove("active"));
      pill.classList.add("active");
      drawerFilter = pill.getAttribute("data-filter");
      renderDrawerList();
    });
  });

  blockSearch.addEventListener("input", renderDrawerList);

  function renderDrawerList() {
    drawerList.innerHTML = "";
    const query = (blockSearch.value || "").toLowerCase().trim();
    const isSing = state.grammMode === "sing";

    DATA.days.forEach(d => {
      const isDone = state.completedDays.includes(d.day);
      if (drawerFilter === "todo" && isDone) return;
      if (drawerFilter === "done" && !isDone) return;

      if (query) {
        const textToMatch = `${d.title_fr} ${d.title_en} ${d.ar_sing} ${d.ar_plur} ${d.phon_sing} ${d.phon_plur} ${d.fr_sing} ${d.en_sing}`.toLowerCase();
        if (!textToMatch.includes(query)) return;
      }

      const item = document.createElement("div");
      item.className = `drawer-item ${d.day === state.currentDay ? "active" : ""} ${isDone ? "completed" : ""}`;
      item.innerHTML = `
        <div class="drawer-item-left">
          <div class="day-badge-num">${isDone ? "✓" : d.day}</div>
          <div class="drawer-item-text">
            <div class="drawer-item-title">${state.langMode === "en" ? d.title_en : d.title_fr}</div>
            <div class="drawer-item-sub">${isSing ? d.ar_sing : d.ar_plur}</div>
          </div>
        </div>
      `;
      item.addEventListener("click", () => {
        stopAudio();
        state.currentDay = d.day;
        state.currentStep = 1;
        saveState();
        renderCurrentDay();
        renderStudio();
        renderFlashcard();
        setStep(1);
        closeDrawer();
      });
      drawerList.appendChild(item);
    });
  }

  // ==================== STUDIO VIEW ====================
  const studioDayTag = document.getElementById("studio-day-tag");
  const studioAr = document.getElementById("studio-ar");
  const studioPhon = document.getElementById("studio-phon");
  const studioTr = document.getElementById("studio-tr");
  const studioBtnPlay = document.getElementById("studio-btn-play");
  const studioBtnPlayLabel = document.getElementById("studio-btn-play-label");
  const studioBtnLoop = document.getElementById("studio-btn-loop");
  const studioBtnPrev = document.getElementById("studio-btn-prev");
  const studioBtnNext = document.getElementById("studio-btn-next");

  function renderStudio() {
    const cur = getDayData(state.currentDay);
    const isSing = state.grammMode === "sing";
    studioDayTag.textContent = `Jour ${cur.day} / 30 · ${isSing ? "Singulier 👤" : "Pluriel 👥"}`;
    studioAr.textContent = isSing ? cur.ar_sing : cur.ar_plur;
    studioPhon.textContent = isSing ? cur.phon_sing : cur.phon_plur;
    studioTr.textContent = isSing ? cur.fr_sing : cur.fr_plur;
  }

  studioBtnPlay.addEventListener("click", () => {
    if (isPlayingAudio) {
      stopAudio();
      studioBtnPlayLabel.textContent = "Écouter";
      studioBtnPlay.classList.remove("playing");
    } else {
      const isSing = state.grammMode === "sing";
      studioBtnPlayLabel.textContent = "Arrêter";
      studioBtnPlay.classList.add("playing");

      function playLoop() {
        playArabicDayAudio(state.currentDay, isSing, 0.9, () => {
          if (studioIsLooping && currentView === "studio") {
            setTimeout(playLoop, 700);
          } else {
            studioBtnPlayLabel.textContent = "Écouter";
            studioBtnPlay.classList.remove("playing");
          }
        });
      }
      playLoop();
    }
  });

  studioBtnLoop.addEventListener("click", () => {
    studioIsLooping = !studioIsLooping;
    studioBtnLoop.classList.toggle("active", studioIsLooping);
    studioBtnLoop.querySelector("span").textContent = `Boucle : ${studioIsLooping ? "ON 🔁" : "OFF"}`;
  });

  studioBtnPrev.addEventListener("click", () => {
    if (state.currentDay > 1) {
      stopAudio();
      state.currentDay--;
      saveState();
      renderStudio();
    }
  });

  studioBtnNext.addEventListener("click", () => {
    if (state.currentDay < 30) {
      stopAudio();
      state.currentDay++;
      saveState();
      renderStudio();
    }
  });

  // ==================== FLASHCARDS VIEW ====================
  const fcCard = document.getElementById("fc-card");
  const fcFrontText = document.getElementById("fc-front-text");
  const fcBackPhon = document.getElementById("fc-back-phon");
  const fcBackFr = document.getElementById("fc-back-fr");
  const fcBackEn = document.getElementById("fc-back-en");
  const fcBtnPrev = document.getElementById("fc-btn-prev");
  const fcBtnNext = document.getElementById("fc-btn-next");

  fcCard.addEventListener("click", () => {
    fcCard.classList.toggle("flipped");
    playChime(true);
  });

  function renderFlashcard() {
    fcCard.classList.remove("flipped");
    const cur = getDayData(state.currentDay);
    const isSing = state.grammMode === "sing";
    fcFrontText.textContent = isSing ? cur.ar_sing : cur.ar_plur;
    fcBackPhon.textContent = isSing ? cur.phon_sing : cur.phon_plur;
    fcBackFr.textContent = isSing ? cur.fr_sing : cur.fr_plur;
    fcBackEn.textContent = isSing ? cur.en_sing : cur.en_plur;
  }

  fcBtnPrev.addEventListener("click", () => {
    if (state.currentDay > 1) {
      state.currentDay--;
      saveState();
      renderFlashcard();
    }
  });

  fcBtnNext.addEventListener("click", () => {
    if (state.currentDay < 30) {
      state.currentDay++;
      saveState();
      renderFlashcard();
    }
  });

  // ==================== PLAN 30J ====================
  const planGrid = document.getElementById("plan-grid");

  function renderPlanGrid() {
    planGrid.innerHTML = "";
    const isSing = state.grammMode === "sing";

    DATA.days.forEach(d => {
      const isDone = state.completedDays.includes(d.day);
      const isCurrent = d.day === state.currentDay;
      const box = document.createElement("div");
      box.className = `plan-day-box ${isDone ? "completed" : ""} ${isCurrent ? "current" : ""}`;
      box.innerHTML = `
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
          <span style="font-size: 0.75rem; font-weight: 800; color: var(--gold);">JOUR ${String(d.day).padStart(2, "0")}</span>
          <span style="font-size: 0.78rem; font-weight: 700;">${isDone ? "✓ Maîtrisé" : "À faire"}</span>
        </div>
        <div style="font-size: 0.9rem; font-weight: 700; margin-bottom: 0.4rem;">${state.langMode === "en" ? d.title_en : d.title_fr}</div>
        <div style="font-family: var(--arabic-font); font-size: 1.15rem; color: var(--emerald); direction: rtl; text-align: right; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">
          ${isSing ? d.ar_sing : d.ar_plur}
        </div>
      `;
      box.addEventListener("click", () => {
        state.currentDay = d.day;
        state.currentStep = 1;
        saveState();
        switchView("parcours");
        setStep(1);
      });
      planGrid.appendChild(box);
    });
  }

  // ==================== TEXTE INTÉGRAL ====================
  const fulltextSubtitle = document.getElementById("fulltext-subtitle");
  const fulltextRowsContainer = document.getElementById("fulltext-rows-container");
  const btnFulltextPlayall = document.getElementById("btn-fulltext-playall");

  function renderFullText() {
    const isSing = state.grammMode === "sing";
    fulltextSubtitle.textContent = `Texte intégral complet — Version ${isSing ? "👤 Singulier (Prière individuelle)" : "👥 Pluriel (En groupe / Assemblée)"}`;
    fulltextRowsContainer.innerHTML = "";

    DATA.days.forEach(d => {
      const row = document.createElement("div");
      row.className = "fulltext-row";
      row.id = `fulltext-row-${d.day}`;
      row.innerHTML = `
        <div class="fulltext-ar">${isSing ? d.ar_sing : d.ar_plur}</div>
        <div style="font-weight: 700; color: var(--indigo); font-size: 0.95rem;">${isSing ? d.phon_sing : d.phon_plur}</div>
        <div style="font-size: 0.95rem; color: var(--ink);">${isSing ? d.fr_sing : d.fr_plur}</div>
        <div style="font-size: 0.85rem; color: var(--ink-muted); font-style: italic;">${isSing ? d.en_sing : d.en_plur}</div>
      `;
      fulltextRowsContainer.appendChild(row);
    });
  }

  btnFulltextPlayall.addEventListener("click", () => {
    if (fulltextPlaying) {
      stopAudio();
      btnFulltextPlayall.querySelector("span").textContent = "Écouter toute la Dou'a d'une traite";
      return;
    }

    fulltextPlaying = true;
    fulltextAudioIndex = 0;
    btnFulltextPlayall.querySelector("span").textContent = "Arrêter la lecture intégrale";
    playNextFulltextSentence();
  });

  function playNextFulltextSentence() {
    if (!fulltextPlaying || fulltextAudioIndex >= DATA.days.length) {
      fulltextPlaying = false;
      btnFulltextPlayall.querySelector("span").textContent = "Écouter toute la Dou'a d'une traite";
      return;
    }

    const cur = DATA.days[fulltextAudioIndex];
    const isSing = state.grammMode === "sing";
    const text = isSing ? cur.ar_sing : cur.ar_plur;

    document.querySelectorAll(".fulltext-row").forEach(r => r.style.background = "transparent");
    const activeRow = document.getElementById(`fulltext-row-${cur.day}`);
    if (activeRow) {
      activeRow.style.background = "var(--emerald-soft)";
      activeRow.scrollIntoView({ behavior: "smooth", block: "center" });
    }

    playArabicDayAudio(cur.day, isSing, 0.9, () => {
      if (fulltextPlaying) {
        fulltextAudioIndex++;
        setTimeout(playNextFulltextSentence, 500);
      }
    });
  }

  // ==================== CELEBRATION CONFETTI ====================
  function triggerConfetti() {
    const canvas = document.getElementById("celebration-canvas");
    const ctx = canvas.getContext("2d");
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;

    const colors = ["#f59e0b", "#10b981", "#059669", "#6366f1", "#ec4899", "#d97706"];
    const particles = [];
    for (let i = 0; i < 110; i++) {
      particles.push({
        x: canvas.width / 2,
        y: canvas.height / 2,
        vx: (Math.random() - 0.5) * 16,
        vy: (Math.random() - 0.7) * 16,
        size: Math.random() * 9 + 4,
        color: colors[Math.floor(Math.random() * colors.length)],
        alpha: 1,
        rotation: Math.random() * 360,
        vr: (Math.random() - 0.5) * 10
      });
    }

    let frame = 0;
    function animate() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      particles.forEach(p => {
        p.x += p.vx;
        p.y += p.vy;
        p.vy += 0.35;
        p.alpha -= 0.014;
        p.rotation += p.vr;

        ctx.save();
        ctx.translate(p.x, p.y);
        ctx.rotate((p.rotation * Math.PI) / 180);
        ctx.fillStyle = p.color;
        ctx.globalAlpha = Math.max(p.alpha, 0);
        ctx.fillRect(-p.size / 2, -p.size / 2, p.size, p.size);
        ctx.restore();
      });

      frame++;
      if (frame < 85) requestAnimationFrame(animate);
      else ctx.clearRect(0, 0, canvas.width, canvas.height);
    }
    animate();
  }

  // ==================== INITIALIZATION ====================
  applyTheme();
  updateGrammUI();
  updateLangUI();
  renderTopStats();
  renderCurrentDay();
  setStep(state.currentStep || 1);
  renderDrawerList();
})();
