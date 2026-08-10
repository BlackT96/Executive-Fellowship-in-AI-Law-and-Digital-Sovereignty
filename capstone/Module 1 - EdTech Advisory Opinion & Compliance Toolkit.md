# TECHNOLOGY ADVISORY OPINION & COMPLIANCE-BY-DESIGN TOOLKIT

## EdTech Platform Deployment in Uganda

**Prepared for:** [Client] — EdTech Startup
**Jurisdiction:** Republic of Uganda
**Date:** July 2026
**Classification:** Privileged & Confidential — Legal Advice

---

## EXECUTIVE SUMMARY

This opinion addresses the full-spectrum legal and technical compliance requirements for an EdTech platform operating in Uganda's pre-primary, primary, and post-primary education sectors. The analysis covers hardware/software liability exposure, network security obligations, database data classification, cloud architecture, and government integration — with compliance embedded into every design decision from inception.

**Compliance posture:** The EdTech sector in Uganda operates at the intersection of education law, child protection law, data protection law, cybercrime legislation, and government IT standards. Non-compliance carries criminal penalties (CMA Amendment 2022: up to 7 years imprisonment for unlawful transmission of child information), regulatory fines (DPA: up to UGX 2 billion or 2% of gross income), and reputational risk.

**Key statutory framework:**

| Statute | Relevance |
|---------|-----------|
| Education Act Cap 247 | Registration, curriculum standards, teacher licensing, institutional oversight |
| Children Act Cap 62 | Best interests principle, child welfare, parental responsibility |
| Data Protection and Privacy Act Cap 97 | Parental consent for children's data, data minimisation, security measures |
| Computer Misuse Act Cap 96 (as amended 2022) | Unauthorised access offences, child online protection |
| NITA-U Act Cap 200 | IT standards, e-government regulation, national databank |
| Constitution of Uganda 1995 Art. 27, 34 | Right to privacy, children's right to education |

---

## PART A — SYSTEM ARCHITECTURE & LIABILITY EXPOSURE
### (Module 1, Week 1: Computer Systems — Hardware, Software, OS, Networks)

### A.1 The Abstraction Layer Problem in EdTech

Every EdTech platform rests on a technology stack of layered abstractions. A system failure — whether a crashed learning management system, corrupted student records, or an unauthorised data access — can originate at any layer. Liability attaches differently depending on which layer fails.

```
User Interface (Web/Mobile App)
    ↓
Application Layer (Learning modules, assessments, grading engine)
    ↓
Operating System (Windows Server / Linux distribution)
    ↓
Virtualisation Layer (VMware / Hyper-V / Docker containers)
    ↓
Hardware (Servers, storage arrays, network equipment)
```

**Legal significance:** Under the Sale of Goods and Supply of Services Act Cap 79, Sections 40-44, a hardware defect (faulty server) triggers liability against the hardware vendor. An OS misconfiguration shifts liability to the system integrator or IT support provider. A software bug in the learning application engages the software developer's liability. The EdTech operator must maintain clear contractual chains with each layer provider and documented evidence to isolate the failure origin.

### A.2 Liability Mapping for EdTech Components

| Component | Failure Mode | Potential Defendant | Legal Basis |
|-----------|-------------|---------------------|-------------|
| Student tablet hardware | Screen failure, battery defect | Hardware manufacturer, importer | Sale of Goods Act Cap 79, s.40-42 |
| School server (refurbished) | Data loss during peak usage | Hardware vendor | Sale of Goods Act, implied fitness |
| Linux OS on server | Privilege escalation breach | System integrator, IT support contractor | Contract for services, negligence |
| Learning management software | Grading algorithm error | Software developer | Contract, Sale of Goods (digital services), s.43-44 |
| Network switch/routers | Packet loss during exams | Network equipment vendor | Sale of Goods Act |
| Cloud infrastructure | Service outage | Cloud service provider | SLA, contract, DPA s.20-21 (security) |

### A.3 Compliance-by-Design: Architecture Requirements

**CBD-A1:** Maintain a hardware and software asset register identifying every component, its vendor, support contract, and warranty status. This register is the first document a regulator or court will request following a system failure or data breach.

**CBD-A2:** Implement segregation of duties in system architecture. No single layer should have unchecked access to student data. The database layer must enforce access controls independently of the application layer.

**CBD-A3:** Design the system to operate on both new and refurbished hardware (common in Ugandan schools). Include hardware compatibility testing and documented failure thresholds.

**CBD-A4:** Maintain kernel-level audit logs (Linux auditd / Windows Event Logging) to distinguish between OS-level breaches and application-level errors. These logs are critical evidence under CMA Cap 96 s.12 (unauthorised access) and s.14 (access with intent).

**CBD-A5:** Document the abstraction layer map of your specific deployment for every school. This map determines who gets sued when something fails.

---

## PART B — NETWORK ARCHITECTURE & SECURITY COMPLIANCE
### (Module 1, Week 2: Internet Architecture — TCP/IP, DNS, HTTP/HTTPS)

### B.1 Network Stack in the EdTech Context

An EdTech platform connects students, teachers, parents, and school administrators across diverse network environments — from high-speed fibre in urban Kampala schools to intermittent mobile data in rural areas. Each network layer presents distinct legal risk.

### B.2 Computer Misuse Act Obligations

The Computer Misuse Act Cap 96 (as amended 2022) creates criminal liability for:

- **Section 12:** Unauthorised access to a computer program or data. In EdTech, this covers any student, teacher, or third party accessing another user's account, grades, or personal data without authorisation.
- **Section 14:** Access with intent to commit a further offence (e.g., accessing grade records to alter marks).
- **CMA Amendment 2022 (Child Online Protection):** Creates a specific offence of sending, sharing, or transmitting any information online about or relating to a child without lawful authorisation, parental consent, or where it is not in the best interest of the child. Penalty: up to 7 years imprisonment or UGX 15,000,000, or both.

### B.3 Network-Level Risks & Mitigations

| Risk | Technical Layer | CMA Offence | Mitigation |
|------|----------------|-------------|------------|
| Student grade interception | HTTP (unencrypted) | s.12 — unauthorised access | Enforce HTTPS/TLS 1.3 across all connections |
| DNS spoofing to phishing site | DNS resolution | s.14 — access with intent | DNSSEC implementation + DNS filtering |
| Session hijacking | Application layer | s.12, CMA child offence | Short session timeouts + device fingerprinting |
| Man-in-the-middle on school WiFi | Network layer | s.12, s.14 | Certificate pinning + EAP-TLS for WiFi |
| SQL injection via web forms | Application layer | s.12, CMA child offence | WAF + prepared statements + input validation |
| DDoS during exam period | Network/Transport | s.14 (if with intent) | DDoS protection service + BCP 38 |

### B.4 Compliance-by-Design: Network Security

**CBD-B1:** All EdTech communications must use HTTPS with TLS 1.3 minimum. HTTP is unacceptable for any platform handling children's data.

**CBD-B2:** Implement network segmentation. Student data traffic must be isolated from administrative traffic. Guest WiFi (parents, visitors) must be on a separate VLAN with no access to the EdTech platform.

**CBD-B3:** Schools in areas with unreliable internet must deploy local caching and store-and-forward synchronisation. The cached data must be encrypted at rest and automatically purged on a schedule compliant with DPA s.14 (minimality) and s.18 (retention).

**CBD-B4:** Maintain network access logs for a minimum of 12 months (CMA s.12 investigation standard). Logs must record source IP, destination, timestamp, and user identifier.

**CBD-B5:** Implement rate limiting and anomaly detection on login endpoints. CMA s.14 requires proving intent — anomalous patterns (e.g., 100 login attempts in 2 minutes) are critical evidence.

**CBD-B6:** Parental consent for child online safety: Under the CMA Amendment 2022, any transmission of child information requires parental consent. The platform must obtain and log this consent before any child data is transmitted over the network.

---

## PART C — DATABASE ARCHITECTURE & DATA CLASSIFICATION
### (Module 1, Week 3: Databases — SQL, NoSQL, Data Warehouses)

### C.1 The EdTech Data Universe

An EdTech platform collects, processes, and stores an unusually broad range of data types — each with distinct legal obligations:

| Data Category | Examples | Legal Classification | Governing Law |
|--------------|----------|---------------------|---------------|
| Student identity | Name, date of birth, National ID/NIN, photo | Personal data (DPA s.2) | DPA 2019 |
| Academic records | Grades, assessments, progression | Personal data | DPA 2019 + Education Act Cap 247 |
| Special educational needs | Disability status, learning support plans | Special personal data (DPA s.9 — health) | DPA s.9 |
| Behavioural data | Discipline records, attendance | Personal data | Children Act Cap 62 s.4 |
| Biometric data (if used) | Fingerprint/facial recognition for attendance | Special personal data | DPA s.9 |
| Parent/guardian data | Name, contact, NIN | Personal data | DPA 2019 |
| Teacher data | Qualifications, NIN, payroll | Personal data | DPA 2019 + Education Act (teacher registration) |
| Payment data | School fees, transaction history | Special personal data (financial) | DPA s.9 + National Payment Systems Act |

### C.2 Children's Data — The Critical Distinction

Under DPA 2019 Section 8:

> *"A person shall not collect or process personal data relating to a child unless the collection or processing thereof is — (a) carried out with the prior consent of the parent or guardian or any other person having authority to make decisions on behalf of the child; (b) necessary to comply with the law; or (c) for research or statistical purposes."*

**Practical impact for EdTech design:**

1. **Parental consent must be obtained before a child account is created.** The consent mechanism must be verifiable (electronic signature, SMS OTP to parent's registered mobile, or in-person consent recorded).
2. **Consent cannot be bundled.** A parent must consent separately to: (a) account creation, (b) academic data processing, (c) behavioural data processing, (d) communications/messaging, (e) data sharing with third parties.
3. **Children's data is not "special personal data" under s.9** (that term covers religion, health, politics, financial information). However, **any data about a child is effectively high-risk** because of the enhanced protections under s.8 and the CMA Amendment 2022. The practical effect is the same: treat all children's data as requiring the highest protection tier.
4. **Children have data subject rights.** Upon turning 18 (or earlier if deemed mature), the former child can exercise DPA s.24 (access) and s.25 (prevent processing) rights — including requesting deletion of their childhood records.

### C.3 Education Act Cap 247 — Record-Keeping Obligations

The Education Act Cap 247 imposes specific record-keeping requirements on education institutions. Section 32 (private schools) requires:

- Maintaining a register of students with prescribed particulars
- Maintaining academic records
- Submitting data to the Ministry of Education through the Education Management Information System (EMIS)
- Compliance with DES (Directorate of Education Standards) inspection requirements

**Compliance-by-Design CBD-C1:** The database schema must include all EMIS-required fields from the outset. The platform must be capable of generating EMIS-compliant reports directly from the database.

### C.4 Children Act Cap 62 — Welfare Assessments

The Children Act Cap 62 Section 3 establishes the **welfare principle**: the child's best interests are paramount in all decisions concerning the child. Section 4 grants every child the right to non-discrimination, parental care, education, and health. Section 5 requires that a child's views be given due weight.

**CBD-C2:** The platform must record welfare-related flags (attendance patterns, behavioural incidents, safeguarding concerns) in a structured format accessible to designated safeguarding officers. These records must be preservable for potential Children Act proceedings.

### C.5 Compliance-by-Design: Database Architecture

**CBD-C3 (Data Classification Schema):** Design the database with field-level classification tags:

```sql
CREATE TABLE student_record (
  student_id INTEGER PRIMARY KEY,
  full_name VARCHAR(100) NOT NULL,           -- CLASSIFICATION: PERSONAL
  date_of_birth DATE NOT NULL,                -- CLASSIFICATION: PERSONAL (CHILD)
  national_id VARCHAR(20),                    -- CLASSIFICATION: PERSONAL (SENSITIVE)
  religion VARCHAR(50),                       -- CLASSIFICATION: SPECIAL (s.9)
  disability_status VARCHAR(200),             -- CLASSIFICATION: SPECIAL (s.9 — health)
  fee_balance DECIMAL(10,2),                  -- CLASSIFICATION: SPECIAL (s.9 — financial)
  CONSTRAINT classification_audit CHECK (...)
);
```

**CBD-C4 (Access Control by Classification):** Implement database-level access controls that enforce:

- Teachers: access to academic + behavioural data only
- Administrators: access to identity + fee data only
- Counsellors: access to special needs + welfare data only
- Parents: access to their own child's data only (via application layer)
- No single role has access to all classifications

**CBD-C5 (Data Minimisation — DPA s.14):** The database schema must collect only data that is strictly necessary for the educational purpose. Do not pre-collect fields "just in case." Examples of excessive collection to avoid: religious affiliation (unless the school is a faith-based institution), political opinions, detailed family financial data beyond fee management.

**CBD-C6 (Retention Schedules — DPA s.18):** Implement automated data purging:
- Student academic records: retain for duration of enrolment + 5 years (Education Act requirement)
- Behavioural/welfare records: retain for duration of enrolment + 3 years
- Biometric data (if used): delete immediately upon student departure
- Communications history: retain for 2 years
- Audit logs: retain for 12 months (minimum)

**CBD-C7 (Right to Erasure — DPA s.25):** Design the database to support soft-delete + hard-delete workflows. Upon a valid erasure request from a data subject (or parent), the system must be capable of irreversibly deleting the individual's personal data across all tables, including backups (within reasonable technical limits).

---

## PART D — CLOUD ARCHITECTURE, API INTEGRATION & GOVERNMENT DATA ACCESS
### (Module 1, Week 4: APIs, Cloud Computing & SDLC)

### D.1 Cloud Deployment Models for EdTech

| Model | Description | Compliance Assessment |
|-------|-------------|----------------------|
| **Government Cloud (NITA-U National Data Centre)** | Hosting on government infrastructure | HIGHEST — Data stays within Uganda. Compliant with DPA s.19 (transfer outside Uganda) as data never leaves. Subject to NITA-U security standards and audits. |
| **Local Private Cloud** (Uganda-based data centre) | Hosting with a private provider (e.g., Raxio, Africa Data Centres) | HIGH — Data stays in Uganda. Must enter DPA with provider ensuring DPA s.20-21 compliance. |
| **Regional Cloud** (East Africa — Kenya, Rwanda) | Hosting in neighbouring country | MODERATE — Cross-border transfer under DPA s.19. Requires adequacy assessment or consent. Under DPA s.19, the recipient country must have "adequate measures at least equivalent to" Uganda DPA. Kenya DPA 2019 is broadly equivalent. |
| **International Cloud** (EU, US, UK, Asia) | Hosting outside Africa | RISKY — DPA s.19 requires consent of each data subject (parent) OR adequacy finding. As of July 2026, the PDPO has not published the list of adequate countries under Regulation 30(4). Practical risk: each parent must individually consent to offshoring. |

**Recommendation:** For an EdTech platform handling children's data, the Government Cloud (NITA-U National Data Centre) is the safest deployment option. It avoids cross-border transfer issues, aligns with data localisation expectations, and demonstrates the highest standard of care to regulators, parents, and schools.

### D.2 NITA-U Compliance Framework

Under the NITA-U Act Cap 200, Section 5, NITA-U has the power to:

- (c) Coordinate, supervise, and monitor IT utilisation in public and private sectors
- (d) Regulate and enforce standards for IT hardware and software procurement in Government
- (e) Create and manage the national databank
- (i) Prescribe IT standards and regulate their use
- (m) Provide guidance on infrastructure for information sharing by Government and stakeholders

**For an EdTech startup seeking to integrate with government systems, the following NITA-U requirements apply:**

| Requirement | Description | Compliance Action |
|-------------|-------------|-------------------|
| IT Standards Compliance | System must comply with NITA-U prescribed IT standards (hardware, software, security) | Conduct NITA-U compliance gap assessment before deployment |
| Registration as Data Processor/Controller | Must register with PDPO (under NITA-U) under Regulation 13 | File registration within 30 days of commencing processing |
| Data Centre Standards | If using Government Cloud, must comply with NITA-U Data Centre standards | Review National Data Centre hosting agreement and SLA |
| E-Government Interoperability Framework (e-GIF) | Systems must comply with government interoperability standards | Design APIs to e-GIF specifications |
| National Information Security Policy (NISP) | Must implement mandatory minimum security controls | Conduct NISP gap analysis, implement controls |

### D.3 UGHUB Integration — Accessing Government Data

The Uganda Government Hub (UGHUB), operated by NITA-U, is the government's data integration platform with over 146 entities onboarded (68 government, 78 private). Key capabilities:

- **API Management:** Create, share, and consume APIs for real-time data interactions
- **Identity and Access Management (IAM):** Secure authentication and authorisation
- **Semantic and Systems Catalogue:** Discover and classify government data services
- **Reporting and Analytics:** Dashboards and insights
- **Hosting:** Entirely within Government of Uganda Data Centre

**EdTech use cases for UGHUB integration:**

| Government Data | UGHUB Source | EdTech Application |
|----------------|--------------|-------------------|
| National ID / NIN verification | NIRA (National Identification and Registration Authority) | Verify student/parent identity during enrolment |
| Student NIN-to-school mapping | Ministry of Education EMIS | Verify school registration status |
| Teacher registration status | Ministry of Education Teacher Register | Verify teacher qualifications for platform access |
| Birth registration data | UBOS/URA/MOH | Verify student age for grade placement |
| Special needs register | Ministry of Gender, Labour and Social Development | Identify students requiring learning support |

### D.4 Compliance-by-Design: API & Integration Architecture

**CBD-D1 (API Security):** All UGHUB-bound API calls must use:
- Mutual TLS (mTLS) authentication
- OAuth 2.0 / OpenID Connect for authorisation
- API keys with rotation policies (maximum 90-day rotation)
- Rate limiting to prevent data scraping
- Payload encryption beyond TLS (JSON Web Encryption)

**CBD-D2 (Data Sharing Agreements):** Before integrating with any government data source via UGHUB, the EdTech startup must execute a Data Sharing Agreement with the source MDA. This agreement must specify:
- Purpose limitation (only for education delivery)
- Data categories shared
- Retention and deletion schedules
- Security measures
- Audit rights for the MDA
- Breach notification obligations

**CBD-D3 (DPA Cross-Border — DPA s.19):** If the EdTech platform uses international cloud services (e.g., AWS in South Africa, Azure in Europe), data from UGHUB integration must not flow outside Uganda unless:
1. The receiving country has been declared adequate by the PDPO (not yet published as of July 2026), OR
2. Each parent/caregiver has given explicit consent to cross-border transfer of their child's data

**CBD-D4 (API Gateway as Compliance Boundary):** Design an API gateway that functions as a compliance enforcement point:
- Validates that only consented data is transmitted
- Logs every API call (who, what, when, why) for audit trail
- Blocks data sharing with unregistered third parties
- Enforces data minimisation (request only fields actually needed)

### D.5 SLA Requirements for EdTech Cloud

Any cloud service agreement for EdTech must include:

| SLA Element | Required Standard | Legal Basis |
|-------------|-------------------|-------------|
| Uptime guarantee | 99.5% minimum (core hours) | Contractual; Education Act continuity obligation |
| Data backup frequency | Daily full + hourly incremental | DPA s.20 (integrity of data) |
| Disaster recovery time | RTO: 4 hours, RPO: 15 minutes | DPA s.20-21 |
| Breach notification | Within 24 hours of discovery | DPA s.23 (notification of breaches) — note this is stricter than GDPR's 72 hours |
| Data localisation commitment | All data stored in Uganda | DPA s.19 |
| Right to audit | Quarterly technical audits | DPA s.21 (security measures by processor) |
| Sub-processor approval | Prior written consent required | DPA s.6 (DPO), implied from s.20-21 |

**CBD-D5 (SDLC Compliance Gates):** Embed these compliance checkpoints into the software development lifecycle:

```
Requirement Phase → Privacy Impact Assessment (PIA)
Design Phase      → Architecture review against CBD-A1 through CBD-D4
Development Phase → Static analysis for data classification tags
Testing Phase     → Penetration testing + data flow verification
Deployment Phase  → NITA-U compliance checklist sign-off
Operations Phase  → Monthly compliance monitoring + quarterly audit
```

---

## PART E — COMPLIANCE REGISTER (MASTER OBLIGATIONS TABLE)

| # | Obligation | Statute | Section | CBD Ref | Verification Method | Frequency |
|---|-----------|---------|---------|---------|--------------------|-----------|
| 1 | Register with PDPO as data controller | DPA 2019 | Reg 13 | D.2 | Registration certificate | One-time |
| 2 | Obtain parental consent for child data | DPA 2019 | s.8 | C.2 | Consent log audit | Per enrolment |
| 3 | Obtain parental consent for online transmission of child info | CMA 2022 (Amendment) | s.12A | B.6 | Consent log audit | Per transmission |
| 4 | Data minimisation — collect only necessary fields | DPA 2019 | s.14 | C.5 | Database schema review | Quarterly |
| 5 | Implement security measures (technical + organisational) | DPA 2019 | s.20-21 | B.1-B.5 | Penetration test report | Annual |
| 6 | Maintain audit logs (12 months minimum) | CMA Cap 96 | s.12 | A.4, B.4 | Log retention verification | Monthly |
| 7 | Notify PDPO within 24 hours of breach | DPA 2019 | s.23 | D.5 | Incident response drill | Quarterly |
| 8 | Register with Ministry of Education (if applicable) | Education Act Cap 247 | s.32 | C.3 | Registration certificate | One-time |
| 9 | Submit EMIS-compliant data to Ministry | Education Act Cap 247 | s.5, s.32 | C.3 | EMIS report generation | Per term |
| 10 | Maintain student register with prescribed particulars | Education Act Cap 247 | s.32 | C.3 | Register audit | Annually |
| 11 | Comply with NITA-U IT standards | NITA-U Act Cap 200 | s.5 | D.2 | Compliance audit | Annually |
| 12 | Sign Data Sharing Agreement for government data | NITA-U Act / Policy | D.2 | D.2 | Executed DSA | Per integration |
| 13 | Register as UGHUB entity | NITA-U / UGHUB policy | D.3 | D.3 | UGHUB registration | One-time |
| 14 | Implement API security (mTLS, OAuth, rate limiting) | DPA s.20, NISP | D.4 | D.4 | Security architecture review | Per API release |
| 15 | Ensure best interests of child in all platform decisions | Children Act Cap 62 | s.3 | C.4 | Welfare impact assessment | Annually |
| 16 | Respect child's right to express views (age-appropriate) | Children Act Cap 62 | s.5 | C.4 | UI review for child participation | Per feature |
| 17 | Data retention and deletion policy enforced | DPA 2019 | s.18 | C.6 | Automated purge verification | Monthly |
| 18 | Right of access to personal data (30-day response) | DPA 2019 | s.24 | C.7 | DSR response time tracking | Per request |
| 19 | Right to prevent processing / erasure | DPA 2019 | s.25 | C.7 | DSR response time tracking | Per request |
| 20 | Cross-border data transfer compliant | DPA 2019 | s.19 | D.1, D.3 | Adequacy assessment / consent log | Per transfer |
| 21 | Data Processing Agreement with all processors | DPA 2019 | s.21 | D.5 | DPA register | Per vendor |
| 22 | Hardware/software asset register maintained | Sale of Goods Act Cap 79, CMA | | A.3 | Asset register audit | Quarterly |
| 23 | Abstraction layer liability map documented | Common law / Contract | | A.5 | Architecture review | Per deployment |
| 24 | Teacher qualification verification for platform access | Education Act Cap 247 | s.11 | D.3 | Verification via UGHUB | Per teacher account |

---

## PART F — TECHNICAL APPENDIX

### F.1 Reference Architecture (Compliant by Design)

```
┌─────────────────────────────────────────────────────────────────┐
│                        PARENTS (Mobile App / Web)               │
│  Consent management │ Fee payment │ Progress reports            │
└───────────────────────────┬─────────────────────────────────────┘
                            │ HTTPS (TLS 1.3)
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│                    API GATEWAY (Compliance Boundary)             │
│  ┌─────────┐  ┌──────────┐  ┌──────────┐  ┌────────────────┐   │
│  │ mTLS    │  │ OAuth    │  │ Rate     │  │ Audit Logger   │   │
│  │ Auth    │  │ 2.0      │  │ Limiter  │  │ (Every call)   │   │
│  └─────────┘  └──────────┘  └──────────┘  └────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
                            │
         ┌──────────────────┼──────────────────┐
         ▼                  ▼                  ▼
┌────────────────┐  ┌────────────────┐  ┌────────────────┐
│ APPLICATION    │  │ UGHUB         │  │ THIRD PARTY    │
│ LAYER          │  │ INTEGRATION   │  │ INTEGRATIONS   │
│ ┌──────────┐   │  │ ┌──────────┐  │  │ ┌──────────┐   │
│ │ LMS      │   │  │ │ NIRA ID  │  │  │ │ Payment  │   │
│ │ Grading  │   │  │ │ EMIS     │  │  │ │ Gateway  │   │
│ │ Comms    │   │  │ │ Teacher  │  │  │ │ SMS      │   │
│ │ Welfare  │   │  │ │ Register │  │  │ │ Provider │   │
│ └──────────┘   │  │ └──────────┘  │  │ └──────────┘   │
└────────────────┘  └────────────────┘  └────────────────┘
         │                  │                  │
         └──────────────────┼──────────────────┘
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│                     DATABASE LAYER                              │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────────┐    │
│  │ Student  │  │ Academic │  │ Welfare  │  │ Audit Logs   │    │
│  │ Records  │  │ Records  │  │ Records  │  │ (12 months)  │    │
│  │ (s.8)    │  │ (s.14)   │  │ (s.9)    │  │ (s.12 CMA)   │    │
│  └──────────┘  └──────────┘  └──────────┘  └──────────────┘    │
│                                                                  │
│  Access control by classification + field-level encryption      │
└─────────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│                     HOSTING LAYER                               │
│  Option 1: NITA-U Government Cloud (recommended)                │
│  Option 2: Uganda-based private data centre                     │
│  Option 3: Regional cloud (with DPA s.19 adequacy assessment)   │
│                                                                  │
│  All options: Daily backup + 4hr RTO + 15min RPO               │
└─────────────────────────────────────────────────────────────────┘
```

### F.2 Data Flow: Consent Lifecycle

```
Student Enrolment Request
    │
    ▼
Parent Identity Verified (via UGHUB/NIRA)
    │
    ▼
Parent Presented with Tiered Consent Options:
  ├── □ Basic: Account + Academic records
  ├── □ Behavioural: Attendance + discipline
  ├── □ Communications: In-app messaging
  ├── □ Third-party: Learning tools integrations
  └── □ Cross-border: (if applicable, DPA s.19)
    │
    ▼
Parent Consent Recorded (Timestamp + IP + Method)
    │
    ▼
Student Account Created (with consent boundary flags)
    │
    ▼
Consent Withdrawable at any time (DPA s.25)
    │
    ▼
Withdrawal triggers automated data minimisation
```

### F.3 Key Statutory Citations

| Citation | Text |
|----------|------|
| DPA 2019 s.8 | "A person shall not collect or process personal data relating to a child unless the collection or processing thereof is carried out with the prior consent of the parent or guardian..." |
| DPA 2019 s.14 | "A data controller or data processor shall collect such personal data as is necessary for the specific purpose..." (data minimisation) |
| DPA 2019 s.19 | "Where a data processor or data controller based in Uganda processes or stores personal data outside Uganda, the data processor or data controller shall ensure that the country in which the data is processed or stored has adequate measures..." |
| DPA 2019 s.23 | "Where a data controller or data processor reasonably believes that a data security breach has occurred, the data controller or data processor shall immediately notify the Personal Data Protection Office." |
| CMA 2022 Amendment | "A person who sends, shares or transmits any information online about or relating to a child without lawful authorisation or parental consent or where it is not in the best interest of the child commits an offence." |
| Education Act Cap 247 s.2 | Objects: quality control, stakeholder partnership, UPE/UPPET implementation |
| Children Act Cap 62 s.3 | "The welfare of the child shall be the paramount consideration in all matters concerning the child." |
| NITA-U Act Cap 200 s.5 | Functions: standards regulation, national databank, coordination of IT in public and private sectors |

---

## CONCLUSION

This opinion has mapped the full compliance landscape for an EdTech platform operating in Uganda, embedding 23 discrete compliance requirements across the four pillars of Module 1 (Digital Technology Fundamentals).

The critical compliance message for EdTech in Uganda: **children's data is the highest-risk category of personal data** because it sits at the intersection of the DPA 2019 (s.8 parental consent), the CMA Amendment 2022 (criminal offence for unauthorised child information transmission), and the Children Act Cap 62 (best interests paramountcy). The convergence of these three regimes means that a single compliance failure involving a child's data can result simultaneously in regulatory fines (DPA), criminal prosecution (CMA), and a Children Act welfare proceeding.

The compliance-by-design framework in Parts A-D ensures that every technical decision — from database schema design to API architecture to cloud provider selection — is legally defensible from day one.

---

*This opinion is provided for the exclusive use of the addressed client. It does not constitute legal advice for any specific matter. A qualified Ugandan lawyer should be engaged for transaction-specific advice. Statutory provisions cited are as at July 2026 and are subject to amendment.*

*Prepared using the Module 1 Digital Technology Fundamentals capstone framework — integrating Week 1 (Computer Systems), Week 2 (Internet Architecture), Week 3 (Databases), and Week 4 (APIs, Cloud Computing & SDLC) into a single compliance artifact.*
