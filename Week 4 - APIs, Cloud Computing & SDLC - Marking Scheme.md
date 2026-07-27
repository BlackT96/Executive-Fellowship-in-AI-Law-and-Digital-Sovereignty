# Week 4 Assessment — Marking Scheme & Model Answers

## General Marking Principles
- Award marks where the student demonstrates sound legal reasoning, even if they did not identify every issue.
- Statutory references to the Electronic Transactions Act Cap. 99 (ETA) should be rewarded where relevant and correctly cited.
- Professional presentation (IRAC structure, clear headings, plain English) should be rewarded.
- There is no single correct answer. The model answer below represents the standard a strong candidate might achieve.

---

## Question 1 — Legal Memorandum to the Board (20 marks)

### Mark Allocation

| Criterion | Marks | What to look for |
|---|---|---|
| Issue identification | 8 | How many relevant legal issues the student spots across the three attached documents. Award 1 mark per issue correctly identified and explained. Max 8. |
| Legal analysis | 6 | Quality of legal reasoning — application of ETA S.29-33, contract law principles, technical understanding of the API vulnerability and SDLC failure, and how these connect to legal exposure. |
| Practical recommendations | 4 | Specific, actionable next steps — not vague statements like "seek legal advice." Examples: preserve the audit log as evidence, notify affected patients, commission a security audit, renegotiate the cloud agreement, engage UK counsel. |
| Structure and presentation | 2 | Proper memorandum format (TO/FROM/DATE/RE), clear headings, professionally written. |

### Key Issues Students Should Identify

| Issue | Source | What the student should explain |
|---|---|---|
| API1 — Broken Object Level Authorization | Attachment 2 | User U-1024 accessed 7 patients' results by incrementing the ID. The API did not verify authorisation per resource. |
| Cloud agreement — governing law / jurisdiction | Attachment 1, Clause 7 | English law and London courts. A Ugandan company suing in London faces significant cost and needs UK solicitors. |
| Cloud agreement — "as-is" disclaimer | Attachment 1, Clause 2 | CloudServe disclaims all warranties. ETA S.29(2)(a) preserves contractual obligations despite the exemption. |
| Cloud agreement — vague SLA / sole remedy | Attachment 1, Clauses 2 & 5 | "Industry standard uptime" is undefined. The sole remedy is a discretionary service credit. |
| Cloud agreement — no data processing terms | Attachment 1, Clause 4 | The agreement contains no confidentiality, security, breach notification, or data return provisions. |
| SDLC failure — no security testing | Attachment 3 | Security testing deferred, code review skipped, deployed from dev branch. Relevant to negligence analysis. |
| ETA S.29 — service provider liability | Statute | CloudServe may claim S.29(1) exemption, but S.29(2)(a) preserves contractual obligations. |
| Evidence preservation | Cross-cutting | The audit and SDLC logs are electronic records (ETA S.6-8). They must be preserved with integrity intact. |

### Model Answer (Summary)

**MEMORANDUM**

TO: Board of Directors, AfyaConnect Ltd
FROM: External Legal Counsel
RE: Legal Position — Data Exposure Incident, 10 July 2026

**1. The API Vulnerability**
The audit log reveals User U-1024 accessed seven different patient records by incrementing the patient ID in the endpoint URL. The API returned 200 OK for each request, confirming no authorisation check was performed at the resource level — a Broken Object Level Authorization vulnerability (OWASP API1).

**2. The Cloud Agreement Problems**
(a) Governing law and jurisdiction (Clause 7): English law and London courts. AfyaConnect would need UK solicitors, pay UK court fees, and litigate in a foreign jurisdiction.
(b) "As-is" disclaimer (Clause 2): Services provided without warranty. However, under ETA S.29(2)(a), contractual obligations are preserved.
(c) Sole remedy (Clause 5): Only a discretionary service credit — no right to actual damages.
(d) Missing data terms (Clause 4): No confidentiality, security, or breach notification obligations.

**3. The SDLC Process Failure**
Security testing was deferred, code review was skipped, and the module was deployed from the development branch. This is relevant to any claim that AfyaConnect failed to take reasonable steps to secure patient data.

**4. ETA Section 29**
CloudServe may argue immunity under S.29(1) as a service provider. However, S.29(2)(a) preserves contractual obligations. Since CloudServe has a contractual duty to host the platform, and the data is AfyaConnect's own data (not third-party material), the exemption is unlikely to shield CloudServe from contractual claims.

**5. Recommendations**
(a) Preserve all audit logs, deployment logs, and correspondence as evidence (ETA S.7).
(b) Engage UK solicitors to advise on enforceability under English law (UCTA 1977).
(c) Commission an independent API security assessment.
(d) Notify affected patients.
(e) Renegotiate the cloud agreement — governing law, SLA, and data terms.

---

## Question 2 — Contractual Amendments (15 marks)

### Mark Allocation

| Criterion | Marks | What to look for |
|---|---|---|
| Amendment 1 | 5 | Original clause identified (1) + replacement wording (2) + legal justification (2) |
| Amendment 2 | 5 | Same structure |
| Amendment 3 | 5 | Same structure |

### Acceptable Amendments

**Amendment A — Governing Law and Jurisdiction**

*Original (Clause 7):* "This Agreement shall be governed by the laws of England and Wales. Any disputes shall be submitted to the exclusive jurisdiction of the courts of London."

*Replacement:* "This Agreement shall be governed by the laws of the Republic of Uganda. Any disputes shall be submitted to the exclusive jurisdiction of the courts of Kampala. Nothing in this clause prevents either party from seeking interim relief in any competent court."

*Justification:* Ugandan law is accessible to AfyaConnect's lawyers. The exclusive London clause creates a barrier to justice for a Ugandan SME.

**Amendment B — SLA Definition and Remedies**

*Original (Clauses 2 & 5):* "Reasonable endeavours to maintain industry standard uptime" and "sole remedy is a service credit calculated at CloudServe's discretion."

*Replacement:* "CloudServe shall maintain 99.9% monthly uptime, calculated as (total minutes — downtime) / total minutes × 100. If uptime falls below 99.9%, AfyaConnect receives a 10% fee credit per 0.5% below target. The service credit is not an exclusive remedy — AfyaConnect retains the right to seek actual damages for data breaches, gross negligence, or wilful default."

*Justification:* The original is unenforceable — "industry standard" is vague and "at CloudServe's discretion" is not a genuine remedy.

**Amendment C — Data Processing Terms**

*Original (Clause 4):* "CloudServe may process data only as necessary to provide the Services."

*Replacement (new clause):* "CloudServe shall process data only on AfyaConnect's documented instructions. CloudServe shall implement measures to protect data against unauthorised access, notify AfyaConnect within 48 hours of a breach, and return/delete all data within 30 days of termination. CloudServe shall not transfer data outside the East African Community without AfyaConnect's prior written consent."

*Justification:* The original is silent on security, breach notification, data return, and cross-border transfer.

**Amendment D — Data Location**

*New clause:* "AfyaConnect's data shall be stored only at CloudServe's Nairobi data centre. CloudServe shall not transfer data elsewhere without AfyaConnect's prior written consent and shall provide a storage location certificate within 14 days of request."

*Justification:* The current agreement does not specify storage location. Certainty protects AfyaConnect's regulatory position.

---

## Question 3 — Enforcement Advice (15 marks)

### Mark Allocation

| Criterion | Marks | What to look for |
|---|---|---|
| Part (a) — UK jurisdiction analysis | 6 | Understanding of governing law, exclusive jurisdiction, reciprocal enforcement between Uganda and UK, practical cost/access barriers, ETA S.29 relevance |
| Part (b) — Kenya data considerations | 4 | Data in Kenya raises practical evidence questions, potential Kenyan law applies to physical infrastructure, no automatic jurisdiction over CloudServe |
| Part (c) — Alternative steps | 5 | Specific alternatives: renegotiation, mediation, UK counsel opinion, evidence preservation, independent security assessment |

### Model Answer (Summary)

**(a) Implications of the UK Clause**

The agreement is governed by English law with exclusive London jurisdiction. This means:
- AfyaConnect must instruct UK solicitors at significantly higher cost.
- The enforceability of clauses will be assessed under the Unfair Contract Terms Act 1977 (UCTA) — a Ugandan lawyer cannot advise on this without a UK-qualified colleague.
- Uganda and the UK are Commonwealth countries with reciprocal enforcement arrangements under the Reciprocal Enforcement of Judgments Act (Cap 8). A Ugandan judgment may be enforceable in the UK if CloudServe has assets there. However, the exclusive jurisdiction clause means a Ugandan court may stay proceedings in favour of London.
- ETA S.29: CloudServe may argue immunity, but S.29(2)(a) preserves contractual claims. However, this argument would be made in a London court applying English law — the ETA is Ugandan law and may need to be pleaded as foreign law.

**(b) Data in Kenya**

The patient data is physically stored in Nairobi. This means:
- If AfyaConnect needs to compel production of raw server logs, Kenyan courts may have jurisdiction over the physical infrastructure.
- The data location adds cost and complexity to any forensic investigation or evidence gathering.
- The dispute involves three jurisdictions — Uganda (harm occurred), UK (contractual forum), and Kenya (data location).

**(c) Alternative Steps**

1. Renegotiate the cloud agreement — CloudServe may prefer amendments over losing a customer.
2. Preserve and secure all evidence (ETA S.7) — audit logs and SDLC logs are critical.
3. Commission an independent cybersecurity report documenting the API1 vulnerability.
4. Engage UK counsel for a preliminary opinion on enforceability under UCTA 1977.
5. Consider mediation or arbitration before litigation.
6. Notify affected patients proactively to manage reputational risk and potential claims.

---

*End of Marking Scheme and Model Answers*