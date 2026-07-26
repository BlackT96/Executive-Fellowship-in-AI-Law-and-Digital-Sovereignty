# Data Processing Agreement (DPA) Agent

## Purpose

The DPA Agent drafts, reviews, and customises Data Processing Agreements and associated schedules, with specific competency in cross-border transfer mechanisms, Standard Contractual Clauses (SCCs), and data governance clauses. It ensures compliance with Uganda's Data Protection and Privacy Act 2019 (DPPA), the Kenyan Data Protection Act 2019, the Tanzanian Personal Data Protection Act 2022, the Rwandan Law Relating to Data Protection and Privacy 2021, and the EU General Data Protection Regulation (GDPR) for comparative alignment. The agent streamlines the DPA workflow for technology companies, SaaS providers, cloud service providers, and enterprises that process personal data across East Africa.

## Competencies

1. **DPA Drafting** — Generate complete data processing agreements that allocate roles (controller, processor, joint controller), define processing instructions, and set data security obligations.
2. **Cross-Border Transfer Documentation** — Draft intra-group transfer agreements, assess adequate jurisdiction designations, and generate SCCs compliant with DPPA 2019 Section 14 and GDPR Article 46.
3. **SCC Generation** — Produce Uganda-specific SCCs modelled on the DPPA Regulations 2021 (Third Schedule) and, for comparative purposes, the EU 2021/914 SCC modules.
4. **Data Governance Clauses** — Draft data retention policies, data minimisation clauses, data breach notification protocols, data subject rights procedures (access, rectification, erasure, portability), and privacy-by-design obligations.
5. **Processor Sub-Processor Management** — Draft sub-processor engagement terms, authorisation procedures (general vs specific), and liability cascade for sub-processor acts.
6. **Data Protection Impact Assessment (DPIA) Support** — Generate DPIA frameworks and trigger identification clauses to help parties determine when a DPIA is mandatory under Section 17 of the DPPA.
7. **Record of Processing Activities (ROPA) Generation** — Produce ROPA templates that satisfy Section 36 of the DPPA Regulations 2021 and Article 30 GDPR requirements.
8. **Data Incident Response Clauses** — Draft notification timelines, escalation procedures, and remediation obligations aligned with Section 32 of the DPPA (72-hour notification benchmark).

## Inputs

| Input Field | Type | Required | Description |
|---|---|---|---|
| `controller_name` | String | Yes | Full legal name of the data controller |
| `controller_registration` | String | No | Company registration number of controller |
| `controller_contact_email` | String | Yes | DPO or contact email for controller |
| `processor_name` | String | Yes | Full legal name of the data processor |
| `processor_registration` | String | No | Company registration number of processor |
| `processor_contact_email` | String | Yes | DPO or contact email for processor |
| `governing_law` | Enum | Yes | uganda / kenya / tanzania / rwanda / eu_gdpr / other |
| `dispute_forum` | Enum | Yes | court / arbitration / regulatory_authority |
| `jurisdiction_regulator` | String | Yes | e.g. Personal Data Protection Office (Uganda), ODPC (Kenya) |
| `processing_purpose` | Text | Yes | Detailed description of the processing purposes |
| `processing_scope` | Enum | Yes | full / limited / joint_processing |
| `data_categories` | Array[String] | Yes | e.g. ["personal_identifiers", "health_data", "financial_data", "biometric_data", "location_data", "criminal_records_data"] |
| `data_subject_categories` | Array[String] | Yes | e.g. ["employees", "customers", "patients", "students", "website_users"] |
| `special_category_data` | Boolean | Yes | Whether processing includes special category data (sensitive data) |
| `special_categories` | Array[String] | No | e.g. ["health", "biometric", "genetic", "political_opinion", "religion"] |
| `transfer_countries` | Array[String] | Yes | Countries to which data will be transferred |
| `transfer_mechanism` | Enum | Conditional | scc / adequacy_decision / binding_corporate_rules / consent / contractual_necessity |
| `scc_type` | Enum | No | uganda_dppa / eu_2021_914 / kenya_dpa |
| `sub_processors` | Array[Object] | No | List of sub-processors: [{name, country, processing_description}] |
| `sub_processor_authorisation` | Enum | No | general_written / specific_prior / both |
| `retention_period_months` | Integer | Yes | Standard retention period in months (default: 36) |
| `security_measures` | Array[String] | Yes | e.g. ["encryption_at_rest", "encryption_in_transit", "access_controls", "pseudonymisation", "audit_logs", "penetration_testing"] |
| `breach_notification_hours` | Integer | No | Notification timeline (default: 72 hours) |
| `breach_notification_parties` | Enum | No | controller_only / regulator_only / both |
| `dpo_name` | String | No | Data Protection Officer name (if appointed) |
| `dpo_email` | String | No | Data Protection Officer email |
| `include_dpia` | Boolean | No | Whether a DPIA is required (default: true if special_category_data is true) |
| `include_roPa` | Boolean | No | Whether ROPA must be maintained (default: true) |
| `processor_fees` | Number | No | Annual processing fees (if any) |
| `termination_deletion_period_days` | Integer | No | Days to delete/return data on termination (default: 30) |
| `governing_law_override` | String | No | Override clause for governing law if different from primary agreement |
| `special_terms` | Text | No | Additional bespoke data processing terms |

## Workflow

```
Step 1: Classify Processing Relationship
        └─ Determine controller/processor/joint controller roles
        └─ Identify whether special category data is involved
        └─ Assess if a DPA is mandatory (it always is if processor processes on behalf of controller)
        │
Step 2: Map Data Flows
        └─ List data categories, data subjects, processing purposes
        └─ Identify all countries involved in processing
        └─ Flag any restricted transfers requiring a transfer mechanism
        │
Step 3: Select Transfer Mechanism
        └─ If adequacy decision exists (e.g. Uganda's list of adequate jurisdictions under DPPA Section 14(2)), use adequacy route
        └─ Else if SCCs required: select Uganda DPPA SCCs or EU 2021/914 SCCs based on governing law
        └─ Else if Binding Corporate Rules (BCRs): draft intra-group data transfer agreement
        └─ Else fall back to data subject consent or contractual necessity exemption
        │
Step 4: Draft Core DPA
        └─ Definitions and interpretation
        └─ Processing instructions and appendices
        └─ Data subject rights procedures
        └─ Data breach management and notification
        └─ Audit and inspection rights
        │
Step 5: Add Security & Governance Clauses
        └─ Technical and organisational measures schedule
        └─ Data retention and deletion schedules
        └─ Privacy by design and default obligations
        └─ Sub-processor management
        │
Step 6: Insert Jurisdictional Provisions
        └─ For Uganda: reference DPPA 2019, the Data Protection and Privacy Regulations 2021, and the Personal Data Protection Office
        └─ For Kenya: reference Data Protection Act 2019, ODPC guidelines, and the Data Protection (General) Regulations 2021
        └─ For EU GDPR: reference Articles 28-32, 44-49, and relevant EDPB guidelines
        └─ Ensure regulator details and notification timelines are correct per jurisdiction
        │
Step 7: Generate Schedules
        └─ Schedule 1: List of Processing Activities
        └─ Schedule 2: Technical and Organisational Measures
        └─ Schedule 3: Sub-Processors
        └─ Schedule 4: Cross-Border Transfer Mechanism (SCCs or adequacy assessment)
        └─ Schedule 5: Data Retention Schedule
        │
Step 8: Quality Check and Output
        └─ Cross-reference all defined terms against the body
        └─ Flag any gaps, inconsistencies, or regulatory risks
        └─ Render as structured markdown with schedules
```

## Prompt Template

```
You are a data protection and privacy specialist with expertise in African data protection laws, particularly Uganda's Data Protection and Privacy Act 2019, the Kenyan Data Protection Act 2019, and the EU GDPR for comparative purposes.

Draft a Data Processing Agreement between:

- Controller: [controller_name] ([controller_registration])
  Contact: [controller_contact_email]
  DPO: [dpo_name] / [dpo_email]

- Processor: [processor_name] ([processor_registration])
  Contact: [processor_contact_email]
  DPO: [dpo_name] / [dpo_email]

Governing Law: [governing_law]
Regulator: [jurisdiction_regulator]

Processing Purpose: [processing_purpose]
Processing Scope: [processing_scope]
Data Categories: [data_categories]
Data Subject Categories: [data_subject_categories]
Special Category Data: [special_category_data] ([special_categories])

Cross-Border Transfers:
  Transfer Countries: [transfer_countries]
  Transfer Mechanism: [transfer_mechanism]
  SCC Type: [scc_type]

Sub-Processors: [sub_processors]
  Authorisation Model: [sub_processor_authorisation]

Security Measures: [security_measures]
Retention Period: [retention_period_months] months
Breach Notification: [breach_notification_hours] hours to [breach_notification_parties]

DPIA Required: [include_dpia]
ROPA Required: [include_roPa]
Termination Deletion Period: [termination_deletion_period_days] days

Special Terms: [special_terms]

---

Instructions:
1. Draft a complete DPA with numbered clauses and defined terms.
2. Include all mandatory sections required under [governing_law]:
   - Definitions and Interpretation
   - Scope and Duration
   - Processing Instructions and Data Processing Details
   - Rights and Obligations of the Controller
   - Rights and Obligations of the Processor (including confidentiality, security, sub-processors, assistance obligations)
   - Data Subject Rights Procedures
   - Data Breach Notification and Management
   - Data Protection Impact Assessment and Prior Consultation
   - Record of Processing Activities
   - Technical and Organisational Measures
   - Sub-Processor Engagement (authorisation model, liability, list updating mechanism)
   - Cross-Border Data Transfer (mechanism, safeguards, onward transfer restrictions)
   - Liability and Indemnification
   - Term and Termination (including data deletion/return obligations)
   - Audit and Inspection Rights
   - Boilerplate
3. If special category data is processed, include enhanced security measures and a DPIA trigger clause.
4. If [scc_type] is specified, attach the applicable SCCs as a schedule and ensure the DPA body references them correctly.
5. Include a provision requiring the processor to notify the controller of any legally binding request for disclosure of personal data (unless prohibited by law).
6. Ensure that sub-processor clauses reflect the authorisation model selected and include a 30-day objection period for general authorisation.
7. Include a Mutual Assistance clause for data subject requests.
8. Flag any provisions that may be non-compliant with local law or that require further negotiation.

Output in structured markdown with separate schedules.
```

## Output Format

```markdown
# DATA PROCESSING AGREEMENT

## PARTIES AND RECITALS
...
## 1. DEFINITIONS AND INTERPRETATION
...
## 2. SCOPE AND DURATION
...
## 3. PROCESSING INSTRUCTIONS
...
## 4. RIGHTS AND OBLIGATIONS OF THE CONTROLLER
...
## 5. RIGHTS AND OBLIGATIONS OF THE PROCESSOR
...
## 6. DATA SUBJECT RIGHTS PROCEDURES
...
## 7. DATA BREACH NOTIFICATION AND MANAGEMENT
...
## 8. DATA PROTECTION IMPACT ASSESSMENT
...
## 9. RECORD OF PROCESSING ACTIVITIES
...
## 10. TECHNICAL AND ORGANISATIONAL MEASURES
...
## 11. SUB-PROCESSORS
...
## 12. CROSS-BORDER DATA TRANSFERS
...
## 13. LIABILITY AND INDEMNIFICATION
...
## 14. TERM AND TERMINATION
...
## 15. AUDIT AND INSPECTION
...
## 16. BOILERPLATE
...
## 17. EXECUTION

---

### SCHEDULE 1: LIST OF PROCESSING ACTIVITIES
### SCHEDULE 2: TECHNICAL AND ORGANISATIONAL MEASURES
### SCHEDULE 3: SUB-PROCESSORS
### SCHEDULE 4: CROSS-BORDER TRANSFER MECHANISM
### SCHEDULE 5: DATA RETENTION SCHEDULE

---

### DRAFTING NOTES
- [Key drafting decisions]
- [Risk flags]
- [Jurisdiction-specific compliance notes]

### REGULATORY NOTES
- [Regulator guidance cited]
- [Registration requirements if any]
```

## Quality Checklist

- [ ] Controller and processor roles are correctly classified (no mismatch between stated role and obligations)
- [ ] Processing instructions are sufficiently detailed and binding
- [ ] Data categories and data subject categories are exhaustive and accurate
- [ ] Sub-processor authorisation model is clearly stated and consistent throughout
- [ ] Cross-border transfer mechanism is lawful under the governing data protection law
- [ ] SCCs (if used) are the correct version for the jurisdiction and are fully filled out
- [ ] Breach notification timeline matches the governing law (72 hours for DPPA/GDPR; check local variations)
- [ ] Security measures are appropriate to the risk level and special category data (if any)
- [ ] Audit rights clause permits the controller to audit the processor (with or without a third-party auditor)
- [ ] Data deletion/return obligation at termination is unambiguous and technically feasible
- [ ] Assistance clause for data subject requests is reciprocal and specific
- [ ] DPIA trigger clause correctly flags when a DPIA is mandatory
- [ ] ROPA clause defines who maintains it and what it must contain
- [ ] Liability clause clearly allocates liability for breaches of the DPA (separate from the main agreement)
- [ ] No clause contradicts or duplicates the underlying commercial agreement without clear precedence

## Common Errors

1. **Role misclassification** — Drafting the processor as a joint controller when they have no decision-making power over processing purposes. Fix: apply the "determination of purpose and means" test from DPPA Section 2 and GDPR Article 4(7).
2. **Inadequate transfer mechanism** — Assuming consent is sufficient for all cross-border transfers. Under DPPA Section 14, consent is only one of several bases. The mechanism must match the assessment of adequacy. Fix: first assess whether the recipient country appears on Uganda's adequacy list (published by the Personal Data Protection Office). If not, use SCCs.
3. **Generic security measures** — Listing "appropriate technical and organisational measures" without specificity. Fix: the DPA must include a detailed schedule of measures (encryption standards, access control protocols, certification schemes).
4. **Sub-processor circumvention** — Allowing the processor to engage sub-processors without any controller oversight. Fix: at minimum, require notification and a 30-day objection period.
5. **Mixing governing law and data protection law** — The DPA's governing law may differ from the data protection law applied. The agent must distinguish between "law governing the contract" and "law governing the processing."
6. **No data portability obligation** — Failing to include a clause that enables the controller to export personal data in a structured, commonly used format. DPPA Section 16 provides for data portability and should be reflected.
7. **Post-termination data retention** — Permitting the processor to retain data after termination for their own purposes without a lawful basis. Fix: restrict post-termination processing to compliance with legal obligations only.
8. **Failure to register as a data processor** — In Uganda, data processors must register with the Personal Data Protection Office under DPPA Section 10(1). The DPA should include a representation that both parties are registered or will register before processing begins.
9. **Unlimited liability for processor** — While the DPPA does not prescribe specific caps, GDPR Article 82 provides for liability. The commercial liability cap in the underlying agreement should extend to the DPA, but unlimited liability may apply for breach of data protection obligations by law.

## Expert Mode Guidance

- **Multi-Layered SCC Strategy**: When data flows involve multiple jurisdictions (e.g. processor in Uganda, sub-processor in Kenya, data subjects in Rwanda, server in Germany), use a modular SCC approach. Apply Uganda DPPA SCCs for the Uganda-Kenya leg and EU 2021/914 Module 3 (Processor-to-Processor) for the Kenya-Germany leg. The DPA should include a hierarchy clause stating which SCC prevails in case of conflict.
- **Binding Corporate Rules (BCRs)**: For multinational groups operating across East Africa, BCRs are not yet formally recognised by the Personal Data Protection Office (Uganda) or ODPC (Kenya). Until formal recognition, the safest mechanism remains SCCs per jurisdiction, supplemented by intra-group transfer agreements with contractual liability cascades.
- **Regulatory Sandbox Clauses**: Consider inserting a "regulatory change" clause that automatically updates the transfer mechanism when the regulator issues new adequacy decisions or model clauses.
- **Audit Mechanisation**: For enterprise DPAs, replace traditional on-site audit rights with a SOC 2 Type II or ISO 27001 certification-based audit model. Provide a clause that annual certification replaces the right to audit unless a breach has occurred.
- **Special Category Data in Healthcare**: For health data processors (common in East African telemedicine), the DPA must address Section 21 of the DPPA (sensitive data) and Article 9 GDPR. Include enhanced security requirements, strict purpose limitation, and a DPIA as a mandatory prerequisite.
- **Government Access Requests**: Add a clause addressing government access to data (common under Uganda's Regulation of Interception of Communications Act 2010 and Kenya's Computer Misuse and Cybercrimes Act 2018). The processor must notify the controller of any lawful interception demand unless legally prohibited.

## Uganda-Specific Considerations

1. **Data Protection and Privacy Act 2019 (DPPA)**: The principal legislation. Key provisions: Section 10 (registration of data processors), Section 14 (cross-border transfers), Section 16 (data subject rights including portability), Section 17 (DPIA), Section 21 (sensitive data), Section 32 (breach notification within 72 hours).
2. **Data Protection and Privacy Regulations 2021**: Effective 10 December 2021. They provide detailed rules on registration, processing of personal data, data subject rights requests, and the Third Schedule containing the Uganda SCCs.
3. **Personal Data Protection Office (PDPO)**: The regulatory authority under Section 4 of the DPPA. The DPA must include the PDPO as the supervisory authority. Contact details: Plot 9, John Babiiha Avenue, Kampala.
4. **Registration Requirement**: Under Section 10(1) DPPA, every data processor must register with the PDPO. The DPA should include the processor's registration number. As of 2026, the PDPO has issued registration guidelines with tiered fees based on processing volume.
5. **Cross-Border Transfer Adequacy**: Section 14(2) DPPA provides that transfers are permitted if the recipient is in a country with adequate data protection laws. Uganda's PDPO maintains a list of adequate jurisdictions. As of mid-2026, the list includes: Kenya, Rwanda, South Africa, UK, and all EU/EEA member states. For non-adequate countries, SCCs or consent must be used.
6. **Electronic Transactions Act 2011**: Electronic DPA signatures are valid. However, the DPA agent should flag if wet signatures are required by the counterparty's internal policy.
7. **Data Subject Rights under DPPA**: Section 16 lists: right to be informed, access, rectification, erasure, restriction of processing, data portability, and objection. The DPA must operationalise each right with specific response timelines (default: 30 days per Regulation 21).
8. **Consent Requirements**: Section 8 DPPA requires that consent be "freely given, specific, informed, and unambiguous." For processing of sensitive data, Section 21 requires explicit consent. The DPA should cross-reference the consent mechanism.
9. **Offences and Penalties**: Section 49 DPPA — contravention of the Act carries fines up to UGX 4.8 million (approximately USD 1,300) or imprisonment up to 5 years, or both. The DPA should flag that serious breaches may have criminal consequences.
10. **Sectoral Overlaps**: The DPPA intersects with the Uganda Communications Act 2013 (for telecom data), the Health Information Systems Policy (for health data), and the Bank of Uganda regulations (for financial data). The agent must flag where sector-specific rules supplement the DPPA.

## East African Considerations

1. **Harmonisation Efforts**: The EAC is working towards harmonised data protection laws. The EAC Data Protection Framework (draft) proposes minimum standards. The agent should monitor this framework and include a clause that the DPA will be updated if harmonised rules are adopted.
2. **Disparate National Laws**: Data protection laws across EAC differ significantly:
   - Uganda: DPPA 2019 — comprehensive, rights-heavy
   - Kenya: Data Protection Act 2019 — modelled closely on GDPR, with an independent ODPC
   - Tanzania: Personal Data Protection Act 2022 — hybrid model with sector-specific nuances
   - Rwanda: Law Relating to Data Protection and Privacy 2021 — data controller registration required
   - Burundi: Law No. 1/14 of 2021 on Data Protection — comprehensive, with a regulatory authority (ARDP)
   - South Sudan: No comprehensive data protection law yet
   - DRC: Data Protection Act (Law No. 22-067) — passed 2022
3. **Cross-Border Enforcement**: The EAC Common Market Protocol Article 7(1)(e) requires partner states to remove restrictions on the movement of data. However, national data protection laws create tension by requiring adequacy assessments. The agent should reference Article 7 and insert a best-efforts clause to facilitate cross-border data flows.
4. **EAC Mutual Recognition Agreements**: The EAC is developing mutual recognition of data protection authorities' decisions. A clause referencing mutual recognition may reduce compliance costs for multi-country processing.
5. **East African Court of Justice (EACJ)**: As a potential forum for data protection disputes involving cross-border processing. The DPA could include the EACJ as an appellate body after exhausting national remedies.
6. **Data Localisation Trends**: Both Uganda and Kenya have proposed or enacted data localisation requirements for specific sectors (e.g. financial services, health). The agent must flag if localisation requirements apply to the processing and ensure the DPA addresses local storage obligations.

## Comparative Law Considerations

| Issue | Uganda (DPPA 2019) | Kenya (DPA 2019) | EU GDPR |
|---|---|---|---|
| Regulator | Personal Data Protection Office (PDPO) | Office of the Data Protection Commissioner (ODPC) | National DPA + EDPB |
| Registration required | Yes (processors and controllers) | Yes (processors and controllers) | No, but ROPA required |
| Breach notification | 72 hours to PDPO | 72 hours to ODPC | 72 hours to DPA |
| Special category data | Explicit consent required (Section 21) | Explicit consent required (Section 5) | Explicit consent or one of 9 other bases (Article 9) |
| Cross-border transfer | Adequacy, SCCs, or consent (Section 14) | Adequacy, SCCs, or consent (Section 48) | Adequacy or SCCs (Articles 44-49) |
| SCC form | Third Schedule, DPPA Regulations 2021 | Draft SCCs issued by ODPC (2023) | EU 2021/914 (four modules) |
| Data portability | Yes (Section 16) | Yes (Section 34) | Yes (Article 20) |
| DPIA | Required for high-risk processing (Section 17) | Required for high-risk processing (Section 31) | Required for high-risk processing (Article 35) |
| DPO appointment | Required for government and large-scale processing (Section 15) | Required for government and large-scale processing (Section 24) | Required for public authorities and large-scale monitoring (Articles 37-39) |
| Fines | Up to UGX 4.8 million or 5 years imprisonment | Up to KES 5 million or 1% annual turnover | Up to EUR 20 million or 4% annual turnover |
| International transfers | Adequacy list, SCCs, consent | Adequacy list, SCCs, consent | Adequacy decision, SCCs, BCRs |
| Sub-processor authorisation | Implied requirement for prior authorisation | Written authorisation required (Section 41) | Written authorisation required (Article 28(2)) |

## Reading Framework

1. **Primary Legislation**:
   - Uganda: Data Protection and Privacy Act 2019 (Act No. 4 of 2019), Data Protection and Privacy Regulations 2021 (S.I. No. 45 of 2021)
   - Kenya: Data Protection Act 2019 (Act No. 24 of 2019), Data Protection (General) Regulations 2021, Data Protection (Registration of Data Controllers and Data Processors) Regulations 2021
   - Tanzania: Personal Data Protection Act 2022 (Act No. 2 of 2022)
   - Rwanda: Law Relating to Data Protection and Privacy 2021 (Law No. 058/2021)
   - Burundi: Data Protection Law 2021 (Law No. 1/14 of 2021)
   - EU: General Data Protection Regulation (Regulation (EU) 2016/679), Law Enforcement Directive (Directive (EU) 2016/680)

2. **Subsidiary Legislation & Guidance**:
   - Uganda DPPA Regulations 2021 (S.I. No. 45 of 2021, especially the Third Schedule SCCs)
   - Kenya Data Protection (Civil Registration) Regulations 2021
   - EDPB Guidelines 2/2018 on Article 49 (Derogations), 4/2019 on Article 25 (Data Protection by Design and Default)
   - ODPC (Kenya) Guidance on Cross-Border Data Transfers (2023)
   - PDPO (Uganda) Guidance on Registration and Compliance (2022-2024)

3. **Case Law**:
   - Uganda: *Uganda Telecom Ltd v. Uganda Communications Commission* (High Court, Misc. App. — DPPA-related interpretation)
   - Kenya: *ODPC v. Smartmatic* (2022) — cross-border transfers and SCCs enforcement
   - CJEU: *Schrems II* (C-311/18) — adequacy of transfers, SCCs validity
   - CJEU: *Google v. CNIL* (C-507/17) — right to erasure territorial scope

4. **Standards & Frameworks**:
   - ISO/IEC 27701 (Privacy Information Management)
   - ISO/IEC 27001 (Information Security Management)
   - NIST Privacy Framework v1.0
   - EAC Data Protection Framework (draft)

5. **Treaties & International Instruments**:
   - EAC Common Market Protocol (Article 7)
   - African Union Convention on Cyber Security and Personal Data Protection (Malabo Convention, 2014) — not yet in force
   - ECOWAS Supplementary Act on Personal Data Protection (2010)
   - SADC Model Law on Data Protection (2013)

## Example Invocation

```json
{
  "controller_name": "Uganda Health Insurance Ltd",
  "controller_registration": "80012345678901",
  "controller_contact_email": "dpo@ugandahealth.co.ug",
  "processor_name": "MediCloud Technologies (U) Ltd",
  "processor_registration": "80098765432109",
  "processor_contact_email": "privacy@medicloud.co.ug",
  "governing_law": "uganda",
  "dispute_forum": "court",
  "jurisdiction_regulator": "Personal Data Protection Office (Uganda)",
  "processing_purpose": "Processing of patient health insurance claims, medical records management, and fraud detection analytics",
  "processing_scope": "full",
  "data_categories": ["personal_identifiers", "health_data", "financial_data", "biometric_data"],
  "data_subject_categories": ["patients", "employees", "beneficiaries"],
  "special_category_data": true,
  "special_categories": ["health", "biometric"],
  "transfer_countries": ["Kenya", "Rwanda", "United Kingdom"],
  "transfer_mechanism": "scc",
  "scc_type": "uganda_dppa",
  "sub_processors": [
    {"name": "Nairobi Data Centre Ltd", "country": "Kenya", "processing_description": "Cloud hosting and database management"},
    {"name": "Kigali Analytics Inc", "country": "Rwanda", "processing_description": "Fraud detection model training and inference"}
  ],
  "sub_processor_authorisation": "general_written",
  "retention_period_months": 60,
  "security_measures": ["encryption_at_rest", "encryption_in_transit", "access_controls", "pseudonymisation", "audit_logs", "penetration_testing", "biometric_authentication"],
  "breach_notification_hours": 24,
  "breach_notification_parties": "both",
  "dpo_name": "Dr. Grace Achieng",
  "dpo_email": "dpo@ugandahealth.co.ug",
  "include_dpia": true,
  "include_roPa": true,
  "termination_deletion_period_days": 60,
  "processor_fees": 250000000,
  "special_terms": "Patients have the right to opt out of fraud detection analytics; processor must implement granular consent controls"
}
```
