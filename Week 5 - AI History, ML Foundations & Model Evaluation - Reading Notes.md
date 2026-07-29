# Week 5: History of AI, Machine Learning Foundations & Model Evaluation — Reading Notes for Legal Practitioners

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

# PART 1: A BRIEF HISTORY OF ARTIFICIAL INTELLIGENCE

## 1.1 What is Artificial Intelligence?

**Plain English:** Artificial Intelligence (AI) is the field of computer science that tries to make machines do things that would require intelligence if done by a human. Think of it as teaching a computer to think, learn, and make decisions — not just follow rigid step-by-step instructions.

**The Two Big Ideas:**

| Idea | What It Means |
|------|---------------|
| **Symbolic AI** (1950s–1980s) | Program the computer with explicit rules written by humans. "If this, then that." Like a legal decision tree. |
| **Machine Learning** (1990s–present) | Do not program rules. Instead, give the computer大量 examples and let it figure out the rules itself. |

**Why this matters for a lawyer:** The type of AI determines who is liable when something goes wrong. Symbolic AI failures trace back to the programmer who wrote the rule. Machine learning failures trace back to the data used to train the system — a fundamentally different liability chain.

## 1.2 The Three Ages of AI

### Age 1: Symbolic AI and Expert Systems (1950s–1980s)

**Plain English:** Early AI researchers believed intelligence could be reduced to logical rules. They built "expert systems" — programs that encoded the knowledge of human experts into thousands of if-then rules.

**Practical Illustration — Ugandan Tax Advisory System:**
Imagine a computer programmed with the entire Tax Procedures Code Act: "IF the taxpayer is a company AND annual turnover exceeds UGX 150 million, THEN VAT at 18% applies." The computer applies these rules mechanically. Every answer is traceable to a specific rule written by a human programmer.

**Why this matters for a lawyer:** Liability is straightforward. If the system gives wrong tax advice, you trace it to the specific rule that was wrong, and the programmer or domain expert who wrote it is responsible. The system cannot "learn" or deviate from its rules.

### Age 2: Machine Learning — the Data-Driven Shift (1990s–2010s)

**Plain English:** Instead of writing rules by hand, researchers realised they could give the computer大量 examples and let it discover patterns on its own. The computer does not follow pre-programmed rules — it builds its own internal model from data.

**Practical Illustration — Credit Scoring:**
You do not tell the computer: "IF income < UGX 500,000 THEN reject loan." Instead, you give it 100,000 past loan applications with their outcomes. The computer finds its own patterns: perhaps people who make mobile money deposits after 10 PM are more likely to default. This is a pattern a human programmer would never have thought to write as a rule.

**Why this matters for a lawyer:** This shift changes everything. The computer's decision-making process becomes opaque — not because someone is hiding it, but because the computer discovered patterns that even its creators cannot fully explain. This is the "black box" problem at the heart of modern AI regulation.

### Age 3: Deep Learning and Foundation Models (2010s–present)

**Plain English:** Modern AI uses massive neural networks — loosely inspired by the human brain — with billions of internal connections trained on internet-scale data. These systems can generate text, recognise images, and hold conversations, but their internal reasoning is largely unknowable.

**Why this matters for a lawyer:** The opacity compounds. When a credit-scoring model denies a loan, the bank cannot give you a rule-based explanation because no rules exist. The reason is buried across billions of mathematical weights in the neural network. This directly engages Article 21 (discrimination) and DPA s.27 (automated decision-taking).

---

# PART 2: MACHINE LEARNING PARADIGMS

## 2.1 Supervised Learning

**Plain English:** You act as a teacher. You give the computer examples that are already labelled with the correct answer, and it learns to predict the label for new, unseen examples.

### Example 1: Classification — Approve or Reject?

| Input Data (Features) | Label (Answer) |
|---|---|
| Income: UGX 2M, Default history: None, MoMo transactions: 45/month | APPROVED |
| Income: UGX 200K, Default history: 2 defaults, MoMo transactions: 3/month | REJECTED |
| Income: UGX 1.5M, Default history: None, MoMo transactions: 12/month | **???** |

The model learns from the labelled examples and predicts the label for the third row.

**Legal Framework (Uganda):**
- **DPA Cap. 97, s.27** — Rights in relation to automated decision-taking. A data subject has the right to require that no decision significantly affecting them be based solely on automated processing. Section 27(4) exempts decisions made in the course of entering or performing a contract — but the data subject must still be notified and given the right to challenge.
- **Constitution Art. 21** — If the model's classification systematically rejects applicants from a particular region or ethnic group, this may constitute discrimination, even if the model "discovered" this pattern on its own.

### Example 2: Regression — Predicting a Number

**Plain English:** Instead of a yes/no answer, regression predicts a numeric value.

**Practical Illustration — Loan Amount Prediction:**
A fintech predicts the maximum loan a borrower can afford. Inputs: monthly MoMo deposit volume, repayment history, airtime spending patterns. Output: "Maximum loan: UGX 500,000."

**Why this matters for a lawyer:** If the regression systematically underestimates loan capacity for a demographic group (e.g., women market vendors whose income is irregular but substantial), this produces discriminatory outcomes even though no explicit discriminatory rule exists.

## 2.2 Unsupervised Learning

**Plain English:** No teacher, no labels. You give the computer data and let it find structure on its own.

**Practical Illustration — Customer Segmentation:**
An insurance company feeds its customer database into an unsupervised model. The model discovers three clusters:
- **Cluster A:** High income, urban, frequent travellers
- **Cluster B:** Low income, rural, limited digital footprint
- **Cluster C:** Students, low income but high digital engagement

The company then designs different products for each cluster.

**Why this matters for a lawyer:** Unsupervised learning can create categories that indirectly map to protected characteristics. If "Cluster B" corresponds predominantly to a particular tribe or region, and the company charges that cluster higher premiums, the discrimination claim under Article 21 is the same as if the company had explicitly targeted that group.

## 2.3 Reinforcement Learning

**Plain English:** The computer learns by trial and error, like training a dog. It takes actions, receives rewards or penalties, and learns to maximise cumulative reward.

**Practical Illustration — Automated Trading:**
A reinforcement learning agent is deployed to trade mobile money float between MTN and Airtel to maximise profit. It tries different strategies, learns which ones work, and settles on an optimal approach over time.

**Why this matters for a lawyer:** Reinforcement learning systems can develop strategies their creators never intended or anticipated. If the system discovers that delaying settlement for certain regions yields higher profit (because of float demand patterns), it may disadvantage those regions, creating regulatory risk under the National Payment Systems Act and consumer protection principles.

---

# PART 3: MODEL EVALUATION — HOW TO JUDGE WHETHER AN ML MODEL IS ANY GOOD

## 3.1 Why a Lawyer Must Understand Model Metrics

When a client says "our model is 92% accurate," they expect you to accept that as a statement of quality. A lawyer who understands model evaluation knows that 92% accuracy can mean very different things depending on context, and that the real legal questions start where the metrics end.

## 3.2 The Confusion Matrix

Every classification model makes two types of errors. The confusion matrix captures all four possible outcomes:

| | **Predicted: APPROVED** | **Predicted: REJECTED** |
|---|---|---|
| **Actual: APPROVED** | True Positive (correct approval) | False Negative (wrongly rejected) |
| **Actual: REJECTED** | False Positive (wrongly approved) | True Negative (correct rejection) |

**Practical Illustration — Micro-Lending Model:**
A Kampala-based digital lender's model processes 10,000 applications:

| | Predicted Approve | Predicted Reject |
|---|---|---|
| **Actually approved** | 4,500 | 500 |
| **Actually defaulted** | 400 | 4,600 |

From this matrix, we calculate:

| Metric | Formula | Value | What It Tells You |
|---|---|---|---|
| **Accuracy** | (4500+4600)/10000 | 91% | Overall correctness — but misleading if data is imbalanced |
| **Precision** | 4500/(4500+400) | 91.8% | Of those approved, how many were correct? High precision = fewer bad loans |
| **Recall** | 4500/(4500+500) | 90% | Of all good borrowers, how many were correctly approved? High recall = fewer missed opportunities |
| **F1-Score** | 2 x (P x R)/(P + R) | 90.9% | Harmonic mean of precision and recall — the balanced measure |

### Why Accuracy Alone is Dangerous

**Practical Illustration — The 99% Problem:**
Suppose only 1% of loan applicants are defaulters. A model that simply rejects everyone achieves 99% accuracy — every defaulter is caught! But it also rejects every good borrower. Accuracy is meaningless when the data is imbalanced.

**Why this matters for a lawyer:** If a vendor guarantees "92% aggregate accuracy," you must demand to see:
- The confusion matrix broken down by demographic group (to detect Article 21 discrimination)
- Precision and F1-Score, not just accuracy
- Performance on Ugandan-specific test data, not generic international benchmarks

## 3.3 Precision and Recall — The Trade-Off

**Plain English:** Precision answers: "When the model says 'approve,' should we believe it?" Recall answers: "Does the model catch all the good borrowers?"

There is always a trade-off. A model can be made more conservative (higher precision, lower recall) or more aggressive (higher recall, lower precision).

**Legal significance:** The trade-off point is a business decision with legal consequences:
- **High precision / Low recall**: Fewer bad loans, but many good borrowers are wrongly rejected. Risk: Article 21 discrimination claim if rejections disproportionately affect a protected group.
- **Low precision / High recall**: More loans, but more defaults. Risk: Shareholder claims if excessive defaults cause losses; regulatory risk if the lender cannot demonstrate responsible lending under UMRA guidelines.

## 3.4 Overfitting, Underfitting, and Model Drift

### Overfitting

The model memorises the training data instead of learning general patterns. It performs brilliantly on historical data but fails on new data.

**Analogy:** A law student who memorises past exam answers without understanding the principles. On the actual exam, every question is slightly different, and they fail.

**Practical Illustration — The 2019 Data Problem:**
A credit model trained exclusively on 2019 data (pre-pandemic) learns that "stable employment for 2+ years" is the strongest predictor of repayment. In 2020, COVID disrupts employment patterns. The model, trained on pre-pandemic data, now systematically rejects borrowers who are employed but have shorter tenure — even though they are creditworthy.

### Underfitting

The model is too simple to capture the patterns in the data. It performs poorly on both training and new data.

### Model Drift

Over time, the real world changes and the model's performance degrades.

**Common causes:**
- **Concept drift:** The relationship between inputs and outputs changes (e.g., post-COVID repayment behaviour is different from pre-COVID)
- **Data drift:** The input data itself changes (e.g., MoMo transaction patterns shift as more merchants accept digital payments)

**Legal significance:** Under the Contracts Act, Cap. 284, a vendor who warrants a specific performance level but does not monitor or address model drift may be liable for misrepresentation or breach of contract.

---

# PART 4: THE UGANDAN LEGAL FRAMEWORK

## 4.1 Constitutional Framework: Article 21

**Article 21(1):** "All persons are equal before and under the law in all spheres of political, economic, social and cultural life and in every other respect and shall enjoy equal protection of the law."

**Article 21(2):** "A person shall not be discriminated against on the ground of sex, race, colour, ethnic origin, tribe, birth, creed or religion, or social or economic standing, political opinion or disability."

**Article 21(3):** Defines discrimination as giving different treatment to different persons attributable mainly to their descriptions under Article 21(2).

**Article 45:** The rights under the Constitution, including Article 21, "shall not be regarded as excluding others not specifically mentioned."

**Case Law:**
- **Uganda Law Society v AG [2024] UGCC 2** — The Constitutional Court held that Article 45 means the list of prohibited grounds under Article 21(3) is not exhaustive. Discrimination may exist on grounds not explicitly listed.
- **Madrama Izama v AG** — Earlier decision that age was not a protected ground under Article 21(2) (now doubted following Uganda Law Society v AG).

**Application to ML Models:**
A credit-scoring model that disproportionately rejects applicants from a particular region (indirectly corresponding to ethnic origin or social/economic standing) may violate Article 21. The fact that the model discovered this pattern independently — rather than being explicitly programmed to discriminate — is not a defence. The outcome is what matters.

## 4.2 DPA Cap. 97 — Key Sections for ML

### Section 3: Principles of Data Protection

| Principle | Application to ML |
|---|---|
| Accountability (s.3(1)(a)) | The lender is accountable even if the model operates automatically |
| Fair and lawful processing (s.3(1)(b)) | Unfair to use a model that systematically discriminates |
| Adequacy, relevance, minimality (s.3(1)(c)) | Only collect data actually needed for credit assessment |
| Retention period (s.3(1)(d)) | Training data should not be kept longer than necessary |
| Transparency and participation (s.3(1)(f)) | The borrower has the right to be informed how their data is processed and to participate in the processing |

### Section 25: Right to Prevent Processing

A data subject may, by notice in writing, require the data controller to stop processing personal data that causes or is likely to cause unwarranted substantial damage or distress. The data controller must respond within 14 days.

**Application:** A borrower who believes an ML model has incorrectly assessed them and caused them damage (e.g., denial of credit, higher interest rates) can invoke s.25 to stop the processing and demand a human review.

### Section 27: Rights in Relation to Automated Decision-Taking

This is the most critical section for ML models. Section 27 creates two distinct protections:

**Section 27(1):** A data subject may by notice require the data controller to ensure that no decision significantly affecting them is based solely on automated processing. This is a proactive right — the data subject can opt out of automated decisions.

**Section 27(4) Exception:** The s.27(1) right does not apply to decisions made in the course of considering whether to enter into a contract, or in the course of performing a contract. Most credit-scoring decisions fall within this exception.

**Section 27(2) — Independent Notification Duty:** Regardless of the s.27(4) exception, where a significant automated decision is made, the data controller must as soon as practicable notify the data subject and inform them of the right to request reconsideration of the decision.

**Practical Impact:** A borrower denied credit by an automated model cannot prevent the model from making the initial decision (s.27(4) exception), but must be notified of the automated decision and given the right to request human reconsideration (s.27(2)). The lender's contract terms cannot waive these notification and reconsideration rights.

### Section 19: Cross-Border Transfers

If the ML model is hosted on international cloud infrastructure (e.g., AWS in South Africa, Azure in Europe), the training data and live scoring data must comply with s.19 — adequate protection or data subject consent.

## 4.3 Contracts Act, Cap. 284

**Relevance:** Procurement of ML models. When a startup or bank procures a credit-scoring model from a vendor, the contract is governed by the Contracts Act.

**Key Issues for ML Procurement:**
- **Performance guarantees:** "92% accuracy" must be defined: on what data, measured how, for how long?
- **Model drift provisions:** The contract should require periodic retraining and benchmarking
- **Audit rights:** The purchaser must have the right to test the model against their own data for bias
- **Limitation of liability:** Standard clauses disclaiming future performance may be unreasonable under Ugandan law if the vendor knew the model would be used in a different demographic context

---

# PART 5: PUTTING IT TOGETHER — THE LAWYER'S TOOLKIT

## 5.1 What to Ask When a Client Says "We Use AI"

| Question | What You Are Really Asking |
|---|---|
| What type of ML is it? (Supervised/Unsupervised/RL) | Determines whether the model learns patterns you cannot explain |
| What data was it trained on? | Is the training data representative of the Ugandan population? |
| What is the performance on Ugandan-specific test data? | Global benchmarks may not apply to local demographics |
| What is the confusion matrix broken down by demographic group? | Reveals Article 21 discrimination |
| What is the Precision, Recall, and F1-Score? | Accuracy alone is misleading |
| Is the model audited for drift? | Ensures it remains reliable over time |
| Can a human override the model's decision? | DPA s.27 requires this |
| Where is the data stored? | DPA s.19 cross-border transfer compliance |

## 5.2 The Model Drift & Compliance Rider

The curriculum's practice task asks you to draft a **Model Drift & Compliance Rider** under the Contracts Act, Cap. 284. Key clauses to include:

1. **Defined Technical Benchmarks:** Precision, Recall, and F1-Score minimum thresholds calculated on a Ugandan-specific test pool stratified by region, gender, and economic standing
2. **Mandatory Validation Loop:** Quarterly audited testing for demographic bias under Article 21, with results reported to both parties
3. **Remedies:**
   - **Data Portability:** If the model fails benchmarks, the purchaser has the right to extract all data in a standardised format to migrate to another provider
   - **Service Credits:** Proportional reduction in fees for each month benchmarks are not met
   - **Termination Rights:** If model drift causes material harm or regulatory action, immediate termination without penalty
4. **Audit Clause:** The purchaser has the right to conduct independent technical audits of the model at the vendor's premises or through a secure remote testing environment
5. **Indemnity:** The vendor indemnifies the purchaser against regulatory fines or third-party claims arising from discriminatory model outcomes

---

**Statutory References:**
- Constitution of the Republic of Uganda, 1995, Article 21
- Data Protection and Privacy Act, Cap. 97, Sections 3, 19, 25, 27
- Contracts Act, Cap. 284
- National Payment Systems Act, Cap. 59
- Tier 4 Microfinance Institutions and Money Lenders Act, Cap. 61

**Key Case Law:**
- Uganda Law Society and 12 Others v Attorney General [2024] UGCC 2 (Constitutional Court — Article 21 grounds not exhaustive)

**Recommended Reading:**
- Russell & Norvig, *Artificial Intelligence: A Modern Approach* — Chapters 1-3 (AI History), Chapter 19 (Forms of Learning)
- Geron, *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow* — Chapter 1 (The Machine Learning Landscape), Chapter 3 (Classification and Evaluation Metrics)

---

*End of Week 5 Reading Notes*
