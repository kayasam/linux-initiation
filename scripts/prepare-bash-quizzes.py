"""Generate six Bash quizzes using the shared Linux quiz UI and engine."""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

def populate(source,destination,courses):
    authored=json.loads((source/'Ressources/quiz/bash-questions.json').read_text(encoding='utf-8'))
    assert set(authored)=={p.stem for p in courses}
    template=(ROOT/'site-content/quiz-template.html').read_text(encoding='utf-8').replace('Linux — Initiation','Bash — Débutant')
    online={};offline={};export={'Ressources/quiz/bash-questions.json':(source/'Ressources/quiz/bash-questions.json').read_bytes()}
    for course in courses:
        slug=course.stem;key='bash-'+slug
        questions=[]
        for i,q in enumerate(authored[slug]):
            answer=i%4;choices=[v for j,v in enumerate(q['choices']) if j!=q['answer']]
            choices.insert(answer,q['choices'][q['answer']])
            assert len(choices)==len(set(choices))==4 and q['explanation']
            questions.append({**q,'choices':choices,'answer':answer})
        assert len(questions)==20 and len({q['question'] for q in questions})==20
        assert [sum(q['answer']==i for q in questions) for i in range(4)]==[5]*4
        title=course.read_text(encoding='utf-8').splitlines()[0].removeprefix('# ')
        bank=dict(id=key,title=title,chapter='Bash — Chapitre '+slug[:2],track='Bash',intro='Vérifie les notions du cours. Chaque réponse est expliquée.',questions=questions)
        online[key]={**bank,'chapterLink':'../../'+slug+'/'}
        offline[key]={**bank,'chapterLink':slug+'.html'}
        page=template.replace('__CHAPTER__',key)
        local=page.replace('../'+key,slug+'.html')
        quiz=course.with_name(slug+'-quiz.html');quiz.write_text(local,encoding='utf-8')
        export[quiz.relative_to(source).as_posix()]=local.encode('utf-8')
        public=page.replace('../../assets/','../../../assets/').replace('../../../assets/quiz/quiz-banks.js','../../assets/quiz/quiz-banks.js').replace('../'+key,'../../'+slug+'/')
        target=destination/'bash/cours/quiz'/f'{slug}.html';target.parent.mkdir(parents=True,exist_ok=True);target.write_text(public,encoding='utf-8')
    def js(banks):return ('window.linuxQuizBanks = '+json.dumps(banks,ensure_ascii=False,indent=2)+'\n').encode('utf-8')
    target=destination/'bash/assets/quiz/quiz-banks.js';target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(js(online))
    files={'assets/quiz/quiz-banks.js':js(offline)}
    for name in ['quiz.css','quiz-engine.js']:
        files['assets/quiz/'+name]=(ROOT/'site-content/assets/quiz'/name).read_bytes()
    for theme in (ROOT/'site-content/assets/themes').glob('*'):
        if theme.is_file():files['assets/themes/'+theme.name]=theme.read_bytes()
    for name,data in files.items():
        target=source/name;target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(data)
    export.update(files)
    return export
