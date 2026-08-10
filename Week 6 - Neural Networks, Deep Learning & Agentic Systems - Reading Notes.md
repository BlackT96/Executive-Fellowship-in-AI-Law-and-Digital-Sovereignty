# Week 6: Neural Networks, Deep Learning & Agentic Systems — Reading Notes for Legal Practitioners

**Module 1:** Digital Technology Fundamentals
**Program:** Executive Fellowship (AI Law & Digital Sovereignty)
**Target Audience:** Lawyers with no prior computing background

---

## How to Use These Notes

Each section follows the same structure:
1. **Plain-English Explanation** — what it is, in everyday language
2. **Practical Illustration** — a concrete example tied to Ugandan legal practice
3. **Why It Matters for a Lawyer** — the legal significance
4. **Legal Framework** — relevant Ugandan statutes, regulations, and case law

---

# PART 1: NEURAL NETWORKS — THE BUILDING BLOCKS

## 1.1 The Neuron and the Perceptron

**Plain English:** A neural network is a computer program loosely inspired by the way brain cells work. It is made of thousands (or billions) of tiny computation units called "neurons," arranged in layers and connected to one another. Each connection has a **weight** — a number that says how strongly one unit influences the next.

The simplest possible unit is the **perceptron**. A perceptron takes several inputs, multiplies each by a weight, adds them up, and then decides: "if this sum is large enough, I fire; otherwise I stay silent." That single decision is the origin of every modern AI system.

| Concept | Plain Meaning |
|---|---|
| **Weight** | How much each input counts in the final decision |
| **Bias** | A threshold the sum must pass before the unit "fires" |
| **Decision rule** | "Is the weighted sum above a set level? If yes → respond 1, if no → respond 0" |

**Practical Illustration — Credit Approval as a Perceptron:**
Imagine one unit deciding whether to approve a small loan. Inputs: (1) monthly income, (2) repayment history, (3) mobile money activity. Each input is multiplied by a weight. The unit adds them and, if the sum clears a bias, answers "GREEN — approve." Change the weights and the same inputs produce a different decision. The weights are the "brains" — and they can be tuned automatically.

**Why this matters for a lawyer:** A single unit's decision is traceable: input × weight + bias = output. But real AI does not use one unit. It stacks millions of units into layers, and that is where explainability collapses. The lawyer's question is always the same: *"Can anyone point to the single calculation that produced this decision?"* For a perceptron, yes. For a deep network, usually no.

## 1.2 Activation Functions: ReLU and Sigmoid

**Plain English:** After a neuron computes its weighted sum, it passes the result through an **activation function** — a simple formula that decides how strongly (or whether) the neuron "fires" its signal onward.

- **Sigmoid:** Squeezes any number into a value between 0 and 1. Often used for outputs that need to read as a probability, e.g., "63% chance of default."
- **ReLU** (Rectified Linear Unit): If the input is negative, the output is zero; if it is positive, it passes through unchanged. It is fast and is the workhorse of most modern networks.

**Practical Illustration — Firing thresholds in a diagnostic model:**
A deep-learning diagnostic tool at a rural health centre uses Sigmoid-type activation at its final layer to output "probability of malaria = 0.87." A doctor (or an automated attendant) acts on that single number. The intermediate layers — hundreds of ReLU gates — are where the reasons, if any, are buried.

**Why this matters for a lawyer:** Activation functions are part of the "hardware of thought" that a regulator, auditor, or plaintiff cannot easily inspect. Choosing one activation over another changes behaviour invisibly. When your client is accused of a biased or reckless AI decision, understanding that the final probability emerges from layered, non-linear gates helps you argue that a single "hidden layer configuration" caused the harm — and that the plaintiff cannot pinpoint it without the technical log.

## 1.3 Hidden Layers, Backpropagation, and Gradient Descent — How the Model Learns

**Plain English:**
- **Hidden layers** are the middle layers of neurons between the inputs (income, history) and the output (approve/reject). The word "deep" simply means *many* hidden layers. The more layers, the more complex patterns the model can capture — and the more opaque it becomes.
- **Gradient descent** is the learning rule. Think of the model's error as a ball rolling down a hill: the model keeps nudging its weights slightly in the direction that reduces the error, one small step at a time, looking for the bottom of the valley.
- **Backpropagation** is the mechanism that tells each weight "how much did you contribute to the mistake, and which way should you shift?" It works backward from the final error, layer by layer.

**Analogy — a law student marking their own essays:**
Imagine a student writes a mock answer, is told the score, then works backward: "The conclusion was wrong, so the argument that fed into it must have been weak; the authority I cited was weak, so the sub-argument that relied on it must change." Each step adjusts one part and re-tests until the answer improves, and the process repeats. That is backpropagation. The student, working over the whole course and every mock essay, keeps nudging their approach in the direction of better marks — that is gradient descent.

**Why this matters for a lawyer:** Two deep consequences:
1. **The weights are *discovered*, not written.** No human rule "says" why the model measured a particular way. This is the practical basis of the "black box."
2. **Training is a statistical, six-month dance**, not a logic proof. The final weights are the result of millions of tiny numeric tweaks. To prove a model was "defective from the outset" under Cap. 292, you need the *validation trail* — the logs of weights, losses, and test scores over time — not a single snapshot of the final weights.

---

# PART 2: DEEP LEARNING ARCHITECTURES

## 2.1 Convolutional Neural Networks (CNNs) — Teaching Computers to "See"

**Plain English:** A CNN is a special neural network designed for images. Instead of feeding a picture in one flat blob, the model slides small windows (kernels/filters) across the image and detects local patterns: edges, then corners, then shapes, and finally whole objects like a face or a car number plate. Each "layer" sees a more abstract version of the picture.

**Practical Illustration — Biometric police surveillance in Kampala:**
A CCTV and facial-recognition network in Kampala is a CNN. Its first layers detect edges and skin texture; later layers assemble faces; the final layer maps the result to an identity. The same weight-stacks technique drives automatic number-plate recognition for smart traffic infrastructure.

**Why this matters for a lawyer:**
- **The output depends on the training set.** A CNN trained mostly on imagery of one skin tone or lighting condition will be more accurate on that group. Misrecognition is therefore not random: it has a demographic pattern you can audit under Article 21 (see Week 5) and via the Human Rights (Enforcement) Act, Cap. 12.
- **A match is a probability, not a fact.** The network's "identified" output is a confidence score. Deploying it as if it were proof of identity is a due-process issue, not a hardware one. Ask for the false-approval rate ("false negatives" on faces) exactly as you would ask for the False-Positive figure in a credit score.

## 2.2 Recurrent Neural Networks (RNNs) — Handling Sequence and Behaviour Over Time

**Plain English:** A CNN sees a picture; an RNN reads a story. RNN models are built to process sequences where order matters: a sentence, a mobile-money transaction history, a sensor reading over time. It keeps a "memory" of what came before and uses it to interpret each new token.

**Practical Illustration — Transaction-sequencing fraud detection:**
A network detects fraud on MTN MoMo by evaluating the *order* of a customer's transactions. A single cash deposit might be innocent; a deposit followed within seconds by a transfer to a new recipient and then to a small bank account is a suspicious sequence. Only an RNN (or the newer transformer) sees the "order" that a per-transaction model misses.

**Why this matters for a lawyer:** RNNs are used where "context" is everything — text, speech, financial history, sensor flows. The legal sensitivity is that two people can have identical *totals* but different *sequences*, and the model treats the sequences as entirely different classes. That destroys the simple "masking by aggregate" assumption and forces you to look at the chronological data log when reconstructing why a decision was taken.

---

# PART 3: AGENTIC AI & EDGE AI

## 3.1 What is an "Agentic System"?

**Plain English:** Earlier chapters describe AI that responds to a prompt or a single request. An **agent** is different: it is an AI program given a *goal* and left to break that goal into steps, *use tools* (call an API, send a message, move money), and *loop* — try, check the result, adjust, and try again — until the goal is reached or it runs out of a limit.

The three capabilities the curriculum flags:
- **Planning** — working out the sequence of steps to reach the goal.
- **Tool use** — calling outside functions: payment APIs, order systems, data lookups.
- **Loop execution** — cycling through the steps, correcting along the way.

**Practical Illustration — The Jinja estate agent (this week's task):**
A professional agricultural estate deploys an agent to **water the crops**, **buy chemical inputs through an integrated digital wallet**, and **sign supply contracts with local distributors**. The agent has a hardware shutdown cap, but its planner is only as safe as its guardrails. If corrupted sensor data tells it the soil is catastrophically dry, it "reasons" it needs fertilizer — and its tool-use loop can autonomously place a **UGX 200,000,000** non-refundable order to a third-party vendor, without a human gate.

**Why this matters for a lawyer:** A single AI agent can now **form a binding intention and cause a binding corporate action** on its controller's behalf. The irreducible legal questions become: Who, if anyone, may an agent bind them? Who authorised this expenditure? Where does the gate fail? And when the estate has lost 200M shillings in a drought, no human "pressed the button" — so which rule, director, or vendor is liable? That is the core crisis of agency, now sitting at the heart of a computer system.

## 3.2 The "Black Box" Problem — Unexplainable Neural Paths

**Plain English:** The deeper the network, the less the model's internal decision can be reverse-engineered. A shallow model can be asked "which inputs contributed?" A 50-layer model cannot — the contribution is spread across millions of real-valued weights. The internal neural path is *unexplainable*.

**Legal significance:** This is not a cosmetic concern. Because the model's decision cannot be decomposed into discrete, traceable steps, meeting **legal causation** becomes difficult for both sides:
- The *plaintiff* must show the defect **caused** the harm.
- The *defendant vendor* must show the product met an implied standard.

Under the Sale of Goods and Supply of Services Act, Cap. 292, liability for an automated failure turns on proving that the system lacked "satisfactory quality" or "fitness for purpose" *at the time of supply*.

**What this means in practice — the lawyer does not fight the box, they fight the record.** Because the internal computation is opaque, the lawyer's evidence is the **technical decision log** (date, model version, inputs, outputs, weights used, validation metrics) and the **validation model trail** — the logged record of training, weights, losses, and test scores over time. These logs are the case's "X-ray" of the black box. But to use them, the lawyer must be able to *get them admitted*. That is a question of electronic-evidence law, addressed in Part 4 below.

## 3.3 Edge AI — Running Intelligence at the Point of Action

**Plain English:** Most AI runs in the cloud. **Edge AI** runs on the device itself — a camera, a VoIP base station, a farm gate, a sensor hub on a factory site. It keeps the model run near the data, not on a distant server. This matters for latency (the agent acts instantly), for offline capability, and for data movement (settings stay local).

**Why this matters for an adviser:** Edge AI blurs the cloud/data-location line. A system that runs at the edge may store much of its data and operate in Uganda, which helps the **data localisation** story — but it does not, itself, resolve who is responsible when it silently executes. Edge execution also means the step that executed the bad decision ran on a local device, so the audit trail may be in a distributed back-end, not a single audit log. A compliance strategy must cover both the cloud and the edge-tier logs — and, for litigation, which device held which log at the time matters for preservation.

---

# PART 4: THE UGANDAN LEGAL FRAMEWORK

## 4.1 Sale of Goods and Supply of Services Act, Cap. 292 — Sections 40–44

**Relevance:** These are the core **implied terms** when your client buys a model, a diagnostic device, surveillance software, or an agentic system — either a "good" or a "service," or both.

| Concept | What it does for the buyer |
|---|---|
| **Satisfactory quality (s.40 area)** | The goods must meet a standard a reasonable person would find acceptable, considering price, description, and the way they are presented |
| **Fitness for a particular purpose (s.41–42 area)** | If the buyer tells the seller the purpose, the model/goods must be reasonably fit for that purpose (e.g., a model sold "for automated credit decision" must actually function on Ugandan data) |
| **Indemnity / enforce remedies** | A breach of these implied terms gives the buyer the usual remedies (rejection, damages, etc.) |

**Ugandan Practice Tune:** Because deep learning is a "black box," the plaintiff cannot point to a hidden layer configuration as the factual cause of an erroneous output. So you **surround the metrics and the trail**: if the model was delivered with misleading validation results, or never was validated on representative Ugandan data, or was already underperforming the claimed numbers, you prove the defect *from the outset* through the **validation record**, not through tracing the neural path. The "fitness for purpose" claim is therefore a **matter of the technical data trail**, not of beating the box.

> *Note:* which Acts and sections are in force should always be confirmed against the current revised edition and any court decisions, because "as amended" provisions (e.g., the Computer Misuse Act Cap. 96 and its 2022 amendment) were the subject of recorded constitutional litigation. Read the note in the appendix, below.

## 4.2 The Computer Misuse Act (Cap. 96, as amended) — Section 12 and Section 27

**Relevance:** In the context of an agentic system that executes an *unauthorized* action (like the fertilizer order in the task):

- **Section 12 — Unauthorised access:** creates criminal liability for access to a computer or data without authority. If an agent "strays" into systems it was meant to stop at, s.12 (and the access logs that record the guardrails) frames the boundary of what is "authorised."
- **Section 27 — Corporate liability:** makes organisations (and, through attribution doctrines, the people who run them) liable where an offence is connected with their business. This clause directly catches **directors** when an agent, operating within the business, commits a wrong.

**The practical point for boards:** A 200M unauthorized purchase executed autonomously by an agent is not automatically a person's *criminal* act — but s.27 creates *civil regulatory* (compliance and governance) exposure for officers. A governance policy built on **boundary constraints**, **manual approval gates**, and **data logs** exists precisely to shield directors from that exposure: it shows the board set execution limits, required a human gate above a spend threshold, and preserved the logs that might confirm where the agent exceeded its authority.

Because the Act's amendment has been litigated, the precise current text of ss. 12 and 27 must be confirmed against the latest official authorised version at the time of advising.

## 4.3 Electronic Evidence — Getting the Neural-Net Trail Into Court

**The right question first:** In artificial intelligence litigation, the black box is not itself evidence — the **logs and records** generated by the model are. Whether those records come into court is governed in Uganda principally by the **Electronic Transactions Act, No. 8 of 2011**, not by any "electronic evidence" section of the Evidence Act. **(Do not confuse this with s.78 of the Evidence Act, Cap. 6, which is about the genuineness of certified copies — it has nothing to do with electronic records.)**

### The electronic evidence framework

- **Electronic Transactions Act, No. 8 of 2011, s.7** — defines when a data message or electronic record is authentic (integrity + the identity/origin of the person who generated it).
- **Electronic Transactions Act, No. 8 of 2011, s.8 — Admissibility and evidential weight of a data message or electronic record.** The rules of evidence shall not be applied so as to deny admissibility of a data message or electronic record *merely because* it is an electronic record, *if it is the best evidence* the party could reasonably be expected to obtain, or *merely because* it is not in original form. The party seeking to introduce it bears the burden of proving authenticity (s.8(2)). When the best-evidence rule applies and authenticity is proved, the rule is fulfilled (s.8(3)).

### Weighing the record

- **s.8(4)** — in assessing evidential weight, the court considers (a) the reliability of how the record was generated, stored or communicated; (b) the reliability of how authenticity was maintained; (c) how the originator was identified; and (d) any other relevant factor.
- **s.8(5)** — the authenticity of the recording system is **presumed** where: (a) it is shown the system was operating properly (or its failure did not affect the record's integrity) and there is no reasonable doubt; (b) the record was recorded by a party adverse in interest to the party seeking to introduce it; or (c) the record was recorded/stored in the usual and ordinary course of business by a person not a party.
- **Electronic Transactions Regulations, S.I. 42 of 2013, reg. 3** — authenticity may be proved by the data message being self-authenticating, having a hash or other metadata, being a public record, or by factual specificity about the process of creation/retention — including evidence of access control, of logging of changes, of backup practice, and the reliability of the computer (reg. 3(2)).

### Why this is the decisive weapon for the black-box case

- **Neural-net logs are electronic records.** To admit them you do **not** try to "explain the neural network." You authenticate the *record* of it: the version, the weights, the test scores, the decision outputs — under ETA s.8.
- **Prove the record's integrity, not the algorithm's logic.** Under s.8(1)-(3) and S.I. 42/2013, the natural way to admit a validation log is to show it was created and preserved in the usual course of business with the system operating normally — the ordinary-course presumption in s.8(5)(c).
- **The "best evidence" point.** s.8(1)(b) lets a party adduce the best reasonably-available electronic evidence without producing the original. For a model vendor, the source logs may be held abroad or in the cloud; the best-evidence rule is not a bar where the record is authenticity-proved.
- **Evidential weight turns on system reliability (s.8(4)(a)).** This is where your capability of explaining *how the model and its logging worked* — not its secret intermediate values — earns its keep. The more you can demonstrate the logging system was reliable and access-controlled, the stronger the weight of the past evidence.

**Practical Illustration — the Jinja estate in court:** The estate alleges the missing fertilizer order of UGX 200,000,000. The agent's purchase record and the digital-wallet transfer trail are electronic records under the ETA. To admit them: lay foundation under s.8(1)-(3) that the wallet and order logs are authentic (system operated normally, access-controlled, recorded in ordinary course); the weight depends on s.8(4) factors, the integrity and credibility of the logging system. No court asks you to reverse-engineer the agent's "reasoning"; you authenticate the record of the decision and the transaction.

> *Note:* confirm the authoritative current text of the Electronic Transactions Act and its Regulations when acting on real facts — especially the interplay between the ETA's authenticity/validity rules and the general Evidence Act provisions on documentary evidence.

## 4.4 Human Rights (Enforcement) Act, Cap. 12 — Accountability in Public Surveillance

**Relevance:** When deep-learning / biometric systems are used by **the State** — biometric police surveillance, smart traffic — the Human Rights (Enforcement) Act gives a pathway for accountability for violations of rights (or threats of violation) against the State. Cap. 12 sits alongside the constitutional rights Chapter (Article 21 non-discrimination — see Week 5) as a procedural route for a petition.

**Application:** A person who believes they were wrongly flagged by an automated surveillance or diagnostic system can invoke accountability mechanisms under Cap. 12, anchor the substantive harm in Article 21 (equal protection) and Article 27/28 (privacy of person), and demand the trail. The state, being accountable (and with the burden), must be able to explain and justify the algorithmic output — pushing the "explainability" technical burden onto the deploying authority.

## 4.5 Contracts Act, Cap. 284 — Agency and the Agent-Automation Gap

**Relevance:** When a digital agent enters a supply contract (as in the weekly task), the question of **"apparent authority"** transfers from the paper world into the automation world.

- **Agency principle:** A person (principal) may be bound by the act of an agent who appears to have authority, even if the agent exceeded the actual authority given, where the principal has held out the agent by an outward sign of authority and the third party relied on that appearance in good faith.
- **Application to AI:** An AI agent that "appears" to have the authority to spend — because the estate's system integrates its digital wallet and pay the third party — creates the form of apparent authority, and the software binds the principal **unless** the principal can prove the agent had no authority to make that kind of binding action *in circumstances the third party knew or should have known of*.

**The flip side:** This is exactly why the curriculum asks you to build an **Agentic AI Corporate Governance Policy** and why **execution gates** matter so much legally: a cap on the agent's spending authority, a human-manual-approval step above a defined threshold, and limits on wallet transfers are the facts that break the appearance of authority. Documentation of the boundary is what protects the principal from being bound — and, in turn, shields the directors.

**Linking the frameworks:**
- Cap. 284 (Contracts) — whether the agent's act formed a binding deal, and whether apparent authority operates to bind the principal.
- Cap. 292 (Sale of Goods & Services) — whether the fertiliser order was within a "purpose" the agent was authorised to procure, and whether the goods are fit / of quality.
- Computer Misuse Act (Cap. 96, s.27) — the corporate-governance shield for directors.

---

# PART 4B: FOUNDATION-TO-TUNE COMPARATIVE ANALYSIS

## Foundation-to-Tune — where to look in Ugandan law

**The Global/Engineering Foundation:** Deep-learning models route data through non-linear hidden layers to make predictive classifications; agentic systems are designed to operate autonomously within set compute caps, able to plan, use tools and loop until a goal is met. Because their internals are opaque and their actions can bind a principal, harm from them raises two distinct questions — *product/fitness liability* and *who is legally answerable for an autonomous act.*

**The Ugandan Practice Tune (what to look for, and where):**

1. **Fitness and quality of the system itself.** Cap. 292 (Sale of Goods and Supply of Services Act) ss. 40–44 — implied satisfactory quality and fitness for a particular purpose. Where a procured model or agent underperforms at delivery, the trail (training window, validation/test scores) is the proof of defect "from the outset."
2. **The crime/boundary question.** Cap. 96 (Computer Misuse Act, as amended) s.12 (unauthorised access) and s.27 (corporate liability) — look at whether an agent exceeding defined limits creates criminal exposure and at the board-governance shield. **Confirm the current text against the latest authorised edition** (the 2022 amendment was judicially litigated).
3. **Binding the principal — apparent authority.** Cap. 284 (Contracts Act) — whether an autonomous agent's act creates apparent authority and binds the corporation, and the executive-gate/governance facts that cut that off.
4. **The evidence that actually proves it.** Electronic Transactions Act, No. 8 of 2011 ss. 7–8 and S.I. 42 of 2013 reg. 3 — admitting the model's logs and records as electronic evidence (authenticity, best evidence, evidential weight). *(Not the Evidence Act s.78 — certified copies — nor CPR Order 12.)*
5. **State surveillance accountability.** Cap. 12 (Human Rights (Enforcement) Act) + Constitution Arts. 21/27/28 — where biometric/deep-learning systems are state-run.
6. **Personal data angle.** Where the system processes personal data, DPA No. 9 of 2019 — esp. s.27 (automated decision-taking; s.27(4) credit/contract exception) and s.19 (cross-border).

**In one principle:** the lawyer does not fight the hidden layer — they fight the *record and the governance around it* — so the statutory path is Cap. 292 (quality) + Cap. 284 (authority) + Cap. 96 (boundary/board) anchored by ETA s.8 (evidence) and DPA s.27 (decisions).

---

## Comparative Overview — how other regimes handle automated decisioning (verified)

> Guidance: these are accurate summaries of the statutory positions, verified to the named sections. Always check the current in-force text of any foreign statute before relying on it in an opinion.

| Regime | Anchor for automated decisioning | Approach |
|---|---|---|
| **EU (GDPR)** | Art. 22 GDPR — right not to be subject to a decision based *solely* on automated processing producing legal/similarly significant effects; with exceptions (contract, consent, law) and safeguards (human intervention, contest) | Default: no solely-automated significant decisions unless a lawful exception applies with safeguards |
| **EU (AI Act)** | Regulation (EU) 2024/1689 — risk-based tiers: unacceptable (banned), high-risk (strict, incl. credit scoring, biometric ID, assessment of people) | First comprehensive horizontal AI law; sets ANNEX III list and conformity/oversight duties, phased in force |
| **Kenya** | Data Protection Act No. 24 of 2019, s.35 — right not to be subject to a decision based solely on automated processing incl. profiling, with contract/capacity exceptions; s.35(3)(b) human reconsideration; Plus Data Protection (General) Regulations 2021, reg 22 | Mirrors the GDPR-type sole-automation test with a notification/reconsideration route and fair-processing specifics. |
| **South Africa** | POPIA No. 4 of 2013, s.71 — automated decision-making that plays a profile with legal consequences; s.71(2)-(3) contract/representation exceptions; underlying-logic disclosure | Similar default prohibition with contract exception and representational safeguard |
| **United Kingdom / USA** | UK: GDPR-derived Art. 22 position + evolving sectoral/AI statute debate. US: no single federal AI ADM law; sectoral rules (employment/credit via FCRA, etc.) and state/framework approaches | Sectoral, principle-led rather than a single comprehensive automated-decision statute — contrasts sharply with the EU |

**Why this matters for the Ugandan student:** the Ugandan position (DPA s.27 — automated decision-right, with a contract-entry exception in s.27(4)) sits **closer to the GDPR/Kenya/South Africa template** than to the US sectoral approach, and unlike the EU AI Act Uganda has no horizontal risk-based AI statute. So when advising, reach first for the DPA/Cap.292/Cap.284/ETA mix; the overseas frameworks are persuasive models (esp. for drafting safeguards), not binding law in Uganda.

---

# PART 5: THE LAWYER'S TOOLKIT — QUESTIONS TO ASK ABOUT ANY NEURAL OR AGENTIC SYSTEM

| Question | What you are really checking |
|---|---|
| How many hidden layers and which activation functions? | How opaque the "black box" is, and what log trail is feasible |
| Was the model trained/validated on representative Ugandan data? | Whether "fitness for purpose" under Cap. 292 can be established |
| Is there a validation and decision log I can subpoena? | Whether causation can be proven through the trail if opacity blocks layer-tracing |
| **Can the log be admitted? Who generated and stored it, and how reliable is the system?** | Whether it is an electronic record you can get into evidence under ETA 2011 s.8 — and what weight it will carry (s.8(4)) |
| Who controls the spend limit and the manual approval gates on this agent? | Whether apparent authority is limited / whether directors have a shield |
| Where does the model run — cloud, edge, or both — and where are the logs? | Localisation, cross-border (s.19 DPA), and where the audit trail lives |
| What happens when the model receives corrupted or manipulated inputs? | Whether there is a residual emergency stop and a guardrail for the executing agent |

---

## Appendix — Verification Notes

- Confirm the **current in-force, unamended** wording of the Computer Misuse Act (Cap. 96) sections 12 and 27 against the latest revised edition, because the 2022 amendment was itself the subject of constitutional litigation (see project general knowledge: the amendment's validity was challenged and addressed by the Constitutional Court in 2026). This verification is separate from the separate question of whether "AI" itself can commit a crime.
- Confirm the current edition and exact section numbering of the **Sale of Goods and Supply of Services Act (Cap. 292)** sections 40–44, the **Contracts Act (Cap. 284)** agency provision on apparent authority, and the **Electronic Transactions Act (No. 8 of 2011) ss. 7–8** and **S.I. 42 of 2013 reg. 3**.

---

**Core statutory references (for the student to verify against the latest edition):**
- Sale of Goods and Supply of Services Act, Cap. 292, ss. 40–44
- Computer Misuse Act, Cap. 96 (as amended), ss. 12, 27
- Electronic Transactions Act, No. 8 of 2011, ss. 7–8 (authenticity and admissibility of electronic records)
- Electronic Transactions Regulations, S.I. 42 of 2013, reg. 3 (proving authenticity)
- Human Rights (Enforcement) Act, Cap. 12
- Contracts Act, Cap. 284
- Data Protection and Privacy Act, No. 9 of 2019, ss. 19, 27 (automated decisions; contract exception)

**Comparative sources (verified):**
- GDPR, Art. 22 (solely automated decisions)
- EU AI Act, Regulation (EU) 2024/1689 (risk-based tiers)
- Kenya Data Protection Act, No. 24 of 2019, s.35; Data Protection (General) Regulations 2021, reg. 22
- South Africa POPIA, No. 4 of 2013, s.71

**Recommended reading (technical):**
- Géron, *Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow* — Ch. 10 (Introduction to Artificial Neural Networks), Ch. 14 (Deep Computer Vision using CNNs)
- Russell & Norvig, *Artificial Intelligence: A Modern Approach* — Ch. 22 (Deep Learning), Ch. 25 (Computer Vision)

---

*End of Week 6 Reading Notes*