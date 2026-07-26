# AI Law & Digital Sovereignty — Unified Agent System

## What This Is

This capstone integrates **26 specialised AI law agents** into a single, coherent system for Ugandan and East African legal practice. Each agent is a self-contained skill module that performs a specific legal function — from drafting pleadings and data processing agreements to conducting regulatory impact assessments and authoring legislative instruments.

The system is organised around the **Executive Fellowship in AI Law & Digital Sovereignty** curriculum and is designed to serve legal practitioners, regulators, policymakers, in-house counsel, and academics operating in Uganda, the East African Community, and comparable jurisdictions.

## Architecture Overview

```
                         ┌──────────────────────────┐
                         │     Entry Point           │
                         │  (User Query / Brief)     │
                         └──────────┬───────────────┘
                                    │
                         ┌──────────▼───────────────┐
                         │    Orchestrator           │
                         │  (Problem Classification  │
                         │   & Agent Routing)        │
                         └──────────┬───────────────┘
                                    │
           ┌────────────────────────┼────────────────────────┐
           │                        │                        │
           ▼                        ▼                        ▼
   ┌───────────────┐      ┌─────────────────┐      ┌─────────────────┐
   │ Primary Agent  │      │ Supporting Agent │      │ Quality Agent   │
   │ (Domain Lead)  │◄────►│ (Research / QA)  │      │ (Review / Audit)│
   └───────────────┘      └─────────────────┘      └─────────────────┘
           │                        │                        │
           └────────────────────────┼────────────────────────┘
                                    │
                         ┌──────────▼───────────────┐
                         │     Output Assembly       │
                         │  (Document / Opinion /    │
                         │   Strategy / Filing)      │
                         └──────────────────────────┘
```

## The 10 Domains

| Domain | Agents | Core Function |
|--------|--------|---------------|
| **Compliance** | Privacy, Cybersecurity | Advisory on regulatory obligations, breach response, compliance gap analysis |
| **Governance** | DPIA, AI Governance, AI Audit | Impact assessments, governance frameworks, internal audits |
| **Litigation** | Digital Evidence, Constitutional Petition, Litigation Strategy, Pleading Drafting | Case strategy, evidence analysis, court filings |
| **Policy** | Regulatory Impact, Policy Drafting, Legislative Drafting | Institutional policy, Bills, Regulations, Statutory Instruments |
| **Research** | Legal Research, Comparative Law, Case Digest | Jurisdictional analysis, precedent mapping, case synthesis |
| **Sovereignty** | Digital Sovereignty | Data localisation, sovereign AI, compute infrastructure |
| **Strategy** | Technology Strategy, Regulatory Strategy | National roadmaps, regulatory engagement, market entry |
| **Teaching** | Curriculum, Expert Witness, Assessment | Course design, expert testimony preparation, assessment generation and evaluation |
| **Transactional** | Legal Opinion, DPA, Contract Drafting | Commercial agreements, regulatory opinions, data transfers |
| **Writing** | Weekly Article, LinkedIn, Book Writer | Legal publishing, thought leadership, manuscript drafting |

## How Agents Work Together

Agents are designed to operate both independently and in sequence. A typical multi-agent workflow follows this pattern:

```
Research Agent ──► Primary Domain Agent ──► Review Agent ──► Writing Agent
     │                     │                      │                │
     │  (case law,         │  (draft opinion,      │  (audit,       │  (publish,
     │   statutes,         │   pleading, policy,   │   quality      │   submit,
     │   comparative law)  │   agreement)          │   check)       │   file)
     ▼                     ▼                      ▼                ▼
```

## Using the System

**For a single legal task** — invoke the relevant agent directly using its prompt template and input specification.

**For a complex matter** — use the orchestrator to identify the primary agent, then chain supporting agents for research, review, and publication.

**For an organisation** — deploy the integration layer to connect agents with practice management systems, document automation, and LLM backends.

## Core Design Principles

1. **Uganda-first, globally aware** — every agent is calibrated to Ugandan law (Constitution 1995, DPA 2019, Computer Misuse Act, Evidence Act) and EAC frameworks, with structured references to EU GDPR, UK, US, India, Singapore, and China.

2. **Curriculum-aligned** — agents map to the modules of the Executive Fellowship curriculum, making them directly usable for teaching, assessment, and capstone projects.

3. **Practitioner-ready** — each agent includes a quality checklist, common errors table, expert mode guidance, and worked example invocations.

4. **Composable** — agents are designed to be chained: Research → Draft → Review → Publish.

## File Map

```
skills/
├── compliance/
│   ├── privacy_compliance_agent.md
│   └── cybersecurity_compliance_agent.md
├── governance/
│   ├── dpia_agent.md
│   ├── ai_governance_agent.md
│   └── ai_audit_agent.md
├── litigation/
│   ├── digital_evidence_agent.md
│   ├── constitutional_petition_agent.md
│   ├── litigation_agent.md
│   └── pleading_drafting_agent.md
├── policy/
│   ├── regulatory_impact_agent.md
│   ├── policy_drafting_agent.md
│   └── legislative_drafting_agent.md
├── research/
│   ├── legal_research_agent.md
│   ├── comparative_law_agent.md
│   └── case_digest_agent.md
├── sovereignty/
│   └── digital_sovereignty_agent.md
├── strategy/
│   ├── technology_strategy_agent.md
│   └── regulatory_strategy_agent.md
├── teaching/
│   ├── curriculum_agent.md
│   ├── expert_witness_agent.md
│   └── assessment_agent.md
├── transactional/
│   ├── legal_opinion_agent.md
│   ├── dpa_agent.md
│   └── contract_drafting_agent.md
└── writing/
    ├── weekly_article_agent.md
    ├── linkedin_writer_agent.md
    └── book_writer_agent.md
```

## Quick Start

```bash
# Identify the agent you need from the domain table above
# Read its specification:
cat skills/litigation/pleading_drafting_agent.md

# Follow the prompt template to invoke the agent
# Chain with supporting agents as needed
# Use the quality checklist to validate output
```

See [orchestrator.md](orchestrator.md) for the routing framework, [scenarios.md](scenarios.md) for worked multi-agent examples, and [integration.md](integration.md) for deployment options.
