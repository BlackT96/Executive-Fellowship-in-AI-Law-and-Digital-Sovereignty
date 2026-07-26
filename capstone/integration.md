# Integration — Deploying the Agent System

## Deployment Models

The 26 agents are standalone skill specifications that can be deployed through multiple channels.

---

### Model 1: Direct LLM Usage (Simplest)

Each agent's **Prompt Template** section contains a ready-to-use system prompt. Copy the agent's full specification as a system prompt, append the user's specific facts, and invoke.

```
System: [Full agent markdown as system context]
User: [Client facts, legal question, documents]
```

**Best for:** Individual practitioners, ad hoc use.

**Requirements:** Access to an LLM (any model) with sufficient context window.

---

### Model 2: Agent Router (CLI / API)

Build a lightweight router that:
1. Accepts a user query
2. Classifies it using the orchestrator decision tree
3. Loads the appropriate agent specification
4. Assembles the prompt
5. Returns the agent's output

**Architecture:**

```
User Query
    │
    ▼
┌─────────────────────┐
│  Classifier Module  │  ──►  Rule-based or LLM-based
│  (orchestrator.md)  │        classification
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  Agent Selector     │  ──►  Map domain + task → agent file
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  Prompt Assembler   │  ──►  Agent spec + user data → final prompt
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  LLM Invocation     │  ──►  API call to LLM provider
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  Output Processor   │  ──►  Format validation, quality check
└─────────────────────┘
```

**Best for:** Law firms, legal departments, regulatory bodies.

**Technology options:**
- Python (FastAPI) / Node.js (Express) / Go
- LangChain or custom LLM wrapper
- Local LLM (Llama, Mistral) or cloud API (GPT, Claude, Gemini)

---

### Model 3: Multi-Agent Orchestrator (Advanced)

Chain multiple agents automatically. For complex matters, the orchestrator:
1. Receives the client brief
2. Decomposes into sub-tasks
3. Routes each sub-task to the appropriate agent
4. Assembles outputs into a coherent deliverable

```
┌─────────────────────┐
│  Brief Decomposer   │  ──►  Split matter into sub-problems
└──────────┬──────────┘
           │
    ┌──────┼──────┐
    │      │      │
    ▼      ▼      ▼
 Agent  Agent  Agent
    │      │      │
    └──────┼──────┘
           │
           ▼
┌─────────────────────┐
│  Output Assembler   │  ──►  Merge, cross-reference, format
└─────────────────────┘
```

**Best for:** Complex cross-disciplinary matters (data breach litigation, national AI policy).

---

### Model 4: Law Firm Practice System

Integrate agents with existing firm infrastructure:

```
┌─────────────────────────────────────────────┐
│           Practice Management System        │
│  (Clio, PracticePanther, LEAP, Custom)      │
└─────────────────────┬───────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────┐
│           Document Management System        │
│  (iManage, NetDocuments, SharePoint)        │
└─────────────────────┬───────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────┐
│           Agent Router Service              │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  │
│  │ Research │  │ Drafting │  │ Review   │  │
│  │ Agents   │  │ Agents   │  │ Agents   │  │
│  └──────────┘  └──────────┘  └──────────┘  │
└─────────────────────┬───────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────┐
│           LLM Backend                       │
│  (Local / Cloud / Hybrid)                   │
└─────────────────────────────────────────────┘
```

**Best for:** Full-service law firms, in-house legal departments.

---

## Implementation Checklist

### Phase 1: Foundation

- [ ] Choose deployment model (1-4)
- [ ] Set up LLM access (API keys or local model)
- [ ] Load all 26 agent specifications
- [ ] Build or configure the classifier using orchestrator.md

### Phase 2: Core Routing

- [ ] Map domain classification → agent file paths
- [ ] Build prompt assembler (agent spec + user input)
- [ ] Implement output validation against agent's quality checklist
- [ ] Test with single-agent queries

### Phase 3: Multi-Agent Workflows

- [ ] Implement brief decomposition
- [ ] Build cross-agent data passing
- [ ] Implement output assembly (merge agent outputs)
- [ ] Test with Scenarios 1-6

### Phase 4: Production

- [ ] Add authentication and access control
- [ ] Add document storage and retrieval
- [ ] Add audit logging (which agent produced what)
- [ ] Add feedback loop (user corrections → agent refinement)
- [ ] Deploy (on-premise or cloud)

---

## Sample Implementation (Python — FastAPI)

```python
# app.py — Minimal agent router
from fastapi import FastAPI
from pydantic import BaseModel
import json, os

app = FastAPI(title="AI Law Agent System")

AGENTS_DIR = "C:\\Users\\DELL\\research\\skills"

class Query(BaseModel):
    text: str
    domain: str | None = None  # Optional: override classification

class AgentRequest(BaseModel):
    query: Query
    agent_path: str
    user_context: dict = {}

def classify_domain(query: str) -> str:
    """Simple keyword-based classification (use LLM for production)."""
    domain_keywords = {
        "privacy|data protection|ndpc|consent": "compliance/privacy_compliance_agent.md",
        "breach|incident|ransomware|cyber": "compliance/cybersecurity_compliance_agent.md",
        "dpia|impact assessment|high-risk": "governance/dpia_agent.md",
        "petition|constitutional|digital rights": "litigation/constitutional_petition_agent.md",
        "pleading|plaint|defence|counterclaim": "litigation/pleading_drafting_agent.md",
        "policy|framework|guidelines": "policy/policy_drafting_agent.md",
        "bill|legislation|regulation|statutory": "policy/legislative_drafting_agent.md",
        "contract|agreement|saas|licence": "transactional/contract_drafting_agent.md",
        "opinion|legal position|interpretation": "transactional/legal_opinion_agent.md",
        "article|weekly|thought leadership": "writing/weekly_article_agent.md",
    }
    for keywords, path in domain_keywords.items():
        if any(kw in query.lower() for kw in keywords.split("|")):
            return path
    return "research/legal_research_agent.md"  # fallback

def load_agent_spec(path: str) -> str:
    full_path = os.path.join(AGENTS_DIR, path)
    with open(full_path, "r", encoding="utf-8") as f:
        return f.read()

def build_prompt(spec: str, query: Query, context: dict) -> str:
    return f"{spec}\n\n---\n\nUser Query: {query.text}\n\nContext: {json.dumps(context)}"

@app.post("/route")
async def route(request: AgentRequest):
    """Route query to agent and get response."""
    agent_path = request.query.domain or classify_domain(request.query.text)
    spec = load_agent_spec(agent_path)
    prompt = build_prompt(spec, request.query, request.user_context)
    # LLM call goes here
    return {
        "agent": agent_path,
        "prompt": prompt,
        "note": "Replace with actual LLM invocation"
    }

@app.get("/agents")
async def list_agents():
    """List all available agents by domain."""
    agents = {}
    for domain in os.listdir(AGENTS_DIR):
        domain_path = os.path.join(AGENTS_DIR, domain)
        if os.path.isdir(domain_path):
            agents[domain] = os.listdir(domain_path)
    return agents
```

---

## Security & Ethics Considerations

| Concern | Mitigation |
|---|---|
| Client confidentiality | Deploy on-premise or use LLMs with guaranteed data isolation. Ensure no training on client data. |
| Hallucination risk | Use each agent's quality checklist. Implement human-in-the-loop review for all output. |
| Jurisdictional accuracy | Agents are calibrated to Uganda/EAC. Always verify citations against current law. |
| Unauthorised practice of law | Agents are tools for qualified lawyers, not substitutes. Disclaimers required. |
| Data localisation | Comply with Uganda DPA data localisation requirements if processing client data in cloud. |

## Maintenance

- **Quarterly:** Update agent references to reflect new legislation (new Acts, Regulations, case law)
- **Per-matter:** Log feedback (what the agent got right/wrong) to improve prompts
- **Curriculum updates:** Sync agent content with curriculum revisions
