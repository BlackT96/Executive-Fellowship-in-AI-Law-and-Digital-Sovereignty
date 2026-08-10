# Module 1: Digital Technology Fundamentals
## Week 5: History of AI, Machine Learning Foundations & Model Evaluation — Formative Assessment

**Total Marks:** 50
**Time Allowed:** 60 Minutes
**Open Book Assessment**

**Instructions:**
1. Answer all questions.
2. Attached Documents 1, 2 and 3 form part of this paper and are the only documents you need beyond this question paper.
3. You are expected to identify for yourself the specific legal provisions that apply. The matter engages the Data Protection and Privacy Act (Cap. 97), the Constitution of the Republic of Uganda, 1995, and the Contracts Act (Cap. 284). You must cite the specific provisions you rely on, with reasons.
4. You may refer to your own statute books and cases. No internet access is permitted.

---

### Fact Pattern

Sekanyolya Credit Ltd is a Kampala-based digital lender regulated under the Tier 4 Microfinance Institutions and Money Lenders Act (Cap. 61). Since January 2026 it has used an automated loan decisioning model, "TukulaScore," procured from **Nairobi AI Systems Ltd**, a Kenyan software vendor.

TukulaScore is a supervised machine learning classification model. It was trained on 250,000 historical loan applications collected between 2019 and 2023 from Sekanyolya's own records and from a third-party data broker in Kenya. The model evaluates applicants using mobile money transaction history, airtime spending, income declarations, and repayment history. It returns a single output — APPROVE or REJECT — with no written reasons given to rejected applicants.

The procurement contract between Sekanyolya and Nairobi AI Systems is set out in **Attachment Document 1 (Model Licensing & Services Agreement)**.

Since deployment, Sekanyolya has approved approximately 8,500 loans and rejected 16,500 applications. In March 2026, a community-based organisation lodged a complaint with the Personal Data Protection Office (PDPO) alleging that TukulaScore systematically rejects applicants from the Karamoja and West Nile regions at higher rates than applicants from Kampala and the Central Region. Sekanyolya's internal review produced:

- **Attachment 2 (Model Evaluation Report)** — the confusion matrix and performance metrics for the last 10,000 applications
- **Attachment 3 (Deployment & Drift Log)** — the training window and retraining history

Sekanyolya's managing director has called you for advice. No claim has been filed yet.

---

### QUESTION 1 — Legal Memorandum to the Board (20 marks)

Prepare a legal memorandum addressed to the Board of Sekanyolya Credit Ltd analysing the company's legal position in respect of TukulaScore.

Your memorandum must identify the legal issues arising from the facts and attached documents, assess the strength of Sekanyolya's position, and recommend practical next steps. Cite the specific legal provisions you rely on.

---

### QUESTION 2 — Drafting: Model Drift & Compliance Rider (15 marks)

The Managing Director has asked you to strengthen the procurement contract. Draft **four specific clauses** for a Model Drift & Compliance Rider to be added to the agreement in Attachment 1.

For each clause:
1. Identify the risk or gap in the current agreement that the clause addresses;
2. Draft the clause in a form a vendor could accept;
3. Give a brief legal justification for the clause.

---

### QUESTION 3 — Advice to the Managing Director (15 marks)

The Managing Director says:
*"The vendor tells us 92% accuracy proves we are fine. And the PDPO complaint is only about regions — our model never considered region. So what do I tell the Board, and can a rejected borrower actually do anything to me?"*

Advise the Managing Director on:

(a) Whether the vendor's "92% accuracy" claim answers the complaint, with reference to the metrics in Attachment 2;

(b) The legal position of a rejected borrower in respect of the automated decision taken against them;

(c) Whether the regional pattern engages a constitutional claim, and what evidence Sekanyolya should now gather.

---

**END OF ASSESSMENT**

---

## ATTACHED DOCUMENTS

### ATTACHMENT 1 — Model Licensing & Services Agreement (extract)

**Parties:** Sekanyolya Credit Ltd ("Licensee") and the Nairobi Trainers Ltd ("Licensor")

**Clause 4.2 — Performance Warranty**
The Licensor warrants that the Licensed Model shall achieve an aggregate accuracy of no less than 92% when deployed for the Licensee's automated credit decision.

**Clause 4.5 — Limitations of Liability**
Notwithstanding any other provision, the Licensor's aggregate liability under this Agreement shall be capped at the total licence fees paid in the preceding twelve months. The Licensor shall not be liable for any indirect, consequential, or special damages.

**Clause 6.1 — Retraining**
The Licensor shall retrain or re-benchmark the Licensed Model at the Licensee's written request. Any retraining is subject to additional fees at the Licensor's standard rates.

**Clause 6.2 — Data**
The Licensee may provide training, testing and validation data to the Licensor for the purposes of this Agreement. The data remains the property of the Licensee.

**Clause 9 — Governing Law and Jurisdiction**
This Agreement is governed by the laws of the Republic of Kenya. The parties submit to the exclusive jurisdiction of the courts of Kenya.

**Clause 11 — Training Data Warranty**
The Licensor warrants that training data was lawfully obtained in Kenya and represents a broadly representative sample of East African retail borrowers.

---

### ATTACHMENT 2 — Model Evaluation Report (extract)

*Sekanyolya internal evaluation on the last 10,000 applications.*

**Confusion Matrix**

| | Predicted: APPROVE | Predicted: REJECT |
|---|---|---|
| Actually creditworthy | 4,200 | 800 |
| Actually defaulted | 400 | 4,600 |

**Metrics**

| Metric | Value |
|---|---|
| Accuracy | 88% |
| Precision | 91.3% |
| Recall | 84% |
| F1-Score | 87.5% |

**Rejection rate by region (raw)**

| Region | Applications | Rejected |
|---|---|---|
| Kampala / Central | 4,000 | 41% |
| Northern | 2,200 | 63% |
| Karamoja | 1,900 | 68% |
| West Nile | 1,900 | 66% |

**Vendor note:** The 92% warranty was computed on a Kenyan test pool sampled in 2022 in Nairobi and Mombasa.

### ATTACHMENT 3 — Deployment & Drift Log (extract)

| Date | Event |
|---|---|
| Jan 2026 | TukulaScore deployed. Training data window: 2019–2023 (data broker, Kenya). |
| Feb 2026 | Uganda Communications Commission notifies tier 4 lenders that mobile money transaction patterns changed materially after 2024 merchant adoption. |
| Mar 2026 | Regional association lodges PDPO complaint alleging regional discrimination. |
| Mar 2026 | Sekanyolya requests re-benchmarking under Clause 6.1. Vendor states retraining involves a supplementary fee and a seven-month timeframe. |
| Mar 2026 | No retraining has been performed. |

**END OF ATTACHED DOCUMENTS**