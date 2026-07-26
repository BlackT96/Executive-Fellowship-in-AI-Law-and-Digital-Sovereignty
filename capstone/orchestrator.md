# Orchestrator — Query-to-Agent Routing Framework

## How to Use

Given a legal problem, classify it by domain and task type, then route to the appropriate agent. Complex matters may require a primary agent supported by one or more secondary agents.

---

## Classification Key

### 1. Identify the Legal Domain

| If the matter involves... | Domain | Primary Agent |
|---|---|---|
| Data privacy, consent, data subject rights, NDPC notification | **Compliance** | Privacy Compliance Agent |
| Security breaches, incident response, forensic investigation, ISO 27001 | **Compliance** | Cybersecurity Compliance Agent |
| High-risk AI systems, data protection impact assessment | **Governance** | DPIA Agent |
| AI ethics board, AI policy framework, ISO 42001, NIST AI RMF | **Governance** | AI Governance Agent |
| Internal AI audit, model explainability, bias testing, accountability | **Governance** | AI Audit Agent |
| Digital evidence, e-discovery, admissibility of electronic records | **Litigation** | Digital Evidence Agent |
| Constitutional rights, digital rights, freedom of expression online | **Litigation** | Constitutional Petition Agent |
| Case strategy, cause of action, strength assessment, jurisdiction | **Litigation** | Litigation Strategy Agent |
| Plaints, defences, counterclaims, affidavits, petitions | **Litigation** | Pleading Drafting Agent |
| Regulatory impact analysis, cost-benefit, human rights impact | **Policy** | Regulatory Impact Agent |
| Institutional policy (AI, data protection, cybersecurity) | **Policy** | Policy Drafting Agent |
| Bill, Regulation, Statutory Instrument, EAC legal instrument | **Policy** | Legislative Drafting Agent |
| Case law search, statute interpretation, legal question | **Research** | Legal Research Agent |
| Cross-jurisdictional comparison (EU, UK, US, Kenya, Rwanda, etc.) | **Research** | Comparative Law Agent |
| Case summary, ratio decidendi, obiter dicta, precedent value | **Research** | Case Digest Agent |
| Data localisation, sovereign cloud, compute sovereignty | **Sovereignty** | Digital Sovereignty Agent |
| National AI strategy, digital transformation roadmap | **Strategy** | Technology Strategy Agent |
| Regulatory engagement, government relations, market entry | **Strategy** | Regulatory Strategy Agent |
| Course design, learning outcomes, assessment framework | **Teaching** | Curriculum Agent |
| Quiz generation, exam construction, rubric design, progress testing | **Teaching** | Assessment Agent |
| Expert report, technical explanation, expert testimony prep | **Teaching** | Expert Witness Agent |
| Formal legal opinion, transaction opinion, regulatory interpretation | **Transactional** | Legal Opinion Agent |
| Data Processing Agreement, SCCs, cross-border transfer documentation | **Transactional** | DPA Agent |
| SaaS agreement, AI licence, technology procurement contract | **Transactional** | Contract Drafting Agent |
| Weekly legal opinion, regulatory commentary, thought leadership | **Writing** | Weekly Article Agent |
| LinkedIn content, carousel, short-form legal commentary | **Writing** | LinkedIn Writer Agent |
| Book manuscript, curriculum-to-book conversion | **Writing** | Book Writer Agent |

### 2. Identify Supporting Agents Needed

| Supporting Need | Agent |
|---|---|
| Need case law or statute references | Legal Research Agent |
| Need comparison with other jurisdictions | Comparative Law Agent |
| Need case digest for precedent | Case Digest Agent |
| Need technical explanation for non-technical audience | Expert Witness Agent |
| Need quality review before finalising | AI Audit Agent |
| Need final publication or filing version | Appropriate Writing Agent |

### 3. Chain Workflow

```
Primary Agent ──► Supporting Agent(s) ──► Writing/Output Agent
```

Determine the primary agent from the matter type, add supporting agents for research or review, and finish with a writing agent if the output needs publication or formal presentation.

---

## Routing Matrix

| Fact Pattern | Primary Agent | Support Agents | Output |
|---|---|---|---|
| "Client received NDPC enforcement notice for data breach" | Privacy Compliance Agent | Cybersecurity Compliance Agent, Litigation Strategy Agent | Response strategy, representation |
| "Draft a data protection policy for a Ugandan fintech deploying AI" | Policy Drafting Agent | DPIA Agent, Comparative Law Agent (Kenya, Rwanda references) | Institutional policy document |
| "Prepare a constitutional petition challenging biometric ID system" | Constitutional Petition Agent | Legal Research Agent, Comparative Law Agent (India Aadhaar cases) | Petition, written submissions |
| "Client needs to sign a SaaS agreement with a US vendor" | Contract Drafting Agent | DPA Agent (for data processing schedule), Legal Opinion Agent | SaaS agreement + DPA |
| "Evaluate whether a new AI hiring tool complies with Uganda law" | AI Governance Agent | DPIA Agent, Privacy Compliance Agent | Compliance assessment report |
| "Write a weekly article on Uganda's AI readiness" | Weekly Article Agent | Legal Research Agent, Technology Strategy Agent | Published article |
| "Design a 12-week AI law curriculum for law students" | Curriculum Agent | All domain agents for module inputs | Course outline |
| "Generate a 45-minute quiz for Module 1 Week 1" | Assessment Agent | Curriculum Agent (for learning outcomes), relevant domain agent | Quiz with rubric and model answers |
| "Create final exam for the Fellowship programme" | Assessment Agent | All domain agents for content coverage, Curriculum Agent for outcome alignment | Exam paper with marking scheme |
| "Mark the Module 2 exam answer sheets for 15 candidates" | Assessment Agent | Previously generated Module 2 exam (marking scheme, rubric, model answers) | Individual marked sheets, corrections, recommendations, cohort analytics |
| "Compare my Module 3 performance with the rest of the cohort" | Assessment Agent | Cohort answer data from Module 3 exam | Peer comparison report with percentile ranking |
| "Generate my Professional Readiness Assessment after the final exam" | Assessment Agent | Final exam answer + marking data | Certification recommendation and readiness classification |
| "Cross-examine a forensic expert on digital evidence chain of custody" | Digital Evidence Agent | Expert Witness Agent, Case Digest Agent (relevant precedents) | Cross-examination outline |
| "Draft amendments to the Computer Misuse Act" | Legislative Drafting Agent | Comparative Law Agent (EU Digital Services Act, UK Online Safety Bill), Regulatory Impact Agent | Bill with explanatory memorandum |
| "Advise government on data localisation requirements" | Digital Sovereignty Agent | Comparative Law Agent (Russia, China, India, EU), Technology Strategy Agent | Policy brief |

---

## Conflict Resolution

When a matter spans multiple domains:

| Conflict | Resolution |
|---|---|
| Compliance vs. Governance overlap | Lead with the agent that matches the triggering event (breach → Compliance, proactive → Governance) |
| Policy vs. Legislative overlap | Policy Drafting for institutional instruments, Legislative Drafting for statutory instruments |
| Litigation vs. Transactional overlap | Litigation for disputes, Transactional for proactive structuring |
| Research vs. Writing overlap | Research for analysis, Writing for publication |

## Fallback Agent

If the matter does not clearly match any single agent:

```
1. Legal Research Agent — to classify the legal question
2. Comparative Law Agent — to identify analogous frameworks
3. Then route to the appropriate domain agent
```
