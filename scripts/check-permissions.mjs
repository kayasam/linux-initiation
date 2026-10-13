import fs from 'node:fs';
import vm from 'node:vm';
import assert from 'node:assert/strict';
const html=fs.readFileSync(new URL('../templates/permissions-interactive.html',import.meta.url),'utf8');
assert.ok(!/<svg|\.svg\b/i.test(html),'The HTML must contain no SVG');
const model=html.match(/<script id="permission-model">([\s\S]*?)<\/script>/)[1];
const context=vm.createContext({});vm.runInContext(model,context);const M=context.PermissionLab;
assert.equal(M.symbols('640'),'-rw-r-----');assert.equal(M.symbols('750','directory'),'drwxr-x---');
assert.equal(M.symbolic('640','u','+','x'),'740');assert.equal(M.symbolic('666','a','-','w'),'444');assert.equal(M.symbolic('777','g','=','r'),'747');assert.equal(M.symbolic('000','a','+','rw'),'666');
for(const value of ['7777','999','64','abc','','-1'])assert.equal(M.valid(value),false);
for(let mode=0;mode<512;mode++){
 const octal=mode.toString(8).padStart(3,'0');assert.equal(M.symbols(octal).length,10);
 for(const owner of ['alice','bob','camille'])for(const group of ['stagiaires','projet','visiteurs'])for(const actor of ['alice','bob','camille']){
  const category=actor===owner?'u':M.people[actor].groups.includes(group)?'g':'o';
  const shift={u:6,g:3,o:0}[category],value=Math.floor(mode/2**shift)%8;
  const r=value>=4,w=Math.floor(value/2)%2===1,x=value%2===1;
  const file=M.access(octal,'file',actor,owner,group),directory=M.access(octal,'directory',actor,owner,group);
  assert.equal(file.category,category);assert.equal(file.actions.read,r);assert.equal(file.actions.write,w);assert.equal(file.actions.execute,x);
  assert.equal(directory.actions.list,r);assert.equal(directory.actions.traverse,x);assert.equal(directory.actions.create,w&&x);assert.equal(directory.actions.remove,w&&x);
 }
}
assert.equal(M.access('077','file','alice','alice','stagiaires').actions.read,false,'Owner cannot fall back to group/others');
assert.equal(M.category('bob','alice','bob'),'g','Primary group counts');
assert.equal(M.access('200','directory','alice','alice','stagiaires').actions.create,false,'Directory w alone is insufficient');
assert.equal(M.access('300','directory','alice','alice','stagiaires').actions.create,true);
// Run the actual interface with a lightweight DOM fixture; no browser required.
const elements=[];
class Element{
 constructor(attrs={}){this.attrs=attrs;this.id=attrs.id;this.dataset={};this.value=attrs.value??'';this.checked='checked'in attrs;this.hidden='hidden'in attrs;this.events={};this.children=[];this.style={};this.textContent='';this.classes=new Set((attrs.class??'').split(' '));this.classList={toggle:(name,value)=>{value?this.classes.add(name):this.classes.delete(name)}};for(const [k,v]of Object.entries(attrs))if(k.startsWith('data-'))this.dataset[k.slice(5).replace(/-([a-z])/g,(_,c)=>c.toUpperCase())]=v;this.parentElement={querySelector:()=>this.label??=new Element()};}
 setAttribute(k,v){this.attrs[k]=String(v)}getAttribute(k){return this.attrs[k]??null}addEventListener(k,f){this.events[k]=f}click(){this.events.click?.({})}focus(){document.activeElement=this}scrollIntoView(){}replaceChildren(...nodes){this.children=nodes}appendChild(node){this.children.push(node)}append(...nodes){this.children.push(...nodes)}
}
for(const match of html.matchAll(/<([a-z][a-z0-9-]*)\b([^>]*)>/gi)){
 const attrs=Object.fromEntries([...match[2].matchAll(/([\w-]+)="([^"]*)"/g)].map(m=>[m[1],m[2]]));
 for(const key of ['checked','hidden'])if(new RegExp('\\b'+key+'\\b').test(match[2]))attrs[key]='';
 if(attrs.id||attrs.role||Object.keys(attrs).some(k=>k.startsWith('data-')))elements.push(new Element(attrs));
}
const document={getElementById(id){const element=elements.find(e=>e.id===id);assert.ok(element,'Missing '+id);return element;},querySelectorAll(selector){if(selector==='[role="tab"]')return elements.filter(e=>e.attrs.role==='tab');const attr=selector.match(/^\[([^\]]+)\]$/)?.[1];assert.ok(attr,selector);return elements.filter(e=>attr in e.attrs);},createElement(){return new Element()}};
for(const [id,value]of [['symbol-who','u'],['symbol-operation','+'],['symbol-rights','x']])document.getElementById(id).value=value;
context.document=document;vm.runInContext(html.match(/<script id="permission-interface">([\s\S]*?)<\/script>/)[1],context);
const get=id=>document.getElementById(id),find=(attr,value)=>elements.find(e=>e.dataset[attr]===value),change=(id,value,event='change')=>{get(id).value=value;get(id).events[event]({});};
const tabs=document.querySelectorAll('[role="tab"]');assert.equal(tabs.length,5);
for(const tab of tabs){tab.click();assert.equal(tabs.filter(t=>t.getAttribute('aria-selected')==='true').length,1);assert.equal(get(tab.getAttribute('aria-controls')).hidden,false);}
tabs[0].events.keydown({key:'End',preventDefault(){}});assert.equal(document.activeElement.id,'tab-test');
find('person','bob').click();find('identityCommand','sudo whoami').click();assert.match(get('identity-output').textContent,/pas autorisé/);
find('person','alice').click();assert.equal(get('identity-output').textContent,'root');
find('identityCommand','id').click();assert.match(get('identity-output').textContent,/uid=1000\(alice\).*2000\(stagiaires\).*27\(sudo\)/);
change('mode-input','077','input');assert.match(get('selected-category').textContent,/propriétaire/);assert.equal(get('access-results').children[0].children[1].textContent,'× Refusé');
change('actor','bob');assert.match(get('selected-category').textContent,/groupe/);assert.equal(get('access-results').children[0].children[1].textContent,'✓ Autorisé');
change('actor','camille');assert.match(get('selected-category').textContent,/autres/);
change('owner','camille');assert.match(get('selected-category').textContent,/propriétaire/);assert.match(get('chown-command').textContent,/camille:stagiaires/);
change('mode-input','999','input');assert.equal(get('mode-input').getAttribute('aria-invalid'),'true');assert.match(get('chmod-command').textContent,/077/);
change('mode-input','600','input');get('apply-symbolic').click();assert.match(get('chmod-command').textContent,/700/);
change('resource-type','directory');change('mode-input','200','input');assert.equal(get('access-results').children[2].children[1].textContent,'× Refusé');
change('mode-input','300','input');assert.equal(get('access-results').children[2].children[1].textContent,'✓ Autorisé');
for(const [name,mission]of Object.entries(M.missions)){
 find('mission',name).click();assert.equal(get('mission-banner').hidden,false);assert.equal(get('mode-input').value,'000');
 get('check-mission').click();assert.match(get('mission-feedback').textContent,/Pas encore/);
 change('mode-input',mission.mode,'input');get('check-mission').click();assert.match(get('mission-feedback').textContent,/Mission réussie/);
 change('mode-input','999','input');get('check-mission').click();assert.match(get('mission-feedback').textContent,/Corrigez le mode/);
}
get('exit-mission').click();assert.equal(get('mission-banner').hidden,true);
change('mode-input','750','input');const execute=find('bit','u-x');execute.checked=false;execute.events.change({});assert.equal(get('mode-input').value,'650');assert.equal(get('digit-u').textContent,6);
find('preset','600').click();assert.equal(get('mode-input').value,'600');
for(const button of document.querySelectorAll('[data-read]')){button.click();assert.ok(get('read-description').textContent.length>20)}
find('meaning','directory').click();assert.match(get('meaning-w-text').textContent,/aussi x/);
// New colored text on both theme surfaces.
const luminance=hex=>{const c=hex.match(/[a-f\d]{2}/gi).map(x=>parseInt(x,16)/255).map(x=>x<=.04045?x/12.92:((x+.055)/1.055)**2.4);return c[0]*.2126+c[1]*.7152+c[2]*.0722};
for(const [theme,bg]of [['light','#ffffff'],['dark','#192936']]){const css=html.match(new RegExp('html\\[data-theme="'+theme+'"\\]\\{([^}]+)'))[1];for(const [,color]of css.matchAll(/--(?:purple|blue|pink):\s*(#[a-f\d]{6})/gi)){const a=luminance(color),b=luminance(bg);assert.ok((Math.max(a,b)+.05)/(Math.min(a,b)+.05)>=4.5)}}
console.log('Permissions: 512 modes across 27 identity/ownership combinations; file/directory access; owner priority; symbolic chmod; tabs/keyboard; identity/sudo; validation; chown; 3 missions; 6 contrast pairs; no SVG.');
