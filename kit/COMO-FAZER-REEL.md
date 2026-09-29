# Kit de Reel MyMotos
1. `tar xjf voz/voz-ptbr-faber.tar.bz2` ; `pip install --break-system-packages sherpa-onnx soundfile` ; `npm i playwright-core @fontsource/montserrat`
2. Copie `reel-modelo.html` e adapte textos/cenas/tempos (CSS keyframes com animation-delay; `seek(t)` posiciona o tempo). Pastas: `F/` = node_modules/@fontsource/montserrat/files, `I/` = img/.
3. Narração: escreva segs.json por cena (escreva foneticamente: "Mai Motos", "i pê vê á", "uótsap", "dê cá", "Jéfi"), `python3 tts.py segs.json`, junte com ffmpeg adelay no início de cada cena.
4. Frames: `node frames.js reel.html fr <segundos> 30` (Chromium em /opt/pw-browsers/chromium).
5. MP4: ffmpeg -framerate 30 -i fr/f%05d.jpg + narração + trilha (volume 0.16) -> libx264 crf 19 yuv420p, aac 192k, +faststart, 1080x1920.
6. Olhe frames-chave antes de publicar (texto cortado, sobreposição, área dos botões do Instagram: evitar y>1550 e x>950).
Metricool: instagramData type REEL, isAiGenerated true (voz sintética).
Voz: piper pt_BR faber medium (dataset CC0).
