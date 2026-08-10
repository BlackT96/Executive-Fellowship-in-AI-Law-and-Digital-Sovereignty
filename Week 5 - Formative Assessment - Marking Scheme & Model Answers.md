# Week 5 — Formative Assessment: Marking Scheme & Model Answers (Marker Copy)

**Assessment:** Week 5, Module 1 — History of AI, ML Foundations & Model Evaluation
**Total Marks:** 50 · **Pass Mark:** 50% · **Distinction:** 75%

---

## Assessment Blueprint

| Q | Outcome tested | Bloom's | Type | Marks | Time |
|---|---|---|---|---|---|
| 1 | Apply DPA principles and constitutional non-discrimination to a procured ML model; evaluate the vendor warrant | Analyse, Evaluate | Memorandum | 20 | 25m |
| 2 | Draft a Model Drift & Compliance Rider under the Contracts Act, Cap. 284 | Create | Drafting | 15 | 15m |
| 3 | Advise on metrics, a borrower's rights against automated decisions, and a constitutional claim | Evaluate | Problem (a/b/c) | 15 | 20m |

---

## QUESTION 1 — Memorandum to the Board (20 marks)

**Marking scheme:**

| Criterion | Marks |
|---|---|
| Issues correctly identified (automated decision; fairness/accuracy of outcomes; regional disparity; vendor warranty vs local performance; cross-border data; confidential information) | 4 |
| Correct DPA framework: protection principles under s.3 applied to a model user; lawful and fair processing | 3 |
| Automated decisioning: explain s.27 and the s.27(4) contract exception; note whether the exception applies and the residual duties | 3 |
| Article 21 non-discrimination, read with Article 45 (non-exhaustive grounds); described harms are outcome-based, not intent-based | 3 |
| Cross-border transfer s.19; the agreement's governing-law clause does not displace Ugandan obligations | 2 |
| The "92% accuracy" figure is a vendor representation not validated on Ugandan data | 2 |
| Practical recommendations (audit, human review, PDPO, renegotiate, benchmark on local data) | 2 |
| Structure and presentation (memorandum form) | 1 |
| **Total** | **20** |

**Model answer — key points:**

1. **Automated decisioning, s.27.** TukulaScore's APPROVE/REJECT is a decision based "solely on the processing by automatic means of personal data." On its face it engages s.27(1). A data subject may by written notice require that no such decision be based solely on automated processing. However, s.27(4) disapplies the section where the decision is made in the course of considering whether to enter into a contract (which a credit decision is), or in the course of performing a contract. So in the lending context the borrower cannot compel a human decision through s.27 alone. The marks are for correctly identifying and applying s.27(1) and s.27(4).

2. **Right to prevent processing, s.25.** A borrower who considers the automated outcome causes, or is likely to cause, unwarranted substantial damage or distress may by notice require processing to stop (s.25(1)). The controller must respond within 14 days (s.25(2)). This is a separate right from s.27 and remains available to a rejected borrower.

3. **Fair and accountable processing, s.3.** s.3(1)(a) accountability and s.3(1)(b) fair and lawful processing apply even where a third party built the model. Fairness is tested by outcome; the higher rejection rates for Karamoja and West Nile (Attachment 2) are material.

4. **Cross-border transfer, s.19.** Training and evaluation data move to and are handled from Kenya. s.19 requires adequate protection or consent. A vendor clause that applies Kenyan law (cl. 9) cannot displace the controller's statutory obligations under Cap. 97.

5. **Constitutional non-discrimination, Articles 21 and 45.** Article 21(1)–(3) guarantees equality and prohibits the discrimination listed in Article 21(3). Article 45 provides that the enumerated rights do not exclude others, indicating the grounds are not exhaustive. Even if the model never used region as a feature, an outcome that falls disproportionately on a socio-economic or regional proxy may amount to indirect discrimination; the effect, not the intent, is relevant.

6. **Recommendations.** Commission an independent region-stratified audit of the confusion matrix; suspend or back the model with a human-in-the-loop process; notify the PDPO; renegotiate the contract to make performance benchmarks local, add drift and retraining obligations, provide audit rights, and set out remedies; keep any notice and response obligations in place.

---

## QUESTION 2 — Model Drift & Compliance Rider (15 marks)

**Marking scheme:** four clauses, up to 5 marks each, capped at 15 (1 = correct identification of the gap, 2 = a faithful, enforceable drafted clause, 2 = legal justification by reference to Cap. 284 / DPA / Constitution).

**Model clauses:**

1. **Defined technical warranties on local data.** Replace the aggregate "92% accuracy" with measurable thresholds — for example precision, recall, and F1 — computed quarterly on a test pool sampled from Uganda, stratified by region, gender, and income. Justification: a performance term expressed as a defined benchmark on a relevant population is enforceable under the Contracts Act; the aggregate figure on a Kenya 2022 pool does not.

2. **Monitoring and retraining on drift.** The vendor shall monitor for material changes in the lending environment and shall retrain the model within a stated period when they occur, at itemised (not discretionary) fees. This converts the open-ended clause 6.1 into an enforceable process term.

3. **Audit right.** The licensee may audit the model on its own data, including a breakdown by demographics (region, gender, income) to test for bias. Justification: an audit right supports accountability under s.3(1)(a) and gives the licensee the evidence needed for a possible Article 21 claim.

4. **Remedies for failure.** Service credits for each month a benchmark is missed; data portability on termination; termination for material uncorrected bias; and an indemnity, with the liability cap carved out where a defective model outcome causes a third-party claim. Justification: enforceable remedies against the risk that the vendor's limited liability clause excludes the very losses at issue.

---

## QUESTION 3 — Advice to the Director (15 marks)

**Marking scheme:**

| Criterion | Marks |
|---|---|
| (a) Metrics: aggregate accuracy vs precision/recall/F1; the 92% was a 2022 Kenya pool; the local figures show the disparity | 4 |
| (b) A borrower's position: s.25 right to prevent processing; s.27 automated decision and the s.27(4) contract exception; the right to complain to the PDPO | 6 |
| (c) Constitutional position: Article 21 read with Article 45; evidence to gather: full dataset disaggregated, an independent bias audit, and re-benchmarking | 5 |

**Model answer — key content:**

(a) The figure of 92% tells you nothing about the problem. It was computed on a 2022 Kenyan (Nairobi/Mombasa) pool. The local evaluation (Attachment 3) shows 88% overall accuracy, and the regional rejection figures are 63–68% for Karamoja and West Nile against 41% for the Central. Accuracy is a single aggregate; it is the precision and the distribution across regions that the complaint concerns.

(b) A rejected borrower has real routes. Under s.25, they may by written notice require the controller to stop processing personal data that causes or is likely to cause unwarranted substantial damage or distress, and the controller must respond within 14 days. Under s.27(1), they may by notice require that a decision significantly affecting them not be based solely on automated processing — though s.27(4) disapplies this where the decision is made in considering whether to enter a contract, which a credit decision is. Even so, the borrower can complain to the PDPO, and nothing in the vendor's law clause (cl. 9) can remove those statutory rights.

(c) Under Article 21 as read with Article 45, systematically different outcomes for a particular region or socio-economic group may amount to discrimination, and the legal test is outcome-based. Evidence to gather: the full application and decision dataset, disaggregated by region and by protective/proxy attributes; an independent audit of the confusion matrix by demographic group; and a fresh benchmark on a current, Ugandan-sampled test pool.

---

## Reading Resource Map

| Q | Week 5 sources |
|---|---|
| 1 | §1.2–1.3, §2, §3, §4 |
| 2 | §5.2 (Model Drift & Compliance Rider), Contracts Act Cap. 284 |
| 3 | §3, §4 |