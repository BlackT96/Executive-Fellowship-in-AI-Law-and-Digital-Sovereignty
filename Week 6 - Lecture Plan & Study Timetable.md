# Week 6 — Lecture Plan & Study Timetable
## Neural Networks, Deep Learning & Agentic Systems

**Module:** 2 — Artificial Intelligence Fundamentals (Weeks 5–8)
**Program:** Executive Fellowship (AI Law & Digital Sovereignty)
**Target Audience:** Lawyers with no prior computing background

---

## How to Use This Plan

This plan breaks the Week 6 reading notes (`Week 6 - Neural Networks, Deep Learning & Agentic Systems - Reading Notes.md`) into **three lectures**, assigns the **time** each lecture and its associated work takes, and sets out the **weekly test**. It follows the study plan's two-stream rhythm: **Learn** (lecture + reading) then **Apply** (deliverables + test).

**Key numbers:**

| Item | Time |
|---|---|
| Lecture 1 (Neural Network Foundations) | ~5 hrs total |
| Lecture 2 (Deep Learning + Agentic & Edge AI) | ~5 hrs total |
| Lecture 3 (Legal Framework + Toolkit) + deliverables | ~8–9 hrs total |
| Weekly test (hybrid) | ~1 hr |
| **Total weekly commitment** | **~18–20 hrs** |

---

## Lecture 1 — Neural Network Foundations (Reading Notes Part 1)

| Item | Time |
|---|---|
| Pre-reading: Part 1 (sections 1.1–1.3) | 1.5 hrs |
| Live lecture + discussion | 2 hrs |
| Post-lecture practice | 1 hr |
| Review and consolidation | 0.5 hr |
| **Total** | **5 hrs** |

**Learning outcomes.** By the end of this lecture the student can:
1. Explain what a neural network is in plain language, and what a perceptron computes (input × weight + bias → decision).
2. Distinguish ReLU from Sigmoid activations and say when each is used.
3. Explain, in one paragraph a court would understand, what hidden layers, backpropagation and gradient descent do.
4. State the single most important legal consequence: in a deep network no human wrote the rule and no single calculation explains the decision.

**Session outline (2 hrs):**

| Minutes | Segment |
|---|---|
| 0–15 | Why this lecture matters: from Week 5's credit-scoring model to Week 6's agent that signs contracts |
| 15–40 | 1.1 The neuron and the perceptron — trace one "GREEN/approve" decision by hand |
| 40–60 | 1.2 Activation functions — Sigmoid probability output vs ReLU gating |
| 60–100 | 1.3 Hidden layers, backpropagation, gradient descent — the "law student marking essays" analogy |
| 100–120 | Legal hook: "can anyone point to the single calculation?" — explainability collapses; the validation trail is the evidence |

**Post-lecture practice (1 hr):**
- **P1.1:** Hand-trace one perceptron: given three inputs and weights, compute the weighted sum, apply the bias, state the decision.
- **P1.2:** Write the one-paragraph answer to "can anyone point to the single calculation that produced this decision?" — the paragraph that will later feed the explainability report.

---

## Lecture 2 — Deep Learning + Agentic & Edge AI (Reading Notes Parts 2–3)

| Item | Time |
|---|---|
| Pre-reading: Parts 2 and 3 (sections 2.1–2.2, 3.1–3.3) | 1.5 hrs |
| Live lecture + discussion | 2 hrs |
| Post-lecture practice | 1 hr |
| Review and consolidation | 0.5 hr |
| **Total** | **5 hrs** |

**Learning outcomes.** By the end of this lecture the student can:
1. Explain what a CNN does (sliding windows detecting edges → faces) and why the output depends on the training set.
2. Explain what an RNN does (order matters: transaction sequences, sensor flows) and why "identical totals, different sequences" can be treated differently.
3. Define an agentic system by its three capabilities: planning, tool use, loop execution.
4. Explain why edge AI blurs the cloud/localisation line, and where the audit trail lives.
5. State the core agentic legal problem: an agent can form a binding intention on its controller's behalf without a human pressing a button.

**Session outline (2 hrs):**

| Minutes | Segment |
|---|---|
| 0–15 | Recap Lecture 1; why architectures differ (image vs sequence vs goal-directed) |
| 15–50 | 2.1 CNNs — Kampala biometrics/surveillance; training-set dependence; match-as-probability (Article 21) |
| 50–80 | 2.2 RNNs — MoMo fraud sequencing; "context is everything" |
| 80–110 | 3.1 Agentic systems — planning/tool-use/loop; walk the Jinja estate chain end-to-end |
| 110–120 | 3.2 Black box + 3.3 Edge AI — the record is the X-ray; edge logs in a distributed back-end |

**Post-lecture practice (1 hr):**
- **P2.1:** Map the Jinja agent's decision chain step-by-step (sensor read → "reasons" dry → wallet transfer → third-party order). Mark each step where a human gate *could* have intervened.
- **P2.2:** One short note on why a facial-recognition output is a probability, not a fact, and what that means for due process.

---

## Lecture 3 — Ugandan Legal Framework + Toolkit (Reading Notes Parts 4–5)

| Item | Time |
|---|---|
| Pre-reading: Parts 4 and 5 (sections 4.1–4.5, Part 5) | 1.5 hrs |
| Live workshop + discussion | 2.5 hrs |
| Weekly deliverables (Jinja memo + expert report section) | 4–5 hrs |
| **Total** | **8–9 hrs** |

**Learning outcomes.** By the end of this lecture the student can:
1. Apply Cap. 292 ss. 40–44 (satisfactory quality, fitness for purpose) to a procured deep-learning system, using the validation trail to prove defect "from the outset."
2. Explain the CMA Cap. 96 ss. 12 and 27 exposure for an agent's unauthorised action, and how governance gates shield directors.
3. **Admit the neural-net record under the correct law:** Electronic Transactions Act, No. 8 of 2011, ss. 7–8 and S.I. 42 of 2013, reg. 3 — not the Evidence Act's s.78 (certified copies).
4. Apply Cap. 12 (Human Rights Enforcement) to state surveillance, and Contracts Act Cap. 284 apparent authority to the agent-automation gap.
5. Use the Part 5 toolkit to interrogate any deployed neural/agentic system.

**Session outline (2.5 hrs):**

| Minutes | Segment |
|---|---|
| 0–25 | 4.1 Cap. 292 ss. 40–44 — the implied terms; the "fitness for purpose" trail |
| 25–50 | 4.2 CMA Cap. 96 ss. 12/27 — unauthorised access + corporate/board exposure |
| 50–90 | 4.3 Electronic evidence — ETA 2011 ss. 7–8, S.I. 42/2013 reg. 3; the "lawyer fights the record, not the box" reframe |
| 90–110 | 4.4 Cap. 12 — state surveillance accountability; explainability burden on the State |
| 110–130 | 4.5 Contracts Act Cap. 284 — apparent authority and the agent-automation gap |
| 130–150 | **Part 4B — Foundation-to-Tune + Comparative** — run the toolkit against the Jinja fact pattern live; locate each issue in Cap. 292 / Cap. 96 / Cap. 284 / ETA s.8 / DPA s.27; contrast the GDPR-AI Act / Kenya s.35 / SA s.71 positions |

**Weekly deliverables (4–5 hrs):** *both* tasks, in one brief:

- **D1 — Jinja Agentic AI Operations Boundary Brief** (curriculum LDC-style task): Executive Board Advisory Memo analysing the corporation's legal exposure under Contracts Act Cap. 284 and Sale of Goods Cap. 292. Analyse "apparent authority" as applied to autonomous agentic systems; identify where the system's execution gates failed; outline an updated Agentic AI Corporate Governance Policy defining expenditure limits, manual approval gates, and data logs to protect directors under CMA Cap. 96 s.27.
- **D2 — Explainability expert-report section** (study plan task): one draft expert-report section explaining whether the TukulaScore- or Jinja-agent-type neural decision is or is not explainable, framed for admissibility under ETA s.8 — the report demonstrates the record's integrity, not the algorithm's secret logic.

---

## Weekly Test — Hybrid (25-min quiz + short drafting)

| Part | Format | Time | Marks |
|---|---|---|---|
| **A — Quiz** | MCQ + true/false + short-answer, drawn from the week's Relevance Assessment, Missing Links and Foundation-to-Tune analysis | 25 min | 10 |
| **B — Short drafting** | One short drafting/advice task (e.g., draft a single execution-gate clause, or a 10-line answer on ETA s.8 admissibility) | 30 min | 10 |
| | **Total** | **~1 hr** | **20** |

**Sample quiz questions (Part A):**
1. A model's output "probability of default = 0.87" is most consistent with which activation function at the final layer? (a) ReLU (b) Sigmoid (c) Perceptron (d) Backpropagation
2. True/False: Under the Electronic Transactions Act 2011, the admissibility of an electronic record is denied merely because it is not in its original form.
3. Name the three capabilities that define an agentic system.
4. Under which statute, and which section, is the genuineness of certified copies addressed — and why is that section *not* the electronic-evidence anchor?
5. Short answer: why does a CNN's output depend on its training set, in one sentence?

**Sample drafting task (Part B):** Draft one clause for the Jinja estate's Agentic AI Corporate Governance Policy establishing a manual approval gate for any agent-initiated purchase above UGX 10,000,000. Justify the clause by reference to apparent authority and CMA s.27.

---

## 7-Day Study Rhythm

Following the study plan's rhythm (read → apply → consolidate):

| Day | Activity | Hours |
|---|---|---|
| 1–2 | **Lecture 1** — pre-read Part 1, attend session, P1.1/P1.2 | ~5 |
| 3–4 | **Lecture 2** — pre-read Parts 2–3, attend session, P2.1/P2.2 | ~5 |
| 5 | **Lecture 3** — pre-read Parts 4–5, attend workshop | ~4 |
| 6 | **Deliverables** — draft D1 (Jinja memo) and D2 (expert report section) | ~4–5 |
| 7 | **Consolidate + weekly test** — run the Part 5 toolkit against the Jinja facts, sit the 1-hr hybrid test | ~1.5 |

**Materials checklist:**
- Reading notes: `Week 6 - Neural Networks, Deep Learning & Agentic Systems - Reading Notes.md`
- Statutes to bring to the test (open book): Cap. 292 ss. 40–44; Cap. 96 ss. 12, 27; ETA No. 8 of 2011 ss. 7–8 + S.I. 42 of 2013 reg. 3; Cap. 12; Cap. 284
- `Agents\teaching\expert_witness_agent.md` for D2 support

---

*End of Week 6 Lecture Plan*
