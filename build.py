from pathlib import Path
import json,html
root=Path(__file__).resolve().parent
d=json.loads((root/'profile-data.json').read_text());e=html.escape
for lang in ['zh','en']:
 en=lang=='en';prefix='../' if en else '';langtag='en' if en else 'zh-CN'
 T=lambda zh,eng:eng if en else zh
 link=lambda label,url:'<a href="'+e(url,quote=True)+'" target="_blank" rel="noopener noreferrer">'+e(label)+'</a>'
 name=T('欧阳瑞志','Ruizhi Ouyang');school=T('北京林业大学','Beijing Forestry University');college=T('经济管理学院','School of Economics and Management');major=T('农林经济管理','Agricultural and Forestry Economics and Management')
 nav=[('background',T('教育经历','Education')),('publications',T('精选论文','Publications')),('projects',T('公开项目','Projects')),('awards',T('奖项与荣誉','Honors'))]
 parts=['<!doctype html><html lang="'+langtag+'"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+T('欧阳瑞志｜学术主页','Ruizhi Ouyang | Academic Homepage')+'</title><meta name="description" content="'+e(T('欧阳瑞志，北京林业大学经济管理学院，系统可靠性与风险管理研究。','Ruizhi Ouyang, Beijing Forestry University. Research in system reliability and risk management.'))+'"><link rel="stylesheet" href="'+prefix+'style.css?v=20261001-mobile"><link rel="icon" href="'+prefix+'assets/favicon.svg"></head><body>']
 parts.append('<a class="skip" href="#main">'+T('跳至正文','Skip to content')+'</a><header><div class="topbar"><a class="brand" href="#top">'+T('欧阳瑞志｜学术主页','Ruizhi Ouyang | Academic Homepage')+'</a><nav aria-label="'+T('主要导航','Main navigation')+'">'+''.join('<a href="#'+id+'">'+label+'</a>' for id,label in nav)+'</nav><div class="language-switch" aria-label="'+T('语言选择','Language selection')+'"><a href="'+('../index.html' if en else 'index.html')+'" lang="zh-CN" '+('' if en else 'aria-current="page"')+'>中文</a><span>/</span><a href="'+('index.html' if en else 'en/index.html')+'" lang="en" '+('aria-current="page"' if en else '')+'>EN</a></div></div></header>')
 bio=T('我的研究关注<strong>系统可靠性与风险管理</strong>。以统计学为基础，结合机器学习与优化方法，探索系统的剩余寿命预测、维护决策与不确定性下的资源配置。','My research focuses on <strong>system reliability and risk management</strong>. With a background in statistics, I combine machine learning and optimization to study remaining useful life prediction, maintenance decisions and resource allocation under uncertainty.')
 parts.append('<main id="main"><section class="hero wrap" id="top"><div class="hero-copy"><div class="profile-heading"><h1>'+name+'</h1><p class="affiliation">'+'<span class="affiliation-item">'+school+'</span><span class="affiliation-item"><span class="affiliation-separator">·</span>'+college+'</span><span class="affiliation-item"><span class="affiliation-separator">·</span>'+major+'</span>'+'</p></div><p class="bio">'+bio+'</p>'+ (root/'contact-links.html').read_text()+'</div><figure class="portrait"><img src="'+prefix+'assets/lifestyle.jpg" alt="'+T('欧阳瑞志在湖边的生活照','Ruizhi Ouyang beside a lake')+'" width="1086" height="1448"></figure></section><div class="wrap content">')
 heading=lambda title:'<div class="section-heading"><h2>'+title+'</h2></div>'
 parts.append('<section id="background">'+heading(T('教育经历','Education'))+'<div class="education-list">')
 for date,study in [(T('在读','In progress'),major+T(' · 直博生',' · Direct-entry Ph.D.')),('2022.09–2026.06',T('统计学 · 理学学士','Statistics · B.Sc.'))]:
  date_html=date.replace('–','–<wbr>')
  college_html='<span class="education-full">'+college+'</span><span class="education-short">Econ. &amp; Management</span>' if en else college
  study_short='Agric. &amp; Forestry Econ. · Ph.D.' if date=='In progress' else 'Statistics · B.Sc.'
  study_html='<span class="education-full">'+study+'</span><span class="education-short">'+study_short+'</span>' if en else ''.join('<span class="education-unit">'+v+'</span>' for v in study.split(' · '))
  school_html='<span class="education-full">'+school+'</span><span class="education-short" title="Beijing Forestry University">Beijing<br>Forestry Univ.</span>' if en else school
  parts.append('<article class="education-row"><div class="education-date">'+date_html+'</div><div class="education-school">'+school_html+'</div><div class="education-college">'+college_html+'</div><div class="education-degree">'+study_html+'</div></article>')
 parts.append('</div></section><section id="publications"><div class="section-heading"><h2>'+T('精选论文','Selected Publications')+'</h2>'+link(T('更多论文 ↗','More publications ↗'),'https://orcid.org/0009-0002-1940-8930')+'</div>')
 for p in d['publications']:
  authors=', '.join('<strong>'+e(a)+'</strong>' if a=='Ruizhi Ouyang' else e(a) for a in p['authors'])
  meta='<em>'+e(p['journal'])+'</em> · '+str(p['year'])+' · '+p['volume']+(('('+p['issue']+')') if p.get('issue') else '')+', '+p['page']
  parts.append('<article class="publication'+(' has-figure' if p.get('figure') else '')+'"><div class="pub-year">'+str(p['year'])+'</div><div><h3>'+link(p['title'],'https://doi.org/'+p['doi'])+'</h3><p class="authors">'+authors+'</p><p class="pub-meta">'+meta+'</p><p class="pub-note">'+e(p['note_en'] if en else p['note'])+'</p>'+link('DOI: '+p['doi'],'https://doi.org/'+p['doi'])+'</div>'+('<figure class="paper-figure"><img src="'+prefix+p['figure']['path']+'" alt="'+e(p['figure'][lang],quote=True)+'" loading="lazy"></figure>' if p.get('figure') else '')+'</article>')
 parts.append('</section><section id="projects">'+heading(T('公开项目','Public Projects'))+'<div class="project-section"><h3 class="subheading">'+T('公开竞赛','Public Competitions')+'</h3><div class="project-grid">')
 tag_zh={'Reinforcement learning':'强化学习','Network flow':'网络流','Fuzzy control':'模糊控制','Optimization':'优化','Clustering':'聚类','Model selection':'模型选择','Bayesian optimization':'贝叶斯优化','Classification':'分类','Regression':'回归','Feature engineering':'特征工程','Statistics':'统计学'}
 projects=d['competition_projects']
 ranked=[p for p in projects if p.get('result',{}).get('leaderboard')=='private' and p['result'].get('status')=='final']
 featured=sorted(ranked,key=lambda p:p['result']['rank']/p['result']['teams'])[:2]
 remaining=sorted([p for p in projects if p not in featured],key=lambda p:p.get('date',''),reverse=True)
 for i,p in enumerate(featured+remaining):
  if i==2:parts.append('</div><details class="more-projects"><summary>'+T('展开更多项目','Show more projects')+'</summary><div class="project-grid">')
  result=p.get('result')
  result_html=''
  if result:
   top=f"{100*result['rank']/result['teams']:.2f}"
   result_text=T('最终私榜：','Final private leaderboard: ')+result['metric']+' '+result['score']+' · '+str(result['rank'])+'/'+str(result['teams'])+' · TOP'+top+'%'
   result_html='<p class="project-label">'+link(result_text,result['url'])+'</p>'
  parts.append('<article class="project"><p class="project-label">'+e(p['label'][lang])+'</p><h3>'+e(p['title'][lang])+'</h3><p>'+e(p['description'][lang])+'</p>'+result_html+'<div class="tags">'+''.join('<span>'+e(t if en else tag_zh.get(t,t))+'</span>' for t in p['tags'])+'</div>'+link(T('查看项目','View project'),p['url'])+'</article>')
 parts.append('</div></details></div><div class="project-section"><h3 class="subheading">'+T('专利与软著','Patents & Software Copyrights')+'</h3><div class="ip-table-scroll"><table class="ip-table"><thead><tr><th scope="col">'+T('日期','Date')+'</th><th scope="col">'+T('名称','Title')+'</th><th scope="col">'+T('类型','Type')+'</th><th scope="col">'+T('登记/公开号','Registration / publication no.')+'</th><th scope="col">'+T('署名','Contribution')+'</th></tr></thead><tbody>')
 for item in sorted(d['intellectual_property'],key=lambda item:(0 if item['kind']=='patent' else 1,item.get('contribution_order',1),-int(item['date'].replace('-','')))):
  number=link(item['number'],item['url']) if item.get('url') else e(item['number'])
  kind=T('发明专利公开','Published patent application') if item['kind']=='patent' else T('软件著作权','Software copyright')
  parts.append('<tr class="ip-'+item['kind']+'"><td>'+item['date']+'</td><td>'+e(item['title'][lang])+'</td><td>'+kind+'</td><td>'+number+'</td><td>'+e(item['role'][lang])+'</td></tr>')
 parts.append('</tbody></table></div></div></section><section id="awards">'+heading(T('奖项与荣誉','Awards & Honors'))+'<div class="awards-list" id="awards-list" role="table" aria-label="'+T('奖项与荣誉','Awards and honors')+'"><div class="award award-header" role="row"><span role="columnheader" aria-sort="descending"><button class="award-sort" data-sort="year" aria-label="'+T('按年份排序','Sort by year')+'">'+T('年份','Year')+'<span class="sort-icon" aria-hidden="true">↓</span></button></span><span role="columnheader">'+T('奖项/荣誉','Award / honor')+'</span><span class="award-result" role="columnheader" aria-sort="descending"><button class="award-sort" data-sort="rank" aria-label="'+T('按级别排序','Sort by distinction')+'">'+T('级别','Distinction')+'<span class="sort-icon" aria-hidden="true">↓</span></button></span></div>')
 for a in sorted(d['honors'],key=lambda a:(-a['year'],-a['rank'],a.get('prize_order',0))):
  parts.append('<article class="award" role="row" data-year="'+str(a['year'])+'" data-rank="'+str(a['rank'])+'" data-prize="'+str(a.get('prize_order',0))+'"><time role="cell">'+str(a['year'])+'</time><h3 role="cell">'+e(a['title'][lang])+'</h3><span class="award-result" role="cell">'+e((a['level'][lang]+(' ' if en or 'H 奖' in a['result'][lang] else ''))+a['result'][lang])+'</span></article>')
 parts.append('</div></section></div></main><footer class="wrap"><span>'+school+'</span><span>'+T('欧阳瑞志｜学术主页','Ruizhi Ouyang | Academic Homepage')+'</span><span>'+T('联系方式：','Contact: ')+'<a href="mailto:ouyangruizhi@bjfu.edu.cn">ouyangruizhi@bjfu.edu.cn</a></span></footer><script src="'+prefix+'script.js"></script></body></html>')
 dest=root/'dist/en' if en else root/'dist';dest.mkdir(exist_ok=True,parents=True);(dest/'index.html').write_text('\n'.join(parts))
print('Built Chinese and English: 3 papers, 7 competition cards, 1 patent, 10 software copyrights, 14 honors')

