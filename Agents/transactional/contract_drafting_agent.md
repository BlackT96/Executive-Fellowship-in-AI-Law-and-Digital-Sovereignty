# Contract Drafting Agent

## Purpose

The Contract Drafting Agent generates, reviews, and refines commercial contracts with a focus on SaaS agreements, technology agreements, AI contracts, licensing agreements, and procurement agreements. It operates within the legal framework of Uganda and the East African Community (EAC), while incorporating comparative insights from common law jurisdictions such as England & Wales, South Africa, and Kenya. The agent reduces drafting time by 60-70% by producing first-draft clauses, flagging missing terms, and aligning language with jurisdictional requirements.

## Competencies

1. **SaaS Agreement Drafting** — Generate subscription terms, SLA frameworks, uptime commitments, data handling provisions, auto-renewal clauses, and termination-for-convenience terms.
2. **Technology Agreement Drafting** — Draft development agreements, system integration terms, API licensing, escrow provisions, and acceptance testing protocols.
3. **AI Contract Drafting** — Draft AI-specific terms including model licensing, training data warranties, output ownership, bias disclaimers, liability caps for algorithmic decisions, and regulatory compliance representations.
4. **Licensing Agreement Drafting** — Prepare exclusive/non-exclusive IP licenses, royalty calculation mechanisms, field-of-use restrictions, territory definitions, and sub-licensing conditions.
5. **Procurement Agreement Drafting** — Structure RFP responses, terms and conditions for goods/services, delivery milestones, inspection rights, warranty periods, and indemnity frameworks.
6. **Clause Library Management** — Maintain and retrieve predefined clause libraries for boilerplate (force majeure, governing law, dispute resolution, notices, assignment).
7. **Risk Flagging** — Identify unbalanced risk allocation, missing limitation-of-liability cascades, non-compliant governing law selections, and unenforceable restraint clauses.

## Inputs

| Input Field | Type | Required | Description |
|---|---|---|---|
| `contract_type` | Enum | Yes | saas / tech_agreement / ai_contract / licensing / procurement |
| `party_a_name` | String | Yes | Full legal name of first party |
| `party_a_type` | Enum | Yes | individual / company / govt_entity / nonprofit |
| `party_a_registration` | String | No | Company registration or national ID number |
| `party_b_name` | String | Yes | Full legal name of second party |
| `party_b_type` | Enum | Yes | individual / company / govt_entity / nonprofit |
| `party_b_registration` | String | No | Company registration or national ID number |
| `governing_law` | Enum | Yes | uganda / kenya / tanzania / rwanda / england / south_africa / other |
| `dispute_forum` | Enum | Yes | uganda_court / arbitration_uganda / arbitration_eac / icc / london_court / other |
| `currency` | String | Yes | e.g. UGX, KES, TZS, USD, EUR |
| `term_months` | Integer | Yes | Initial term duration in months |
| `auto_renew` | Boolean | No | Whether contract auto-renews (default: true) |
| `renewal_notice_days` | Integer | No | Notice period for non-renewal (default: 30) |
| `payment_model` | Enum | Yes | fixed / subscription / milestone / royalty / consumption |
| `annual_fee` | Number | Conditional | Required for subscription-based contracts |
| `liability_cap_multiplier` | Number | No | Multiplier of fees for liability cap (default: 1x) |
| `include_sla` | Boolean | No | Whether to include service level agreement (default: false) |
| `sla_uptime` | Number | No | Required uptime percentage (default: 99.5) |
| `sla_credit_model` | Enum | No | standard / escalating / custom |
| `include_dpa` | Boolean | No | Whether to link a data processing agreement (default: false) |
| `ai_use_case` | String | No | Description of AI use case if contract_type is ai_contract |
| `training_data_source` | String | No | Source and nature of training data for AI contracts |
| `training_data_ownership` | Enum | No | customer / provider / joint / unknown |
| `ip_ownership` | Enum | No | customer / provider / joint |
| `software_escrow_required` | Boolean | No | Whether source code escrow is required |
| `territory` | String | No | Geographic scope (default: Uganda) |
| `exclusivity` | Enum | No | exclusive / non_exclusive / sole |
| `special_terms` | Text | No | Additional bespoke terms requested |
| `force_majeure_included` | Boolean | No | Whether to include a force majeure clause (default: true) |
| `force_majeure_events` | String | No | Custom force majeure events |

## Workflow

```
Step 1: Validate Inputs
        └─ Check required fields based on contract_type
        └─ Validate enum values and data types
        └─ If include_dpa=true, confirm governing_law supports DPAs
        └─ If ai_contract, validate ai_use_case is non-empty
        │
Step 2: Select Clause Templates
        └─ Load jurisdiction-specific clause library (Uganda/EAC default)
        └─ Load contract_type-specific master template
        └─ Inject party details into recitals and definitions
        │
Step 3: Apply Business Terms
        └─ Populate payment, term, renewal, and termination sections
        └─ Generate fee schedules and invoicing mechanics
        └─ Build limitation-of-liability cascade
        └─ Insert indemnity provisions based on risk profile
        │
Step 4: Add Specialised Modules
        └─ If include_sla: generate SLA schedule with credits
        └─ If include_dpa: append DPA reference and data schedules
        └─ If software_escrow_required: insert escrow clause
        └─ If ai_contract: add AI-specific representations and disclaimers
        │
Step 5: Insert Boilerplate
        └─ Force majeure
        └─ Governing law and dispute resolution
        └─ Notices, assignment, waiver, severability
        └─ Entire agreement clause
        │
Step 6: Apply Jurisdictional Adjustments
        └─ For Uganda: incorporate provisions compliant with the Contracts Act 2010, the Electronic Transactions Act 2011, the Data Protection and Privacy Act 2019, and the Uganda Registration Services Bureau (URSB) requirements
        └─ For Kenya: align with the Kenya Information and Communications Act and Data Protection Act 2019
        └─ For England: reflect the Unfair Contract Terms Act 1977 and applicable EU-derived regulations
        └─ Replace dispute resolution clauses with appropriate forum
        │
Step 7: Generate Output
        └─ Render contract in structured markdown
        └─ Append risk flags and drafting notes
        └─ Provide change summary if input is a variation
```

## Prompt Template

```
You are a senior commercial lawyer specialising in technology and AI transactions in East Africa.

Draft a [contract_type] agreement between:

- Party A: [party_a_name] ([party_a_type], registered as [party_a_registration])
- Party B: [party_b_name] ([party_b_type], registered as [party_b_registration])

Governing Law: [governing_law]
Dispute Forum: [dispute_forum]
Currency: [currency]
Term: [term_months] months | Auto-renew: [auto_renew] | Renewal notice: [renewal_notice_days] days
Payment: [payment_model] | Annual Fee: [annual_fee] | Liability cap: [liability_cap_multiplier]x

Include SLA: [include_sla] (uptime: [sla_uptime]%, credits: [sla_credit_model])
Include DPA: [include_dpa]
Exclusivity: [exclusivity] | Territory: [territory]
IP Ownership: [ip_ownership]

AI Use Case: [ai_use_case]
Training Data: [training_data_source] | Training Data Ownership: [training_data_ownership]
Software Escrow: [software_escrow_required]

Special Terms: [special_terms]
Force Majeure: [force_majeure_included] (events: [force_majeure_events])

---

Instructions:
1. Draft a complete, self-contained agreement with numbered clauses and defined terms.
2. Use clear, plain English. Avoid legalese unless it is standard and necessary.
3. Include the following sections in order:
   - Parties and Recitals
   - Definitions and Interpretation
   - Term and Termination
   - Fees and Payment Terms (with invoicing schedule)
   - Rights and Obligations of Each Party
   - Intellectual Property (licence grant, ownership, residual rights)
   - Confidentiality (duration, exceptions, return of materials)
   - Warranties and Disclaimers (including AI-specific disclaimers if applicable)
   - Limitation of Liability (cascaded: unlimited for IP infringement, breach of confidentiality, fraud; capped for others)
   - Indemnification
   - Insurance Requirements (if applicable)
   - [if SLA] Service Level Agreement (uptime measurement, credits, exclusions)
   - [if DPA] Data Processing Terms
   - [if Escrow] Source Code Escrow
   - Boilerplate
   - Signatures
4. Ensure governing law and dispute resolution clauses reference [governing_law] and [dispute_forum] correctly.
5. Flag any clause that may be unenforceable under [governing_law] law.
6. If AI-specific: include training data warranty, output ownership, bias disclaimer, and compliance with applicable AI regulations in force.
7. If procurement: include delivery milestones, acceptance testing, inspection rights, and warranty period.
8. Output in structured markdown with appendices as separate sections where needed.
```

## Output Format

```markdown
# [CONTRACT TYPE] AGREEMENT

## PARTIES & RECITALS
...
## 1. DEFINITIONS AND INTERPRETATION
...
## 2. TERM AND TERMINATION
...
## 3. FEES AND PAYMENT
...
## 4. RIGHTS AND OBLIGATIONS
...
## 5. INTELLECTUAL PROPERTY
...
## 6. CONFIDENTIALITY
...
## 7. WARRANTIES AND DISCLAIMERS
...
## 8. LIMITATION OF LIABILITY
...
## 9. INDEMNIFICATION
...
## 10. INSURANCE
...
## 11. [SLA SCHEDULE]
...
## 12. [DATA PROCESSING TERMS]
...
## 13. [SOURCE CODE ESCROW]
...
## 14. BOILERPLATE
...
## 15. SIGNATURES

---

### DRAFTING NOTES
- [Key drafting decisions]
- [Risk flags]
- [Jurisdiction-specific notes]

### CHANGE SUMMARY
- [List of changes if this is a revision]
```

## Quality Checklist

- [ ] Party names and registration numbers exactly match supporting documents
- [ ] Definitions are internally consistent and used throughout
- [ ] No contradictory clauses (e.g. unlimited liability and a capped liability both appearing)
- [ ] Governing law and dispute forum are the same jurisdiction or a recognised combination
- [ ] Limitation of liability clause satisfies the reasonableness test under governing law
- [ ] Auto-renewal provisions comply with applicable automatic renewal laws (e.g. Uganda's Consumer Protection Act)
- [ ] SLA credits are commercially reasonable and not punitive
- [ ] Indemnities are reciprocal where appropriate
- [ ] AI-related clauses (if any) reflect current regulatory environment and exclude output warranties
- [ ] Data processing terms (if applicable) are consistent with the DPA Act 2019 (Uganda) or equivalent
- [ ] No bare licence grant — exclusivity, territory, field-of-use clearly defined
- [ ] Force majeure covers pandemic, internet failure, power outages, and regulatory changes
- [ ] Contract does not create a partnership or agency relationship unless intended
- [ ] Execution blocks are present and correct for both parties
- [ ] Currency and payment mechanics are unambiguous

## Common Errors

1. **Misaligned governing law and dispute forum** — Drafting governing law as Uganda but dispute forum as ICC London without an express provision. Fix: always specify the relationship. Uganda law with ICC London arbitration is permissible but must be explicit.
2. **Missing data import/export restrictions** — For SaaS agreements, failing to address where data is stored and whether cross-border transfer is compliant with the Data Protection and Privacy Act 2019 (Uganda) or the Data Protection Act 2019 (Kenya).
3. **AI output warranty** — Warranting that AI-generated output is accurate, non-infringing, or unbiased. Fix: include an express disclaimer that output is provided "as-is" and the customer bears responsibility for review.
4. **Unlimited liability for all losses** — Failing to cap liability appropriately. Fix: use a cascaded cap — unlimited only for IP infringement, breach of confidentiality, fraud, and death/personal injury.
5. **No termination for convenience** — Subscribers locked into long terms without exit. Fix: include a termination-for-convenience clause with a notice period (e.g. 30-90 days) and early termination fee if applicable.
6. **Overbroad IP assignment** — Work-for-hire or assignment clauses that purport to assign IP created before or outside the engagement. Fix: narrow to "deliverables" only with a licence for pre-existing IP.
7. **Inconsistent renewal notice periods** — Stating 30 days in one clause and 60 in another. Fix: single source of truth for notice periods.
8. **Failure to register with URSB** — Not flagging that exclusive IP licences or certain commercial agreements require registration with the Uganda Registration Services Bureau.

## Expert Mode Guidance

- **Negotiation Heuristics**: For SaaS agreements with enterprise customers, expect pressure to increase the liability cap from 1x to 3x annual fees. Acceptable trade-off is to narrow the indemnity scope simultaneously. For procurement agreements with government entities, the Public Procurement and Disposal of Public Assets Act (PPDA) 2003 (Uganda) imposes mandatory terms — flag deviations early.
- **AI Contract Nuances**: In AI contracts, the most contentious clauses are (a) training data warranty — providers should warrant only that they have the right to use the data, not that the data is error-free; (b) output ownership — if the model trains on customer data, clarify whether improvements belong to provider; (c) regulatory compliance — include a representation that both parties will comply with emerging AI regulations (e.g. Uganda's draft National AI Policy, the African Union's AI Continental Strategy).
- **Escrow Mechanics**: For technology agreements, software escrow should specify the deposit materials (source code, build scripts, documentation, third-party dependency list), the release conditions (bankruptcy, cessation of support, breach of SLA), and verification frequency (annual).
- **Multi-jurisdictional Deals**: When parties span Uganda and Kenya, consider drafting an EAC choice of law clause referencing the EAC Common Market Protocol, or default to English law as a neutral choice with arbitration in Nairobi or Kigali.

## Uganda-Specific Considerations

1. **Electronic Signatures**: The Electronic Transactions Act 2011 (Cap 8, Laws of Uganda) recognises electronic signatures as legally valid. However, contracts for land, wills, and guarantees still require wet signatures or advanced electronic signatures compliant with the Act.
2. **Withholding Tax**: Payments for royalties, management fees, and professional services to non-residents are subject to 15% withholding tax under the Income Tax Act (Cap 340). The draft must flag withholding obligations and gross-up clauses.
3. **Stamp Duty**: Agreements executed in Uganda or relating to property in Uganda may be subject to stamp duty under the Stamp Duty Act 2014. The agent should flag stamp duty obligations — especially for exclusive IP licences and long-term leases embedded in procurement contracts.
4. **URSB Registration**: Exclusive patent and trademark licences must be recorded with the Uganda Registration Services Bureau to be enforceable against third parties. The drafter must insert a covenant to register.
5. **PPDA Compliance**: Procurement contracts with government entities or state-owned enterprises must comply with the PPDA Act 2003. The agent should default to PPDA-compliant templates when `party_b_type` is `govt_entity`.
6. **Consumer Protection**: The Consumer Protection Act 2019 applies where one party is a consumer. SaaS contracts with SMEs that fall within the consumer definition must include cooling-off periods and cannot include unfair terms (as defined in the Act).
7. **Data Protection & Privacy Act 2019**: Any contract involving processing of personal data must incorporate DPPA-compliant data processing terms. The agent must include a DPA schedule when `include_dpa=true`.
8. **Competition Act 2012**: Exclusivity clauses, tying arrangements, and resale price maintenance must be reviewed against the Competition Act 2012.

## East African Considerations

1. **EAC Common Market Protocol**: Contracts for services, goods, or investment across EAC partner states (Uganda, Kenya, Tanzania, Rwanda, Burundi, South Sudan, DRC) must recognise the right of establishment and free movement of services. Non-discrimination clauses should reference the Protocol.
2. **East African Customs Union**: For procurement of goods, tariff classifications and rules of origin under the EAC Customs Union affect pricing and delivery obligations. Consider referencing the EAC tariff schedule for cross-border procurement.
3. **EAC Competition Act**: The EAC Competition Act 2006 prohibits anti-competitive agreements, abuse of dominance, and restrictive trade practices affecting trade between partner states. Cross-border exclusivity arrangements must be assessed against this Act.
4. **Mutual Recognition of Accredited Standards (MRA)**: The EAC has mutual recognition agreements for professional services and product standards. Service-level descriptions should reference applicable EAC standards where relevant.
5. **EAC AI and Digital Trade Framework**: Monitor the emerging EAC Digital Trade Framework and the EAC AI Strategy, both of which will influence cross-border AI service agreements. The agent should include a representation that the parties will comply with EAC digital trade rules as they come into force.
6. **Currency and Foreign Exchange**: Use of USD or EUR in cross-border EAC contracts is common but the Central Bank of Kenya, Bank of Uganda, and other national banks may impose reporting thresholds. Insert a clause requiring compliance with foreign exchange regulations of each relevant partner state.

## Comparative Law Considerations

| Issue | Uganda | Kenya | England & Wales |
|---|---|---|---|
| Contract formation | Contracts Act 2010 (offer, acceptance, consideration) | Law of Contract Act Cap 23 (similar English common law) | Common law (Contract Act 1999) — consideration required |
| Electronic signatures | Electronic Transactions Act 2011 — valid (except land/wills) | Kenya Information and Communications Act 1998 — valid | eIDAS Regulation (UK version) — valid |
| Limitation of liability | No statutory cap; reasonableness test per common law | Common law reasonableness; no specific statute | Unfair Contract Terms Act 1977 — reasonableness test applies |
| Data protection | Data Protection and Privacy Act 2019 | Data Protection Act 2019 | UK GDPR / Data Protection Act 2018 |
| Withholding tax on royalties | 15% (Income Tax Act Cap 340) | 20% (Income Tax Act Cap 470) | 20% (if non-treaty) |
| AI regulation | Draft National AI Policy (not yet law) | Draft AI & Robotics Association guidelines | UK AI White Paper (pro-innovation approach) |
| Exclusive licence registration | URSB — required | KIPI — required | UKIPO — recommended but not mandatory |
| Competition law | Competition Act 2012 | Competition Act Cap 504 | Competition Act 1998 / Chapter I & II prohibitions |
| Consumer protection | Consumer Protection Act 2019 | Consumer Protection Act 2012 | Consumer Rights Act 2015 |

## Reading Framework

1. **Primary Legislation**:
   - Uganda: Contracts Act 2010 (Cap 76), Electronic Transactions Act 2011 (Cap 8), Data Protection and Privacy Act 2019, Consumer Protection Act 2019, Competition Act 2012, Stamp Duty Act 2014, Income Tax Act (Cap 340), PPDA Act 2003
   - Kenya: Law of Contract Act (Cap 23), Data Protection Act 2019, Consumer Protection Act 2012, Competition Act (Cap 504)
   - EAC: EAC Common Market Protocol, EAC Competition Act 2006
   - England: Unfair Contract Terms Act 1977, Consumer Rights Act 2015

2. **Regulatory Bodies**:
   - Uganda Registration Services Bureau (URSB) — contract registration
   - Uganda Revenue Authority (URA) — stamp duty and tax
   - Personal Data Protection Office (Uganda) — DPA compliance
   - Public Procurement and Disposal of Public Assets Authority (PPDA) — government procurement
   - National Information Technology Authority (NITA-U) — technology standards

3. **Soft Law & Guidance**:
   - Uganda Law Reform Commission — contract law reform reports
   - Law Development Centre — precedents
   - IACCM / WorldCC — commercial contracting standards
   - African Union AI Continental Strategy (2024)
   - UNCITRAL Model Law on Electronic Commerce (influences E-transactions Act)

4. **Precedent Libraries**:
   - Uganda Law Reports (ULR) — contract enforcement cases
   - East African Court of Justice — treaty interpretation cases
   - Kenyan eKLR — comparable common law precedents
   - BAILII / LawCite — international contract case law

## Example Invocation

```json
{
  "contract_type": "saas",
  "party_a_name": "CloudSync Technologies Ltd",
  "party_a_type": "company",
  "party_a_registration": "80012345678901",
  "party_b_name": "Jinja Hospital Group",
  "party_b_type": "company",
  "party_b_registration": "80098765432109",
  "governing_law": "uganda",
  "dispute_forum": "arbitration_uganda",
  "currency": "UGX",
  "term_months": 24,
  "auto_renew": true,
  "renewal_notice_days": 60,
  "payment_model": "subscription",
  "annual_fee": 120000000,
  "liability_cap_multiplier": 2,
  "include_sla": true,
  "sla_uptime": 99.9,
  "sla_credit_model": "escalating",
  "include_dpa": true,
  "ai_use_case": "",
  "ip_ownership": "customer",
  "software_escrow_required": false,
  "territory": "Uganda",
  "exclusivity": "non_exclusive",
  "special_terms": "Hospital requires 24/7 support with 1-hour critical response time",
  "force_majeure_included": true,
  "force_majeure_events": "pandemic, internet outage, power failure, act of God"
}
```
