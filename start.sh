#!/usr/bin/env bash
PORT=8091
echo "=========================================================="
echo "  Dou'a Khatm al-Qur'an 30 — Apprentissage pas à pas      "
echo "  Disponible sur http://localhost:$PORT                   "
echo "=========================================================="
python3 -m http.server $PORT
