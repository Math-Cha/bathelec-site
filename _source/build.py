# -*- coding: utf-8 -*-
"""Générateur du site bathelec.fr (méthode site-vitrine-pro).
Usage : python3 -I build.py  ->  dist/
"""
import os, sys, shutil, json, html

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT)
from refs_data import SITES, MULTI
IDF = json.load(open(os.path.join(ROOT, "data", "idf.json")))
DIST = os.path.join(ROOT, "dist")
DOMAIN = "https://www.bathelec.fr"
FORM_CONTACT = "https://formsubmit.co/contact@bathelec.fr"
FORM_RH = "https://formsubmit.co/recrutement@bathelec.fr"
TEL = "01 55 99 03 89"
TEL_HREF = "+33155990389"
MAIL = "contact@bathelec.fr"
MAIL_RH = "recrutement@bathelec.fr"
LINKEDIN = "https://fr.linkedin.com/company/bathelec"

# ---------------------------------------------------------------- contenu
STATS = [
    ("20 M€", "de chiffre d'affaires en 2025"),
    ("Classe 5", "Qualifelec moyen & gros tertiaire"),
    ("40+", "marchés et accords-cadres de référence"),
    ("8", "départements d'Île-de-France"),
]

CA = [("2023", "16,7 M€"), ("2024", "22,1 M€"), ("2025", "20,1 M€")]

# Réalisations (source : liste de références Bathelec, nov. 2026) — sans montants
REALISATIONS = [
    ("AP-HP Nord · Université Paris Cité", "Entretien et aménagement des bâtiments de 5 sites du GHU AP-HP Nord", "2026", "CFO / CFA"),
    ("EDF", "Marché-cadre de petits travaux immobiliers sur sites tertiaires et semi-industriels, sur 8 ans", "2026", "CFO / CFA"),
    ("Ministère des Armées", "Accord-cadre d'entretien et de grosses réparations des sites de l'ESID d'Île-de-France", "2023", "Électricité"),
    ("Région Île-de-France", "Maintenance multitechnique des bâtiments administratifs de la Région", "2024", "Électricité"),
    ("Université Paris Cité · EPAURIF", "Remplacement du poste HT/BT et création d'un TGS, faculté de Pharmacie (Paris 6e)", "2024", "Courants forts"),
    ("Ministère de l'Économie et des Finances", "Backbones optiques de Bercy et Chevaleret, travaux courants forts et faibles de l'administration centrale", "2021-2024", "VDI · CFO / CFA"),
    ("Ministère de l'Enseignement supérieur", "Remplacement du SSI et création d'un poste central de sécurité, site Descartes (Paris 5e)", "2022", "Sécurité incendie"),
    ("Ville de Neuilly-sur-Seine", "Réhabilitation du centre aquatique", "2023", "Électricité"),
    ("Ville d'Antony", "Centrale solaire sur les tribunes du stade Georges Suant", "2026", "Photovoltaïque"),
    ("CROUS de Paris", "Aménagement du centre Bièvre", "2025", "CFO / CFA"),
    ("COVEA", "Aménagement bailleur des niveaux R+5 / R+6 de l'immeuble Nord Pont (Paris 14e)", "2025", "CFO / CFA"),
    ("SDIS 95", "Marché à bons de commande de travaux courants d'électricité", "2025-2026", "CFO / CFA"),
]

EXPERTISES = [
    {
        "slug": "courants-forts", "num": "01", "img": "courants-forts.jpg",
        "title": "Courants forts",
        "short": "Colonnes montantes, TGBT, postes MT/BT, distribution et éclairage.",
        "lead": "Notre métier d'origine : alimenter des bâtiments occupés, sans interrompre leur activité. Des colonnes montantes jusqu'au dernier circuit d'éclairage.",
        "cards": [
            ("Colonnes montantes et horizontales", "Création, réfection et mise en conformité des colonnes électriques d'immeubles collectifs et tertiaires, en coordination avec le gestionnaire de réseau."),
            ("TGBT et postes MT/BT", "Remplacement de tableaux généraux basse tension, raccordement et équipement de postes de transformation, sélectivité et protections."),
            ("Distribution et armoires", "Tableaux divisionnaires, chemins de câbles, distribution des étages et des plateaux, adaptation aux réaménagements."),
            ("Éclairage", "Éclairage intérieur et extérieur, relamping LED, éclairage de sécurité, commandes et détection de présence."),
        ],
        "faq": [
            ("Intervenez-vous en site occupé ?", "Oui, c'est notre quotidien : bureaux, établissements recevant du public, logements habités. Les coupures sont planifiées avec l'exploitant et réduites au strict nécessaire."),
            ("Prenez-vous en charge la réfection complète d'une colonne montante ?", "Oui, du diagnostic à la remise en service, avec les démarches auprès du gestionnaire de réseau et la coordination des occupants."),
            ("Quelles qualifications détenez-vous ?", "Qualifelec MGTI classe 5 (moyen et gros tertiaire, industrie) et LCPT classe 4 avec la mention Colonnes ; travaux selon NF C 15-100 et NF C 14-100."),
        ],
    },
    {
        "slug": "courants-faibles", "num": "02", "img": "courants-faibles.jpg",
        "title": "Courants faibles",
        "short": "Câblage VDI, informatique, téléphonie, interphonie et visiophonie.",
        "lead": "Des infrastructures de communication fiables, propres et documentées, prêtes à évoluer avec les usages de vos occupants.",
        "cards": [
            ("Câblage VDI", "Réseaux voix-données-images cuivre et fibre, baies de brassage, recettes et cahiers de mesures."),
            ("Informatique", "Infrastructures réseau des locaux techniques aux postes de travail, accompagnement des déménagements et réaménagements."),
            ("Téléphonie", "Installation et raccordement des équipements de téléphonie, reprise et rationalisation des réseaux existants."),
            ("Interphonie et visiophonie", "Portiers, interphones et visiophones pour immeubles collectifs, sièges et établissements publics."),
        ],
        "faq": [
            ("Livrez-vous un dossier de recette ?", "Oui : plans de repérage, cahier de mesures et dossier des ouvrages exécutés à la réception."),
            ("Pouvez-vous reprendre un réseau existant ?", "Oui, nous auditons l'existant, conservons ce qui peut l'être et remettons l'ensemble au propre."),
            ("Intervenez-vous hors des heures de bureau ?", "Oui, lorsque l'activité du site l'exige, les interventions sont planifiées le soir ou le week-end."),
        ],
    },
    {
        "slug": "surete-securite", "num": "03", "img": "surete.jpg",
        "title": "Sûreté & sécurité",
        "short": "Contrôle d'accès, portes automatiques, vidéoprotection, SSI.",
        "lead": "Protéger les personnes et les sites sensibles : commissariats, administrations, établissements de santé et d'enseignement nous confient leur sécurité.",
        "cards": [
            ("Contrôle d'accès", "Lecteurs de badges, gestion des droits, portes et portails automatiques, intégration aux systèmes existants."),
            ("Vidéoprotection", "Caméras, enregistrement et postes d'exploitation, dimensionnés selon les zones à protéger."),
            ("Sécurité incendie (SSI)", "Installation, extension et mise en conformité de systèmes de sécurité incendie et de leurs asservissements."),
            ("Sécurisation de sites", "Programmes de sécurisation multi-sites pour donneurs d'ordre publics, dans le respect des calendriers opérationnels."),
        ],
        "faq": [
            ("Avez-vous l'expérience des sites sensibles ?", "Oui, nous avons conduit des programmes de sécurisation de commissariats pour un donneur d'ordre ministériel."),
            ("Assurez-vous une astreinte ?", "Oui, nos clients sous contrat bénéficient d'une astreinte et d'une intervention rapide."),
            ("Intervenez-vous sur les SSI existants ?", "Oui : extensions, modifications liées aux réaménagements et mises en conformité."),
        ],
    },
    {
        "slug": "energie-irve", "num": "04", "img": "irve.jpg",
        "title": "Énergie & IRVE",
        "short": "Bornes de recharge, puissance, raccordement et photovoltaïque.",
        "lead": "Électrifier les flottes et les parkings, produire de l'énergie sur site : de l'étude de puissance à la mise en service, par des équipes qualifiées Qualifelec IRVE.",
        "cards": [
            ("Étude de puissance", "Analyse de l'existant, bilan de puissance et solution de raccordement adaptée au site."),
            ("Installation de bornes", "Pose et raccordement de bornes de recharge, y compris stations de plus de 36 kVA (Qualifelec IRVE indice 2)."),
            ("Parkings et flottes publiques", "Déploiements multi-sites pour administrations et entreprises, dans les délais des plans d'équipement."),
            ("Solaire photovoltaïque", "Centrales solaires sur bâtiments et équipements publics, raccordement et mise en service."),
        ],
        "faq": [
            ("Êtes-vous qualifiés pour installer des bornes IRVE ?", "Oui, Bathelec détient la qualification Qualifelec IRVE indice 2, qui couvre les stations de recharge de plus de 36 kVA."),
            ("Pouvez-vous équiper plusieurs sites en même temps ?", "Oui, nous avons mené des plans « bornes de recharge » multi-sites pour un donneur d'ordre ministériel."),
            ("Faut-il augmenter la puissance du bâtiment ?", "Pas toujours : l'étude de puissance le détermine, et le pilotage de la charge permet souvent de l'éviter."),
        ],
    },
]

SECTEURS = [
    ("Tertiaire et sièges", "Immeubles de bureaux, sièges sociaux, réaménagements de plateaux en site occupé."),
    ("Établissements publics", "Administrations, collectivités, ministères, commissariats, organismes de sécurité sociale."),
    ("Santé et enseignement", "Centres hospitaliers, universités, établissements recevant du public sensibles."),
    ("Habitat collectif", "Colonnes montantes, parties communes, interphonie pour bailleurs et gestionnaires."),
    ("Industrie", "Distribution de puissance, TGBT, éclairage et sécurité des sites industriels."),
]

CLIENTS = [
    "AP-HP Nord", "EDF", "Ministère des Armées", "Région Île-de-France", "Ministère de l'Économie et des Finances",
    "Préfecture de Police", "Université Paris Cité", "Sorbonne Université", "Centre Hospitalier Sud Francilien", "CROUS de Paris",
    "CCI Paris Île-de-France", "CPAM de Paris", "CPAM de Seine-Saint-Denis", "Conseil départemental du Val-de-Marne", "SDIS 95",
    # suite (page Références)
    "Ministère de l'Enseignement supérieur", "Académie de Créteil", "ENSEA", "CAF de Seine-Saint-Denis", "Grand Paris Sud Est Avenir",
    "Ville de Versailles", "Ville de Levallois", "Ville d'Antony", "Ville de Massy", "Ville de Neuilly-sur-Seine",
    "Ville de Rueil-Malmaison", "Ville de Suresnes", "Ville de Bezons", "Ville de Dammarie-lès-Lys", "Ville de Saint-Cloud",
    "COVEA", "CIPAV", "ICADE", "Nexity", "BNP Paribas",
]

TEMOIGNAGES = [
    ("Le professionnalisme des équipes et leur réactivité, y compris en astreinte, l'appui technique et le devoir de conseil ont permis la concrète réalisation des plans « bornes de recharge » et « sécurisation des commissariats ».", "Préfecture de Police"),
    ("Une entreprise réactive, qui fournit un travail de qualité, avec un réel savoir-faire. Les travaux de réhabilitation ont été réalisés dans les règles de l'art.", "CPAM de Seine-Saint-Denis"),
    ("Un très grand professionnalisme et de vrais conseils sur le choix des matériaux. Nous n'hésiterons pas à faire de nouveau appel à Bathelec.", "Université Paris Cité"),
]

CERTIFS = [
    ("Qualifelec MGTI classe 5", "Moyen & gros tertiaire, industrie (50 à 250 exécutants)"),
    ("Qualifelec LCPT classe 4", "Logement, commerce, petit tertiaire · mentions Colonnes et Autocontrôle"),
    ("Qualifelec IRVE indice 2", "Bornes de recharge, stations de plus de 36 kVA"),
    ("NF C 15‑100 · 14‑100", "Installations intérieures et branchements"),
    ("Amiante SS4 · Plomb", "Prévention des risques sur bâtiments anciens"),
    ("SST", "Sauveteurs secouristes du travail"),
]

METHODE = [
    ("Visite et diagnostic", "Un chargé d'affaires visite le site, relève l'existant et identifie les contraintes d'exploitation."),
    ("Étude et offre", "Notre bureau d'étude de prix chiffre une solution argumentée, avec planning et phasage."),
    ("Travaux en site occupé", "Équipes encadrées, coupures planifiées, propreté et sécurité du chantier au quotidien."),
    ("Réception et suivi", "Essais, DOE, formation de l'exploitant, puis maintenance et astreinte si vous le souhaitez."),
]

ENGAGEMENTS = [
    ("Marchés à bons de commande", "Chiffrage rapide sur bordereau de prix, équipes mobilisables dans toute l'Île-de-France, suivi de chaque commande jusqu'à sa réception."),
    ("Accords-cadres pluriannuels", "Jusqu'à 8 ans d'engagement : des équipes stables qui connaissent votre patrimoine et ses contraintes d'exploitation."),
    ("Astreinte et réactivité", "Une organisation pensée pour répondre vite, y compris hors des heures ouvrées."),
    ("Devoir de conseil", "Choix des matériels, phasage, contraintes réglementaires : nous vous aidons à décider."),
]

POSTES = [
    ("Électricien monteur câbleur HT/BT", "CAP électricien ou équivalent · habilitations H1V, H2V, B1V, B2V"),
    ("Technicien SSI", "Système de sécurité incendie · CAP ou expérience équivalente"),
    ("Technicien contrôle d'accès", "Badges, portes automatiques · CAP ou expérience équivalente"),
    ("Technicien vidéosurveillance", "Vidéoprotection · CAP ou expérience équivalente"),
    ("Chargé d'étude de prix CFA/CFO & SSI", "BTS ou expérience équivalente"),
]

# ---------------------------------------------------------------- icônes (Lucide, MIT)
ICONS = {
    "bolt": '<path d="M13 2 3 14h9l-1 8 10-12h-9l1-8z"/>',
    "network": '<rect x="16" y="16" width="6" height="6" rx="1"/><rect x="2" y="16" width="6" height="6" rx="1"/><rect x="9" y="2" width="6" height="6" rx="1"/><path d="M5 16v-3a1 1 0 0 1 1-1h12a1 1 0 0 1 1 1v3"/><path d="M12 12V8"/>',
    "shield": '<path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"/><path d="m9 12 2 2 4-4"/>',
    "plug": '<path d="M12 22v-5"/><path d="M9 8V2"/><path d="M15 8V2"/><path d="M18 8v5a4 4 0 0 1-4 4h-4a4 4 0 0 1-4-4V8Z"/>',
    "arrow": '<path d="M5 12h14"/><path d="m12 5 7 7-7 7"/>',
    "phone": '<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.91.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92z"/>',
    "mail": '<rect width="20" height="16" x="2" y="4" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/>',
    "pin": '<path d="M20 10c0 4.99-5.54 10.19-7.4 11.8a1 1 0 0 1-1.2 0C9.54 20.19 4 14.99 4 10a8 8 0 0 1 16 0"/><circle cx="12" cy="10" r="3"/>',
    "check": '<path d="M20 6 9 17l-5-5"/>',
    "building": '<rect width="16" height="20" x="4" y="2" rx="2"/><path d="M9 22v-4h6v4"/><path d="M8 6h.01"/><path d="M16 6h.01"/><path d="M12 6h.01"/><path d="M12 10h.01"/><path d="M12 14h.01"/><path d="M16 10h.01"/><path d="M16 14h.01"/><path d="M8 10h.01"/><path d="M8 14h.01"/>',
    "landmark": '<line x1="3" x2="21" y1="22" y2="22"/><line x1="6" x2="6" y1="18" y2="11"/><line x1="10" x2="10" y1="18" y2="11"/><line x1="14" x2="14" y1="18" y2="11"/><line x1="18" x2="18" y1="18" y2="11"/><polygon points="12 2 20 7 4 7"/>',
    "hospital": '<path d="M12 6v4"/><path d="M14 14h-4"/><path d="M14 18h-4"/><path d="M14 8h-4"/><path d="M18 12h2a2 2 0 0 1 2 2v6a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2v-9a2 2 0 0 1 2-2h2"/><path d="M18 22V4a2 2 0 0 0-2-2H8a2 2 0 0 0-2 2v18"/>',
    "home": '<path d="M15 21v-8a1 1 0 0 0-1-1h-4a1 1 0 0 0-1 1v8"/><path d="M3 10a2 2 0 0 1 .709-1.528l7-5.999a2 2 0 0 1 2.582 0l7 5.999A2 2 0 0 1 21 10v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/>',
    "factory": '<path d="M2 20a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V8l-7 5V8l-7 5V4a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2Z"/><path d="M17 18h1"/><path d="M12 18h1"/><path d="M7 18h1"/>',
    "linkedin": '<path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"/><rect width="4" height="12" x="2" y="9"/><circle cx="4" cy="4" r="2"/>',
    "cal": '<path d="M8 2v4"/><path d="M16 2v4"/><rect width="18" height="18" x="3" y="4" rx="2"/><path d="M3 10h18"/>',
    "file": '<path d="M15 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7Z"/><path d="M14 2v4a2 2 0 0 0 2 2h4"/><path d="m9 15 2 2 4-4"/>',
    "clock": '<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>',
    "chat": '<path d="M7.9 20A9 9 0 1 0 4 16.1L2 22Z"/>',
    "menu": '<line x1="4" x2="20" y1="6" y2="6"/><line x1="4" x2="20" y1="12" y2="12"/><line x1="4" x2="20" y1="18" y2="18"/>',
}
EXP_ICON = {"courants-forts": "bolt", "courants-faibles": "network", "surete-securite": "shield", "energie-irve": "plug"}
SECT_ICON = ["building", "landmark", "hospital", "home", "factory"]


def ic(name, cls="ic"):
    return f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[name]}</svg>'


e = html.escape

# ---------------------------------------------------------------- CSS
CSS = open(os.path.join(ROOT, "style.css"), encoding="utf-8").read()


JS = r"""
document.querySelector('.burger')?.addEventListener('click',()=>document.querySelector('nav.m').classList.toggle('open'));
document.querySelectorAll('nav.m a').forEach(a=>a.addEventListener('click',()=>document.querySelector('nav.m').classList.remove('open')));
const io=new IntersectionObserver(es=>es.forEach(x=>{if(x.isIntersecting){x.target.classList.add('in');io.unobserve(x.target)}}),{threshold:.12});
document.querySelectorAll('.rv').forEach(el=>io.observe(el));
"""

MAP_JS = r"""
(function(){
const root=document.getElementById('refmap'); if(!root) return;
const D=JSON.parse(document.getElementById('refdata').textContent);
const svg=root.querySelector('svg'), gp=svg.querySelector('#pins'), panel=document.getElementById('mpanel'), def=panel.innerHTML;
const FULL=[0,0,D.W,D.H], PAR=D.paris; let vb=FULL.slice(), mode='idf', sel=null;
const NS='http://www.w3.org/2000/svg';
const P=(lon,lat)=>[(lon-D.proj[0])*D.proj[2]*D.proj[3],(D.proj[1]-lat)*D.proj[3]];
function setVB(v){vb=v;svg.setAttribute('viewBox',v.join(' '));draw();}
function anim(to){const fr=vb.slice(),t0=performance.now();function st(t){const k=Math.min(1,(t-t0)/450),e=k<.5?2*k*k:1-Math.pow(-2*k+2,2)/2;setVB(fr.map((a,i)=>a+(to[i]-a)*e));if(k<1)requestAnimationFrame(st)}requestAnimationFrame(st)}
function el(n,a){const x=document.createElementNS(NS,n);for(const k in a)x.setAttribute(k,a[k]);return x}
function draw(){gp.innerHTML='';const s=vb[2]/D.W, r=7.5*s;svg.querySelectorAll('.dlab').forEach(t=>t.setAttribute('font-size',11*s));
 const show=D.sites.filter(x=>mode==='paris'||!x.paris);
 show.forEach(x=>{const [cx,cy]=P(x.lon,x.lat);const g=el('g',{class:'pin'+(sel===x.id?' on':''),tabindex:0,'aria-label':x.client,'data-id':x.id});
  g.append(el('circle',{class:'halo',cx,cy,r:r*2}),el('circle',{class:'dot',cx,cy,r}));
  g.addEventListener('mouseenter',()=>open(x));g.addEventListener('click',e=>{e.stopPropagation();open(x)});g.addEventListener('focus',()=>open(x));gp.append(g)});
 if(mode==='idf'){const ps=D.sites.filter(x=>x.paris);const [cx,cy]=P(2.3488,48.8566);const g=el('g',{class:'pin cl',tabindex:0,'aria-label':'Paris'});
  g.append(el('circle',{class:'halo',cx,cy,r:r*2.6}),el('circle',{class:'dot',cx,cy,r:r*1.7}));const t=el('text',{x:cx,y:cy+4*s,'text-anchor':'middle','font-size':12*s});t.textContent=ps.length;g.append(t);
  g.addEventListener('click',e=>{e.stopPropagation();zoomParis()});g.addEventListener('mouseenter',()=>{panel.innerHTML='<div class="def"><span class="kicker">Paris</span><h3>'+ps.length+' sites de référence dans Paris</h3><p style="margin-top:12px">Cliquez sur le point pour zoomer sur Paris et la petite couronne.</p></div>'});gp.append(g)}
}
function mark(){gp.querySelectorAll('.pin[data-id]').forEach(g=>g.classList.toggle('on',g.dataset.id===sel))}
function open(x){if(sel===x.id)return;sel=x.id;mark();
 panel.innerHTML=(x.logo?'<div class="lgo"><img src="'+D.base+'img/logos/'+x.logo+'.png" alt=""></div>':'')+'<h3>'+x.client+'</h3><div class="loc">'+D.pinIcon+x.lieu+'</div><ul class="ops">'+x.ops.map(o=>'<li><div class="meta"><span>'+o[2]+'</span><span>'+o[1]+'</span></div><p>'+o[0]+'</p></li>').join('')+'</ul><div class="mlist" style="margin-top:22px"><button data-reset>← Toutes les références</button></div>';
 panel.querySelector('[data-reset]').onclick=()=>{sel=null;mark();panel.innerHTML=def;bindDef()};
}
function zoomParis(){mode='paris';btns();anim(PAR)}
function zoomIdf(){mode='idf';btns();anim(FULL)}
function btns(){root.querySelectorAll('[data-z]').forEach(b=>b.classList.toggle('on',b.dataset.z===mode))}
root.querySelectorAll('[data-z]').forEach(b=>b.onclick=()=>b.dataset.z==='paris'?zoomParis():zoomIdf());
function bindDef(){panel.querySelectorAll('[data-site]').forEach(b=>b.onclick=()=>{const x=D.sites.find(y=>y.id===b.dataset.site);if(x.paris&&mode!=='paris')zoomParis();if(!x.paris&&mode!=='idf')zoomIdf();setTimeout(()=>open(x),x.paris?460:0)})}
bindDef(); setVB(FULL);
})();
"""


# ---------------------------------------------------------------- gabarit
def rel(depth):
    return "../" * depth


def shell(title, desc, body, path, depth=0, active="", extra_js=""):
    r = rel(depth)
    canon = DOMAIN + "/" + path.replace("index.html", "")
    menu_exp = "".join(
        f'<a href="{r}expertises/{x["slug"]}.html">{ic(EXP_ICON[x["slug"]])}<span>{x["title"]}<small>{e(x["short"])}</small></span></a>'
        for x in EXPERTISES)
    def on(k):
        return ' class="on"' if active == k else ""
    ld = {
        "@context": "https://schema.org", "@type": "Electrician", "name": "BATHELEC",
        "url": DOMAIN, "telephone": "+33 1 55 99 03 89", "email": MAIL, "logo": DOMAIN + "/img/logo.png",
        "address": {"@type": "PostalAddress", "streetAddress": "1-3 rue de la Procession", "postalCode": "93210",
                    "addressLocality": "Saint-Denis", "addressCountry": "FR"},
        "areaServed": "Île-de-France", "parentOrganization": {"@type": "Organization", "name": "Groupe SITTE"},
    }
    return f"""<!DOCTYPE html>
<html lang="fr"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{canon}">
<meta property="og:type" content="website"><meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(desc)}">
<meta property="og:image" content="{DOMAIN}/img/og.jpg"><meta property="og:url" content="{canon}"><meta property="og:locale" content="fr_FR">
<link rel="icon" type="image/svg+xml" href="{r}img/favicon.svg"><link rel="icon" type="image/png" href="{r}img/favicon.png"><link rel="apple-touch-icon" href="{r}img/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Inter+Tight:wght@600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{r}assets/style.css">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
</head><body>
<div class="top"><div class="wrap"><span class="hide-m">Électricité · Courants faibles · Sûreté · IRVE — Île-de-France · Une société du Groupe SITTE</span>
<div class="r"><a href="tel:{TEL_HREF}">{ic("phone")}{TEL}</a><a href="mailto:{MAIL}">{ic("mail")}{MAIL}</a><a href="{LINKEDIN}" target="_blank" rel="noopener" aria-label="LinkedIn">{ic("linkedin")}</a></div></div></div>
<header class="h"><div class="wrap">
<a class="brand" href="{r}index.html" aria-label="BATHELEC, accueil"><img src="{r}img/logo.svg" alt="BATHELEC — 100% disponible" width="186" height="46"></a>
<nav class="m">
<div class="dd"><a href="{r}index.html#expertises"{on("exp")}>Expertises</a><div class="menu">{menu_exp}</div></div>
<a href="{r}index.html#secteurs"{on("sect")}>Secteurs</a>
<a href="{r}references.html"{on("refs")}>Références</a>
<a href="{r}entreprise.html"{on("ent")}>L'entreprise</a>
<a href="{r}carrieres.html"{on("car")}>Carrières</a>
<a href="{r}contact.html"{on("contact")}>Contact</a>
<a class="btn btn-o" href="{r}contact.html#form">Demander un devis {ic("arrow")}</a>
</nav>
<a class="callm" href="tel:{TEL_HREF}" aria-label="Appeler Bathelec">{ic("phone")}</a>
<button class="burger" aria-label="Menu">{ic("menu")}</button>
</div></header>
<main>{body}</main>
<footer><div class="wrap">
<div class="cols">
<div><a class="brand" href="{r}index.html"><img src="{r}img/logo.svg" alt="BATHELEC" width="178" height="44"></a><p>Courants forts, courants faibles, sûreté et IRVE pour les bâtiments tertiaires, publics et privés d'Île-de-France. Spécialiste des marchés à bons de commande. Une société du Groupe SITTE.</p></div>
<div><h4>Expertises</h4><ul>{"".join(f'<li><a href="{r}expertises/{x["slug"]}.html">{x["title"]}</a></li>' for x in EXPERTISES)}</ul></div>
<div><h4>Bathelec</h4><ul><li><a href="{r}references.html">Références</a></li><li><a href="{r}entreprise.html">L'entreprise</a></li><li><a href="{r}carrieres.html">Carrières</a></li><li><a href="{r}contact.html">Contact</a></li></ul></div>
<div><h4>Contact</h4><ul><li>1-3 rue de la Procession<br>93210 Saint-Denis</li><li><a href="tel:{TEL_HREF}">{TEL}</a></li><li><a href="mailto:{MAIL}">{MAIL}</a></li></ul></div>
</div>
<div class="bot"><span>© BATHELEC — Groupe SITTE</span><span><a href="{r}mentions-legales.html">Mentions légales</a> · <a href="{LINKEDIN}" target="_blank" rel="noopener">LinkedIn</a></span></div>
</div></footer>
<script>{JS}{extra_js}</script>
</body></html>"""


def cta_band(r):
    return f"""<section class="band"><div class="wrap"><div class="box"><p>Un marché à bons de commande, un accord-cadre, un projet de rénovation ? Nos chargés d'affaires étudient votre besoin et vous répondent rapidement.</p>
<a class="btn btn-o" href="{r}contact.html#form">Demander un devis {ic("arrow")}</a></div></div></section>"""


def cta_final(r):
    return f"""<section class="cta"><div class="wrap"><div class="box">
<div class="rv"><span class="kicker">Parlons de votre projet</span><h2>Un interlocuteur unique pour l'électricité de vos bâtiments.</h2>
<p class="lead">Visite, étude de prix et proposition sur demande, sans engagement.</p></div>
<div class="contact-l rv"><a class="t" href="tel:{TEL_HREF}">{ic("phone")}{TEL}</a><a class="t" href="mailto:{MAIL}">{ic("mail")}{MAIL}</a>
<a class="btn btn-w" href="{r}contact.html#form">Demander un devis {ic("arrow")}</a></div>
</div></div></section>"""


def reals_html(items):
    return "".join(f'<article class="real rv"><div class="meta"><span>{e(t)}</span><span>{d}</span></div><h3>{e(c)}</h3><p>{e(a)}</p></article>' for c, a, d, t in items)


# logos de la mosaïque : (logo, nom)
LOGOS = [("aphp", "AP-HP"), ("edf", "EDF"), ("armees", "Ministère des Armées"), ("region", "Région Île-de-France"),
         ("minefi", "Ministère de l'Économie"), ("prefecture", "Préfecture de Police"), ("upc", "Université Paris Cité"),
         ("sorbonne", "Sorbonne Université"), ("chsf", "CH Sud Francilien"), ("crous", "Crous"), ("ccip", "CCI Paris IDF"),
         ("cd94", "Val-de-Marne"), ("cpam75", "CPAM de Paris"), ("cpam93", "CPAM 93"), ("caf", "CAF"), ("academie", "Académie de Créteil"),
         ("ensea", "ENSEA"), ("gpsea", "Grand Paris Sud Est Avenir"), ("versailles", "Versailles"), ("levallois", "Levallois"),
         ("antony", "Antony"), ("massy", "Massy"), ("neuilly", "Neuilly-sur-Seine"), ("rueil", "Rueil-Malmaison"),
         ("suresnes", "Suresnes"), ("bezons", "Bezons"), ("dammarie", "Dammarie-lès-Lys"), ("stcloud", "Saint-Cloud"),
         ("covea", "Covéa"), ("cipav", "CIPAV"), ("icade", "Icade"), ("nexity", "Nexity"), ("bnp", "BNP Paribas"), ("", "SDIS du Val-d'Oise"),
         ("", "Ministère de l'Enseignement supérieur")]


def logos_html(r, n=None):
    items = LOGOS if n is None else LOGOS[:n]
    return '<div class="logos rv">' + "".join(
        f'<div class="lg" title="{e(t)}"><img src="{r}img/logos/{k}.png" alt="{e(t)}" loading="lazy"></div>' if k else f'<div class="lg txt">{e(t)}</div>'
        for k, t in items) + "</div>"


def map_html(r):
    lp = IDF["proj"]
    def P(lon, lat):
        return ((lon - lp[0]) * lp[2] * lp[3], (lp[1] - lat) * lp[3])
    x0, y0 = P(2.13, 48.97); x1, y1 = P(2.58, 48.74)
    paris = [round(x0, 1), round(y0, 1), round(x1 - x0, 1), round((x1 - x0) * IDF["H"] / IDF["W"], 1)]
    deps = "".join(f'<path class="dep{" p75" if k == "75" else ""}" d="{d}"/>' for k, d in IDF["paths"].items())
    labs = {"95": (2.10, 49.10), "78": (1.85, 48.80), "91": (2.25, 48.50), "77": (2.95, 48.62), "93": (2.50, 48.945), "94": (2.50, 48.765), "92": (2.20, 48.835)}
    dl = "".join(f'<text class="dlab" x="{P(*v)[0]:.0f}" y="{P(*v)[1]:.0f}" text-anchor="middle">{k}</text>' for k, v in labs.items())
    data = {"W": IDF["W"], "H": IDF["H"], "proj": lp, "paris": paris, "base": r, "pinIcon": ic("pin"),
            "sites": [{"id": i, "logo": lg, "client": c, "lieu": l, "lat": la, "lon": lo, "paris": pa, "ops": ops}
                      for i, lg, c, l, la, lo, pa, ops in SITES]}
    nops = sum(len(x[7]) for x in SITES)
    chips = "".join(f'<button data-site="{x[0]}">{e(x[2].split(" · ")[0])}</button>' for x in SITES)
    return f"""<div class="mapbox" id="refmap">
<div class="map rv"><div class="mtools"><button data-z="idf" class="on">Île-de-France</button><button data-z="paris">Paris &amp; petite couronne</button></div>
<svg viewBox="0 0 {IDF['W']} {IDF['H']}" role="img" aria-label="Carte des références Bathelec en Île-de-France"><g>{deps}</g><g>{dl}</g><g id="pins"></g></svg>
<span class="hint">Survolez ou touchez un point</span></div>
<aside class="mpanel rv" id="mpanel"><div class="def"><span class="kicker">Nos chantiers</span><h3>Une présence dans toute l'Île-de-France</h3>
<div class="big"><div><b>{len(SITES)}</b><span>sites de référence</span></div><div><b>{nops}</b><span>opérations</span></div><div><b>{len(MULTI)}</b><span>accords multi-sites</span></div></div>
<p>Survolez un point de la carte pour découvrir l'opération réalisée. Le point bleu regroupe les sites parisiens : cliquez dessus pour zoomer.</p></div>
<div class="mlist">{chips}</div></aside></div>
<script type="application/json" id="refdata">{json.dumps(data, ensure_ascii=False)}</script>"""


def multi_html(r):
    return '<div class="multi">' + "".join(
        f'<div class="mc rv"><div class="top2"><img src="{r}img/logos/{k}.png" alt="{e(n)}" loading="lazy"><span>{e(y)}</span></div><h3>{e(n)}</h3><p>{e(t)}</p></div>'
        for k, n, t, y in MULTI) + "</div>"


ENG_ICONS = ["file", "cal", "clock", "chat"]


# ---------------------------------------------------------------- pages
def home():
    r = ""
    stats = "".join(f'<div class="stat"><b>{a}</b><span>{b}</span></div>' for a, b in STATS)
    exps = "".join(f"""<a class="exp rv" href="expertises/{x['slug']}.html"><div class="ph"><img src="img/{x['img']}" alt="{e(x['title'])}" loading="lazy"></div>
<div class="bd"><span class="n">{x['num']}</span><h3>{x['title']}</h3><p>{e(x['short'])}</p><span class="link">Découvrir {ic("arrow")}</span></div></a>""" for x in EXPERTISES)
    eng = "".join(f'<div class="rv"><span class="ico">{ic(ENG_ICONS[i])}</span><h3>{a}</h3><p>{b}</p></div>' for i, (a, b) in enumerate(ENGAGEMENTS))
    sect = "".join(f'<li><span class="ico">{ic(SECT_ICON[i])}</span><div><h3>{a}</h3><p>{b}</p></div></li>' for i, (a, b) in enumerate(SECTEURS))
    quotes = "".join(f'<blockquote class="q rv"><p>{e(t)}</p><cite>{e(a)}</cite></blockquote>' for t, a in TEMOIGNAGES)
    certs = "".join(f"<div><b>{a}</b><span>{b}</span></div>" for a, b in CERTIFS)
    steps = "".join(f'<div class="step rv"><h3>{a}</h3><p>{b}</p></div>' for a, b in METHODE)
    body = f"""
<section class="hero"><div class="wrap"><div class="grid">
<div><span class="kicker">Spécialiste des marchés à bons de commande · Île-de-France</span>
<h1>BATHELEC, l'énergie de vos bâtiments, <em>100&nbsp;% disponible.</em></h1>
<p class="lead">Courants forts, courants faibles, sûreté et bornes de recharge&nbsp;: collectivités, administrations et grands comptes nous confient l'entretien, la rénovation et les travaux de leurs bâtiments.</p>
<div class="ctas"><a class="btn btn-o" href="contact.html#form">Demander un devis {ic("arrow")}</a><a class="btn btn-l" href="#references">Nos références</a></div></div>
<div class="pic"><img src="img/hero.jpg" alt="Hall lumineux d'un immeuble tertiaire">
<div class="badge"><span class="ico">{ic("landmark")}</span><div><b>Marchés publics et grands comptes</b><span>AP-HP, EDF, ministère des Armées, Région Île-de-France</span></div></div>
<div class="badge badge2"><span class="ico">{ic("shield")}</span><div><b>Qualifelec classe 5</b><span>Moyen et gros tertiaire</span></div></div></div>
</div>
<div class="stats">{stats}</div></div></section>
{cta_band(r)}
<section id="expertises"><div class="wrap">
<div class="sec-head rv"><div><span class="kicker">Nos expertises</span><h2>Quatre métiers, une seule exigence.</h2>
<p class="lead">Des colonnes montantes aux systèmes de sûreté, nos équipes couvrent l'ensemble du lot électricité de vos bâtiments.</p></div></div>
<div class="exp-grid">{exps}</div></div></section>
<section class="soft"><div class="wrap">
<div class="sec-head rv"><div><span class="kicker">Notre spécialité</span><h2>Le partenaire des marchés <br>à bons de commande.</h2></div>
<p class="lead" style="max-width:460px">L'essentiel de notre activité repose sur des marchés récurrents, exécutés commande après commande pour des donneurs d'ordre publics et privés.</p></div>
<div class="eng">{eng}</div></div></section>
<section id="references"><div class="wrap">
<div class="sec-head rv"><div><span class="kicker">Carte des réalisations</span><h2>Nos chantiers en Île-de-France.</h2>
<p class="lead">Survolez la carte pour découvrir les opérations menées pour nos clients.</p></div>
<a class="link" href="references.html">Toutes nos références {ic("arrow")}</a></div>
{map_html(r)}</div></section>
<section class="soft"><div class="wrap">
<div class="sec-head rv"><div><span class="kicker">Ils nous font confiance</span><h2>Des références institutionnelles.</h2></div></div>
{logos_html(r, 18)}
<div class="quotes">{quotes}</div></div></section>
<section id="secteurs"><div class="wrap split">
<div class="img rv"><img src="img/equipe.jpg" alt="Électricien Bathelec sur une armoire électrique" loading="lazy"></div>
<div class="rv"><span class="kicker">Secteurs d'intervention</span><h2>Au service des bâtiments publics et privés.</h2>
<ul class="sect">{sect}</ul></div></div></section>
<section style="padding-top:0"><div class="wrap">
<div class="sec-head rv"><div><span class="kicker">Notre méthode</span><h2>De la visite à la réception.</h2></div></div>
<div class="steps">{steps}</div></div></section>
<section style="padding-top:0"><div class="wrap">
<div class="sec-head rv"><div><span class="kicker">Qualifications</span><h2>Des compétences reconnues.</h2></div></div>
<div class="certs rv">{certs}</div></div></section>
<section style="padding-top:0"><div class="wrap"><div class="gbox rv">
<div class="t"><span class="kicker">Groupe SITTE</span><h2>Un ancrage francilien, la solidité d'un groupe.</h2>
<p>Spécialiste historique des colonnes montantes, Bathelec a rejoint le Groupe SITTE en 2019. Depuis Saint-Denis et Ivry-sur-Seine, nos équipes interviennent dans les huit départements d'Île-de-France.</p>
<div class="zone">{"".join(f"<span>{d}</span>" for d in ["75","77","78","91","92","93","94","95"])}</div>
<a class="btn btn-l" href="entreprise.html">Découvrir l'entreprise {ic("arrow")}</a></div>
<div class="im" style="background-image:url(img/courants-forts.jpg)"></div></div></div></section>
{cta_final(r)}"""
    return shell("BATHELEC | L'énergie de vos bâtiments, 100 % disponible — électricité en Île-de-France",
                 "Spécialiste des marchés à bons de commande, Bathelec (Groupe SITTE) installe et rénove les équipements électriques des bâtiments tertiaires, publics et privés d'Île-de-France : courants forts, courants faibles, sûreté, IRVE.",
                 body, "index.html", extra_js=MAP_JS)


def phero(r, crumb, h1, p, img=None, num=None):
    pic = f'<div class="pic rv"><img src="{r}img/{img}" alt=""></div>' if img else ""
    return f"""<section class="phero"><div class="wrap"><div class="grid"{' style="grid-template-columns:1fr"' if not img else ''}>
<div><div class="crumb">{crumb}</div>{f'<div class="num">{num}</div>' if num else ''}<h1>{h1}</h1><p>{p}</p></div>{pic}</div></div></section>"""


def expertise(x):
    r = "../"
    cards = "".join(f'<div class="card rv"><div class="ico">{ic(EXP_ICON[x["slug"]])}</div><h3>{a}</h3><p>{b}</p></div>' for a, b in x["cards"])
    faq = "".join(f"<details><summary>{a}</summary><p>{b}</p></details>" for a, b in x["faq"])
    others = "".join(f'<a href="{o["slug"]}.html">{o["title"]} {ic("arrow")}</a>' for o in EXPERTISES if o is not x)
    body = phero(r, f'<a href="../index.html">Accueil</a> / <a href="../index.html#expertises">Expertises</a> / {x["title"]}', x["title"], e(x["lead"]), x["img"], f'{x["num"]} — EXPERTISE') + f"""
{cta_band(r)}
<section><div class="wrap"><div class="sec-head rv"><div><span class="kicker">Ce que nous réalisons</span><h2>{x['title']} : nos interventions.</h2></div></div>
<div class="cards4">{cards}</div></div></section>
<section style="padding-top:0"><div class="wrap"><div class="sec-head rv"><div><span class="kicker">Questions fréquentes</span><h2>Vos questions.</h2></div></div>
<div class="faq rv">{faq}</div></div></section>
<section style="padding-top:0"><div class="wrap"><div class="sec-head"><div><span class="kicker">Nos autres expertises</span></div></div><div class="other">{others}</div></div></section>
{cta_final(r)}"""
    return shell(f"{x['title']} | BATHELEC", f"{x['title']} — {x['short']} Bathelec, Île-de-France.", body,
                 f"expertises/{x['slug']}.html", 1, "exp")


def references():
    quotes = "".join(f'<blockquote class="q rv"><p>{e(t)}</p><cite>{e(a)}</cite></blockquote>' for t, a in TEMOIGNAGES)
    body = phero("", '<a href="index.html">Accueil</a> / Références', "Nos références",
                 "Administrations, universités, hôpitaux, collectivités et grands comptes privés nous confient leurs bâtiments, le plus souvent dans le cadre de marchés à bons de commande et d'accords-cadres.", "hall.jpg") + f"""
<section style="padding-top:20px" id="carte"><div class="wrap">
<div class="sec-head rv"><div><span class="kicker">Carte des réalisations</span><h2>Nos chantiers en Île-de-France.</h2></div></div>
{map_html("")}</div></section>
<section class="soft" id="realisations"><div class="wrap"><div class="sec-head rv"><div><span class="kicker">Accords-cadres multi-sites</span><h2>Des marchés à l'échelle d'un patrimoine.</h2>
<p class="lead">Ces marchés couvrent plusieurs sites et s'exécutent commande après commande.</p></div></div>
{multi_html("")}</div></section>
<section><div class="wrap"><div class="sec-head rv"><div><span class="kicker">Ils nous font confiance</span><h2>Nos clients.</h2></div></div>
{logos_html("")}<div class="quotes">{quotes}</div></div></section>
{cta_final("")}"""
    return shell("Références | BATHELEC", "Les références de Bathelec en Île-de-France : AP-HP, EDF, ministère des Armées, Région Île-de-France, universités, collectivités et grands comptes.", body, "references.html", 0, "refs", extra_js=MAP_JS)


def entreprise():
    certs = "".join(f"<div><b>{a}</b><span>{b}</span></div>" for a, b in CERTIFS)
    eng = "".join(f'<div class="rv"><span class="ico">{ic(ENG_ICONS[i])}</span><h3>{a}</h3><p>{b}</p></div>' for i, (a, b) in enumerate(ENGAGEMENTS))
    body = phero("", '<a href="index.html">Accueil</a> / L\'entreprise', "Notre histoire, notre ADN",
                 "Des femmes et des hommes, un savoir-faire et un engagement : être 100 % disponibles pour nos clients.", "equipe.jpg") + f"""
<section><div class="wrap split">
<div class="rv"><span class="kicker">Notre histoire</span><h2>Des colonnes montantes à l'ensemble du lot électricité.</h2>
<p class="lead" style="margin-top:20px">À l'origine filiale du groupe Léon Grosse, Bathelec rejoint le Groupe SITTE en 2019. Spécialisée dans l'installation et la réfection de colonnes montantes, l'entreprise intervient aujourd'hui en courants forts et courants faibles auprès de clients institutionnels, majoritairement publics, et de grands comptes privés.</p>
<p class="lead" style="margin-top:16px">La recherche de marchés récurrents et d'une clientèle stable repose sur des valeurs humaines fortes, indispensables à un engagement durable envers nos clients et nos partenaires.</p>
<div class="timeline">{"".join(f"<div><b>{v}</b><p>Chiffre d'affaires {a}</p></div>" for a, v in CA)}</div></div>
<div class="img rv"><img src="img/surete.jpg" alt="Hall d'un bâtiment public équipé en contrôle d'accès" loading="lazy"></div></div></section>
<section class="soft"><div class="wrap"><div class="sec-head rv"><div><span class="kicker">Direction</span><h2>Une équipe de direction engagée.</h2></div>
<p class="lead" style="max-width:480px">Bathelec est dirigée par Pierre Chaplain, Jean-Baptiste Manca et Bernard Dupont.</p></div>
<div class="eng">{eng}</div></div></section>
<section><div class="wrap"><div class="sec-head rv"><div><span class="kicker">Qualifications</span><h2>Des compétences reconnues.</h2></div></div>
<div class="certs rv">{certs}</div></div></section>
<section style="padding-top:0"><div class="wrap split">
<div class="rv"><span class="kicker">Implantations</span><h2>Deux sites en Île-de-France.</h2>
<ul class="sect"><li><span class="ico">{ic("pin")}</span><div><h3>Siège — Saint-Denis</h3><p>1-3 rue de la Procession, 93210 Saint-Denis</p></div></li>
<li><span class="ico">{ic("pin")}</span><div><h3>Agence — Ivry-sur-Seine</h3><p>1 rue Michelet, 94200 Ivry-sur-Seine</p></div></li></ul></div>
<div class="rv"><span class="kicker">Périmètre d'action</span><h2>Toute l'Île-de-France.</h2><p class="lead" style="margin-top:16px">Paris, Seine-et-Marne, Yvelines, Essonne, Hauts-de-Seine, Seine-Saint-Denis, Val-de-Marne et Val-d'Oise.</p></div></div></section>
{cta_final("")}"""
    return shell("L'entreprise | BATHELEC", "Bathelec, filiale du Groupe SITTE depuis 2019 : histoire, direction, qualifications Qualifelec et implantations en Île-de-France.", body, "entreprise.html", 0, "ent")


def carrieres():
    jobs = "".join(f'<div class="job rv"><h3>{a}</h3><p>{b}</p><div class="tags"><span>CDI</span><span>Île-de-France</span><span>Véhicule de fonction</span><span>RTT</span><span>Primes</span></div></div>' for a, b in POSTES)
    opts = "".join(f"<option>{e(a)}</option>" for a, _ in POSTES) + "<option>Candidature spontanée</option>"
    body = f"""
<section class="phero"><div class="bg" style="background-image:url(img/equipe.jpg)"></div><div class="wrap">
<div class="crumb"><a href="index.html">Accueil</a> / Carrières</div><h1>Rejoignez Bathelec</h1>
<p>Nous recrutons des profils confirmés pour notre département Tertiaire : des chantiers variés, des équipes soudées, du lundi au vendredi en journée.</p></div></section>
<section><div class="wrap"><div class="sec-head rv"><div><span class="kicker">Nos offres</span><h2>Postes ouverts.</h2></div></div>
<div class="jobs">{jobs}</div></div></section>
<section style="padding-top:0" id="postuler"><div class="wrap cgrid">
<div class="info rv"><span class="kicker">Postuler</span><h2>Envoyez-nous votre candidature.</h2>
<p class="lead" style="margin-top:16px">Candidatures spontanées bienvenues.</p><h3>Recrutement</h3><a href="mailto:{MAIL_RH}">{ic("mail")}{MAIL_RH}</a></div>
<form class="f rv" action="{FORM_RH}" method="POST">
<input type="hidden" name="_subject" value="Candidature via bathelec.fr"><input type="hidden" name="_next" value="{DOMAIN}/merci.html"><input type="hidden" name="_captcha" value="false"><input type="text" name="_honey" style="display:none">
<div><label>Prénom</label><input name="Prénom" required></div><div><label>Nom</label><input name="Nom" required></div>
<div><label>E-mail</label><input type="email" name="email" required></div><div><label>Téléphone</label><input name="Téléphone"></div>
<div class="full"><label>Poste</label><select name="Poste">{opts}</select></div>
<div class="full"><label>Lien vers votre CV ou profil LinkedIn</label><input name="CV"></div>
<div class="full"><label>Message</label><textarea name="Message"></textarea></div>
<div class="full"><button class="btn btn-o" type="submit">Envoyer ma candidature {ic("arrow")}</button></div></form></div></section>"""
    return shell("Carrières | BATHELEC", "Rejoignez Bathelec : électriciens HT/BT, techniciens SSI, contrôle d'accès, vidéosurveillance, chargés d'étude de prix en Île-de-France.", body, "carrieres.html", 0, "car")


def contact():
    opts = "".join(f"<option>{x['title']}</option>" for x in EXPERTISES) + "<option>Marché à bons de commande / accord-cadre</option><option>Autre</option>"
    body = f"""
<section class="phero"><div class="bg" style="background-image:url(img/hero.jpg)"></div><div class="wrap">
<div class="crumb"><a href="index.html">Accueil</a> / Contact</div><h1>Contact</h1>
<p>Visite, étude de prix et proposition sur demande, sans engagement.</p></div></section>
<section id="form"><div class="wrap cgrid">
<div class="info rv"><span class="kicker">Nous joindre</span><h2>Parlons de votre projet.</h2>
<h3>Téléphone</h3><a href="tel:{TEL_HREF}">{ic("phone")}{TEL}</a>
<h3>E-mail</h3><a href="mailto:{MAIL}">{ic("mail")}{MAIL}</a>
<h3>Siège</h3><p>1-3 rue de la Procession<br>93210 Saint-Denis</p>
<h3>Agence</h3><p>1 rue Michelet<br>94200 Ivry-sur-Seine</p>
<h3>Recrutement</h3><a href="carrieres.html">{ic("arrow")}Nos offres d'emploi</a></div>
<form class="f rv" action="{FORM_CONTACT}" method="POST">
<input type="hidden" name="_subject" value="Demande de contact via bathelec.fr"><input type="hidden" name="_next" value="{DOMAIN}/merci.html"><input type="hidden" name="_captcha" value="false"><input type="text" name="_honey" style="display:none">
<div><label>Prénom</label><input name="Prénom" required></div><div><label>Nom</label><input name="Nom" required></div>
<div><label>Organisation</label><input name="Organisation"></div><div><label>Fonction</label><input name="Fonction"></div>
<div><label>E-mail</label><input type="email" name="email" required></div><div><label>Téléphone</label><input name="Téléphone"></div>
<div class="full"><label>Objet</label><select name="Objet">{opts}</select></div>
<div class="full"><label>Votre projet</label><textarea name="Message" required placeholder="Site, nature des travaux, calendrier…"></textarea></div>
<div class="full"><button class="btn btn-o" type="submit">Envoyer ma demande {ic("arrow")}</button></div></form></div></section>"""
    return shell("Contact et devis | BATHELEC", "Contactez Bathelec pour vos travaux d'électricité, courants faibles, sûreté et IRVE en Île-de-France. Devis sur demande, sans engagement.", body, "contact.html", 0, "contact")


def merci():
    body = f"""<section class="phero" style="min-height:60vh"><div class="bg" style="background-image:url(img/hero.jpg)"></div><div class="wrap">
<h1>Merci.</h1><p>Votre message a bien été envoyé. Nous revenons vers vous rapidement.</p><p style="margin-top:30px"><a class="btn btn-g" href="index.html">Retour à l'accueil {ic("arrow")}</a></p></div></section>"""
    return shell("Merci | BATHELEC", "Message envoyé.", body, "merci.html")


def legal():
    body = f"""<section><div class="wrap legal"><span class="kicker">Informations légales</span><h1 style="font-size:44px">Mentions légales</h1>
<h2>Éditeur</h2><p>BATHELEC, société anonyme au capital de 150 000 €, société du Groupe SITTE<br>Siège social : 1-3 rue de la Procession, 93210 Saint-Denis<br>Téléphone : {TEL} — {MAIL}<br>SIRET : 438 765 083 00045 — APE : 4321A — TVA : FR 23 438 765 083<br>Directeur de la publication : Pierre Chaplain</p>
<h2>Hébergement</h2><p>GitHub, Inc. (GitHub Pages), 88 Colin P. Kelly Jr Street, San Francisco, CA 94107, États-Unis.</p>
<h2>Données personnelles</h2><p>Les informations transmises via les formulaires sont utilisées uniquement pour répondre à votre demande ou traiter votre candidature, et ne sont jamais cédées à des tiers. Les formulaires sont acheminés par le service FormSubmit. Conformément au RGPD, vous disposez d'un droit d'accès, de rectification et de suppression : écrivez à {MAIL}.</p>
<h2>Cookies</h2><p>Ce site n'utilise aucun cookie de mesure d'audience ni de publicité.</p>
<h2>Propriété intellectuelle</h2><p>Les contenus de ce site (textes, logo, visuels) sont la propriété de BATHELEC, sauf mention contraire. Les noms de clients sont cités à titre de références.</p></div></section>"""
    return shell("Mentions légales | BATHELEC", "Mentions légales du site bathelec.fr.", body, "mentions-legales.html")


# ---------------------------------------------------------------- build
def write(path, content):
    p = os.path.join(DIST, path)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        f.write(content)


def main():
    if os.path.exists(DIST):
        shutil.rmtree(DIST)
    os.makedirs(DIST)
    shutil.copytree(os.path.join(ROOT, "img"), os.path.join(DIST, "img"),
                    ignore=shutil.ignore_patterns("*_raw*", "*_src*", "src"))
    write("assets/style.css", CSS)
    pages = {"index.html": home(), "references.html": references(), "entreprise.html": entreprise(),
             "carrieres.html": carrieres(), "contact.html": contact(), "merci.html": merci(),
             "mentions-legales.html": legal()}
    for x in EXPERTISES:
        pages[f"expertises/{x['slug']}.html"] = expertise(x)
    for k, v in pages.items():
        write(k, v)
    urls = "".join(f"<url><loc>{DOMAIN}/{k.replace('index.html','')}</loc></url>" for k in pages if k != "merci.html")
    write("sitemap.xml", f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>')
    write("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {DOMAIN}/sitemap.xml\n")
    write("CNAME", "www.bathelec.fr\n")
    print("OK", len(pages), "pages")


if __name__ == "__main__":
    main()
