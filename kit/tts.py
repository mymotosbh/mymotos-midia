# Uso: python3 tts.py segs.json  -> gera seg_<k>.wav  (segs.json: {"1":["texto",1.1], ...})
# Antes: tar xjf voz/voz-ptbr-faber.tar.bz2 (cria vits-piper-pt_BR-faber-medium/) ; pip install sherpa-onnx soundfile
import sherpa_onnx, soundfile as sf, sys, json, os
d=os.path.join(os.path.dirname(os.path.abspath(__file__)),'vits-piper-pt_BR-faber-medium')+'/'
cfg=sherpa_onnx.OfflineTtsConfig(model=sherpa_onnx.OfflineTtsModelConfig(vits=sherpa_onnx.OfflineTtsVitsModelConfig(model=d+'pt_BR-faber-medium.onnx',tokens=d+'tokens.txt',data_dir=d+'espeak-ng-data'),num_threads=2))
tts=sherpa_onnx.OfflineTts(cfg); out={}
for k,(txt,speed) in json.load(open(sys.argv[1])).items():
    a=tts.generate(txt,sid=0,speed=speed); sf.write(f'seg_{k}.wav',a.samples,a.sample_rate); out[k]=round(len(a.samples)/a.sample_rate,2)
print(out)
