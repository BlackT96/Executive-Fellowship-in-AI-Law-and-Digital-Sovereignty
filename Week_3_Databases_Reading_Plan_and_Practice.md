# Week 3: Databases (SQL, NoSQL, Data Warehouses) — Reading Plan & Practice

**Program:** Executive Fellowship (AI Law & Digital Sovereignty)
**Level:** Practitioner/Graduate — Ugandan Legal Context

---

## 1. Relevance: Why This Matters for Legal Practice

- Digital financial transactions (fintech, mobile money, micro-lending) rely on database log integrity as evidence
- Attorneys must distinguish ACID-compliant (SQL) vs BASE-compliant (NoSQL) systems to authenticate or challenge digital evidence
- Statutory frameworks (Evidence Act Cap. 6, Electronic Transactions Act Cap. 99) govern admissibility of database records
- Data warehouse audit trails are critical for regulatory compliance (DPA 2019, PDPO investigations)

---

## 2. Actionable Learning Outcomes

By end of Week 3, participants will be able to:

1. **Explain** the structural differences between SQL (relational) and NoSQL (non-relational) databases
2. **Compare** ACID vs BASE consistency models and their legal implications for data integrity
3. **Analyse** how database architecture affects admissibility of digital evidence under Ugandan law
4. **Evaluate** data retention and deletion practices against statutory requirements (ETA Cap. 99, Evidence Act Cap. 6)
5. **Assess** data warehouse architecture (e.g., BigQuery) for regulatory compliance and audit trail integrity

---

## 3. Reading Plan

### A. Foundational Technical Resources (Read First)

| Resource | Format | Location | Time |
|---|---|---|---|
| *How Computers Really Work* (Justice), Ch.9 — Files and Databases | Textbook PDF | `Resources/How Computers Really Work...pdf` | 90 min |
| SQL vs NoSQL Comprehensive Guide (2026) | Web article | `research/week3_sql_vs_nosql_guide.txt` | 60 min |
| BigQuery Architecture Overview (Google Cloud Blog) | Web article | `research/week3_bigquery_architecture.txt` | 45 min |

### B. Legal & Regulatory Resources (Essential)

| Resource | Format | Location | Time |
|---|---|---|---|
| Evidence Act Cap. 6 (full text) | PDF | `Resources/Evidence_Act_Cap_6.pdf` | 60 min |
| Electronic Transactions Act Cap. 99 | PDF | `Resources/Electronic Transactions Act Cap 99.pdf` | 45 min |
| KTA Advocates — Electronic Evidence Legal Alert | PDF | `Resources/KTA_Electronic_Evidence_Legal_Alert.pdf` | 30 min |

### C. Supplementary Resources

| Resource | Purpose |
|---|---|
| Electronic Transactions Regulations | Technical compliance details |
| Data Protection and Privacy Act 2019 | Data retention/deletion obligations |
| PDPO Guidelines | Regulatory expectations on data integrity |

---

## 4. Key Technical Concepts for Legal Context

### SQL (Relational Databases)
- Tables, schemas, primary/foreign keys, structured querying
- **ACID**: Atomicity, Consistency, Isolation, Durability
- Vertical scaling (bigger servers)
- Examples: PostgreSQL, MySQL
- **Legal significance**: Strong consistency guarantees — data is accurate at time of query; suitable for financial records

### NoSQL (Non-Relational Databases)
- Document stores, key-value pairs, graph databases, column-family
- **BASE**: Basically Available, Soft state, Eventual consistency
- Horizontal scaling (more servers)
- Examples: MongoDB, Redis, Cassandra
- **Legal significance**: Eventual consistency means data may be stale — critical for cross-examination on data accuracy

### Data Warehousing & Serverless Analytics
- Centralised storage, ETL pipelines
- Google BigQuery: serverless, decoupled storage/compute, Dremel execution engine
- **Legal significance**: Audit trail integrity, data retention configurability, access controls

---

## 5. Statutory Framework for Digital Evidence

### Evidence Act Cap. 6 — Key Sections
- **S.2**: Definition of "document" — includes electronic records
- **S.59-90**: Documentary evidence provisions (presumptions as to documents)
- **S.78**: Presumption as to genuineness of certified copies
- **S.91**: Exclusion of oral by documentary evidence

### Electronic Transactions Act Cap. 99 — Key Sections
- **S.5**: Writing requirement satisfied by electronic form
- **S.6**: Originality — electronic records qualify as originals
- **S.8**: Admissibility of electronic messages in proceedings
- **S.9**: Retention of electronic records — data integrity requirements

### Key Case Law
- *Commodity Export International Ltd v. MKM Trading Co. Ltd* (CACA 84/2008) — Courts must adapt to digital evidence
- *Amongin Jane Frances Akili v. Lucy Akello & Anor* — Definition of electronic evidence per Mutonyi J.
- *Sematimba Peter Simon & Anor v. Sekigozi Stephen* (EP 0008 & 0010/2016) — Evidence Act predates computers

---

## 6. Practice Task

### Problem Question (20 marks)

**Scenario:**
SwiftPay Ltd, a Kampala-based fintech, processes 500,000 mobile money transactions daily using:
- A **PostgreSQL database** for transaction records (account balances, transfer history)
- A **MongoDB database** for customer profiles and behaviour analytics
- **Google BigQuery** for monthly regulatory reporting to the Bank of Uganda

A customer, Ms. Nakato, claims her account was debited UGX 5,000,000 without authorisation on 15 March 2026. SwiftPay's system logs show the transaction was recorded in PostgreSQL at 14:32:15 with ACID compliance. However, the MongoDB customer profile still showed a "pending" status for 47 seconds before updating.

**Questions:**

1. **(5 marks)** Explain whether the PostgreSQL or MongoDB record is more reliable as evidence of the transaction. Refer to the ACID/BASE models in your answer.

2. **(5 marks)** Under the Electronic Transactions Act Cap. 99, what requirements must SwiftPay satisfy for the PostgreSQL log to be admissible as evidence? Cite specific sections.

3. **(5 marks)** If SwiftPay deletes the MongoDB customer profile data 90 days after account closure, is this compliant with data retention obligations under Ugandan law? Discuss.

4. **(5 marks)** Assess how BigQuery's serverless architecture (decoupled storage and compute) affects the integrity of audit trails for regulatory reporting to the Bank of Uganda.

---

## 7. Practice Task — Model Answer Guidance

### Q1: PostgreSQL vs MongoDB Reliability
| Factor | PostgreSQL (SQL) | MongoDB (NoSQL) |
|---|---|---|
| Consistency model | ACID — strong consistency | BASE — eventual consistency |
| Transaction state | Immediately consistent after commit | 47-second propagation delay |
| Data integrity | Enforced via constraints (FK, CHECK) | Application-level enforcement |
| **Evidential weight** | **Higher** — reflects ground truth at transaction time | Weaker — may show stale state |

Best answer: PostgreSQL log is more reliable. The 47-second delay in MongoDB demonstrates eventual consistency — a hallmark of BASE systems. Under Evidence Act S.2, both are "documents" but weight of evidence differs.

### Q2: ETA Requirements for Admissibility
- **S.5**: The electronic form satisfies writing requirements
- **S.6**: The PostgreSQL log qualifies as an "original" if it reliably reproduces the information
- **S.8**: The log is admissible if it is relevant (Evidence Act S.4) and authenticated
- **S.9**: SwiftPay must show the log was retained with full integrity (no alteration), accessible, and in its original format

### Q3: Data Retention Compliance
- DPA 2019 S.14: Personal data must not be kept longer than necessary
- ETA S.9: Records must be retained for legally prescribed periods
- BOU guidelines on financial records: Typically 5-7 years for transaction data
- **Answer**: 90-day deletion likely violates statutory retention periods for financial records. SwiftPay must retain customer data for at least the limitation period for claims (6 years under Limitation Act Cap. 80)

### Q4: BigQuery Audit Trail Integrity
- Serverless architecture separates storage (Colossus) from compute (Dremel)
- Columnar storage (Capacitor) ensures immutable data at rest
- Access controls via IAM, audit logs via Cloud Audit Logs
- **Strengths**: Immutable storage, fine-grained access control, built-in logging
- **Weaknesses**: Shared tenancy model; reliance on Google's infrastructure for chain of custody
- Regulatory recommendation: Enable Data Catalog, use VPC Service Controls, retain audit logs independently

---

## 8. Resources Checklist

| Resource | Status |
|---|---|
| Evidence Act Cap. 6 PDF | ✅ `Resources/Evidence_Act_Cap_6.pdf` |
| Electronic Transactions Act Cap. 99 | ✅ `Resources/Electronic Transactions Act Cap 99.pdf` |
| KTA Electronic Evidence Legal Alert | ✅ `Resources/KTA_Electronic_Evidence_Legal_Alert.pdf` |
| How Computers Really Work Ch.9 | ✅ `Resources/How Computers Really Work...pdf` |
| SQL vs NoSQL Guide (2026) | ✅ `research/week3_sql_vs_nosql_guide.txt` |
| BigQuery Architecture Overview | ✅ `research/week3_bigquery_architecture.txt` |

---

## 9. Delivery Notes

- **Session format**: 2-hour seminar + 1-hour practice session
- **Teaching method**: Case-based learning — use *Commodity Export International* and SwiftPay scenario
- **Privacy Compliance Agent**: Invoke for Q3-Q4 analysis (data retention, audit trail compliance)
- **Curriculum Agent**: Invoke for adapting reading plan to learner progress
