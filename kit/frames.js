const {chromium}=require('playwright-core');
const [,,html,out,dur,fps,only]=process.argv;
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
const p=await b.newPage({viewport:{width:1080,height:1920}});
await p.goto('file://'+process.cwd()+'/'+html);await p.evaluate(async()=>{await document.fonts.ready;await Promise.all([...document.images].map(i=>i.decode().catch(()=>{})))});
require('fs').mkdirSync(out,{recursive:true});
const times= only? only.split(',').map(Number) : [...Array(Math.round(dur*fps)).keys()].map(i=>i/fps);
let i=0;for(const t of times){await p.evaluate(t=>seek(t),t);await p.screenshot({path:`${out}/f${String(i++).padStart(5,'0')}.jpg`,type:'jpeg',quality:92});}
await b.close();})();
