# Single source of truth for the MVT flashcards. Every fact is transcribed from
# ESVS 2025 Chapter 7 (Eur J Vasc Endovasc Surg 2025;70:153-218) as already
# verified for the knowledge base. Fields: d=deck, q=question, a=answer (short,
# big), x=extra detail (optional), s=source. Rec cards add cls/lvl/st.
import json, os

DECKS = [
  # id, name, tagline, gradient start, gradient end, ink on the gradient
  ("def",  "Definitions",        "Words that mean different things",  "#3730a3", "#4f46e5", "#ffffff"),
  ("epi",  "Epidemiology",       "The numbers worth memorising",       "#115e59", "#0f766e", "#ffffff"),
  ("aet",  "Risk factors",       "Why it happened",                    "#fb923c", "#f97316", "#1c1917"),
  ("haem", "Haematology workup", "JAK2, thrombophilia, APS",           "#5b21b6", "#7c3aed", "#ffffff"),
  ("pres", "Presentation",       "Pain first, peritonism late",        "#9d174d", "#be185d", "#ffffff"),
  ("dx",   "Diagnosis & imaging","One test decides it",                "#075985", "#0369a1", "#ffffff"),
  ("acute","Acute management",   "Heparin first, then watch",          "#4ade80", "#22c55e", "#052e16"),
  ("esc",  "Endovascular & surgery","When heparin is not enough",      "#991b1b", "#dc2626", "#ffffff"),
  ("dur",  "Anticoagulation duration","Months, extended, or for life", "#fbbf24", "#f59e0b", "#1c1917"),
  ("ev",   "Evidence numbers",   "Rates, ratios and trials",           "#1e3a8a", "#1d4ed8", "#ffffff"),
  ("rec",  "Recommendations",    "Class, level and exact wording",     "#065f46", "#047857", "#ffffff"),
  ("trap", "Traps",              "Where clinicians go wrong",          "#0f172a", "#334155", "#ffffff"),
]

C = []
def card(d, q, a, x="", s="ESVS 2025 §7", **kw):
    C.append(dict(d=d, q=q, a=a, x=x, s=s, **kw))

# ── DEFINITIONS ────────────────────────────────────────────────
card("def","What is the working definition of mesenteric venous thrombosis (MVT)?",
 "Thrombosis within the <b>superior mesenteric vein</b>, with or without extension into the <b>portal or splenic vein</b>.",
 "Acute MVT may occur with obstruction of the SMV, IMV, splenic vein or portal vein.","ESVS 2025 §7.1")
card("def","Which venous segments are most often involved together?",
 "<b>Portal vein + SMV</b> most often, followed by the <b>splenic vein</b> and <b>inferior mesenteric vein</b>.",
 "Concomitant involvement of more than one venous segment is frequent.","ESVS 2025 §7.1")
card("def","What defines <u>acute</u> MVT (AMVT)?",
 "Symptom onset <b>within four weeks</b> of presentation.",
 "The four-week cut-off is explicitly arbitrary.","ESVS 2025 §7.3.3")
card("def","What defines <u>chronic</u> MVT (CMVT)?",
 "Symptoms for <b>more than four weeks without bowel infarction</b> — or MVT found <b>incidentally</b> on imaging.","","ESVS 2025 §7.3.3")
card("def","What is venous mesenteric ischaemia (VMI)?",
 "The <b>acute onset of symptoms in the presence of AMVT</b>.",
 "This clinical entity, not the radiological clot, is the main focus of the guideline.","ESVS 2025 §7.1")
card("def","Are acute and chronic MVT different diseases?",
 "No — <b>successive stages of the same disease</b> with the same causes, but they need <b>different management</b>.","","ESVS 2025 §7.3.3")
card("def","Name the four conditions ESVS Chapter 7 explicitly <u>excludes</u>.",
 "<b>Budd–Chiari</b> (± cirrhosis) · <b>isolated portal vein obstruction</b> · <b>sinusoidal obstruction</b> (hepatic veno-occlusive disease) · <b>hepatic disorders from heart failure or chemotherapy</b>.","","ESVS 2025 §7.1")
card("def","ESVS class wording: I, IIa, IIb, IIIa, IIIb?",
 "I = <b>is recommended</b> · IIa = <b>should be considered</b> · IIb = <b>may be considered</b> · IIIa = <b>is not indicated</b> · IIIb = <b>is not recommended</b>.","","ESVS 2025 Table 2")
card("def","What does ESVS <b>Level C</b> evidence mean?",
 "<b>Consensus</b> of experts, <b>low-quality studies</b> (small retrospective series, case series), or a meta-analysis of such studies.","","ESVS 2025 Table 3")
card("def","How many of the 11 MVT recommendations reach Level B?",
 "<b>Two</b> — Rec 46 (investigate the cause) and Rec 52 (three to six months of anticoagulation).",
 "The other nine are Level C. None is Level A.","ESVS 2025 §7")

# ── EPIDEMIOLOGY ───────────────────────────────────────────────
card("epi","What share of all acute mesenteric ischaemia is due to AMVT?",
 "<b>11.5%</b> (95% CI 9–14%).","It is the least common cause of acute mesenteric ischaemia.","ESVS 2025 §7.2 · Tamme 2022")
card("epi","How often does AMVT appear among emergency department admissions?",
 "About <b>1 in 1000</b> emergency department admissions.","","ESVS 2025 §7.2 · Tamme 2022")
card("epi","Incidence of VMI in the Swedish population study?",
 "<b>2.7 per 100 000</b> person-years.","402 patients, with an autopsy rate of 87%.","ESVS 2025 §7.2 · Acosta 2010")
card("epi","Incidence of VMI in Finland?",
 "<b>0.5 per 100 000</b> person-years.","Compare Sweden's autopsy-based figure of 2.7 per 100 000.","ESVS 2025 §7.2 · Kärkkäinen 2015")
card("epi","Mean age and sex distribution at presentation?",
 "Mean age <b>45–62 years</b>; only <b>34.3% female</b> (95% CI 30.5–38.5%).","A male-predominant disease.","ESVS 2025 §7.2 · Acosta & Salim 2021")
card("epi","What is the current in-hospital mortality of AMVT?",
 "Around <b>10%</b>.","It has fallen over recent decades.","ESVS 2025 §7.5")
card("epi","Mortality: AMVT vs acute arterial AMI vs NOMI?",
 "<b>~10%</b> vs <b>~50%</b> vs <b>~70%</b>.","MVT is by far the most survivable of the three.","ESVS 2025 §5, §6, §7.5")
card("epi","In the AMESI study, what proportion of adult admissions were acute VMI?",
 "<b>0.004%</b> (95% CI 0.002–0.007%).","A worldwide multicentre prospective observational study.","ESVS 2025 §7.2 · AMESI 2024")

# ── RISK FACTORS ───────────────────────────────────────────────
card("aet","On thorough investigation, how many MVT patients have a <u>systemic</u> prothrombotic factor?",
 "About <b>60–70%</b>.","","ESVS 2025 §7.3.1")
card("aet","How many MVT patients have a <u>local</u> triggering factor?",
 "<b>30–40%</b>.","","ESVS 2025 §7.3.1")
card("aet","How many MVT cases remain unprovoked (idiopathic)?",
 "<b>20–30%</b>.","","ESVS 2025 §7.3.1")
card("aet","Name the three <u>permanent</u> risk factors ESVS lists for MVT.",
 "<b>Solid cancer</b> · <b>liver cirrhosis</b> · <b>myeloproliferative disease</b>.","","ESVS 2025 §7.3.1")
card("aet","Name the four <u>transient</u> risk factors ESVS lists for MVT.",
 "<b>Abdominal inflammation or infection</b> · <b>recent surgery</b> · <b>hormonal therapy</b> · <b>trauma</b>.","","ESVS 2025 §7.3.1")
card("aet","Pooled prevalences (1725 patients): cirrhosis/portal hypertension, liver disease, pancreatitis, IBD?",
 "Cirrhosis/PHT <b>28.8%</b> · liver disease <b>27.8%</b> · pancreatitis <b>11.1%</b> · IBD <b>10.0%</b>.","","ESVS 2025 §7.3.1 · Wu 2023")
card("aet","Which inherited thrombophilias are over-represented in MVT (systematic review of 14 studies)?",
 "<b>Prothrombin G20210A</b>, <b>antithrombin deficiency</b> and <b>protein S deficiency</b>.",
 "Higher than in both the general population and patients with a single VTE elsewhere.","ESVS 2025 §7.3.1 · Zarrouk 2017")
card("aet","Which two infections are linked to AMVT?",
 "<b>Cytomegalovirus</b> and <b>severe SARS-CoV-2</b>.","CMV may act synergistically with a prothrombin G20210A mutation.","ESVS 2025 §7.3.2")

# ── HAEMATOLOGY ────────────────────────────────────────────────
card("haem","What is the <i>JAK2</i> mutation prevalence in AMVT?",
 "<b>32.7%</b> (95% CI 25.5–35.9%) — against about <b>1%</b> in VTE at other sites.","","ESVS 2025 §7.3.1 · Dentali 2009")
card("haem","What is the odds ratio for the association between <i>JAK2</i> and MVT?",
 "<b>OR 53.9</b> (95% CI 13.1–222.5).","A very large association, measured imprecisely.","ESVS 2025 §7.3.1 · Dentali 2009")
card("haem","Of MVT patients carrying <i>JAK2</i>, how many were later diagnosed with an MPN?",
 "<b>52%</b> (95% CI 38–67%) — with MVT as the <b>first manifestation</b>.","","ESVS 2025 §7.3.1 · Dentali 2009")
card("haem","When does ESVS say to screen for <i>JAK2</i> V617F?",
 "In MVT <b>without evidence of other major systemic or local risk factors</b>.","","ESVS 2025 §7.3.1")
card("haem","Which myeloproliferative neoplasms commonly present first with AMVT?",
 "<b>Polycythaemia vera</b> and <b>essential thrombocythaemia</b>.","","ESVS 2025 §7.3.1")
card("haem","Who should be tested for thrombophilia after AMVT?",
 "<b>Selected</b> patients who will <b>stop anticoagulation after three to six months</b>.","Rec 48 · Class IIb, Level C.","ESVS 2025 Rec 48")
card("haem","MVT plus another indication for lifelong anticoagulation (e.g. AF). Test for thrombophilia?",
 "<b>No</b> — there is no indication, because the result cannot change management.","","ESVS 2025 §7.3.2")
card("haem","Who should be investigated for antiphospholipid syndrome?",
 "Patients with <b>recurrent MVT and recurrent foetal loss</b>.","Rec 47 · Class IIa, Level C.","ESVS 2025 Rec 47")
card("haem","Which assays does ESVS list for APS and thrombophilia testing?",
 "<b>Lupus anticoagulant</b>, <b>anticardiolipin</b>, <b>β2-glycoprotein</b> antibodies; <b>antithrombin</b>, <b>protein C</b>, <b>protein S</b>.","","ESVS 2025 §7.3.2")
card("haem","What does ASH 2023 advise on thrombophilia testing in MVT?",
 "<b>Conditional testing</b> for patients who would stop anticoagulation after three to six months.","Very low certainty of evidence about effects.","ESVS 2025 §7.3.2 · Middeldorp 2023")
card("haem","Is there a reliable biomarker for MVT?",
 "<b>No.</b> A single lactate or D-dimer to confirm or exclude acute mesenteric ischaemia is <b>Class IIIb — not recommended</b>.","","ESVS 2025 §7.3.2 · Recs 31, 42")
card("haem","How did the D-dimer advice change from 2017 to 2025?",
 "2017 recommended D-dimer to <b>rule out</b> AMI. 2025 is <b>Class IIIb against</b> any single biomarker to confirm or exclude it.","","ESVS 2025 · What is new")

# ── PRESENTATION ───────────────────────────────────────────────
card("pres","What is the mean duration of symptoms at presentation in AMVT?",
 "<b>6–14 days</b>.","","ESVS 2025 §7.3.3")
card("pres","In more than 75% of cases, how long do symptoms persist before diagnosis?",
 "<b>Two to three days</b>.","","ESVS 2025 §7.3.3")
card("pres","What share of patients with SMV involvement are symptomatic?",
 "<b>92%</b> — in contrast to isolated portal vein thrombosis.","","ESVS 2025 §7.3.3")
card("pres","Untreated SMV thrombosis: risk of haemorrhagic bowel infarction?",
 "<b>33–45%</b>.","","ESVS 2025 §7.3.3")
card("pres","What are the most common symptoms of MVT?",
 "<b>Abdominal pain</b>, <b>anorexia</b> and <b>diarrhoea</b>.",
 "Pain is non-specific early; localised tenderness develops later.","ESVS 2025 §7.3.3")
card("pres","What do fever and peritoneal signs indicate in MVT?",
 "<b>Progression of ischaemia to bowel infarction.</b>","They are the complication, not the presentation.","ESVS 2025 §7.3.3")
card("pres","What share of MVT presents acutely?",
 "<b>20–74%</b>, depending on the vein segment involved.","Acute presentation is more common when the mesenteric veins are involved.","ESVS 2025 §7.3.3")
card("pres","What is pylephlebitis?",
 "<b>Infectious thrombophlebitis of the portal vein</b> and its branches — high fever, malaise, abdominal tenderness, sepsis.",
 "May come with liver abscesses; follows appendicitis, pancreatitis or diverticulitis.","ESVS 2025 §7.3.3")
card("pres","What is a portal cavernoma?",
 "Chronic MVT in which the <b>obstructed portal vein is replaced by a network of collateral veins</b>.",
 "Complete portal vein occlusion is virtually always associated with portal hypertension.","ESVS 2025 §7.3.3")
card("pres","What are the classical (but rare) presentations of a cavernoma?",
 "<b>Ruptured oesophageal or gastric varices</b>, or <b>portal cholangiopathy</b> — jaundice, cholangitis, cholecystitis, pancreatitis.","","ESVS 2025 §7.3.3")

# ── DIAGNOSIS ──────────────────────────────────────────────────
card("dx","What is the imaging investigation of choice for suspected MVT?",
 "<b>Contrast-enhanced CT</b> with <b>arterial and portal venous phases</b> (optional non-contrast run).","","ESVS 2025 §7.4 · Rec 49")
card("dx","What slice thickness does the CTA protocol specify?",
 "Three-phase CTA with <b>1 mm maximum</b> slice thickness.","","ESVS 2025 §7.4")
card("dx","Which CT phase shows the extent of the venous thrombosis?",
 "The <b>portal venous phase</b>.","It also shows the secondary bowel findings.","ESVS 2025 §7.4")
card("dx","Name the five non-vascular CT findings to look for.",
 "<b>Bowel wall thickening</b> · <b>bowel dilatation</b> · <b>mesenteric fat stranding</b> · <b>pneumatosis intestinalis</b> · <b>portal venous gas</b>.","","ESVS 2025 §7.4")
card("dx","Is duplex ultrasound enough to diagnose MVT?",
 "<b>No</b> — it cannot show the extent of thrombosis or the bowel changes, and <b>must be complemented by CT</b>.","","ESVS 2025 §7.4")
card("dx","Why write \"?mesenteric ischaemia\" on the CT request?",
 "Stating the suspicion is associated with <b>better diagnosis and outcomes</b>.","New Class I Rec 32.","ESVS 2025 Rec 32")
card("dx","Should CTA wait for renal function results?",
 "<b>No</b> — urgent CTA is recommended <b>regardless of renal function</b>.","Rec 33 · Class I.","ESVS 2025 Rec 33")
card("dx","What is the hardest diagnostic judgement in AMVT?",
 "Telling <b>reversible from irreversible</b> intestinal ischaemia — notably difficult, <b>especially in AMVT</b>.","","ESVS 2025 §7.4")

# ── ACUTE MANAGEMENT ───────────────────────────────────────────
card("acute","What is the first-line treatment for every AMVT patient without a major contraindication?",
 "<b>Unfractionated or low molecular weight heparin.</b>","Start soon after diagnosis.","ESVS 2025 §7.5.1 · Rec 50")
card("acute","Why is unfractionated heparin favoured in the acute phase?",
 "It can be <b>reversed with protamine</b> if laparotomy becomes necessary or bleeding occurs.","","ESVS 2025 §7.5.1")
card("acute","How often does early anticoagulation achieve recanalisation?",
 "In <b>40–80%</b> of patients.","Complete recanalisation is associated with less extensive thrombosis.","ESVS 2025 §7.5.1")
card("acute","What are the goals of treating AMVT?",
 "<b>Stop propagation</b> and <b>promote recanalisation</b> — to prevent bowel infarction, portal hypertension and recurrence.","","ESVS 2025 §7.5")
card("acute","What extra goals apply in chronic MVT?",
 "Preventing and treating <b>GI bleeding</b> and <b>portal cholangiopathy</b>.","","ESVS 2025 §7.5")
card("acute","What supportive care starts immediately?",
 "<b>Pain control</b>, <b>fluids and electrolytes</b>, <b>bowel rest</b>.",
 "Add NG aspiration for ileus or vomiting, transfusion for bleeding, parenteral nutrition.","ESVS 2025 §7.5.2")
card("acute","Are antibiotics routine in MVT?",
 "<b>No</b> — no mortality or length-of-stay benefit shown.",
 "Give them for perforation, sepsis from bacterial translocation, pylephlebitis or septic thrombophlebitis.","ESVS 2025 §7.5.2")
card("acute","What is the single decision point at presentation in the ESVS algorithm?",
 "<b>Peritonitis?</b> Yes → laparotomy. No → anticoagulation plus supportive care.","","ESVS 2025 Fig. 6")
card("acute","Anatomically, when does bowel infarction become likely?",
 "When the <b>venous arcades and vasa recta</b> are involved, causing <b>complete venous occlusion</b>.","","ESVS 2025 §7.5")
card("acute","Most patients with AMVT are cured by…?",
 "<b>Therapeutic anticoagulation and supportive treatment</b> alone.","Endovascular therapy and surgery are escalation steps.","ESVS 2025 §7.5")

# ── ESCALATION ─────────────────────────────────────────────────
card("esc","When should endovascular thrombolysis or thrombectomy be considered?",
 "When the patient <b>deteriorates during anticoagulant therapy</b>.","Not simply because the clot is large.","ESVS 2025 §7.5.3 · Rec 51")
card("esc","Name the endovascular options for AMVT.",
 "<b>TIPS + aspiration thrombectomy</b> · <b>direct thrombolysis ± angioplasty</b> · <b>percutaneous transhepatic thrombectomy or thrombolysis</b> · <b>thrombolysis via the SMA</b>.","","ESVS 2025 §7.5.3")
card("esc","Direct venous vs SMA route for thrombolysis — which is preferred?",
 "The <b>direct venous</b> route — used in more centres and <b>may be more effective</b>.","","ESVS 2025 §7.5.3")
card("esc","Transjugular or transhepatic access: mean time to thrombus resolution?",
 "A mean of <b>40 hours</b>.","","ESVS 2025 §7.5.3")
card("esc","Thrombolysis systematic review (480 patients): complete recanalisation, bleeding, bowel resection?",
 "<b>58%</b> (46–70%) · bleeding <b>18%</b> (7–32%) · resection <b>3%</b> (0–8%).","","ESVS 2025 §7.5.3 · Gao 2023")
card("esc","Clinical effectiveness: anticoagulation vs endovascular treatment?",
 "<b>89%</b> vs <b>93%</b> — but <b>low-quality evidence with obvious selection bias</b>.","","ESVS 2025 §7.5.3 · Wang 2022")
card("esc","What are the indications for open surgery?",
 "<b>Persisting or worsening symptoms</b>, <b>organ failure</b>, <b>perforation</b> or <b>peritonitis</b>.","","ESVS 2025 §7.5.4")
card("esc","What is the aim of surgery in AMVT?",
 "<b>Remove irreversibly ischaemic bowel</b> and <b>preserve as much bowel as possible</b>.","","ESVS 2025 §7.5.4")
card("esc","Bowel resection rate in AMVT (systematic review of 599 patients)?",
 "<b>43.9%</b>.","Rates vary widely between studies.","ESVS 2025 §7.5.4 · Acosta & Salim 2021")
card("esc","What are the two hard problems of surgery in AMVT?",
 "<b>When to operate</b>, and <b>when a bowel segment is irreversibly injured</b>.","","ESVS 2025 §7.5.4")
card("esc","What unresolved research question does ESVS name for MVT?",
 "The value of <b>endovascular treatment when anticoagulation fails</b> in extensive mesenteric or portal thrombosis.","","ESVS 2025 §11.4")

# ── DURATION ───────────────────────────────────────────────────
card("dur","When can a vitamin K antagonist usually be started after AMVT?",
 "<b>Two to three weeks</b> after onset, once the acute ischaemic phase has passed.","","ESVS 2025 §7.6")
card("dur","What is the estimated one-year recurrence after AMVT?",
 "<b>2.7%</b>.","","ESVS 2025 §7.6")
card("dur","What is the minimum duration of anticoagulation for all AMVT?",
 "<b>Three to six months</b> of a VKA or LMWH.","A DOAC may be considered as an alternative.","ESVS 2025 Recs 52, 53")
card("dur","AMVT with a <u>transient</u> risk factor. Stop at six months?",
 "<b>Consider extending beyond six months.</b>","VKA: should be considered (IIa). DOAC: may be considered (IIb).","ESVS 2025 Recs 54, 55")
card("dur","AMVT with a <u>permanent</u> risk factor — duration?",
 "<b>Indefinite</b> anticoagulation.","Class I, based on consensus.","ESVS 2025 Rec 56")
card("dur","<u>Idiopathic</u> AMVT — duration?",
 "<b>Indefinite</b> anticoagulation.","Class I, based on consensus. Check that <i>JAK2</i> was tested first.","ESVS 2025 Rec 56")
card("dur","Why is extending anticoagulation for <u>transient</u> factors counterintuitive?",
 "In most VTE, a resolved transient factor means <b>stop at three months</b>. In MVT, recurrence can mean <b>extensive bowel loss and short bowel syndrome</b>.","","ESVS 2025 §7.6")
card("dur","What three things must be balanced when deciding on extended anticoagulation?",
 "<b>Bleeding risk</b> (varices, low platelets, prior bleeds) · <b>recurrence risk</b> (persisting factors, prior VTE) · <b>consequences of recurrence</b> (bowel involvement, short bowel).","A shared decision with the patient.","ESVS 2025 §7.6")
card("dur","Which DOACs have small retrospective data after AMVT?",
 "<b>Rivaroxaban</b> and <b>apixaban</b> — possibly as effective as VKA or enoxaparin.","Their use is off-label.","ESVS 2025 §7.6")

# ── EVIDENCE ───────────────────────────────────────────────────
card("ev","IPD meta-analysis (1635 patients): recurrent VTE on vs off anticoagulation?",
 "<b>3.4</b> vs <b>6.6</b> per 100 patient-years.","Mean anticoagulation 316 days.","ESVS 2025 §7.6 · Candeloro 2022")
card("ev","Same IPD meta-analysis: major bleeding on vs off anticoagulation?",
 "<b>3.1</b> vs <b>5.8</b> per 100 patient-years.","Higher after stopping, which points to confounding: sicker patients stop and bleed.","ESVS 2025 §7.6 · Candeloro 2022")
card("ev","In the IPD meta-analysis, what share of recurrences were in the mesenteric veins?",
 "<b>38.5%</b>.","","ESVS 2025 §7.6 · Candeloro 2022")
card("ev","International registry (604 patients): thrombotic events on vs off anticoagulation?",
 "<b>5.6</b> vs <b>10.5</b> per 100 patient-years.","","ESVS 2025 §7.6 · Ageno 2015")
card("ev","Same registry: major bleeding on vs off anticoagulation?",
 "<b>3.9</b> vs <b>1.0</b> per 100 patient-years.","The opposite direction to the IPD meta-analysis.","ESVS 2025 §7.6 · Ageno 2015")
card("ev","Which subgroup had the highest rates of both thrombosis and bleeding?",
 "<b>Cirrhosis</b> — 11.3 thrombotic and 10.0 major bleeding events per 100 patient-years.","","ESVS 2025 §7.6 · Ageno 2015")
card("ev","Which subgroup had the lowest rates of thrombosis and bleeding?",
 "MVT secondary to <b>transient risk factors</b>.","","ESVS 2025 §7.6 · Ageno 2015")
card("ev","Anticoagulation vs stopping (meta-analysis): effect on recanalisation, bleeding, mortality, recurrence?",
 "Recanalisation <b>RR 2.39</b> · bleeding <b>RR 0.73</b> · mortality <b>RR 0.45</b> · recurrence <b>RR 0.91</b> (no difference).","","ESVS 2025 §7.6 · Valeriani 2021")
card("ev","VKA vs DOAC in 102 MVT patients: recanalisation and major bleeding?",
 "Recanalisation <b>71% vs 69%</b>; major bleeding <b>14.3% vs 9.1%</b>.","No significant difference except more GI bleeding with DOACs.","ESVS 2025 §7.6 · Salim 2019")
card("ev","Rivaroxaban cohort (96 patients): recurrent VTE at three and six months?",
 "<b>2.1%</b> at three months (two patients) · <b>3.1%</b> cumulative at six months.","","ESVS 2025 §7.6 · Ageno 2022")
card("ev","Ten-year recurrence-free survival: isolated splenic vein vs isolated mesenteric vein thrombosis?",
 "<b>97%</b> vs <b>60%</b>.","The segment affected changes the prognosis.","ESVS 2025 §7.6 · Thatipelli 2010")

# ── RECOMMENDATIONS (verbatim) ─────────────────────────────────
def rec(n, q, text, cls, lvl, st, refs):
    card("rec", q, text, refs, f"ESVS 2025 Rec {n}", n=n, cls=cls, lvl=lvl, st=st)
rec(46,"Investigating the cause of MVT — what does ESVS recommend, and how strongly?",
 "Investigation for the presence of an intra-abdominal malignancy, inflammatory disease, myeloproliferative neoplasm, cytomegalovirus and SARS-CoV-2 infection, and chronic liver disease is recommended for patients with mesenteric venous thrombosis.",
 "I","B","Unchanged","Thatipelli 2010 · Primignani 2010 · De Broucker 2022 · El-Hady 2023 · Elkrief 2023")
rec(47,"Recurrent MVT with recurrent foetal loss — what does ESVS recommend, and how strongly?",
 "Patients with recurrent mesenteric venous thrombosis and recurrent foetal loss should be investigated for antiphospholipid antibody syndrome.",
 "IIa","C","Unchanged","Thatipelli 2010 · Primignani 2010 · Elkrief 2023")
rec(48,"Thrombophilia testing after AMVT — what does ESVS recommend, and how strongly?",
 "Testing for thrombophilia may be considered in selected patients with acute venous mesenteric thrombosis who will discontinue anticoagulation treatment after three to six months.",
 "IIb","C","Unchanged","Middeldorp 2023")
rec(49,"Imaging for suspected MVT — what does ESVS recommend, and how strongly?",
 "Contrast enhanced computed tomography scanning with imaging in the arterial and portal phases (and optional non-contrast CT run) is recommended for patients suspected of mesenteric vein thrombosis.",
 "I","C","Changed","Salim 2018 · Henes 2017 — rephrased, LoE downgraded B → C")
rec(50,"First-line treatment of AMVT — what does ESVS recommend, and how strongly?",
 "Anticoagulation with unfractionated or low molecular weight heparin as first line therapy is recommended for all patients with acute mesenteric vein thrombosis.",
 "I","C","Unchanged","Wang 2022")
rec(51,"Deterioration on anticoagulation — what does ESVS recommend, and how strongly?",
 "Endovascular venous thrombolysis and mechanical thrombectomy may be considered for patients with acute venous mesenteric ischaemia who deteriorate during anticoagulant therapy.",
 "IIb","C","New","Acosta 2021 · Wang 2022 · Gao 2023")
rec(52,"Three to six months of VKA or LMWH — what does ESVS recommend, and how strongly?",
 "Anticoagulation for three to six months with a vitamin K antagonist or low molecular weight heparin is recommended for all patients with acute mesenteric vein thrombosis.",
 "I","B","Unchanged","Candeloro 2022 · Valeriani 2021 · Ageno 2015")
rec(53,"A DOAC for the first three to six months — what does ESVS recommend, and how strongly?",
 "Anticoagulation for three to six months with a direct oral anticoagulant as an alternative to a vitamin K antagonist or low molecular weight heparin may be considered for all patients with acute mesenteric vein thrombosis.",
 "IIb","C","New","Salim 2019 · Janczak 2018 · Ageno 2022 · Valeriani 2021")
rec(54,"Extending a VKA beyond six months for transient risk factors — what does ESVS recommend, and how strongly?",
 "Extended anticoagulation beyond six months with a vitamin K antagonist should be considered for patients with acute mesenteric vein thrombosis and transient risk factors for venous thrombosis.",
 "IIa","C","New","Candeloro 2022 · Valeriani 2021 · Ageno 2015")
rec(55,"Extending with a DOAC beyond six months for transient risk factors — what does ESVS recommend, and how strongly?",
 "Extended anticoagulation beyond six months with a direct oral anticoagulant as an alternative to a vitamin K antagonist may be considered for all patients with acute mesenteric vein thrombosis and transient risk factors for venous thrombosis.",
 "IIb","C","New","Valeriani 2021")
rec(56,"Idiopathic AMVT, or permanent risk factors — what does ESVS recommend, and how strongly?",
 "Indefinite anticoagulation is recommended for patients with idiopathic acute mesenteric vein thrombosis and patients with permanent risk factors for venous thrombosis.",
 "I","C","Unchanged","Consensus")
rec(39,"Assessing bowel viability at operation — what does ESVS recommend, and how strongly? (Ch. 5, applies to AMVT)",
 "Quantitative indocyanine green fluorescent imaging may be considered as an aid in the assessment of bowel viability in patients undergoing laparotomy or laparoscopy for acute mesenteric ischaemia.",
 "IIb","—","New","Used in only 7% of practices")
rec(40,"Bowel resection strategy — what does ESVS recommend, and how strongly? (Ch. 5, applies to AMVT)",
 "Resection without primary reconstruction and second look laparotomy for definitive treatment should be considered in patients undergoing acute mesenteric revascularisation who need bowel resection.",
 "IIa","—","Changed","Rephrased · consensus")
rec(41,"Antibiotics in acute mesenteric ischaemia — what does ESVS recommend, and how strongly? (Ch. 5)",
 "Treatment with antibiotics is recommended for patients with acute mesenteric ischaemia.",
 "I","C","Changed","LoE downgraded B → C. In MVT itself, antibiotics are indicated only for perforation, translocation sepsis, pylephlebitis or septic thrombophlebitis.")

# ── TRAPS ──────────────────────────────────────────────────────
card("trap","A normal full blood count rules out a myeloproliferative neoplasm. True?",
 "<b>False.</b> Test <i>JAK2</i> V617F.","52% of JAK2-positive MVT patients declared an MPN only during follow-up.","ESVS 2025 §7.3.1")
card("trap","A normal lactate makes MVT unlikely. True?",
 "<b>False.</b> No biomarker is reliable; a single lactate or D-dimer is <b>Class IIIb</b>.","The CT decides.","ESVS 2025 §7.3.2")
card("trap","The CT shows a large clot. Thrombolyse?",
 "<b>Not on clot burden alone.</b> The trigger is <b>deterioration during anticoagulation</b>.","Pooled bleeding with thrombolysis: 18%.","ESVS 2025 Rec 51")
card("trap","Appendicitis explains this patient's MVT. Workup complete?",
 "<b>No.</b> Systemic factors are found in 60–70%; investigate <b>every</b> patient.","Rec 46 applies to all patients with MVT.","ESVS 2025 Rec 46")
card("trap","Transient cause, now resolved. Stop anticoagulation at three months?",
 "<b>Not by default.</b> ESVS suggests considering <b>extension beyond six months</b>.","Recs 54 and 55.","ESVS 2025 Recs 54, 55")
card("trap","Order a full thrombophilia screen for every MVT patient?",
 "<b>No.</b> Only in selected patients who will <b>stop anticoagulation</b> at three to six months.","Rec 48.","ESVS 2025 Rec 48")
card("trap","A trial of splanchnic vein thrombosis tells you about MVT. True?",
 "<b>Only partly.</b> Isolated splenic vein thrombosis has 97% ten-year recurrence-free survival; isolated MVT only 60%.","Always ask which veins were studied.","ESVS 2025 §7.6")
card("trap","Duplex ultrasound shows SMV thrombus. Enough to plan treatment?",
 "<b>No.</b> Duplex cannot show the full extent or the bowel changes — <b>get the CT</b>.","","ESVS 2025 §7.4")

for i,c in enumerate(C): c["id"]=f"{c['d']}-{i:03d}"
out=dict(decks=[dict(id=a,name=b,tag=c,g1=d,g2=e,ink=f) for a,b,c,d,e,f in DECKS], cards=C)
json.dump(out, open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","cards.json"),"w",encoding="utf-8"), ensure_ascii=False, indent=1)
from collections import Counter
cnt=Counter(c["d"] for c in C)
print("total cards:",len(C))
for d in DECKS: print(f"  {d[1]:26s} {cnt[d[0]]}")
