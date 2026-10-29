"""Write the new slides for the PSI redox talk (run from the repo root).

Each slide uses the same 1920x1080 layout as the rest of the deck: eyebrow,
zoom/breadcrumb line, title, a live <x-embed> canvas, text cards, a citation
footer and a page number. Page numbers and speaker notes are filled in later
by scripts/notes_redox.py.
"""
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
STEPS = ["absorb", "funnel", "climb", "trap", "poise", "design"]
HEAD = "'Space Grotesk', Arial, sans-serif"
MONO = "'JetBrains Mono', 'Courier New', monospace"

LIB = """const c=document.getElementById("c"),x=c.getContext("2d"),SF="system-ui,-apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif";
function R(){const d=devicePixelRatio||1,W=innerWidth||DW,H=innerHeight||DH;c.width=W*d;c.height=H*d;c.style.width=W+"px";c.style.height=H+"px";const s=Math.min(W/DW,H/DH);x.setTransform(d*s,0,0,d*s,(W-DW*s)*d/2,(H-DH*s)*d/2)}
function T(s,X,Y,z,k,a,w){x.font=(w||400)+" "+z+"px "+SF;x.fillStyle=k;x.textAlign=a||"left";x.fillText(s,X,Y)}
function C(X,Y,r,k){x.beginPath();x.arc(X,Y,Math.max(r,0),0,6.2832);x.fillStyle=k;x.fill()}
function Ln(a,b,e,f,k,w){x.beginPath();x.moveTo(a,b);x.lineTo(e,f);x.strokeStyle=k;x.lineWidth=w||2;x.stroke()}
function L(m){x.save();x.setTransform(1,0,0,1,0,0);x.clearRect(0,0,c.width,c.height);x.restore();x.save();D(m/1000);x.restore();requestAnimationFrame(L)}
const sm=k=>{k=Math.min(Math.max(k,0),1);return k*k*(3-2*k)};"""


def crumb(step, zoom):
    parts = [f'<span style="color:#B45309"><b>{s}</b></span>' if s == step else s for s in STEPS]
    z = f'<span style="color:#2F7D4F;font-weight:600">zoom {zoom}</span> · ' if zoom else ""
    return z + " → ".join(parts)


def embed(left, top, w, h, js):
    return (f'<x-embed style="position:absolute;left:{left}px;top:{top}px;width:{w}px;height:{h}px">'
            '<meta charset="utf-8"><style>html,body{margin:0;height:100%;overflow:hidden;background:transparent}'
            f'canvas{{display:block}}</style><canvas id="c"></canvas><script>\nconst DW={w},DH={h};\n{LIB}\n'
            f'{js.strip()}\nonresize=R;R();requestAnimationFrame(L);\n</script></x-embed>')


def card(top, title, body, color="#0E7490", n=1, left=1040, width=696):
    return (f'<div data-build-in="rise {n}" style="position:absolute;left:{left}px;top:{top}px;width:{width}px;background:#F4F6FA;'
            'border:1px solid #DDE3EC;border-radius:16px;padding:28px;display:flex;flex-direction:column;gap:12px">\n'
            f'<h3 style="font-family:{HEAD};font-size:32px;font-weight:600;color:{color}">{title}</h3>\n'
            f'<p style="font-size:26px;line-height:1.4;color:#2D3748">{body}</p>\n</div>')


def eq(top, lines, n=1, left=1040, width=704):
    ps = "".join(f'<p style="font-family:{MONO};font-size:26px;line-height:1.5;color:{k}">{s}</p>' for s, k in lines)
    return (f'<div data-build-in="rise {n}" style="position:absolute;left:{left}px;top:{top}px;width:{width}px;background:#FBF7EF;'
            f'border-left:6px solid #B45309;border-radius:12px;padding:24px;display:flex;flex-direction:column;gap:2px">{ps}</div>')


def slide(sid, eyebrow, step, zoom, title, emb, cards, foot, transition="fade"):
    body = emb + "\n" + cards
    return f"""<section id="{sid}" data-transition="{transition}" style="background:#FFFFFF;color:#1A2233;font-family:'IBM Plex Sans', Arial, sans-serif;padding:128px 128px 160px;display:flex;flex-direction:column">
<p style="position:absolute;left:128px;top:92px;width:800px;font-size:24px;letter-spacing:4px;text-transform:uppercase;color:#B45309;font-weight:600">{eyebrow}</p>
<p style="position:absolute;left:960px;top:92px;width:832px;font-size:24px;text-align:right;color:#6B7280">{crumb(step, zoom)}</p>
<h2 style="position:absolute;left:128px;top:132px;width:1664px;font-family:{HEAD};font-size:60px;font-weight:600;line-height:1.1;color:#1A2233">{title}</h2>
{body}
<p style="position:absolute;left:128px;bottom:64px;width:1480px;font-size:24px;color:#6B7280">{foot}</p>
<p style="position:absolute;left:1672px;bottom:64px;width:120px;font-size:24px;color:#6B7280;text-align:right">00</p>
<aside></aside>
</section>
"""


S = {}

# ---------------------------------------------------------------- cover
S["cover"] = f"""<section id="cover" data-transition="fade" style="background:radial-gradient(circle at 75% 45%, #EEF4FB 0%, #FFFFFF 62%);color:#1A2233;font-family:'IBM Plex Sans', Arial, sans-serif;padding:128px;display:flex;flex-direction:column">
<p style="position:absolute;left:128px;top:150px;width:900px;font-size:24px;letter-spacing:4px;text-transform:uppercase;color:#B45309;font-weight:600">CHM 598 · Introduction to Photochemistry</p>
<h1 data-build-in="rise 1 auto" style="position:absolute;left:128px;top:206px;width:900px;font-family:{HEAD};font-size:88px;font-weight:700;line-height:1.05;color:#1A2233">Light, redox and energy flow in Photosystem I</h1>
<p data-build-in="fade 2 auto" style="position:absolute;left:128px;top:520px;width:880px;font-size:36px;line-height:1.3;color:#4A5568">How the protein’s redox state decides where an absorbed photon’s energy goes</p>
<p data-build-in="fade 3 auto" style="position:absolute;left:128px;top:680px;width:860px;font-size:30px;line-height:1.35;color:#B45309">An excited chlorophyll has about 6 ns. An open reaction centre uses it in about 30 ps. A closed one does not.</p>
<p data-build-in="fade 4 auto" style="position:absolute;left:128px;top:870px;width:900px;font-size:28px;color:#1A2233"><b>Ditsa Mallick</b> · [presentation date]</p>
{embed(1060, 150, 740, 780, '''
const N=[];for(let r=0;r<5;r++){const n=r?r*7:1;for(let i=0;i<n;i++){const a=i/n*6.2832+r*.5;N.push([370+Math.cos(a)*r*62,360+Math.sin(a)*r*62,r==4&&i%7==3])}}
let P=[],last=-9;
function D(t){const cyc=t%16,open=cyc<8;
if(t-last>.6){last=t;let n;do{n=1+Math.floor(Math.random()*(N.length-1))}while(N[n][2]);P.push({n,t0:t,path:[n],end:Math.random()})}
for(let i=0;i<N.length;i++)for(let j=i+1;j<N.length;j++){const dx=N[i][0]-N[j][0],dy=N[i][1]-N[j][1];if(dx*dx+dy*dy<5600)Ln(N[i][0],N[i][1],N[j][0],N[j][1],"rgba(47,125,79,.25)",1.5)}
N.forEach((p,i)=>C(p[0],p[1],i?(p[2]?11:9):18,i?(p[2]?"#B91C1C":"#2F7D4F"):(open?"#0E7490":"#94A3B8")));
P=P.filter(p=>t-p.t0<2.6);
for(const p of P){const s=t-p.t0,q=N[p.n];
if(s<.6){const k=s/.6;C(q[0],q[1],30*(1-k)+4,"rgba(242,165,65,"+(1-k).toFixed(2)+")")}
else if(s<1.6){const red=N.findIndex(z=>z[2]&&Math.hypot(z[0]-q[0],z[1]-q[1])<200),goal=open?N[0]:(red>0?N[red]:N[0]),k=sm((s-.6)/1);C(q[0]+(goal[0]-q[0])*k,q[1]+(goal[1]-q[1])*k,10,"#1A2233")}
else{const k=(s-1.6)/1;if(open)C(N[0][0],N[0][1],18+40*k,"rgba(14,116,144,"+(.5*(1-k)).toFixed(2)+")");else{const red=N.findIndex(z=>z[2]&&Math.hypot(z[0]-q[0],z[1]-q[1])<200),z=red>0?N[red]:N[0];C(z[0],z[1],12+30*k,"rgba(185,28,28,"+(.5*(1-k)).toFixed(2)+")")}}}
T(open?"reaction centre open: energy becomes charge":"reaction centre closed: energy waits, or leaves as red light",370,700,26,open?"#0E7490":"#B91C1C","center",600);
C(120,750,8,"#2F7D4F");T("chlorophyll",136,758,24,"#4A5568");C(310,750,9,"#B91C1C");T("red chlorophyll",326,758,24,"#4A5568");C(540,750,10,"#0E7490");T("P700",556,758,24,"#4A5568");
}''')}
<aside></aside>
</section>
"""

# ---------------------------------------------------------------- fates
S["fates"] = slide("fates", "The question", "absorb", "1 nm", "Three fates for one absorbed photon", embed(128, 250, 860, 660, '''
const F=[["charge separation","#0E7490"],["heat","#94A3B8"],["fluorescence","#B45309"]];
const OPEN=[.97,.02,.01],SHUT=[0,.8,.2];let cnt=[0,0,0],mode=-1,P=[],last=0;
function D(t){const m=(t%20)<10?0:1;if(m!=mode){mode=m;cnt=[0,0,0];P=[]}
const pr=m?SHUT:OPEN;
if(t-last>.25){last=t;const r=Math.random();const f=r<pr[0]?0:r<pr[0]+pr[1]?1:2;P.push({t0:t,f,y:120+Math.random()*200})}
T(m?"reaction centre closed":"reaction centre open",430,40,30,m?"#B91C1C":"#0E7490","center",600);
C(120,230,46,"#E8F1E9");C(120,230,22,"#2F7D4F");T("Chl*",120,310,24,"#2F7D4F","center",600);
const ends=[[600,120],[600,230],[600,340]];
ends.forEach((e,i)=>{Ln(170,230,e[0]-40,e[1],"rgba(148,163,184,.5)",2);C(e[0],e[1],28,F[i][1]);T(F[i][0],e[0]+44,e[1]+8,24,"#2D3748")});
P=P.filter(p=>t-p.t0<1.2);for(const p of P){const k=sm((t-p.t0)/1),e=ends[p.f];C(170+(e[0]-40-170)*k,230+(e[1]-230)*k,8,F[p.f][1]);if(t-p.t0>1&&!p.c){p.c=1;cnt[p.f]++}}
const tot=Math.max(cnt[0]+cnt[1]+cnt[2],1);T("photons counted: "+tot,40,450,24,"#6B7280");
F.forEach((f,i)=>{const y=480+i*52,w=cnt[i]/tot*560;x.fillStyle=f[1];x.fillRect(220,y,Math.max(w,2),34);T(f[0],210,y+26,24,"#2D3748","right");T((cnt[i]/tot*100).toFixed(0)+" %",230+w,y+26,24,"#1A2233","left",600)});
}'''), "\n".join([
    card(250, "Branching ratios", "Every absorbed photon ends in exactly one fate. Its yield is its rate divided by the sum of all rates.", "#0E7490", 1),
    eq(486, [("Φᵢ = kᵢ / Σⱼ kⱼ", "#1A2233"), ("open PSI: Φ_CS ≈ 0.97–0.99", "#B45309")], 2),
    card(630, "Today’s question", "If the protein’s redox state changes one rate, where does the photon’s energy go instead?", "#B45309", 3),
]), "Trapping yield of PSI: Gobets &amp; van Grondelle, BBA 1507, 80 (2001) · CHM 598 L13, L16 · the closed-centre split is illustrative")

# ---------------------------------------------------------------- uphill
S["uphill"] = slide("uphill", "Red chlorophylls", "climb", "2 nm", "Some chlorophylls sit below the trap", embed(128, 250, 860, 660, '''
const kB=8.617e-5,E={bulk:1239.84/700,p:1239.84/700,red:1239.84/740};const y=e=>560-(e-1.62)*2600;
function D(t){const s=(Math.sin(t*.45)+1)/2,K=77+s*(295-77),dE=E.bulk-E.red,r=Math.exp(-dE/(kB*K));
T("T = "+K.toFixed(0)+" K",40,44,30,"#1A2233","left",600);T("kT = "+(kB*K*1000).toFixed(1)+" meV",40,82,24,"#6B7280");
const lv=[["bulk Chl ~700 nm",E.bulk,160,"#2F7D4F",-1],["P700 (trap)",E.p,400,"#0E7490",-1],["red Chl ~740 nm",E.red,620,"#B91C1C",1]];
lv.forEach(([n,e,X,k,u])=>{Ln(X,y(e),X+200,y(e),k,6);T(n,X+100,y(e)+(u<0?-18:40),24,k,"center",600);T(e.toFixed(3)+" eV",X+100,y(e)+(u<0?40:72),24,"#6B7280","center")});
Ln(120,y(E.bulk),120,y(E.red),"#94A3B8",2);Ln(110,y(E.bulk),130,y(E.bulk),"#94A3B8",2);Ln(110,y(E.red),130,y(E.red),"#94A3B8",2);T("ΔE ≈ "+(dE*1000).toFixed(0)+" meV",140,(y(E.red)+y(E.bulk))/2+40,24,"#1A2233","left",600);
const wDown=10,wUp=Math.max(10*r*40,1.2);
x.beginPath();x.moveTo(360,y(E.bulk)+14);x.quadraticCurveTo(470,y(E.red)-10,612,y(E.red)-4);x.strokeStyle="rgba(185,28,28,.75)";x.lineWidth=wDown;x.stroke();T("downhill: fast",450,y(E.red)+44,24,"#B91C1C","center");
x.beginPath();x.moveTo(800,y(E.red)-14);x.quadraticCurveTo(840,y(E.bulk)-90,610,y(E.bulk)-10);x.strokeStyle="rgba(14,116,144,.85)";x.lineWidth=wUp;x.stroke();T("uphill: needs heat",720,y(E.bulk)-74,24,"#0E7490","center");
T("k_up / k_down = e^(−ΔE/kT) = "+(r<1e-3?r.toExponential(1):r.toFixed(3)),40,640,28,"#1A2233","left",600);
}'''), "\n".join([
    card(250, "Low-energy “red” pigments", "Strongly coupled chlorophyll clusters absorb at 708–740 nm, below P700 at 700 nm. Cyanobacterial PSI trimers have several, and the Spirulina trimer has one at ~740 nm.", "#B91C1C", 1),
    eq(560, [("k_up/k_down = (g_up/g_down) e^(−ΔE/kT)", "#1A2233"), ("295 K: ≈ 0.02 · 77 K: ≈ 5 × 10⁻⁷", "#B45309")], 2),
    card(704, "Detailed balance", "At room temperature heat lifts energy back to P700. Freeze to 77 K and it stays trapped on the red pigments.", "#0E7490", 3),
]), "Karapetyan, Holzwarth &amp; Rögner, FEBS Lett. 460, 395 (1999) · Gobets &amp; van Grondelle 2001 · CHM 598 L13 · degeneracy ratio set to 1 in the plot")

# ---------------------------------------------------------------- cold
S["cold"] = slide("cold", "Low-temperature fluorescence", "climb", "15 nm", "At 77 K, red emission reports where the energy is stuck", embed(128, 250, 860, 660, '''
const g=(l,c0,s)=>Math.exp(-((l-c0)**2)/(2*s*s));const X=l=>60+(l-660)/(800-660)*760,Y=v=>520-v*400;
function D(t){const s=sm((Math.sin(t*.5)+1)/2),K=295-s*(295-77),q=(Math.sin(t*.23)+1)/2;
const open=.45+.55*q;
const sp=l=>(1-s)*(.22*g(l,690,14)+.12*g(l,725,22))+s*(.1*g(l,685,7)+.12*g(l,725,12)+(.95-.6*open)*g(l,760,11));
Ln(60,520,820,520,"#94A3B8",2);Ln(60,100,60,520,"#94A3B8",2);
for(const l of [680,720,760,800])T(l+"",X(l),556,24,"#4A5568","center");T("emission wavelength (nm)",440,600,24,"#6B7280","center");
x.beginPath();for(let l=660;l<=800;l+=1){const v=sp(l);if(l==660)x.moveTo(X(l),Y(v));else x.lineTo(X(l),Y(v))}x.strokeStyle="#B45309";x.lineWidth=4;x.stroke();
x.lineTo(X(800),520);x.lineTo(X(660),520);x.fillStyle="rgba(180,83,9,.08)";x.fill();
T("T = "+K.toFixed(0)+" K",80,60,30,"#1A2233","left",600);
if(s>.7){T("F760",X(760),Y(sp(760))-16,26,"#B91C1C","center",600);T("trap "+(open>.75?"open: more quenching":"closed: less quenching"),820,60,24,"#0E7490","right",600)}
}'''), "\n".join([
    card(250, "Why freeze", "At 77 K uphill transfer stops (previous slide), so red pigments keep their energy long enough to fluoresce. The F760 band becomes a direct readout.", "#0E7490", 1),
    eq(500, [("Φ_F760 = k_F / (k_F + k_nr + k_Q)", "#1A2233"), ("k_Q: quenching by the reaction centre", "#B45309")], 2),
    card(644, "A redox reporter", "In Spirulina trimers, P700⁺ quenches F760. So the red band’s size depends on the reaction centre’s redox state.", "#B91C1C", 3),
]), "Karapetyan et al. 1999; Shubin, Bezsmertnaya &amp; Karapetyan, J. Photochem. Photobiol. B 30, 153 (1995) · spectra are a schematic model, not measured data")

# ---------------------------------------------------------------- poise
S["poise"] = slide("poise", "Redox poising", "poise", "3 nm", "Solution potential sets which cofactors are reduced", embed(128, 250, 860, 660, '''
const Co=[["P700⁺/P700",.43],["F_A",-.52],["F_B",-.58],["dithionite (pH 7)",-.66],["F_X",-.70],["A₁",-.80],["A₀",-1.05]],F=96485,RT=8.314*295;
const yy=e=>60+(.55-e)/1.7*560;
function D(t){const Eh=.45-((Math.sin(t*.35-1.2)+1)/2)*1.15;
Ln(140,yy(.55),140,yy(-1.15),"#94A3B8",2);for(const e of [.2,-.2,-1])T(e.toFixed(1)+" V",128,yy(e)+8,24,"#6B7280","right");for(const [n,e] of [["Fe(CN)₆³⁻",.36],["S₂O₄²⁻",-.66]]){Ln(140,yy(e),850,yy(e),"rgba(185,28,28,.45)",2);T(n,128,yy(e)+8,22,"#B91C1C","right",600)}
x.fillStyle="rgba(14,116,144,.08)";x.fillRect(150,yy(Eh),700,yy(-1.15)-yy(Eh));
Ln(150,yy(Eh),850,yy(Eh),"#0E7490",3);T("solution E_h = "+Eh.toFixed(2)+" V",840,yy(Eh)-12,24,"#0E7490","right",600);
Co.forEach(([n,e],i)=>{const red=1/(1+Math.exp(F*(Eh-e)/RT)),X=[200,200,470,0,200,470,200][i],Y=yy(e);
if(n.startsWith("dithionite"))return;
C(X,Y,16,"#E2E8F0");x.beginPath();x.arc(X,Y,16,-1.5708,-1.5708+6.2832*red);x.lineTo(X,Y);x.fillStyle=i?"#2F7D4F":"#B45309";x.fill();
T(n+"  "+e.toFixed(2)+" V · "+(red*100).toFixed(0)+"% red.",X+28,Y+8,22,"#1A2233")});
}'''), "\n".join([
    card(250, "Nernst on every cofactor", "Each cofactor is reduced or oxidised according to how the solution potential compares with its midpoint.", "#0E7490", 1),
    eq(460, [("f_red = 1 / (1 + e^(nF(E_h − E_m)/RT))", "#1A2233"), ("ferricyanide ≈ +0.36 V · dithionite ≈ −0.66 V", "#B45309")], 2),
    card(604, "Open or closed", "Oxidise P700 and the trap becomes a quencher. Reduce F_A/F_B and electrons cannot leave, so charge pairs recombine. Either way the photon’s energy is redistributed.", "#B91C1C", 3),
]), "Midpoints: Brettel, BBA 1318, 322 (1997) · dithionite: Mayhew, Eur. J. Biochem. 85, 535 (1978), depends on pH and concentration · CHM 598 L13 (equilibrium)")

# ---------------------------------------------------------------- titrate
S["titrate"] = slide("titrate", "Experimental design", "poise", "1 cm", "Testing redox control: titrate, freeze, measure, reverse", embed(128, 250, 860, 660, '''
const st=["reductant","measure E_h","freeze 77 K","emission","oxidant"];
function D(t){const s=t%15,k=Math.min(s/2.6,4.999),i=k|0;
st.forEach((n,j)=>{const X=90+j*170,on=j<=i;C(X,60,22,on?"#0E7490":"#E2E8F0");T(j+1+"",X,68,22,on?"#FFFFFF":"#6B7280","center",600);T(n,X,112,20,on?"#1A2233":"#94A3B8","center")});
const red=i<4?Math.min(s/5,1):Math.max(1-(s-10.4)/2,0);
x.fillStyle="#CBD5E1";x.fillRect(150,170,120,300);x.fillStyle="rgba("+(120-60*red|0)+","+(170-40*red|0)+","+(120+20*red|0)+",.75)";x.fillRect(158,220,104,242);
T("PSI sample",210,510,24,"#2D3748","center");
Ln(300,300,380,300,"#94A3B8",3);x.fillStyle="#1A2233";x.fillRect(380,250,150,100);T("ORP",455,290,24,"#FFFFFF","center",600);T((80-640*red).toFixed(0)+" mV",455,330,24,"#F2A541","center",600);
if(i>=2){const f=Math.min((s-5.2)/1.5,1);x.fillStyle="rgba(186,230,253,"+(.5*f).toFixed(2)+")";x.fillRect(140,160,140,320);T("77 K",210,200,24,"#0E7490","center",600)}
if(i>=3){x.strokeStyle="#94A3B8";x.lineWidth=2;x.strokeRect(570,200,260,230);const g=(l,c0,w)=>Math.exp(-((l-c0)**2)/(2*w*w));x.beginPath();for(let l=670;l<=800;l+=2){const v=.15*g(l,685,7)+.15*g(l,725,12)+(.2+.6*red)*g(l,760,11),X=570+(l-670)/130*260,Y=420-v*200;if(l==670)x.moveTo(X,Y);else x.lineTo(X,Y)}x.strokeStyle="#B45309";x.lineWidth=3;x.stroke();T("emission (schematic)",700,460,22,"#6B7280","center")}
T(i<4?"reducing…":"back-titrating with oxidant",430,600,26,"#B91C1C","center",600);
}'''), "\n".join([
    card(250, "The protocol", "Add a reductant (dithionite) in steps, measure the potential, freeze each sample to 77 K and record its emission. Then add an oxidant (ferricyanide).", "#0E7490", 1),
    card(486, "Reading the result", "A change that reverses with oxidant means redox control. A change that does not reverse means the protein was damaged.", "#B45309", 2),
    card(704, "Good practice", "Measure E_h in the sample itself, add redox mediators so it equilibrates, and dark-adapt before freezing.", "#2F7D4F", 3),
]), "Schematic of the experimental approach, no measured data shown · Mayhew 1978 · Karapetyan et al. 1999")

# ---------------------------------------------------------------- compete
S["compete"] = slide("compete", "Kinetic model", "poise", "2 nm", "Closing the trap redistributes the photon", embed(128, 250, 860, 660, '''
const kF=1/15,kN=1/5;const Xq=q=>90+Math.log10(q/.01)/3*700,Yf=f=>420-f*1400;
function D(t){const lq=-2+3*((Math.sin(t*.4)+1)/2),kQ=10**lq,phi=kF/(kF+kN+kQ),tau=1/(kF+kN+kQ);
Ln(90,420,790,420,"#94A3B8",2);Ln(90,60,90,420,"#94A3B8",2);
x.beginPath();for(let u=-2;u<=1.001;u+=.02){const q=10**u,f=kF/(kF+kN+q);if(u<-1.99)x.moveTo(Xq(q),Yf(f));else x.lineTo(Xq(q),Yf(f))}x.strokeStyle="#B45309";x.lineWidth=4;x.stroke();
C(Xq(kQ),Yf(phi),12,"#B91C1C");
for(const [q,s] of [[.01,"0.01"],[.1,"0.1"],[1,"1"],[10,"10 ns⁻¹"]])T(s,Xq(q),456,24,"#4A5568","center");
T("k_Q, quenching by the reaction centre",440,496,24,"#6B7280","center");T("Φ_F",90,40,24,"#6B7280","center",600);T("0.25",78,Yf(.25)+8,22,"#6B7280","right");
T("Φ_F = "+phi.toFixed(3)+"   τ = "+(tau*1000<1000?(tau*1000).toFixed(0)+" ps":tau.toFixed(2)+" ns"),440,560,30,"#1A2233","center",600);
T(kQ>1?"trap working: red emission quenched":kQ<.1?"trap closed: red emission bright":"in between",440,610,26,kQ>1?"#0E7490":"#B91C1C","center",600);
}'''), "\n".join([
    card(250, "One state, many exits", "An excitation on a red pigment can fluoresce, decay as heat, or be removed by the reaction centre. Change one exit and the others change too.", "#0E7490", 1),
    eq(486, [("Φ₀/Φ = 1 + k_Q τ₀", "#1A2233"), ("τ₀ = 1/(k_F + k_nr)", "#B45309")], 2),
    card(630, "What the model predicts", "Making the trap less effective should brighten F760 and lengthen its lifetime. Lifetime measurements can test this separately from yield.", "#B45309", 3),
]), "Stern–Volmer form of rate competition · CHM 598 L13, L16 · k_F = (15 ns)⁻¹, k_nr = (5 ns)⁻¹ are illustrative values")

# ---------------------------------------------------------------- engineer
S["engineer"] = slide("engineer", "Ongoing work", "poise", "1 nm", "Next: tuning a single red-chlorophyll site", embed(128, 250, 860, 660, '''
const ph=["Ser  –OH","Cys  –SH","Cys  –S–S–"];
function D(t){const i=Math.floor(t/4)%3,k=sm((t%4)/1);
const cx=300,cy=320;x.save();x.translate(cx,cy);
for(let a=0;a<4;a++){const A=a*1.5708+.785;x.beginPath();x.arc(Math.cos(A)*95,Math.sin(A)*95,46,0,6.2832);x.strokeStyle="#2F7D4F";x.lineWidth=5;x.stroke()}
x.beginPath();x.arc(0,0,130,0,6.2832);x.strokeStyle="rgba(47,125,79,.35)";x.lineWidth=3;x.stroke();
C(0,0,22,"#64748B");T("Mg",0,8,22,"#FFFFFF","center",600);x.restore();
T("red chlorophyll",cx,cy+190,24,"#2F7D4F","center",600);
const X=620,Y=320;Ln(cx+135,cy,X-50,Y,"rgba(148,163,184,.7)",3);T("≈ 3–5 Å",(cx+135+X-50)/2,Y-14,24,"#6B7280","center");
C(X,Y,44,i==0?"#FDE68A":"#FCD34D");T(ph[i],X,Y+90,28,"#1A2233","center",600);T(i==0?"O":i==1?"S":"S–S",X,Y+10,28,"#1A2233","center",700);
const base=480,shift=[0,8,20][i]*k+[0,0,8][i]*(1-k);Ln(160,base,440,base,"#94A3B8",3);T("site energy",150,base+8,22,"#6B7280","right");
Ln(160,base+60+shift,440,base+60+shift,"#B91C1C",5);T("hypothesis",450,base+66+shift,22,"#B91C1C");
}'''), "\n".join([
    card(250, "The idea", "Place a cysteine a few ångströms from one red chlorophyll, with serine as the near-identical control (O vs S).", "#0E7490", 1),
    card(450, "Why cysteine", "Its thiol can be oxidised or reduced. Each form carries different charge and polarity, which could shift the pigment’s site energy.", "#B45309", 2),
    card(686, "How to test", "Same titrate–freeze–reverse protocol: does the F760 band shift or change size only when the thiol can change redox state?", "#2F7D4F", 3),
]), "Hypothesis and design only, no data shown · site-energy tuning by the protein environment: Gobets &amp; van Grondelle 2001; Karapetyan et al. 2014")

# ---------------------------------------------------------------- takeaways
S["takeaways"] = f"""<section id="takeaways" data-transition="fade" style="background:#FFFFFF;color:#1A2233;font-family:'IBM Plex Sans', Arial, sans-serif;padding:128px 128px 160px;display:flex;flex-direction:column">
<p style="position:absolute;left:128px;top:92px;width:800px;font-size:24px;letter-spacing:4px;text-transform:uppercase;color:#B45309;font-weight:600">Summary</p>
<p style="position:absolute;left:960px;top:92px;width:832px;font-size:24px;text-align:right;color:#1A2233"><b>{" → ".join(STEPS)}</b></p>
<h2 style="position:absolute;left:128px;top:132px;width:1664px;font-family:{HEAD};font-size:60px;font-weight:700;line-height:1.1;color:#1A2233">Conclusions: the trap’s redox state steers the photon</h2>
{embed(128, 300, 1100, 600, '''
const St=[["absorb","E = hc/λ, Franck–Condon"],["funnel","exciton coupling, Förster"],["climb","detailed balance, e^(−ΔE/kT)"],["trap","Marcus, tunneling"],["poise","Nernst, redox state"],["design","lessons for solar fuels"]];
function D(t){const p=(t*.35)%St.length;
St.forEach(([n,d],i)=>{const X=140+i*164,Y=200+(i%2)*160,on=p>=i;C(X,Y,40,on?"#0E7490":"#E2E8F0");T(n,X,Y+8,22,on?"#FFFFFF":"#6B7280","center",600);T(d,X,Y+(i%2?78:-60),20,"#4A5568","center");if(i)Ln(140+(i-1)*164+40,200+((i-1)%2)*160,X-40,Y,"rgba(148,163,184,.6)",2)});
const i=Math.floor(p),f=sm(p-i),j=Math.min(i+1,St.length-1),A=[140+i*164,200+(i%2)*160],B=[140+j*164,200+(j%2)*160];x.beginPath();x.arc(A[0]+(B[0]-A[0])*f,A[1]+(B[1]-A[1])*f,50,0,6.2832);x.strokeStyle="#F2A541";x.lineWidth=5;x.stroke();
}''')}
<p data-build-in="rise 1" style="position:absolute;left:1280px;top:300px;width:512px;font-size:26px;line-height:1.4;color:#1A2233"><b>1 · Rates compete.</b> Each fate’s yield is its share of the total rate: Φᵢ = kᵢ/Σk.</p>
<p data-build-in="rise 2" style="position:absolute;left:1280px;top:440px;width:512px;font-size:26px;line-height:1.4;color:#1A2233"><b>2 · Red pigments need heat.</b> Uphill transfer follows e^(−ΔE/kT), so at 77 K they become reporters.</p>
<p data-build-in="rise 3" style="position:absolute;left:1280px;top:590px;width:512px;font-size:26px;line-height:1.4;color:#1A2233"><b>3 · Redox poises the trap.</b> The Nernst equation sets which cofactors are reduced, which opens or closes the trap.</p>
<p data-build-in="rise 4" style="position:absolute;left:1280px;top:740px;width:512px;font-size:26px;line-height:1.4;color:#1A2233"><b>4 · Design lesson.</b> A solar-fuel catalyst must keep its trap open: clear electrons away fast.</p>
<p style="position:absolute;left:128px;bottom:64px;width:1480px;font-size:24px;color:#6B7280">Each step pairs a stage of the photon’s path with the lecture concept that governs it</p>
<p style="position:absolute;left:1672px;bottom:64px;width:120px;font-size:24px;color:#6B7280;text-align:right">00</p>
<aside></aside>
</section>
"""


def refs(sid, n, title, items):
    half = (len(items) + 1) // 2
    col = lambda xs, left: (f'<div style="position:absolute;left:{left}px;top:250px;width:800px;display:flex;flex-direction:column;gap:10px">'
                            + "".join(f'\n<p style="font-size:24px;line-height:1.3;color:#2D3748">{r}</p>' for r in xs) + "\n</div>")
    return f"""<section id="{sid}" data-transition="fade" style="background:#FFFFFF;color:#1A2233;font-family:'IBM Plex Sans', Arial, sans-serif;padding:128px 128px 160px;display:flex;flex-direction:column">
<p style="position:absolute;left:128px;top:92px;width:1664px;font-size:24px;letter-spacing:4px;text-transform:uppercase;color:#7C3AED;font-weight:600">References {n}/2</p>
<h2 style="position:absolute;left:128px;top:132px;width:1664px;font-family:{HEAD};font-size:60px;font-weight:600;line-height:1.1;color:#1A2233">{title}</h2>
{col(items[:half], 128)}
{col(items[half:], 992)}
<p style="position:absolute;left:1672px;bottom:64px;width:120px;font-size:24px;color:#6B7280;text-align:right">00</p>
<aside>References.</aside>
</section>
"""


R1 = ["Lewis NS, Nocera DG. Powering the planet. PNAS 103, 15729 (2006).",
      "Blankenship RE et al. Comparing photosynthetic and photovoltaic efficiencies. Science 332, 805 (2011).",
      "Franck J. Trans. Faraday Soc. 21, 536 (1926); Condon EU. Phys. Rev. 28, 1182 (1926).",
      "Kasha M. Characterization of electronic transitions in complex molecules. Discuss. Faraday Soc. 9, 14 (1950).",
      "Gouterman M. Spectra of porphyrins. J. Mol. Spectrosc. 6, 138 (1961).",
      "Weber G, Teale FWJ. Absolute quantum yield of fluorescent solutions. Trans. Faraday Soc. 53, 646 (1957).",
      "Kasha M, Rawls HR, El‑Bayoumi MA. The exciton model in molecular spectroscopy. Pure Appl. Chem. 11, 371 (1965).",
      "Förster T. Zwischenmolekulare Energiewanderung und Fluoreszenz. Ann. Phys. 437, 55 (1948).",
      "Blankenship RE. Molecular Mechanisms of Photosynthesis, 2nd ed. Wiley‑Blackwell (2014).",
      "Jordan P et al. Three‑dimensional structure of cyanobacterial photosystem I at 2.5 Å. Nature 411, 909 (2001).",
      "Malavath T et al. Structure and function of wild‑type and subunit‑depleted photosystem I in Synechocystis. BBA Bioenerg. 1859, 645 (2018); PDB 5OY0.",
      "Pettersen EF et al. UCSF ChimeraX. Protein Sci. 30, 70 (2021).",
      "CHM 598 Introduction to Photochemistry, lectures 13–16 (Fall 2026)."]
R2 = ["Gobets B, van Grondelle R. Energy transfer and trapping in photosystem I. Biochim. Biophys. Acta 1507, 80 (2001).",
      "Karapetyan NV, Holzwarth AR, Rögner M. The photosystem I trimer of cyanobacteria: molecular organization, excitation dynamics and physiological significance. FEBS Lett. 460, 395 (1999).",
      "Shubin VV, Bezsmertnaya IN, Karapetyan NV. Efficient energy transfer from the long‑wavelength antenna chlorophylls to P700 in photosystem I complexes from Spirulina platensis. J. Photochem. Photobiol. B 30, 153 (1995).",
      "Karapetyan NV et al. Long‑wavelength chlorophylls in photosystem I of cyanobacteria: origin, localization, and functions. Biochemistry (Moscow) 79, 213 (2014).",
      "Deisenhofer J, Epp O, Miki K, Huber R, Michel H. Photosynthetic reaction centre of Rhodopseudomonas viridis at 3 Å. Nature 318, 618 (1985).",
      "Guergova‑Kuras M et al. Evidence for two active branches for electron transfer in photosystem I. PNAS 98, 4437 (2001).",
      "Brettel K. Electron transfer and arrangement of the redox cofactors in photosystem I. Biochim. Biophys. Acta 1318, 322 (1997).",
      "Marcus RA. J. Chem. Phys. 24, 966 (1956); Marcus RA, Sutin N. Biochim. Biophys. Acta 811, 265 (1985).",
      "Page CC, Moser CC, Chen X, Dutton PL. Natural engineering principles of electron tunnelling. Nature 402, 47 (1999).",
      "Reiter S, Kiss FL, Hauer J, de Vivie‑Riedle R. Thermal site energy fluctuations in photosystem I. Chem. Sci. 14, 3117 (2023).",
      "Mayhew SG. The redox potential of dithionite and SO₂⁻ from equilibrium reactions with flavodoxins, methyl viologen and hydrogen plus hydrogenase. Eur. J. Biochem. 85, 535 (1978).",
      "Gray HB. Powering the planet with solar fuel. Nat. Chem. 1, 7 (2009).",
      "Takata T et al. Photocatalytic water splitting with a quantum efficiency of almost unity. Nature 581, 411 (2020).",
      "Nishiyama H et al. Photocatalytic solar hydrogen production from water on a 100‑m² scale. Nature 598, 304 (2021).",
      "Zhou P et al. Solar‑to‑hydrogen efficiency of more than 9% in photocatalytic water splitting. Nature 613, 66 (2023)."]
S["refsA"] = refs("refsA", 1, "Light, excited states and photosynthesis", R1)
S["refsB"] = refs("refsB", 2, "Photosystem I, red chlorophylls, redox and solar fuels", R2)

for sid, html in S.items():
    (ROOT / "slides" / f"{sid}.html").write_text(html)
print("wrote", ", ".join(S))
