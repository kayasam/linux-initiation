// Exercise the authored interactions without requiring a browser installation.
import fs from 'node:fs';
import vm from 'node:vm';
import assert from 'node:assert/strict';
const html=fs.readFileSync(new URL('../templates/introduction-interactive.html',import.meta.url),'utf8');
const elements=[];
const base='file:///course/cours/01-comprendre-linux/01-comprendre-linux.html';
class Element{
  constructor(attrs={}){this.attrs=attrs;this.id=attrs.id;this.dataset={};for(const [k,v]of Object.entries(attrs))if(k.startsWith('data-'))this.dataset[k.slice(5).replace(/-([a-z])/g,(_,c)=>c.toUpperCase())]=v;this.events={};this.children=[];this.style={};this.textContent='';this.hidden='hidden'in attrs;}
  setAttribute(k,v){this.attrs[k]=String(v)}getAttribute(k){return this.attrs[k]??null}
  addEventListener(k,f){this.events[k]=f}click(){this.events.click?.({})}
  focus(){document.activeElement=this}scrollIntoView(){}
  replaceChildren(...nodes){this.children=nodes}appendChild(node){this.children.push(node)}
  querySelector(selector){assert.equal(selector,'.check');return this.check??=new Element()}
  get src(){return new URL(this.attrs.src??'',base).href}set src(v){this.attrs.src=v}
}
for(const match of html.matchAll(/<([a-z][a-z0-9-]*)\b([^>]*)>/gi)){
  const attrs=Object.fromEntries([...match[2].matchAll(/([\w-]+)="([^"]*)"/g)].map(m=>[m[1],m[2]]));
  if(/\bhidden\b/.test(match[2]))attrs.hidden='';
  if(attrs.id||attrs.role||Object.keys(attrs).some(k=>k.startsWith('data-'))||attrs.class?.includes('assembly-meter'))elements.push(new Element(attrs));
}
const document={getElementById(id){const e=elements.find(e=>e.id===id);assert.ok(e,'Missing '+id);return e;},querySelectorAll(selector){
  if(selector==='[role="tab"]')return elements.filter(e=>e.attrs.role==='tab');
  const attr=selector.match(/^\[([^\]]+)\]$/)?.[1];assert.ok(attr,'Unsupported '+selector);return elements.filter(e=>attr in e.attrs);
},querySelector(selector){assert.equal(selector,'.assembly-meter');return elements.find(e=>e.attrs.class?.includes('assembly-meter'));},createElement(){return new Element()}};
const script=[...html.matchAll(/<script>([\s\S]*?)<\/script>/g)].at(-1)[1];
vm.runInNewContext(script,{document,URL,Set});
const tabs=document.querySelectorAll('[role="tab"]');assert.equal(tabs.length,5);
for(const tab of tabs){tab.click();assert.equal(tabs.filter(t=>t.getAttribute('aria-selected')==='true').length,1);assert.equal(document.getElementById(tab.getAttribute('aria-controls')).hidden,false)}
tabs[0].events.keydown({key:'End',preventDefault(){}});assert.equal(document.activeElement,tabs.at(-1));
tabs.at(-1).events.keydown({key:'ArrowRight',preventDefault(){}});assert.equal(document.activeElement,tabs[0]);
tabs[0].events.keydown({key:'ArrowLeft',preventDefault(){}});assert.equal(document.activeElement,tabs.at(-1));
const eras=document.querySelectorAll('[data-era]');assert.equal(eras.length,5);
eras.forEach((button,i)=>{button.click();assert.equal(document.getElementById('era-counter').textContent,`Étape ${i+1} / 5`);assert.equal(eras.filter(e=>e.getAttribute('aria-pressed')==='true').length,1)});
document.getElementById('next-era').click();assert.equal(document.getElementById('era-counter').textContent,'Étape 1 / 5');
eras[1].click();assert.equal(document.getElementById('story-person').textContent,'Richard Stallman');assert.match(document.getElementById('story-photo').src,/richard-stallman\.jpg$/);
eras[3].click();assert.equal(document.getElementById('story-person').textContent,'Linus Torvalds');assert.match(document.getElementById('story-photo').src,/linus-torvalds\.jpg$/);
document.querySelectorAll('[data-part]').forEach(button=>button.click());assert.equal(document.getElementById('assembly-count').textContent,'4 / 4 pièces');assert.equal(document.querySelector('.assembly-meter').getAttribute('aria-valuenow'),'4');assert.equal(document.getElementById('assembly-lines').children.length,4);
document.getElementById('reset-assembly').click();assert.equal(document.getElementById('assembly-count').textContent,'0 / 4 pièces');
for(const button of document.querySelectorAll('[data-answer]')){button.click();assert.match(document.getElementById('rights-feedback').textContent,button.dataset.answer==='no'?/^Bien vu/:/^Pas tout/)}
for(const button of document.querySelectorAll('[data-license]')){button.click();assert.match(document.getElementById('license-name').textContent,button.dataset.license==='mit'?/MIT/:/GPL/);assert.equal(document.getElementById('license-tags').children.length,2)}
assert.match(html,/youtube\.com\/embed\/oL6YcXLegC0/);
// Check new colored text against both shared surfaces.
const luminance=hex=>{const c=hex.match(/[a-f\d]{2}/gi).map(x=>parseInt(x,16)/255).map(x=>x<=.04045?x/12.92:((x+.055)/1.055)**2.4);return c[0]*.2126+c[1]*.7152+c[2]*.0722};
for(const [theme,background]of [['light','#ffffff'],['dark','#192936']]){
 const css=html.match(new RegExp('html\\[data-theme="'+theme+'"\\]\\{([^}]+)'))[1];
 for(const [,name,color]of css.matchAll(/--(amber|violet|rose|blue|mint):\s*(#[a-f\d]{6})/gi)){
  const a=luminance(color),b=luminance(background),contrast=(Math.max(a,b)+.05)/(Math.min(a,b)+.05);assert.ok(contrast>=4.5,`${theme} ${name}: ${contrast}`);
 }
}
console.log('Introduction: 5 tabs and keyboard navigation; 5 timeline steps/portraits; assembly/reset; license interactions; video; 10 new text contrast pairs >= 4.5:1.');
