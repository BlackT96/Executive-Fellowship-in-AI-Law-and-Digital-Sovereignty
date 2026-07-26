# Week 4: APIs, Cloud Computing & SDLC — Reading Notes for Legal Practitioners

**Module 1:** Digital Technology Fundamentals
**Program:** Executive Fellowship (AI Law & Digital Sovereignty)
**Target Audience:** Lawyers with no prior computing background
**Status:** Book Manuscript — Chapter 4

---

## How to Use These Notes

Each section follows the same structure:
1. **Plain-English Explanation** — what it is, in everyday language
2. **Practical Illustration** — a concrete example tied to legal practice
3. **Why It Matters for a Lawyer** — the legal significance
4. **Legal Framework** — relevant Ugandan statutes, regulations, and international instruments

---

# PART 1: APPLICATION PROGRAMMING INTERFACES (APIs)

## 1.1 What is an API? The Waiter Analogy

Imagine you are at a restaurant. You are sitting at your table (the **client**). The kitchen (the **server**) has all the food and capabilities. But you cannot walk into the kitchen and cook for yourself — that would be chaos. Instead, a **waiter** brings your order to the kitchen and returns with your food.

The waiter is the **API**. It is a messenger that takes requests, tells the kitchen what to do, and returns the response to you.

| Real World | Technical World |
|---|---|
| You (customer) | Client application (mobile app, website) |
| Waiter | API (Application Programming Interface) |
| Kitchen | Server (back-end system, database) |
| Menu | API documentation (endpoints available) |
| Your order ("I want chicken and chips") | API request (HTTP method + endpoint + data) |
| Food returned to your table | API response (data in JSON/XML format) |
| Kitchen rules ("No substitutions") | API schema and validation rules |

**Plain English:** An API is a set of rules that allows one piece of software to talk to another. It defines what requests can be made, how to make them, and what format the response will take. It is the contract between two systems.

**Practical Illustration — MTN Mobile Money API:**
When a fintech app like "PesaPal" wants to check whether a customer has enough money in their MTN Mobile Money account to make a payment, it does not access MTN's database directly. Instead, it sends an API request to MTN's server:
- "Hey MTN, can you tell me the balance of account 0771000111?"
- The API verifies the request is authorised, checks the balance, and sends back: "Balance is UGX 500,000."

The fintech never sees MTN's database. It only sees what the API allows it to see.

**Why this matters for a lawyer:**
- If a transaction fails and money is lost, the API log is the evidence trail
- If unauthorised data is exposed, the API security configuration determines who is liable
- If a third-party API goes down, the SLA attached to that API determines whether there is a remedy
- If an API returns incorrect data, you need to know whether the error is in the API itself or in the system behind it

---

## 1.2 RESTful Architecture — The Most Common API Type

Not all APIs are built the same way. The most common type used in web and mobile applications today is called **REST** (Representational State Transfer).

**Plain English:** REST is a set of design principles that makes APIs simple, predictable, and scalable. It uses the same structure as the World Wide Web itself — which is why REST APIs are sometimes called "Web APIs."

**Key characteristics of REST:**

1. **Stateless** — Each request from a client to the server must contain all the information the server needs. The server does not remember previous requests. Imagine a client meeting where you have to reintroduce yourself at every meeting because the lawyer does not keep notes between meetings.

2. **Resource-based** — Everything is a "resource" (a customer, a payment, an invoice), and each resource has a unique address (URL/endpoint).

3. **Standard operations** — REST uses standard HTTP methods (verbs) to operate on resources, just like the web.

**Why this matters for a lawyer:**
The stateless nature of REST means each API call is self-contained. If you subpoena API logs, you should see complete records of every transaction — each log entry contains all the information needed to understand what happened. There is no hidden "state" on the server that changes how requests are processed.

---

## 1.3 API Endpoints and HTTP Verbs

### 1.3.1 Endpoints (URLs)

An endpoint is the specific address where an API can be accessed. Think of it as a specific desk in a government office — each desk handles a specific type of request.

**Example — A Bank's API Endpoints:**

| Endpoint | What it does |
|---|---|
| `https://api.bank.co.ug/customers` | Access customer records |
| `https://api.bank.co.ug/customers/123` | Access a specific customer (ID 123) |
| `https://api.bank.co.ug/accounts` | Access account records |
| `https://api.bank.co.ug/transactions` | Access transaction records |
| `https://api.bank.co.ug/payments` | Initiate or view payments |

**Plain English:** An endpoint is like a URL in your browser. When you type `www.ulii.org/akn/ug/act/2019/9/eng@2019-05-03`, you are accessing a specific resource (the DPA Act) at a specific location. APIs work the same way, but for software-to-software communication.

### 1.3.2 HTTP Verbs (Methods)

HTTP verbs tell the API what action to perform on the resource. They are the "verbs" of the API language.

| HTTP Verb | Action | Legal Analogy |
|---|---|---|
| **GET** | Retrieve data (read) | Requesting a copy of a court file — you are just looking, not changing anything |
| **POST** | Create new data | Filing a new claim — you are submitting something new |
| **PUT** | Replace existing data | Amending a pleadings — you are replacing the entire document with an updated version |
| **PATCH** | Partially update data | Correcting a typo in a filed document — you change only the error |
| **DELETE** | Remove data | Withdrawing a claim — you are removing something that exists |

**Practical Illustration — A Law Firm's API:**

A law firm's case management system exposes an API. When a paralegal updates a client's contact details through the web interface, the browser sends:
- `PATCH https://api.firm.co.ug/clients/456` with the new phone number
- The API receives it, validates it, updates the database, and returns: `{ "status": "updated", "clientId": 456 }`

**Why this matters for a lawyer:**
If you are investigating whether data was improperly accessed or modified, the HTTP verb tells you what happened:
- A **GET** request to `/customers` with no filters could indicate data scraping
- A **DELETE** request to `/transactions/789` could indicate evidence tampering
- A **POST** request to `/customers` with incorrect data could indicate fraudulent account creation

API logs typically record the verb, endpoint, timestamp, user identity, and response status. This is your evidence chain.

---

## 1.4 Payloads — JSON and XML

When an API sends or receives data, that data is packaged in a specific format. The two most common formats are **JSON** (JavaScript Object Notation) and **XML** (eXtensible Markup Language).

**Plain English:** A payload is the actual data being carried by the API message. Think of it as the envelope containing the letter — the API request/response is the postal service, the payload is the letter inside.

### JSON — The Modern Standard

JSON is the most common API data format today. It is lightweight, easy for both computers and humans to read, and uses a simple key-value structure.

**Example — JSON Payload for a Mobile Money Transfer Request:**
```json
{
  "sender": "+256771000111",
  "recipient": "+256772000222",
  "amount": 50000,
  "currency": "UGX",
  "reference": "INV-2026-001",
  "timestamp": "2026-07-20T14:30:00Z"
}
```

**Example — JSON Response (Success):**
```json
{
  "status": "success",
  "transactionId": "TXN-789012",
  "message": "Transfer completed"
}
```

**Example — JSON Response (Error):**
```json
{
  "status": "error",
  "code": "INSUFFICIENT_BALANCE",
  "message": "Sender has insufficient funds. Available: UGX 30,000. Requested: UGX 50,000."
}
```

### XML — The Older Standard

XML is older, more verbose, and less common in modern APIs, but still used in banking and government systems.

**Same data in XML:**
```xml
<transfer>
  <sender>+256771000111</sender>
  <recipient>+256772000222</recipient>
  <amount>50000</amount>
  <currency>UGX</currency>
  <reference>INV-2026-001</reference>
  <timestamp>2026-07-20T14:30:00Z</timestamp>
</transfer>
```

**Why the format matters for a lawyer:**
- JSON is more compact, making it harder to hide extra data fields
- XML supports attributes and namespaces, which can add complexity to the data structure
- When requesting data in discovery, specify: "Produce all API request and response payloads in their native format (JSON or XML) with full field definitions"

The key forensic question: **"Was the data in the API payload exactly what the user authorised, or could additional fields have been included without the user's knowledge?"** This is a data minimisation question under the DPA.

---

## 1.5 API Authentication — OAuth, API Keys, and Tokens

How does a server know who is making an API request? This is **authentication**. There are three common methods.

### 1.5.1 API Keys

The simplest method. A long string of characters that identifies the client application.

**Example:** `X-API-Key: a1b2c3d4e5f6g7h8i9j0`

**Analogy:** A building access card. Anyone holding the card can enter. If the card is lost or stolen, anyone can use it.

### 1.5.2 OAuth 2.0 — The Modern Standard

OAuth (Open Authorisation) is a more secure framework. Instead of sharing a password, the client receives a temporary **token** that grants limited access for a limited time.

**Analogy:** A visitor's pass at a secured office building. You present your ID at reception, they verify who you are, and issue a temporary badge that only gives access to specific floors. The badge expires at 5:00 PM.

**How it works in practice:**
1. The user logs into their mobile banking app with their username and password
2. The app sends these credentials to the bank's authentication server
3. The authentication server returns a **token** (a short-lived digital pass)
4. The app uses this token for all subsequent API calls
5. The token expires after a set period (e.g., 15 minutes)

### 1.5.3 Token Authentication (JWT)

A JSON Web Token (JWT) is a self-contained token that carries the user's identity and permissions within the token itself. It is digitally signed so it cannot be forged.

**Analogy:** A notarised letter of introduction. The letter contains who you are, what you are authorised to do, and the notary's seal confirms it is genuine. Anyone who trusts the notary can accept the letter without calling the notary to verify.

**Why this matters for a lawyer:**
- If a data breach occurs via an API, the first question is: **"How was the API authenticated? Was a compromised API key used? Was an OAuth token stolen?"**
- If an employee exfiltrates data via an API, the token log will show whose credentials were used
- If OAuth was used, the token expiry time is relevant — a response saying "the session was still active" when the employee had left the company could indicate a security control failure
- Under **DPA Section 20**, the data controller must implement "appropriate, reasonable, technical and organisational measures." The choice of authentication method is directly relevant to whether this duty was discharged.

---

## 1.6 API Security — The OWASP API Security Top 10

The Open Web Application Security Project (OWASP) publishes the industry standard for API security risks. The current version (2023) identifies the top 10 API security risks:

| Rank | Risk | What it means |
|---|---|---|
| API1 | Broken Object Level Authorization | User A can access User B's data by changing an ID in the API request |
| API2 | Broken Authentication | Weak or compromised authentication allows unauthorised access |
| API3 | Broken Object Property Level Authorization | API returns more data than the user should see (excessive data exposure) |
| API4 | Unrestricted Resource Consumption | No rate limiting — an attacker can flood the API with requests |
| API5 | Broken Function Level Authorization | Regular user can access admin functions |
| API6 | Unrestricted Access to Sensitive Business Flows | Automated bots abuse business logic (e.g., scalpers buying tickets) |
| API7 | Server Side Request Forgery | Attacker tricks the server into making requests to internal systems |
| API8 | Security Misconfiguration | Default passwords, unpatched systems, unnecessary features enabled |
| API9 | Improper Inventory Management | Deprecated API versions still accessible — no longer patched |
| API10 | Unsafe Consumption of APIs | Client blindly trusts third-party API responses |

**Practical Illustration — Broken Object Level Authorization (API1):**

A mobile money app has an API endpoint: `GET https://api.momo.co.ug/transactions/{id}`

The app intends for the user to see only their own transactions. But if the API does not verify that the logged-in user owns transaction ID `TXN-789012`, then:
- User A can change the URL to `.../transactions/TXN-789013` and see User B's transactions
- User A can enumerate all transactions in the system simply by incrementing the ID

This is the most common API vulnerability — and it is entirely a **legal compliance failure** under DPA Section 20.

**Why this matters for a lawyer:**
The OWASP API Security Top 10 is not a law, but it is the **generally accepted information security practice** referred to in **DPA Section 20(3)**, which requires data controllers to "observe generally accepted information security practices and procedures." If an API breach occurs and the organisation had not addressed the relevant OWASP risks, this is evidence that the organisation failed to meet its statutory duty.

**Cross-examination question:** "Were you aware of the OWASP API Security Top 10 at the time of the breach? Which of the ten risks had you assessed for your API? Please produce the API security assessment report."

---

## 1.7 Real-World Example: UGHub — Uganda's National API Gateway

This is not a hypothetical. Uganda already has a national API platform.

**What is UGHub?**
UGHub is the Government of Uganda's enterprise API gateway, operated by NITA-U. It runs on **WSO2 API Manager** and **WSO2 Integrator** — the same technology used by major global enterprises. As of 2026, it connects **over 135 government entities**, enabling secure data exchange between ministries, departments, and agencies (MDAs).

**What it does:**
- Provides a single, secure entry point for all government API traffic
- Enforces authentication and authorisation policies centrally
- Logs all API traffic for audit purposes
- Enables data sharing between MDAs without direct database access

**Why this matters for a lawyer:**
- If you are litigating against a government agency, the API logs from UGHub may contain the evidence you need
- If you are advising a contractor building a system that integrates with government data, they must comply with UGHub's API security requirements
- UGHub demonstrates that Uganda already has an API regulatory infrastructure — it is not a theoretical concept

---

## 1.8 Legal Framework for APIs

### Electronic Transactions Act, Cap. 99, Sections 29–33 — Service Provider Liability

These are the most important statutory provisions for APIs in Uganda. They determine when a service provider (including an API provider) is liable for third-party data.

**Section 29 — Liability of a service provider:**
A service provider is **not** liable for third-party material to which it merely provides access, if the liability is founded on:
- (a) making, publication, dissemination or distribution of the material; or
- (b) infringement of any rights in the material.

**However**, this exemption does not affect:
- (a) contractual obligations
- (b) obligations under a licensing or regulatory framework
- (c) obligations imposed by law or court order to remove, block, or deny access

**Section 30 — Information location tools:**
A service provider that links or refers users to infringing material is not liable if it:
- (a) does not have actual knowledge of the infringement
- (b) is not aware of facts indicating infringement
- (c) does not receive direct financial benefit
- (d) removes or disables access after being notified

**Section 31 — Notification procedure:**
A person claiming infringement must notify the service provider in writing with full details, including the right allegedly infringed, description of the material, remedial action required, and a declaration of good faith. False statements attract liability.

**Section 32 — No duty to monitor:**
A service provider is not obliged to monitor data it transmits or stores, or to actively seek out unlawful activity.

**Practical application to APIs:**
- An API provider that merely transmits data between parties may benefit from the Section 29 liability exemption
- **But** the exemption does not apply if the API provider has a **contractual obligation** (Section 29(2)(a)) — this is why cloud SLAs matter
- If the API provider processes or stores data (not merely transmits), it may be a **data processor** under the DPA, with separate obligations
- The "notice and takedown" procedure in Section 31 applies when an API is used to distribute infringing content

### Data Protection and Privacy Act, 2019, Section 20 — Security Measures

**Section 20(1):** A data controller, data collector, or data processor shall secure the integrity of personal data by adopting **appropriate, reasonable, technical and organisational measures** to prevent:
- Loss, damage, or unauthorised destruction
- Unlawful access to or unauthorised processing of personal data

**Section 20(2):** The data controller shall:
- (a) identify reasonably foreseeable internal and external risks
- (b) establish and maintain appropriate safeguards
- (c) regularly verify that safeguards are effectively implemented
- (d) continually update safeguards in response to new risks or deficiencies

**Section 20(3):** The data controller shall observe **generally accepted information security practices and procedures** and specific industry or professional rules.

**Application to APIs:**
- API security is a **legal requirement**, not optional — DPA Section 20 mandates it
- The OWASP API Security Top 10 constitutes "generally accepted information security practices" — failure to address them is evidence of non-compliance
- API authentication, authorisation, encryption, and logging are all "technical and organisational measures" under Section 20
- Regular verification (Section 20(2)(c)) means periodic API security testing — penetration testing, vulnerability assessments

### Data Protection and Privacy Regulations, 2021, Regulations 31–33

**Regulation 31 — Publication of personal data security practices and procedures:**
Data controllers must publish their security practices, including technical measures for data protection.

**Regulation 32 — Security measures by data controller:**
Requires specific technical and organisational security measures, including access control, data encryption, and system monitoring.

**Regulation 33 — Notification of data security breaches:**
Data controllers must notify the Personal Data Protection Office (PDPO) of any data breach that poses a risk to the rights and freedoms of data subjects.

**Application to APIs:**
- An API breach that exposes personal data triggers the mandatory breach notification obligation under Regulation 33
- The 72-hour notification timeline (aligned with global standards) means API security monitoring must be in place to detect breaches promptly
- If an organisation cannot produce API audit logs after a breach, that is a compliance failure under Regulation 32

### Uganda Communications Act, Cap. 103 — Conditional Application

The UCC Act applies to **licensed communications operators**. If the API provider is a licensed operator (e.g., MTN, Airtel, a licensed data communication service provider), additional obligations arise:

- **Section 5(o):** UCC regulates "interconnection and access systems between operators and users"
- **UCC (Interconnection and Access) Regulations 2019:** Govern how operators connect their systems — relevant to APIs that interconnect licensed operators
- **UCC (Quality of Service) Regulations 2019:** Set minimum standards for service availability, latency, and reliability — relevant to API performance and SLAs

**When UCC applies to an API:**
- The API is provided by a licensed telecommunications operator
- The API facilitates interconnection between licensed operators (e.g., MTN MoMo API connecting to Airtel Money)
- The API is part of a "data communication service" offered to the public

**When UCC does NOT apply:**
- A standard fintech or healthtech company using APIs for its own operations
- Internal enterprise APIs
- APIs provided by non-licensed entities

---

## 1.9 Cross-Examination Questions for API Evidence

### For API Authentication and Access
1. "What authentication method did your API use — API keys, OAuth 2.0, or something else?"
2. "Were API keys stored in plain text or encrypted?"
3. "What was the token expiry period for OAuth tokens?"
4. "Was multi-factor authentication required for administrative API access?"
5. "Can you produce the API access logs for the period in question?"

### For API Security
1. "Had you conducted an API security assessment based on the OWASP API Security Top 10?"
2. "When was the last API penetration test conducted, and can you produce the report?"
3. "Was your API tested for Broken Object Level Authorization (API1) — could User A access User B's data?"
4. "Were deprecated API versions still accessible, and were they still patched?"

### For API Data Integrity
1. "Can you produce the complete API request and response payloads for the disputed transaction?"
2. "Was the API payload logged before or after processing?"
3. "Could the API have returned incorrect data without logging an error?"
4. "What data validation did the API perform before processing the request?"

### For ETA Section 29 Liability
1. "Was the API merely transmitting data, or was it processing or storing data?"
2. "Did you have a contractual obligation to the API consumer that goes beyond mere transmission?"
3. "Were you notified of infringing activity under Section 31, and if so, what action did you take?"
4. "Did you have actual knowledge of the infringing activity at any point?"

---

# PART 2: CLOUD COMPUTING

## 2.1 What is Cloud Computing? The Renting Analogy

Imagine you need a place to store your law firm's files:

- **Option A — Buy and maintain your own building:** You purchase land, construct a building, install shelves, hire security, pay for electricity, maintain the roof, and manage everything yourself. This is **on-premise computing**.

- **Option B — Rent space in an existing building:** You pay monthly rent to a building owner who handles security, maintenance, electricity, and cleaning. You bring your own furniture and files. This is **Infrastructure as a Service (IaaS)** .

- **Option C — Rent a fully furnished office:** The building owner provides not just space, but also desks, chairs, computers, phones, and internet. You just bring your work. This is **Platform as a Service (PaaS)** .

- **Option D — Rent a serviced office with a receptionist:** Everything is provided — office, furniture, receptionist, cleaning, coffee. You just show up and work. This is **Software as a Service (SaaS)** .

| Model | Analogy | What you manage | What the provider manages |
|---|---|---|---|
| **On-Premise** | Own and maintain your building | Everything | Nothing |
| **IaaS** | Rent empty office space | Applications, data, OS, middleware | Servers, storage, networking, virtualisation |
| **PaaS** | Rent furnished office | Applications, data | Everything else |
| **SaaS** | Rent serviced office | Nothing — just use the software | Everything |

**Plain English:** Cloud computing is the delivery of computing services (servers, storage, databases, networking, software, analytics) over the internet ("the cloud"). You pay only for what you use, like a utility bill — similar to how you pay for electricity or water.

---

## 2.2 The Three Cloud Service Models

### 2.2.1 Infrastructure as a Service (IaaS)

**What it is:** You rent raw computing resources — virtual servers, storage, and networking — and install whatever software you want on them.

**Examples:** Amazon Web Services (AWS) EC2, Google Compute Engine, Microsoft Azure Virtual Machines.

**Legal analogy:** Renting bare land. You build whatever structure you want, but you are responsible for everything above the foundation.

**Practical Illustration — Law Firm Server:**
A law firm wants to run its case management system. Instead of buying a physical server and housing it in their office, they rent a virtual server from AWS. They install Ubuntu Linux, PostgreSQL, and their case management software themselves. If the server crashes, the firm is responsible for restoring the software — AWS is only responsible for the virtual hardware.

**Why it matters:** In IaaS, the customer has the most control but also the most responsibility. Under **DPA Section 20**, the customer (data controller) must implement technical measures — the IaaS provider is only responsible for the infrastructure layer.

### 2.2.2 Platform as a Service (PaaS)

**What it is:** You rent a complete platform — the operating system, middleware, database, and development tools — and deploy your own applications on top.

**Examples:** Google App Engine, Heroku, AWS Elastic Beanstalk.

**Legal analogy:** Renting a furnished apartment. The landlord provides the structure, plumbing, electricity, and appliances. You bring your furniture and decorations.

**Practical Illustration — Fintech Application:**
A fintech startup builds a mobile money application. Instead of managing servers, operating systems, and databases, they deploy their code to Google App Engine. Google automatically manages the underlying infrastructure, scales the application as demand grows, and handles security patches for the platform layer.

**Why it matters:** In PaaS, liability is shared. The provider is responsible for the platform's security. The customer is responsible for the application code deployed on it. The **DPA Section 21** requirement for a contract between data controller and data processor becomes critical — the PaaS agreement must specify each party's security obligations.

### 2.2.3 Software as a Service (SaaS)

**What it is:** You use a complete application provided by the vendor over the internet. You do not manage anything — just configure and use the software.

**Examples:** Google Workspace (Gmail, Docs), Microsoft 365, Salesforce, LexisNexis, Clio (legal practice management).

**Legal analogy:** Renting a hotel room. Everything is provided — bed, bathroom, TV, cleaning service. You just check in and use it.

**Practical Illustration — Cloud-Based Legal Research:**
A law firm subscribes to LexisNexis or a cloud-based legal research platform. Lawyers access it through a web browser. The provider manages everything — servers, databases, security, updates. The firm just uses the service.

**Why it matters:** In SaaS, the provider has the most control and therefore the most responsibility. However, the customer (data controller) still has obligations under the DPA — including ensuring the provider has adequate security measures. A SaaS agreement should include a **Data Processing Agreement (DPA)** that specifies the provider's obligations.

---

## 2.3 Cloud Deployment Models

### Public Cloud
Shared infrastructure, multiple customers, accessible over the public internet.
- **Examples:** AWS, Google Cloud, Microsoft Azure
- **Legal concern:** Data resides on shared infrastructure — who else might access it?

### Private Cloud
Dedicated infrastructure for a single organisation.
- **Examples:** A bank's private cloud, NITA-U National Data Centre
- **Legal concern:** Higher cost, but full control over data location and security

### Sovereign Cloud
A private cloud that is physically located within a specific country's borders, operated by or on behalf of that country's government, and subject exclusively to that country's laws.
- **Examples in East Africa:**
  - **Servernah** (Nairobi, Kenya) — Kenya's first sovereign AI cloud, launched June 2026
  - **Savannah Cloud** (Nairobi, Kenya) — Atlancis + EverseTech sovereign cloud
  - **Konza National Data Centre** (Kenya) — government data centre expansion
  - **Karuma AI Supercomputing Hub** (Uganda) — announced September 2025, first module 2026
  - **EAC Cloud** (Arusha, Tanzania) — regional multi-sectoral cloud for health data
  - **UniCloud Africa** — pan-African sovereign cloud, plans for Uganda, Kenya, Tanzania, Rwanda

**Why sovereign cloud matters for a Ugandan lawyer:**
- Data localisation is emerging as a regulatory requirement (Kenya Cloud Policy 2025, Rwanda enforcement against MTN)
- The AfCFTA Digital Trade Protocol (Article 22) prohibits mandatory data localisation, but allows exceptions for legitimate public policy and national security
- Ugandan government data must increasingly be hosted on sovereign infrastructure — UGHub and NITA-U's National Data Centre are part of this
- When drafting contracts, lawyers must specify: **where is data stored? Under which jurisdiction's laws? Who has access?**

---

## 2.4 Service Level Agreements (SLAs)

### 2.4.1 What is an SLA?

An SLA is the **contractual promise** of service quality. It defines measurable targets that the cloud provider must meet.

**Plain English:** An SLA is like a landlord's promise to maintain the building — keep the lifts working, fix leaks within 24 hours, ensure 24-hour security. If they fail, you get compensation (usually a credit against your rent).

### 2.4.2 Common SLA Metrics

| Metric | What it measures | Typical Promise |
|---|---|---|
| **Uptime / Availability** | Percentage of time the service is accessible | 99.9% ("three nines") = ~8.7 hours downtime/year |
| **Latency** | How fast the API responds | 95th percentile < 200ms |
| **Throughput** | How many requests can be handled | 10,000 requests per minute |
| **Error Rate** | Percentage of failed requests | < 0.1% error rate |
| **Recovery Time** | How fast service is restored after failure | < 4 hours |
| **Recovery Point** | How much data could be lost in a failure | < 15 minutes of data |

### 2.4.3 The "Nines" — Uptime Explained

| Uptime % | Downtime per Year | Downtime per Month |
|---|---|---|
| 99% ("two nines") | 3.65 days | 7.2 hours |
| 99.9% ("three nines") | 8.76 hours | 43.2 minutes |
| 99.99% ("four nines") | 52.56 minutes | 4.32 minutes |
| 99.999% ("five nines") | 5.26 minutes | 25.9 seconds |

**Why this matters:** A 99% SLA sounds good to a non-technical person. But 3.65 days of downtime per year could be catastrophic for a mobile money platform. The lawyer's job is to understand what the numbers actually mean.

### 2.4.4 The Problem with SLA Remedies

Most cloud SLAs do not pay you cash when they fail. Instead, they give you a **service credit** — a percentage of your monthly fee credited to your next bill.

**Typical SLA credit structure:**
| Uptime | Credit |
|---|---|
| 99.0% – 99.9% | 10% credit |
| 95.0% – 99.0% | 25% credit |
| < 95.0% | 50% credit |

**The trap for lawyers:** If a mobile money platform generates UGX 500 million per month and the cloud provider's outage causes UGX 50 million in losses, the SLA credit might be UGX 5 million (1% of monthly fee). The SLA is the **exclusive remedy** — you cannot sue for the actual loss.

**Cross-examination question:** "Is it correct that the SLA credit is the sole and exclusive remedy for any service failure, regardless of the actual loss suffered by the customer?"

---

## 2.5 Legal Framework for Cloud Computing

### The Controller-Processor Framework (DPA Sections 20-22)

Under the DPA, cloud service providers are typically **data processors** — they process personal data on behalf of the customer (the **data controller**).

**Section 21** — Security measures relating to data processed by data processor:
- A data controller shall not permit a data processor to process personal data unless the processor establishes and complies with the security measures under the Act
- The contract between controller and processor **must** require the processor to establish and maintain confidentiality and security measures

**Practical implication:** Every cloud services agreement involving personal data must include a **Data Processing Agreement (DPA)** that:
1. Defines what personal data is being processed
2. Specifies the security measures the cloud provider will implement
3. Restricts sub-processing (the cloud provider using other providers)
4. Requires breach notification
5. Ensures data is returned or deleted at the end of the contract

### ETA Sections 29-33 — Application to Cloud Services

The ETA liability framework applies to cloud providers as "service providers." The key question is whether the cloud provider is **merely transmitting** data (protected by Section 29) or **processing/storing** data (separate obligations apply).

### UCC (Quality of Service) Regulations 2019 — For Licensed Operators

If the cloud customer is a licensed communications operator, the UCC QoS Regulations impose minimum service standards:
- Network availability standards
- Call completion rates
- Fault repair times
- Customer complaint handling

These regulations effectively **override** contractual SLA terms if the contractual terms are weaker.

### UNCITRAL Notes on Cloud Computing Contracts (2019)

The United Nations Commission on International Trade Law (UNCITRAL) published the most authoritative international soft-law instrument on cloud contracts. Key recommendations:

1. **Liability allocation:** Clearly define which party is responsible for which layer of the cloud stack
2. **Data protection:** Include specific provisions on data location, access, and deletion
3. **Service levels:** Define measurable, enforceable SLA metrics
4. **Limitation of liability:** Caps should be reasonable and proportionate — not nominal
5. **Termination and transition:** Ensure data can be retrieved when the contract ends
6. **Sub-processing:** Require prior consent before the provider engages sub-processors
7. **Audit rights:** The customer must have the right to verify the provider's security measures

**Practical significance:** These Notes are not binding law, but they represent international best practice. A Ugandan court may have regard to them as persuasive authority in interpreting cloud contracts, particularly where Ugandan law is silent.

---

## 2.6 Data Localisation and Cross-Border Cloud Storage

### The Current East African Landscape

| Jurisdiction | Data Localisation Requirement | Source |
|---|---|---|
| **Uganda** | No explicit data localisation law. DPPA restricts cross-border transfers unless the destination has adequate protection or the data subject consents. | DPPA Section 26 |
| **Kenya** | Data localisation for certain categories under Kenya Cloud Policy 2025. Section 50 DPA requires processing through a local data server for public interest data. | Kenya Cloud Policy (May 2025), DPA Section 50 |
| **Rwanda** | Data localisation enforced. MTN Rwanda fined FRw 7.03 billion (USD 8.2M) for transferring data outside Rwanda without authorisation. | RURA Regulations 2016 |
| **Tanzania** | No explicit data localisation law. | PDPC Act 2022 |
| **EAC Level** | Harmonised cross-border data flows framework under development (validated June 2026). | EAC/EARDIP |
| **AfCFTA** | Article 22 prohibits mandatory data localisation (with exceptions for legitimate public policy and national security). | AfCFTA Digital Trade Protocol 2024 (not yet ratified) |

**Why this matters for cloud contracting:**
- A cloud contract that stores Ugandan data in Kenya, Rwanda, or South Africa may trigger cross-border transfer restrictions
- The AfCFTA Digital Trade Protocol (Article 22) may eventually limit data localisation requirements, but it is not yet ratified
- The emerging EAC harmonised framework (validated June 2026) may change the landscape further
- For now, the safest approach is to require that personal data of Ugandan citizens be stored in Uganda or in a jurisdiction with equivalent data protection

---

## 2.7 Cross-Examination Questions for Cloud Disputes

### For SLA Failures
1. "What was the promised uptime percentage in your SLA?"
2. "Can you produce the uptime calculation for the month in dispute?"
3. "Was the downtime measured from when the provider became aware, or from when the customer reported it?"
4. "Did the SLA exclude scheduled maintenance from the uptime calculation? How much scheduled maintenance occurred?"

### For Data Location
1. "In which country or countries was the data physically stored?"
2. "Was this disclosed in the cloud services agreement?"
3. "Did the provider have the right to transfer data to sub-processors in other jurisdictions?"
4. "Was a Transfer Impact Assessment conducted before the data was transferred across borders?"

### For Security
1. "What security certifications does the cloud provider hold (ISO 27001, SOC 2, etc.)?"
2. "Were these certifications current at the time of the breach?"
3. "Can you produce the cloud provider's security audit report for the relevant period?"
4. "Did the cloud provider notify you of the breach within the time required by DPA Regulation 33?"

### For Liability
1. "Is the SLA credit the exclusive remedy for service failure?"
2. "Does the limitation of liability clause exclude claims arising from data protection law?"
3. "Can you quantify the actual loss and compare it to the SLA credit the customer received?"
4. "Does the Data Processing Agreement (DPA) specify each party's liability for a data breach?"

---

# PART 3: THE SOFTWARE DEVELOPMENT LIFECYCLE (SDLC) & LLMOps

## 3.1 What is the SDLC? The House-Building Analogy

**Plain English:** The Software Development Lifecycle (SDLC) is the process used to build software applications. Just as a house is built in stages — foundation, walls, roof, plumbing, finishing — software is built in phases.

**The House Analogy:**

| SDLC Phase | House-Building Analogy | What Happens |
|---|---|---|
| **Requirements** | Architect meets with client | Determine what the software must do |
| **Design** | Architect draws blueprints | Plan how the software will be structured |
| **Development / Coding** | Construction workers build | Write the actual code |
| **Testing / QA** | Building inspector checks | Verify the software works correctly |
| **Deployment** | Client moves in | Release the software to users |
| **Maintenance** | Ongoing repairs and renovations | Fix bugs, add features, security patches |

**Why this matters for a lawyer:**
- Each phase generates **evidence** — requirements documents, design specifications, test results, deployment logs, maintenance records
- If software fails and causes loss, the SDLC documentation shows **who did what, when, and whether proper procedures were followed**
- Under the **DPA Section 20**, security must be built in from the **design phase** — not added after deployment

---

## 3.2 The Six Phases of the SDLC

### Phase 1: Requirements

**What happens:** The development team meets with stakeholders to determine what the software must do. This produces a **Requirements Specification** document.

**Legal significance:**
- The requirements specification is the **baseline** for determining whether the software performed as intended
- If the software does something it was not required to do, that is a **defect**
- If the software fails to do something it was required to do, that is a **breach of contract**
- Privacy requirements (data minimisation, consent, purpose limitation) should be specified here

**Cross-examination question:** "Does the requirements specification mention data protection or privacy requirements? If not, why not?"

### Phase 2: Design

**What happens:** Architects create the blueprint — system architecture, database schema, API design, security architecture.

**Legal significance:**
- This is where **privacy-by-design** and **security-by-design** must be embedded
- **DPA Section 20(2)(a)** requires identification of reasonably foreseeable risks — this happens in the design phase
- If security was not designed in from the start, it is much harder (and more expensive) to add later

**The PDPO's privacy-by-design initiative:**
In May 2026, Uganda's Personal Data Protection Office (PDPO) conducted a public consultation on **privacy-by-design regulations**. This signals that privacy-by-design will become a formal regulatory requirement in Uganda, not merely best practice.

**Cross-examination question:** "Was a Data Protection Impact Assessment (DPIA) conducted during the design phase? Can you produce it?"

### Phase 3: Development / Coding

**What happens:** Programmers write the actual code. This is the longest phase.

**Legal significance:**
- The code itself is **intellectual property** — who owns it?
- If third-party code (open source libraries) is used, the licence terms must be complied with
- If AI-assisted coding tools are used, who is liable for code quality?

**Cross-examination question:** "Was any third-party or open-source code used? What were the licence terms? Was a licence compliance audit conducted?"

### Phase 4: Testing / Quality Assurance

**What happens:** The software is tested to verify it works correctly. This includes:
- **Unit testing:** Testing individual components
- **Integration testing:** Testing that components work together
- **Security testing:** Testing for vulnerabilities (penetration testing, OWASP Top 10)
- **User acceptance testing:** Testing with real users

**Legal significance:**
- If the software causes loss because of a bug that testing should have caught, the adequacy of the testing process is directly relevant to liability
- **DPA Section 20(2)(c)** requires regular verification that safeguards are effective — this maps directly to security testing
- The **NIST SP 800-228** guidelines recommend API security testing throughout the API lifecycle — not just at the end

**Cross-examination question:** "Can you produce the test reports for the disputed feature? Was a security test conducted? What vulnerabilities were found and remediated?"

### Phase 5: Deployment

**What happens:** The software is released to users. This may be:
- A one-time release (Waterfall model)
- Continuous deployment (DevOps model)

**Legal significance:**
- The deployment log shows **when** the software was released and **what version**
- If a dispute arises about what the software did on a specific date, the deployment log establishes which version was running
- Under **ETA Section 8**, electronic records (including deployment logs) are admissible evidence

**Cross-examination question:** "Can you produce the deployment log showing which version of the software was running on the date of the disputed transaction?"

### Phase 6: Maintenance

**What happens:** After deployment, the software is monitored, bugs are fixed, security patches are applied, and new features are added.

**Legal significance:**
- Security patches must be applied promptly — failure to do so is a breach of **DPA Section 20(2)(d)** (continually updating safeguards)
- The maintenance log shows whether known vulnerabilities were addressed
- If a breach occurs because of an unpatched vulnerability that was known for months, the organisation faces increased liability

**Cross-examination question:** "When was the vulnerability that led to this breach first discovered? When was a patch available? When was the patch applied?"

---

## 3.3 Waterfall vs Agile vs DevOps

### Waterfall — The Traditional Approach

**Plain English:** Like building a house — complete the foundation before starting the walls, complete the walls before starting the roof. You cannot go back to an earlier phase without significant cost.

**When it is used:** Government systems, banking systems, safety-critical systems.

**Legal implication:** The contract should specify phase completion dates, acceptance criteria for each phase, and what happens if requirements change after the design phase is complete.

### Agile — The Modern Approach

**Plain English:** Like renovating a house room by room. Instead of planning everything upfront, you work in short cycles (sprints) — plan a little, build a little, test a little, then repeat. Each cycle delivers a working piece of the software.

**When it is used:** Startups, web applications, mobile apps, SaaS products.

**Legal implication:** Agile contracts need different terms — instead of fixed scope, they use:
- A **statement of work** that describes the overall vision
- **Sprint cycles** with deliverable increments
- **Change management** procedures for evolving requirements
- **Acceptance criteria** for each sprint deliverable

### DevOps — The Continuous Approach

**Plain English:** Like a restaurant that continuously improves its menu based on customer feedback, with the kitchen and serving staff working as one team. Development (Dev) and Operations (Ops) are combined into a single team that builds, tests, deploys, and monitors the software continuously.

**When it is used:** Cloud-native applications, SaaS platforms, high-velocity teams.

**Legal implication:** In DevOps, software changes may be deployed **many times per day**. The legal framework must address:
- Who authorises each deployment?
- What testing must occur before deployment?
- How are deployment logs maintained?
- What is the rollback procedure if a deployment fails?

### Comparison Table for Lawyers

| Aspect | Waterfall | Agile | DevOps |
|---|---|---|---|
| **Planning** | Complete upfront | Iterative, evolving | Continuous |
| **Documentation** | Comprehensive, detailed | Minimal, just-in-time | Automated from code |
| **Testing** | Dedicated phase | Throughout each sprint | Automated, continuous |
| **Deployment** | Single event at end | Every sprint (weeks) | Continuous (daily/hourly) |
| **Change cost** | High (late changes are expensive) | Low (expected) | Very low |
| **Best for** | Fixed requirements, regulated industries | Evolving products, startups | Cloud-native, high-velocity teams |
| **Legal risk** | Scope disputes, change orders | Scope creep, acceptance criteria | Deployment control, version tracking |

---

## 3.4 LLMOps — The SDLC for AI Models

**Plain English:** LLMOps (Large Language Model Operations) is the SDLC adapted for AI models. Just as traditional software has a lifecycle, AI models have a lifecycle — from training to deployment to monitoring.

**Why this is in Week 4:** The curriculum includes LLMOps alongside traditional SDLC because AI models are increasingly deployed through APIs on cloud infrastructure — connecting all three Week 4 topics.

### The LLMOps Lifecycle

| Phase | What Happens | Legal Concern |
|---|---|---|
| **Data Collection & Preparation** | Gather training data, clean it, label it | Data protection (DPA), copyright, consent |
| **Model Training & Tuning** | Train the model on the data | IP ownership of the model |
| **Testing & Evaluation** | Evaluate for accuracy, bias, safety | Bias under Article 21 Constitution |
| **Deployment** | Expose the model via an API | API security, SLA commitments |
| **Monitoring** | Track performance, drift, hallucinations | Liability for incorrect outputs |
| **Governance** | Audit logs, version control, rollback | Accountability, evidence |

**The LLMOps Governance Layer:**
LLMOps adds a governance layer that traditional SDLC does not have:
- **Data lineage:** Where did each piece of training data come from?
- **Bias detection:** Does the model treat different groups differently?
- **Explainability:** Can the model's decision be explained?
- **Human-in-the-loop:** Is a human required to verify certain outputs?
- **Hallucination detection:** Is the model generating false information?
- **Prompt security:** Is the model vulnerable to prompt injection attacks?

**Why this matters for a lawyer:**
- If an AI model deployed via API gives incorrect legal advice, the LLMOps governance log determines liability
- If the model was not monitored for drift (performance degradation over time), the deployer may be liable for relying on outdated outputs
- The **Kenya AI Bill 2026, Section 26** requires data logging for high-risk AI systems — this maps directly to LLMOps governance requirements

---

## 3.5 Legal Framework for the SDLC

### DPA Section 20 — The SDLC Compliance Mandate

Section 20 of the DPA transforms the SDLC from a technical choice into a **legal obligation**:

| SDLC Phase | DPA Section 20 Requirement | What This Means in Practice |
|---|---|---|
| **Requirements** | Identify foreseeable risks (S.20(2)(a)) | Privacy risks must be identified and documented at the start |
| **Design** | Establish appropriate safeguards (S.20(2)(b)) | Security must be designed into the architecture, not added later |
| **Testing** | Regularly verify safeguards are effective (S.20(2)(c)) | Security testing must be conducted and documented |
| **Deployment** | Apply organisational measures (S.20(1)) | Deployment procedures must include security checks |
| **Maintenance** | Continually update safeguards (S.20(2)(d)) | Patches and updates must be applied promptly |

### NITA-U National Information Security Framework (NISF) 2026

The **Updated NISF**, launched in July 2026, is the most current Ugandan government security framework. It introduces:
- **Minimum baseline security controls** for critical information infrastructure
- **A cybersecurity readiness assessment toolkit** for government entities
- Requirements aligned with international standards (ISO 27001, NIST)

**Application to SDLC:**
- The NISF requires that security be integrated into the system development lifecycle
- Government contractors must comply with NISF requirements — this should be written into procurement contracts
- The NISF references **ISO 27001 Annex A.8.25** (Secure Development Lifecycle) as the standard for SDLC security

### ETA Section 6 — Originality of Electronic Records

Section 6 of the ETA provides that an electronic record qualifies as an "original" if there is a **reliable assurance as to the integrity of the information** from the time it was first created.

**Application to SDLC documentation:**
- SDLC documentation (requirements, test reports, deployment logs) are electronic records
- If the SDLC tools used do not provide integrity assurance (tamper-proof logs, version control), the documentation may not qualify as an "original" under Section 6
- Using a **version control system** (e.g., Git) provides assurance of integrity — every change is tracked and attributable

### Evidence Act Cap. 6 — SDLC Documentation as Evidence

**Section 2:** Defines "document" to include electronic records — SDLC documentation is covered.
**Section 78:** Certified copies presumed genuine (rebuttable).
**Section 91:** Oral evidence cannot replace documentary evidence.

**Practical significance:** If litigation arises from a software failure, the SDLC documentation will be the primary evidence. If it does not exist, or if it exists but cannot be authenticated, the party relying on it faces an evidential hurdle.

---

## 3.6 Cross-Examination Questions for SDLC Failures

### For Requirements Phase
1. "Can you produce the requirements specification for the disputed feature?"
2. "Was a Data Protection Impact Assessment (DPIA) conducted during the requirements phase?"
3. "Were security requirements included in the specification?"
4. "Who approved the requirements specification?"

### For Design Phase
1. "Was a security architecture review conducted during the design phase?"
2. "Was the design reviewed by an independent security team?"
3. "Were data minimisation principles embedded in the database schema design?"
4. "Can you produce the design documents showing how security was architected?"

### For Testing Phase
1. "What testing was conducted before deployment?"
2. "Was security testing (penetration testing, vulnerability scanning) conducted?"
3. "Were the test results reviewed and approved before deployment?"
4. "Was the specific vulnerability that caused the breach tested for?"

### For Deployment Phase
1. "Who authorised the deployment?"
2. "Was there a rollback plan in case of failure?"
3. "Can you produce the deployment log showing when the version was deployed?"
4. "Were post-deployment security checks conducted?"

### For Maintenance Phase
1. "When was the vulnerability that was exploited first discovered?"
2. "When was a patch available?"
3. "Why was the patch not applied before the breach occurred?"
4. "Can you produce the vulnerability management log for the relevant period?"

---

# PART 4: FOUNDATION-TO-TUNE COMPARATIVE ANALYSIS

## The Global/Engineering Foundation

Globally, the SDLC is engineered to **minimise deployment friction and optimise runtime throughput**. API security is treated as a risk management choice. Cloud SLAs are commercial terms negotiated between parties. Security testing is a project management decision.

Key assumptions in the global model:
- The organisation has dedicated cybersecurity and legal teams
- Contractual remedies (SLA credits) are sufficient recourse
- The regulatory environment is stable and well-understood
- Cloud infrastructure is assumed to be reliable and sovereign risk is minimal

## The Ugandan Practice Tune

In Uganda, multiple statutes transform these choices into **legal obligations**:

1. **DPA Section 20** mandates technical and organisational security measures — this turns the OWASP API Top 10 from best practice into a compliance requirement. A lawyer cannot advise a client to "accept the risk" of a known API vulnerability without documenting that the decision complies with Section 20(2).

2. **ETA Sections 29-33** define when a service provider (including a cloud or API provider) is liable for third-party data. But the exemption does not apply if there is a contract — and there is always a contract. The lawyer must draft the contract carefully to preserve or exclude the exemption.

3. **DPA Section 21** requires a contract between controller and processor. The cloud SLA and DPA are not just commercial documents — they are **statutory requirements**.

4. **UCC QoS Regulations 2019** impose minimum service standards for licensed operators. These override weaker contractual SLA terms.

5. **NITA-U NISF 2026** requires government systems (and their contractors) to follow a secure SDLC, aligned with ISO 27001.

6. **Data localisation** is emerging as a sovereign requirement. Kenya's Cloud Policy 2025 imposes localisation for certain data categories. Rwanda enforces it with significant fines. The EAC is developing a harmonised framework. A lawyer drafting a cloud contract must consider where data can and cannot flow.

## The Practical Difference

| Issue | Global Foundation | Ugandan Tune |
|---|---|---|
| API security | Risk management choice | DPA S.20 legal obligation |
| Cloud SLA | Commercial term | Statutory requirement (DPA S.21) + regulatory overlay (UCC QoS) |
| SDLC documentation | Project management best practice | Evidence Act evidentiary requirement + ETA S.6 originality requirement |
| Data location | Commercial negotiation | Emerging localisation laws + EAC framework |
| Service provider liability | Contractual allocation | ETA S.29-33 statutory framework |
| Breach response | Contractual notice | DPA Reg 33 mandatory notification to PDPO |

---

# PART 5: LEGAL PROBLEM-SOLVING FRAMEWORK

## 5.1 How to Analyse an API/Cloud/SDLC Problem

### Step 1: Identify What Failed
- Was it an **API failure**? (wrong data returned, authentication bypassed, excessive data exposed)
- Was it a **cloud failure**? (outage, data loss, SLA breach, data location violation)
- Was it an **SDLC failure**? (bug introduced in development, inadequate testing, unpatched vulnerability)

### Step 2: Map the Legal Framework
- **API issues:** ETA S.29-33 (service provider liability), DPA S.20 (security), OWASP Top 10 (generally accepted practices)
- **Cloud issues:** DPA S.20-22 (security measures, controller-processor contract), ETA S.6 (record integrity), UCC QoS (for licensed operators), UNCITRAL Notes (best practice)
- **SDLC issues:** DPA S.20 (security from design to maintenance), ETA S.6 (originality of records), Evidence Act (admissibility), NISF 2026 (government systems)

### Step 3: Assess Compliance
- Was an API security assessment conducted? (OWASP Top 10)
- Was a Data Processing Agreement in place? (DPA S.21)
- Was a DPIA conducted? (PDPO privacy-by-design requirement)
- Were SDLC documentation records maintained? (Evidence Act, ETA S.6)
- Was the UCC QoS applicable and complied with? (licensed operators)

### Step 4: Determine Liability
- **API provider:** ETA S.29 exemption if merely transmitting; liable if contractual obligation exists
- **Cloud provider:** DPA S.21 liability for processor; SLA remedies
- **Data controller:** DPA S.20 primary liability for security
- **SDLC team:** Contractual liability for defects; potential criminal liability under CMA

### Step 5: Challenge or Authenticate Evidence
- **Challenge:** No API audit logs, no SDLC documentation, inadequate security testing, SLA exclusion clauses
- **Authenticate:** API logs showing authorised requests, SDLC documentation showing security testing, SLA compliance reports, ISO 27001 certification

---

## 5.2 The Week 4 Practice Task — SLA Compliance Audit

### Scenario
Your client, a high-growth Ugandan healthtech company, is outsourcing its hosting infrastructure to a multinational cloud provider (PaaS model) via an API gateway integration. The provider's boilerplate contract contains:
1. Standard disclaimers stating services are provided "as-is"
2. Uptime defined as "industry standard"
3. No specific metrics for API response time
4. SLA credits as the sole and exclusive remedy
5. No data processing agreement (DPA) attached

### Step-by-Step Analysis

**Step 1 — Identify the legal issues:**
- DPA Section 21 requires a contract between controller and processor — the missing DPA is a statutory violation
- DPA Section 20 requires "appropriate, reasonable, technical and organisational measures" — "as-is" disclaimers are inconsistent with this duty
- ETA Section 29(2)(a) — the contractual obligation removes the liability exemption
- UCC QoS Regulations — may apply if the healthtech platform qualifies as a data communication service

**Step 2 — Draft the contractual amendments:**

| Issue | Problem | Corrective Amendment |
|---|---|---|
| **Uptime** | "Industry standard" — vague | Define: "99.9% monthly uptime, calculated per calendar month, excluding scheduled maintenance with 48-hour notice" |
| **API latency** | Not addressed | Define: "95th percentile API response time ≤ 200ms, measured monthly" |
| **Throughput** | Not addressed | Define: "Minimum 10,000 API requests per minute without degradation" |
| **Downtime** | Not defined | Define: "Downtime = any period where API error rate exceeds 1% or latency exceeds 500ms for more than 5 consecutive minutes" |
| **Remedy** | SLA credits as exclusive remedy | Preserve right to seek actual damages for: (a) data breach, (b) DPA non-compliance, (c) gross negligence |
| **Data processing** | No DPA | Attach a DPA specifying: data types, processing purposes, security measures, sub-processor restrictions, breach notification, data return/deletion |
| **Data location** | Not specified | Specify: "Primary data storage in Uganda or [approved jurisdiction]. No transfer to non-approved jurisdictions without prior written consent and Transfer Impact Assessment." |

**Step 3 — Cross-reference with the ETA:**
Under ETA Section 29(2)(a), once a contractual obligation exists, the service provider cannot claim the liability exemption. The amendment brief must explicitly state that:
> *"By agreeing to specific technical metrics in this contract, the cloud provider accepts contractual liability for service failures. The ETA Section 29 exemption for 'mere conduit' providers does not apply because Section 29(2)(a) expressly preserves contractual obligations."*

---

# PART 6: QUICK REFERENCE CARDS

## Cheat Sheet: HTTP Verbs

| Verb | Action | Safe? | Idempotent? | Legal Analogy |
|---|---|---|---|---|
| GET | Read | Yes | Yes | Requesting a court file |
| POST | Create | No | No | Filing a new claim |
| PUT | Replace | No | Yes | Amending entire pleadings |
| PATCH | Partial update | No | No | Correcting a typo |
| DELETE | Remove | No | Yes | Withdrawing a claim |

*Safe = does not change data. Idempotent = repeating the request has the same effect as doing it once.*

## Cheat Sheet: Cloud Service Models

| Model | You Manage | Provider Manages | Analogy |
|---|---|---|---|
| On-Premise | Everything | Nothing | Own and maintain your building |
| IaaS | Apps, data, OS, middleware | Servers, storage, networking, virtualisation | Rent empty office space |
| PaaS | Applications, data | Everything else | Rent furnished office |
| SaaS | Nothing — just use it | Everything | Rent serviced office with receptionist |

## Cheat Sheet: SLA Uptime "Nines"

| Uptime % | Downtime/Year | Downtime/Month | Downtime/Week |
|---|---|---|---|
| 99% | 3.65 days | 7.2 hours | 1.68 hours |
| 99.9% | 8.76 hours | 43.2 minutes | 10.1 minutes |
| 99.99% | 52.56 minutes | 4.32 minutes | 1.01 minutes |
| 99.999% | 5.26 minutes | 25.9 seconds | 6.05 seconds |

## Cheat Sheet: SDLC Phases

| Phase | Key Document | Legal Risk | DPA Section |
|---|---|---|---|
| Requirements | Requirements Specification | Incomplete or missing requirements | S.20(2)(a) — identify risks |
| Design | Architecture/Design Document | No security-by-design | S.20(2)(b) — establish safeguards |
| Development | Source code, version control | IP ownership, open source compliance | — |
| Testing | Test reports, security scan results | Inadequate testing | S.20(2)(c) — verify safeguards |
| Deployment | Deployment log, release notes | Unauthorised deployment | S.20(1) — organisational measures |
| Maintenance | Patch log, vulnerability register | Unpatched vulnerabilities | S.20(2)(d) — update safeguards |

## Cheat Sheet: ETA Key Sections for APIs

| Section | What it Says | Practical Use |
|---|---|---|
| S.29 | Service provider not liable for third-party material if merely providing access | API provider exemption — but lost if contract exists (S.29(2)(a)) |
| S.30 | No liability for linking to infringing content if no knowledge | API that links to third-party content |
| S.31 | Notice-and-takedown procedure | How to notify API provider of infringement |
| S.32 | No duty to monitor | API provider not required to proactively police data |
| S.33 | Territorial jurisdiction | Which courts have jurisdiction over API disputes |

## Cheat Sheet: DPA Key Sections for Cloud/SDLC

| Section | What it Says | Practical Use |
|---|---|---|
| S.20 | Technical and organisational security measures | API security, SDLC security, cloud security all mandated |
| S.21 | Contract between controller and processor required | Cloud DPA is a statutory requirement |
| S.22 | Operator/authorised person confidentiality | Cloud provider staff confidentiality obligations |
| Reg. 31 | Publish security practices | Organisations must document and publish API/cloud security measures |
| Reg. 32 | Specific security measures | Access control, encryption, monitoring for cloud systems |
| Reg. 33 | Breach notification to PDPO | API breach = mandatory notification |

---

# PART 7: GLOSSARY FOR LAWYERS

| Term | Plain English Definition |
|---|---|
| **Agile** | A software development approach where work is done in short cycles (sprints) with continuous feedback and adaptation. |
| **API (Application Programming Interface)** | A set of rules that allows one software application to communicate with another. Like a waiter between a customer and the kitchen. |
| **API Endpoint** | The specific URL where an API can be accessed. Like a specific desk in a government office. |
| **API Key** | A simple string that identifies a client application to an API server. Like a building access card. |
| **Cloud Computing** | Delivering computing services (servers, storage, software) over the internet, paying only for what you use. |
| **Data Localisation** | The requirement that data be stored on servers physically located within a specific country's borders. |
| **Data Processing Agreement (DPA)** | A contract between a data controller and data processor that specifies each party's data protection obligations. Required by DPA Section 21. |
| **DevOps** | A software development approach that combines development and operations into a single team, with continuous deployment and monitoring. |
| **DPIA (Data Protection Impact Assessment)** | A process to identify and mitigate privacy risks before processing personal data. Increasingly required by the PDPO. |
| **Endpoint** | The specific URL where an API can be accessed. |
| **HTTP Verbs** | Standard methods (GET, POST, PUT, PATCH, DELETE) that tell an API what action to perform. |
| **IaaS (Infrastructure as a Service)** | Renting raw computing resources (servers, storage, networking) from a cloud provider. |
| **JSON (JavaScript Object Notation)** | A lightweight, human-readable format for transmitting data between systems. The most common API payload format. |
| **LLMOps** | The lifecycle management process for Large Language Models, adapted from traditional SDLC with additional governance layers. |
| **OAuth 2.0** | An industry-standard protocol for authorising API access using temporary tokens. |
| **OWASP API Security Top 10** | The industry-standard list of the 10 most critical API security risks. |
| **PaaS (Platform as a Service)** | Renting a complete platform (OS, database, middleware) from a cloud provider to deploy your own applications. |
| **Payload** | The actual data carried by an API request or response, typically in JSON or XML format. |
| **REST** | A set of design principles for building web APIs, using standard HTTP methods and stateless communication. |
| **SaaS (Software as a Service)** | Using a complete application provided by a vendor over the internet, without managing any underlying infrastructure. |
| **SDLC (Software Development Lifecycle)** | The process of building software in phases: Requirements, Design, Development, Testing, Deployment, Maintenance. |
| **SLA (Service Level Agreement)** | A contractual promise of service quality, defining measurable targets (uptime, latency, throughput) and remedies for failure. |
| **Sovereign Cloud** | A cloud infrastructure physically located within a country's borders, operated under that country's laws. |
| **Token** | A temporary digital pass used to authenticate API requests. Like a visitor's badge at a secure office. |
| **UGHub** | Uganda's national API gateway, operated by NITA-U, connecting over 135 government entities for secure data exchange. |
| **UNCITRAL Notes on Cloud Computing** | International best-practice guidelines for drafting cloud computing contracts, published by the United Nations. |
| **Waterfall** | A traditional software development approach where each phase must be completed before the next begins. |
| **XML (eXtensible Markup Language)** | An older, more verbose format for transmitting data between systems. Still used in banking and government systems. |

---

*End of Week 4 Reading Notes. These notes cover all curriculum topics: APIs (REST, endpoints, HTTP verbs, payloads, OAuth, OWASP Top 10), Cloud Computing (IaaS/PaaS/SaaS, public/private/sovereign, SLAs, data localisation), and SDLC & LLMOps (phases, Waterfall/Agile/DevOps, governance), with the Ugandan legal framework (ETA S.29-33, DPA S.20-22, DPA Regs 31-33, UCC Act, NITA-U NISF 2026, UNCITRAL Notes) integrated throughout.*

*Corrected statutory references: DPA Section 20 (not Section 22 as previously cited), DPA Regulations 31-33 (not Regulation 22). The UCC Act applies conditionally — only to licensed operators and data communication service providers.*
