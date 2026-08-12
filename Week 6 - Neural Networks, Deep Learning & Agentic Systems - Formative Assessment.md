# Module 2: Artificial Intelligence Fundamentals
## Week 6: Neural Networks, Deep Learning & Agentic Systems — Formative Assessment

**Total Marks:** 20
**Time Allowed:** 55 Minutes
**Open Book Assessment**

**Instructions:**
1. Answer all questions.
2. You may refer to your own statute books, cases, and the Week 6 Reading Notes. No internet access is permitted.
3. This is a formative (weekly check) assessment. It tests your grasp of the week's concepts and your ability to locate them in the correct law.
4. Where a question asks you to identify a legal provision, you must name the specific statute and section you rely on, with a brief reason.

---

### PART A — QUIZ (10 marks) [25 minutes]

**Q1.** A model's output reads "probability of default = 0.87." Which activation function at the final layer is most consistent with that output?

(a) ReLU
(b) Sigmoid
(c) Perceptron
(d) Backpropagation

**(2 marks)**

---

**Q2.** True or False: Under the Electronic Transactions Act, No. 8 of 2011, the admissibility of an electronic record is denied merely because it is not in its original form.

State your answer and cite the section that governs it.

**(2 marks)**

---

**Q3.** Name the **three capabilities** that define an agentic system, as set out in the Week 6 reading notes.

**(2 marks)**

---

**Q4.** Section 78 of the Evidence Act, Cap. 6 is sometimes misdescribed as the electronic-evidence anchor. State briefly: (a) what s.78 is actually about, and (b) which statute and sections are the correct anchor for admitting the logs and records of a neural-network or agentic system.

**(2 marks)**

---

**Q5.** In one sentence: why does a CNN's output depend on its training set, and what single legal consequence follows for a biometric match produced by such a network?

**(2 marks)**

---

### PART B — SHORT DRAFTING (10 marks) [30 minutes]

**Q6.** The Jinja Agricultural Estates Ltd operates an agentic system that manages irrigation, procures chemical inputs through an integrated digital wallet, and signs supply contracts with local distributors. The system is authorised to make purchases up to UGX 5,000,000 without human approval. Following corrupted sensor data, the agent autonomously placed a UGX 200,000,000 non-refundable fertilizer order with a third-party vendor. No human approved the transaction.

**Part B(i).** Draft **one clause** for the Jinja estate's Agentic AI Corporate Governance Policy establishing a manual approval gate for any agent-initiated purchase above a specified threshold. The clause must state the threshold, who approves, and what is recorded.

**(5 marks)**

**Part B(ii).** In no more than 8 lines, justify the clause by reference to **apparent authority** under the Contracts Act (Cap. 284) and **board exposure** under the Computer Misuse Act (Cap. 96). Cite the relevant sections.

**(5 marks)**

---

**END OF ASSESSMENT**

---

## MARKING SCHEME & MODEL ANSWERS

### PART A — QUIZ (10 marks)

**Q1 — (2 marks)**
- Correct answer: **(b) Sigmoid** (2 marks)
- Reason (not required for full marks): Sigmoid squeezes any value into 0–1, which reads as a probability; ReLU passes positives through unchanged and cannot itself produce a bounded probability; backpropagation and perceptron are learning mechanisms / single units, not activation functions at a final layer.

**Q2 — (2 marks)**
- **False.** (1 mark)
- **Electronic Transactions Act, No. 8 of 2011, s.8(1)(b)** — the rules of evidence shall not be applied so as to deny admissibility of a data message or electronic record merely because it is not in its original form (if it is the best evidence the party could reasonably be expected to obtain). (1 mark for the section; award 0.5 for the section without the sub-provision reference, provided s.8 is correctly named.)

**Q3 — (2 marks)**
- **Planning** (breaking the goal into steps)
- **Tool use** (calling external functions — APIs, payment systems, order systems)
- **Loop execution** (cycling: try → check → adjust → repeat until goal or limit)
- (2/3 = 1.5; 2/3 = 1.5; all three correct = 2 marks. Deduct 0.5 per missing or incorrect item.)

**Q4 — (2 marks)**
- (a) **s.78 of the Evidence Act, Cap. 6 concerns the genuineness/presumption as to certified copies** — it is not about electronic records. (1 mark)
- (b) The correct anchor is the **Electronic Transactions Act, No. 8 of 2011, ss. 7–8** (authenticity; admissibility and evidential weight of data messages and electronic records), read with the **Electronic Transactions Regulations, S.I. 42 of 2013, reg. 3** (proving authenticity). (1 mark)

**Q5 — (2 marks)**
- A CNN's output depends on its training set because **the network learns its weights from the data it was trained on**, so a model trained mostly on one skin tone, lighting, or demographic will be more accurate on that group. (1 mark)
- Legal consequence: **a biometric "match" is a probability, not a fact** — so treating it as proof of identity raises a due-process / non-discrimination question (Article 21), and the false-approval rate should be demanded exactly as one would demand the false-positive figure in credit scoring. (1 mark)

### PART B — SHORT DRAFTING (10 marks)

**Q6 Part B(i) — execution-gate clause (5 marks)**

*Award marks for a clause that contains:*

| Element | Marks |
|---|---|
| Threshold stated (e.g., UGX 10,000,000, or any purchase above the authorised UGX 5,000,000) | 1 |
| Named human approver (e.g., the managing director or finance director) | 1 |
| Requirement that no order/payment executes without the recorded approval | 1 |
| What is recorded: approver, timestamp, transaction details (audit trail) | 1 |
| Professional drafting quality (operable, unambiguous, no legalese) | 1 |

*Model clause:*

> **Clause 7 — Agent Expenditure Approval Gate.**
> (1) The Agent is authorised to execute purchases up to UGX 5,000,000 (Uganda Shillings Five Million) per transaction without further approval.
> (2) Any agent-initiated purchase or payment exceeding UGX 5,000,000 shall not be transmitted, authorised, or executed unless and until the Managing Director (or, in their absence, the Finance Director) has reviewed and approved the transaction in writing through the platform's approval interface.
> (3) The system shall record, for every approved and every blocked transaction: the transaction value, the vendor, the sensor or input data that triggered the purchase, the identity of the approving officer, and the timestamp of approval.
> (4) No agent action shall be irreversible until a human approval recorded under sub-clause (3) is complete.

**Q6 Part B(ii) — justification (5 marks)**

*Award marks for:*

| Element | Marks |
|---|---|
| **Apparent authority identified:** under the Contracts Act, a principal may be bound where an agent "appears" to have authority, the principal held the agent out, and the third party relied in good faith — the estate's integrated wallet and prior authority to spend create that appearance | 2 |
| **The gate breaks the appearance:** a documented spend cap and human-approval requirement are the facts that show the agent had no authority to bind above the threshold in circumstances the vendor knew or should have known | 1.5 |
| **Board exposure under Cap. 96 s.27:** corporate/regulatory exposure for an agent's unauthorised action connected with the business; a documented governance policy shields directors by showing the board set limits and required gates | 1.5 |

*Model answer (indicative):*

An autonomous agent that "appears" to have spending authority — because the estate's system integrates the digital wallet and pays third parties — creates the form of apparent authority under the Contracts Act, Cap. 284: the principal is bound unless it can prove the agent had no authority to make that kind of binding action in circumstances the third party knew or should have known of. The execution-gate clause is exactly the evidence that breaks that appearance: it caps the agent's authority, requires a named human approver above the threshold, and documents the boundary. Where a vendor deals with an agent known to be capped, reliance cannot be good-faith. Separately, under the Computer Misuse Act, Cap. 96, s.27, an unauthorised action executed by an agent connected with the business engages corporate (and, by attribution, officer) exposure. A governance policy built on boundary constraints, manual approval gates, and data logs is the shield: it shows the board set execution limits and preserved the audit trail that would confirm where the agent exceeded its authority.

*(Note: confirm the current text of Cap. 96 ss. 12 and 27 against the latest authorised edition before relying on them in practice — the Act's amendment was the subject of recorded constitutional litigation.)*

---

## READING RESOURCE MAP

| Question | Tests | Reading Resource |
|---|---|---|
| Q1 | Activation functions (Sigmoid vs ReLU) | Week 6 Reading Notes §1.2 |
| Q2 | Admissibility of electronic records; ETA 2011 s.8(1)(b) | Week 6 Reading Notes §4.3 |
| Q3 | Agentic systems: planning, tool use, loop | Week 6 Reading Notes §3.1 |
| Q4 | Correct electronic-evidence anchor; Evidence Act s.78 misdescription | Week 6 Reading Notes §4.3 (correction note) |
| Q5 | CNNs, training-set dependence, match-as-probability | Week 6 Reading Notes §2.1 |
| Q6 | Apparent authority (Cap. 284); CMA s.27; execution gates; governance policy | Week 6 Reading Notes §§4.2, 4.5; Week 6 Lecture Plan (D1, sample drafting task) |

---

*End of Week 6 Formative Assessment*
