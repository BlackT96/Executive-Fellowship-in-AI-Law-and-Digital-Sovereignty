# Module 1: Digital Technology Fundamentals

## Week 2: Internet Architecture (TCP/IP, DNS, HTTP/HTTPS, Web Applications)

---

### Learning Objectives

By the end of this chapter, you should be able to:

1. **Map the TCP/IP 5-layer model** to data flows in digital forensics and determine at which layer an interception, breach, or service failure occurred.
2. **Analyse the DNS resolution chain** to establish jurisdiction over domain registration data and trace content distribution paths.
3. **Evaluate HTTP/HTTPS communications** to distinguish between encrypted and unencrypted data for purposes of lawful interception under RICA and the DPA.
4. **Apply Uganda's content and consumer protection regulations** to internet-based services, including OTT platforms, web applications, and cloud computing.

---

### 2.1 The Internet as a Network of Networks

#### 2.1.1 The 5-Layer TCP/IP Model

The Internet does not use the 7-layer OSI model in practice. Instead, it operates on a **5-layer TCP/IP model** that maps approximately to the OSI layers:[^1]

| Layer | TCP/IP Model | Protocols | Role |
|-------|--------------|-----------|------|
| 5 | **Application** | HTTP, HTTPS, DNS, SMTP, FTP | User-facing protocols; data originates here |
| 4 | **Transport** | TCP, UDP | End-to-end delivery; port numbers, segmentation |
| 3 | **Network** | IP (IPv4, IPv6) | Routing; logical addressing across networks |
| 2 | **Link** | Ethernet, Wi-Fi (802.11) | Physical addressing (MAC); local frame delivery |
| 1 | **Physical** | Copper, fibre, radio | Raw bit transmission |

**Encapsulation** is the process by which each layer adds its own header (and sometimes trailer) to the data received from the layer above:

```
Application Data        [HTTP Header | Body]
    ↓
Transport Segment      [TCP Header | HTTP Header | Body]
    ↓
Network Datagram       [IP Header | TCP Header | HTTP Header | Body]
    ↓
Link Frame             [Ethernet Header | IP Header | TCP Header | HTTP Header | Body | Ethernet Trailer]
```

For the legal practitioner, encapsulation is critical because **each header reveals different jurisdictional information**:[^2]
- The **IP header** (Layer 3) reveals the source and destination IP addresses, which can be geolocated.
- The **TCP header** (Layer 4) reveals port numbers, identifying the type of application (port 80 = HTTP, port 443 = HTTPS, port 53 = DNS).
- The **application data** (Layer 5) is the actual content — which may be encrypted (HTTPS) or plaintext (HTTP).

#### 2.1.2 The Network Edge vs. the Network Core

- **Network Edge:** End systems (hosts) where applications run — smartphones, laptops, servers, IoT devices. The edge is where data is created and consumed.
- **Network Core:** The mesh of routers and links that move data between edge devices. The core has no knowledge of application content; it only forwards packets based on IP addresses.[^3]

**Legal significance:** Lawful interception under RICA targets specific points in the network. The distinction between edge and core determines whether data is "in transit" (core) or "at rest on a device" (edge), which affects both the warrant requirement and the admissibility of intercepted data.

#### 2.1.3 Packet Switching vs. Circuit Switching

The Internet uses **packet switching**: data is broken into packets, each routed independently through the network. This contrasts with circuit switching (traditional telephone networks), where a dedicated path is reserved for the entire communication.[^4]

**Forensic implication:** Because packets can take different routes, the geographical path of data is not predetermined. A packet sent from Kampala to Nairobi might transit through London or Dubai. This creates jurisdictional complexity for cross-border data claims under the DPA §19 adequacy requirement.

---

### 2.2 The Domain Name System (DNS)

#### 2.2.1 The Problem DNS Solves

Humans prefer mnemonic hostnames (www.google.com); routers prefer fixed-length, hierarchically structured IP addresses (142.250.190.4). **DNS** is the Internet's directory service that translates between the two.[^5]

The DNS is:
1. A **distributed database** implemented in a hierarchy of DNS servers.
2. An **application-layer protocol** that allows hosts to query the distributed database.

DNS runs over **UDP** (port 53), with TCP fallback for large responses.

#### 2.2.2 The DNS Hierarchy

No single DNS server holds all mappings. Instead, DNS servers are organised hierarchically:[^6]

```
Root DNS Servers (13 logical roots, 1000+ instances globally)
    ↓
Top-Level Domain (TLD) Servers (.com, .org, .ug, .ke, .tz, .rw)
    ↓
Authoritative DNS Servers (e.g., amazon.com, google.com)
    ↓
Local DNS Server (provided by ISP — e.g., MTN Uganda, Airtel Uganda)
```

**Root servers** provide IP addresses of TLD servers. **TLD servers** handle top-level domains (.com, .org, .ug, .ke, .tz, .rw). **Authoritative servers** hold the actual DNS records for specific domains. **Local DNS servers** (also called default name servers) act as proxies, forwarding queries from user hosts into the hierarchy.[^7]

#### 2.2.3 The DNS Resolution Process

When a user in Kampala types `www.example.com` into a browser:[^8]

1. The browser calls `gethostbyname()` (client side of DNS).
2. The DNS query is sent to the **local DNS server** (e.g., MTN Uganda's DNS server).
3. The local DNS server queries a **root server** → gets TLD server for `.com`.
4. The local DNS server queries the `.com` **TLD server** → gets authoritative server for `example.com`.
5. The local DNS server queries the **authoritative server** for `example.com` → gets the IP address.
6. The IP address is returned to the browser, which then initiates a TCP connection.

**Caching:** DNS responses are cached at the local DNS server, reducing query traffic and improving performance. The Time-To-Live (TTL) value in DNS records determines how long a response may be cached.

#### 2.2.4 DNS Services Beyond Address Translation

DNS provides several additional services relevant to legal practice:[^9]

- **Host aliasing:** A host with a complicated canonical hostname can have simpler alias names. For example, `relay1.west-coast.enterprise.com` might have aliases `enterprise.com` and `www.enterprise.com`. This is relevant to identifying the true server behind a branded URL in phishing or fraud cases.
- **Mail server aliasing:** MX records allow mail servers and web servers to share identical (aliased) hostnames. This is relevant when tracing the origin of email communications.
- **Load distribution:** Busy sites (cnn.com, google.com) are replicated across multiple servers. DNS rotates the order of IP addresses in each response, distributing traffic. Content distribution companies (Akamai, Cloudflare) use sophisticated DNS techniques for traffic management.

#### 2.2.5 The .ug ccTLD and Ugandan Domain Administration

The **.ug** country-code top-level domain (ccTLD) is administered by the **Uganda Internet Exchange Point (UIXP)** under the authority of the Uganda Communications Commission. Key points:

- Domain registration for .ug, .or.ug, .ac.ug, .go.ug, .sc.ug follows UCC guidelines.
- WHOIS lookups reveal registrant information, which may be relevant to identifying website operators in content disputes.
- The UCC Content Regulations, 2019, Regulation 7 requires operators to retain records of all broadcast content for at least 60 days — a provision that applies to internet-based content services as well (Regulation 5 defines "content services" broadly to include services offered by a content provider).[^10]

---

### 2.3 HTTP and HTTPS

#### 2.3.1 The Web's Application-Layer Protocol

**HTTP (HyperText Transfer Protocol)** is the foundation of data communication on the World Wide Web. It is a **stateless, text-based request-response protocol** that runs over TCP (typically port 80 for HTTP, port 443 for HTTPS).[^11]

#### 2.3.2 HTTP Request-Response Cycle

```
Client (Browser)                      Server
    │                                     │
    │─────── HTTP Request ──────────────→│
    │   GET /index.html HTTP/1.1         │
    │   Host: www.example.com            │
    │   User-Agent: Mozilla/5.0          │
    │   Cookie: session_id=abc123        │
    │                                     │
    │←────── HTTP Response ──────────────│
    │   HTTP/1.1 200 OK                  │
    │   Content-Type: text/html          │
    │   Set-Cookie: session_id=def456    │
    │   [body of page]                   │
    │                                     │
```

**HTTP Methods (most relevant to legal practice):**[^12]

| Method | Purpose | Legal Relevance |
|--------|---------|-----------------|
| **GET** | Retrieve a resource | Access logs show what content was requested and when |
| **POST** | Submit data to be processed | Form submissions, login credentials, payment data |
| **PUT** | Upload/replace a resource | Content uploads to servers |
| **DELETE** | Remove a resource | Evidence of intentional data destruction |
| **PATCH** | Partial modification | Data alteration records |

#### 2.3.3 HTTP Status Codes

Status codes are grouped into classes:[^13]

| Code | Class | Meaning | Example |
|------|-------|---------|---------|
| 1xx | Informational | Request received, processing | 101 Switching Protocols (WebSocket upgrade) |
| 2xx | Success | Request understood and accepted | 200 OK, 201 Created, 204 No Content |
| 3xx | Redirection | Further action needed | 301 Moved Permanently, 302 Found, 304 Not Modified |
| 4xx | Client Error | Request cannot be fulfilled | 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found |
| 5xx | Server Error | Server failed to fulfil valid request | 500 Internal Server Error, 502 Bad Gateway, 503 Service Unavailable |

**Forensic relevance:** Status codes in server logs reveal how a web application responded to specific requests. A 403 Forbidden response may indicate access controls were functioning; a 200 OK response to an unauthorised request may indicate a security failure.

#### 2.3.4 Cookies and State Management

HTTP is inherently **stateless** — each request-response pair is independent. To create stateful sessions (shopping carts, authenticated accounts), web applications use **cookies**:[^14]

- **Set-Cookie:** The server instructs the browser to store a small piece of data.
- **Cookie:** The browser sends stored cookies back to the server with subsequent requests.

**Legal significance:** Session cookies store authentication tokens. If a cookie is intercepted (e.g., via an unencrypted HTTP connection), the attacker can impersonate the user — known as **session hijacking**. This is directly relevant to the Computer Misuse Act §12 (unauthorised access) and §14 (access with intent to commit a further offence).

#### 2.3.5 HTTPS and TLS

**HTTPS (HTTP over TLS)** encrypts the entire HTTP message (headers, body, cookies) before it is transmitted over TCP. The **Transport Layer Security (TLS)** protocol provides:[^15]

1. **Encryption:** Data is unreadable to intermediaries.
2. **Authentication:** The server presents a digital certificate verified by a Certificate Authority (CA).
3. **Integrity:** Tampering with data in transit is detectable.

**Layers of encryption visibility:**

| Data | HTTP (Port 80) | HTTPS (Port 443) |
|------|----------------|-------------------|
| Application content | Plaintext | Encrypted |
| URLs and paths | Visible in request | Encrypted |
| Cookies | Visible in headers | Encrypted |
| Domain name (from DNS) | Visible before connection | Visible before connection |
| IP addresses (Network layer) | Visible | Visible |
| Port numbers (Transport layer) | Visible (80) | Visible (443) |

**NOTE for lawful interception:** Under RICA, interception of communications requires a warrant (RICA §5). However, HTTPS means that even with lawful interception, the **content** of the communication may remain inaccessible if the interceptor does not also obtain the TLS session keys. This creates a practical tension between surveillance authority and technological encryption.

---

### 2.4 Web Applications and Cloud Services

#### 2.4.1 From Static Pages to Web Applications

Modern web applications go beyond serving static HTML pages. They involve:

- **Client-side processing:** JavaScript in the browser handles user interaction, makes API calls, and updates pages dynamically.
- **Server-side processing:** Application servers execute business logic, query databases, and generate responses.
- **APIs (Application Programming Interfaces):** RESTful APIs and GraphQL endpoints allow programmatic communication between systems.

#### 2.4.2 Cloud Computing Models

| Model | Description | Example | Legal Implications |
|-------|-------------|---------|-------------------|
| **IaaS** | Virtualised computing resources (servers, storage, networking) | AWS EC2, Google Compute Engine | Customer may control the OS; provider controls physical infrastructure |
| **PaaS** | Platform for deploying applications without managing underlying infrastructure | Google App Engine, Heroku | Provider manages OS and runtime; customer manages application code |
| **SaaS** | Ready-to-use software delivered over the web | Google Workspace, Microsoft 365 | Provider controls everything; customer only uses the application |

#### 2.4.3 Data Sovereignty and Cloud Jurisdiction

The Uganda Data Protection and Privacy Act (DPA) §19 requires:

> "Where a data processor or data controller based in Uganda processes or stores personal data outside Uganda, the data processor or data controller shall ensure that — (a) the country in which the data is processed or stored has adequate measures in place for the protection of personal data at least equivalent to the protection provided for by this Act; or (b) the data subject has consented."[^16]

**Practical implications for cloud use:**

- A Ugandan company using AWS (servers in South Africa, Ireland, or US-East) must verify that the host country has adequate data protection measures.
- If adequacy cannot be established, the company must obtain **explicit consent** from each data subject.
- Cloud providers typically offer data residency options (e.g., AWS Africa Region in Cape Town), but data may still be replicated globally for redundancy unless contractually restricted.

---

### 2.5 Uganda's Regulatory Framework for the Internet

#### 2.5.1 The Uganda Communications Act (UCA) and UCC

The **Uganda Communications Commission (UCC)** is the primary regulator of communications services, including internet and data communications, under the Uganda Communications Act, 2013.[^17a] UCC's powers extend to:

- Licensing of internet service providers (ISPs) and communications operators.
- Regulation of content (UCC Content Regulations, 2019).
- Consumer protection in communications services (UCC Consumer Protection Regulations, 2019).
- Quality of service monitoring.
- Equipment type approval.[^17]

#### 2.5.1A UCC Licensing Regulations, 2019 (Statutory Instrument No. 95 of 2019) — Relevance to Internet Architecture

The **Uganda Communications (Licensing) Regulations, 2019** (S.I. No. 95)[^17a] operationalise UCC's licensing mandate under the Uganda Communications Act, 2013. For Week 2 purposes, the following provisions are most relevant to internet architecture:

**Prohibition of unlicensed activity (Reg. 6):** No person may operate a communications system or provide communications services without a licence. This covers ISPs, OTT platforms, and any entity transmitting data over the internet.

**Licence categories determining network layer control (Part II, Reg. 7):**
- **Public Infrastructure Providers (NPIP/RPIP)** own and operate physical network infrastructure (cables, data centres, towers) — corresponding to Layers 1–2 (Physical and Link) of the TCP/IP model.
- **Public Service Providers (NPSP/RPSP)** and **Service Only Providers** deliver services over leased infrastructure — operating at Layers 3–5 (Network, Transport, Application).
- **National Telecommunications Operators (NTO)** carry universal service obligations and hold spectrum rights.

**Value Added Services (Part VII, Reg. 83–86):** VAS includes mobile money, content distribution, and internet-based application services. VAS providers require a licence unless exempted (Reg. 86). This classification is directly relevant to whether OTT platforms (WhatsApp, Netflix, Zoom) fall within UCC's regulatory scope.

**Licence conditions affecting internet services (Reg. 97–98):** All licences are granted subject to terms and conditions, which typically include:
- Network security obligations and data protection standards
- Lawful interception facilitation requirements (linking to RICA, §2.5.4)
- Consumer information protection (linking to Consumer Protection Reg. 16, §2.5.3)
- Content regulation compliance (linking to Content Regulations, §2.5.2)

**Enforcement powers affecting internet operators (Part VIII):**
- **Financial penalty:** Up to 10% of the licensee's annual turnover for breach of conditions (Reg. 105(10)(c))
- **Suspension or revocation:** For serious or repeated breach, fraud, or where the operator's platform is used for prohibited content (Reg. 104, 110)
- **Confiscation of apparatus:** For unlawfully possessed or operated equipment (Reg. 112)

**Connection to Week 2 Topics:**

| Curriculum Section | Relevance of Licensing Regulations |
|-------------------|-----------------------------------|
| §2.1 TCP/IP Model | Licence type determines network layer control: infrastructure licences cover Layers 1–2 (physical equipment); service licences cover Layers 3–5 (data services) |
| §2.2 DNS / .ug ccTLD | Only licensed ISPs may operate DNS servers; .ug domain administration derives from UCC's licensing authority |
| §2.3 HTTP/HTTPS | Licence conditions impose security and data protection obligations on how web traffic is handled |
| §2.4 Cloud/Web Apps | Cloud services and data centres may require infrastructure or VAS licences depending on their service model (IaaS/PaaS/SaaS) |
| §2.5.2–2.5.3 Content & Consumer Protection | Licensing is the gateway — only licensed operators are subject to these regulations |
| §2.5.4 RICA | Licence conditions may include lawful interception obligations |
| §2.6.1 OTT Regulation | The VAS classification (Part VII) determines whether OTT platforms need a licence |
| §2.7 Practice Task | Consider: Does the ISP hold a valid licence? Were licence conditions on network security breached? |

**Fees relevant to ISPs and internet service operators**[^17b] (UCC Fees and Fines Regulations, S.I. No. 94, as amended):

| Licence Category | Application Fee | Annual Licence Fee (minimum) |
|-----------------|-----------------|------------------------------|
| Infrastructure Provider (Nat./Reg.) | USD 2,500 | USD 9,900–60,000 or 0.89% of gross annual revenue |
| Service Provider (Nat./Reg.) | USD 2,500 | USD 3,300–20,000 or 0.89% of revenue |
| Service Only Provider | USD 2,500 | USD 12,000 or 0.89% of revenue |
| Value Added Service | As prescribed | As prescribed by Commission |

The licensing framework is relevant to legal practice because the **type of licence determines the legal obligations** an internet service operator owes. The proposed Single Digital Media Law 2026 (§2.5.6) would introduce a unified licensing regime for all digital platforms, potentially expanding UCC's reach to OTT services and online content platforms.

#### 2.5.1B Comparative Analysis: General Licensing Regimes for Communications Services

The UCC Licensing Regulations represent one of several regulatory models for authorising communications services. A comparative analysis of Uganda, Kenya, the UK/EU, and the United States reveals fundamentally different approaches to who must be licensed and at what cost, with direct implications for internet architecture and the legal obligations of service providers.

**Uganda (Person-Based Licensing):**

The UCC model requires any person offering a communications service to hold an individual licence granted by the Commission (S.I. No. 95, Reg. 6). Licence categories are tied to the type of service and network layer: Infrastructure Providers (Layers 1–2), Service Providers (Layers 3–5), and Value Added Service providers (application layer). Annual fees range from USD 3,300 (Regional Service Provider) to USD 60,000 (National Infrastructure Provider), plus a 0.89% levy on gross annual revenue. The same framework applies regardless of scale — a neighbourhood hotspot operator falls under obligations equivalent to MTN Uganda's. Enforcement power includes financial penalties (up to 10% of annual turnover), suspension, revocation, and confiscation of apparatus (Reg. 105, 110, 112).

**Kenya (Tiered Licensing — Unified Licensing Framework):**

Kenya's Communications Authority (CAK) operates a Unified Licensing Framework (ULF) with three authorisation classes:
- **Network Facility Provider (NFP):** Owns and operates physical infrastructure (fibre, towers, spectrum) — analogous to Layers 1–2.
- **Application Service Provider (ASP):** Provides services over infrastructure (internet, voice, data). National ASP: KES 100,000/year (~USD 770). Micro ASP: KES 10,000–50,000/year (~USD 77–385) — a tier designed specifically to accommodate small-scale operators.
- **Content Service Provider (CSP):** Provides content and broadcasting services.
- **Public Communication Access Class (PCAC):** Self-registration for public Wi-Fi, cybercafés, telecentres — no individual licence fee; operators file a letter of undertaking with the CAK.

The tiered structure explicitly accommodates operators of different scales. Kenya's ICT Policy (2016, rev. 2019) recognised that proportionate licensing is essential to last-mile connectivity. The consequence is that a small ISP or a public Wi-Fi operator can operate legally without bearing the same regulatory cost as Safaricom.

**UK and European Union (General Authorisation / Class Licensing):**

The UK and EU operate a **General Authorisation** regime under the UK Electronic Communications Code and the European Electronic Communications Code (Directive 2018/1972/EU):
- No person requires an individual licence to provide communications services.
- Any person may provide electronic communications networks or services upon filing a simple notification (free of charge) with the national regulator (Ofcom in the UK).
- Ofcom's General Conditions of Entitlement apply to all providers but are applied **proportionately** — micro-entities (<10 employees, turnover <€2M) may be exempted from certain conditions (Art. 12(4), Directive 2018/1972).
- Regulators focus on competition, consumer protection, and spectrum management — not on authorising individual operators.
- A public Wi-Fi hotspot, an ISP reseller, and BT all operate under the same legal framework, differing only in the obligations that apply at their scale.

**United States (Equipment-Based Regulation — No Service Licensing):**

The United States does not require a licence to provide internet access services or operate a Wi-Fi hotspot:
- **No ISP licence:** The Communications Act of 1934 (as amended) does not create a licensing category for "internet service provider" or "internet access reseller." Any person may resell internet access or offer public Wi-Fi without a federal licence.
- **Part 15 (Equipment authorisation):** The FCC certifies that radio-frequency devices (routers, access points) will not cause harmful interference. Once a device is Part 15-certified, any person may buy and operate it without further authorisation.
- **Spectrum:** Licence-exempt bands (2.4 GHz, 5 GHz, 6 GHz) are designated for unlicensed Wi-Fi use — no individual spectrum licence required.
- **State-level:** Some states require franchises for wireline infrastructure (e.g., laying fibre), but resale of internet service over existing infrastructure is generally unregulated at the state level.
- **Contractual constraints:** The only restriction on reselling internet access comes from the ISP's terms of service (a private contract law issue), not from regulatory licensing.

**Summary of approaches:**

| Aspect | Uganda | Kenya | UK/EU | United States |
|--------|--------|-------|-------|---------------|
| Licensing model | Individual licence (S.I. 95) | Tiered licences + class registration (ULF) | General Authorisation (free notification) | No ISP licence required |
| Who needs a licence? | Anyone offering a communications service | Varies by scale: NFP/ASP/CSP/PCAC | Anyone providing electronic communications (free notification) | No one (for ISP or Wi-Fi service) |
| Entry cost | USD 3,300–60,000/year + 0.89% revenue levy | KES 10,000–100,000/year (ASP); free (PCAC) | Free (notification only) | Free |
| Equipment regulation | Type approval (separate process) | Type approval (separate process) | CE marking / RED Directive | FCC Part 15 certification |
| Enforcement focus | Licensed vs. unlicensed operators | Compliance within tier | Competition, consumer protection, spectrum | Equipment interference, anti-competitive conduct |
| Micro-operator treatment | Same obligations as largest operators | Reduced fees (Micro ASP, PCAC) | Exemptions from certain conditions | No regulatory barrier to entry |

**Relevance to internet architecture:** The licensing regime of a jurisdiction determines who may lawfully operate at each layer of the TCP/IP model — from physical infrastructure (Layers 1–2) to application services (Layer 5). A legal practitioner advising an internet-based business must understand which model applies in the target jurisdiction, as the consequences of operating without authorisation range from administrative fines and equipment confiscation to criminal penalties. The comparative contrast also informs policy analysis: a jurisdiction that treats a neighbourhood Wi-Fi operator the same as a national telecommunications carrier has made a deliberate regulatory choice, not followed a universal norm.

#### 2.5.2 UCC Content Regulations, 2019 (Statutory Instrument 2019 No. 91)

The Content Regulations apply to "all content in telecommunications, data and radio communications and broadcasting and postal communications" (Regulation 1(2)).[^18]

**Key provisions for internet-based services:**

- **Regulation 5 (Content services):** Defines content services broadly, covering any service offered by a content provider, including internet-based content distribution.
- **Regulation 7 (Record keeping):** Operators must retain records of all programmes, presentations, and content broadcast for at least 60 days. Records must be "complete, authentic and original."
- **Regulation 8 (General requirements):** Prohibits content that uses offensive language, presents sexual matters explicitly, glorifies violence, incites hatred, or is contrary to public morality.
- **Regulation 38 (Privacy):** Prohibits broadcasting material relating to a person's private affairs unless there is "compelling and legitimate public interest." The identity of victims of sexual offences and minors must not be divulged.
- **Regulation 45 (Broadcasting prohibited content):** Offence punishable by a fine not exceeding 48 currency points (UGX 960,000) or imprisonment not exceeding two years, or both.

**Application to OTT services:** The broad definition of "content" in Regulation 3 — "any sound, text, still picture, moving picture or other audio-visual representation ... capable of being created, manipulated, stored, retrieved or communicated electronically" — extends the Regulations beyond traditional broadcasting to internet-based content platforms.

#### 2.5.3 UCC Consumer Protection Regulations, 2019 (Statutory Instrument 2019 No. 87)

The Consumer Protection Regulations establish consumer rights for all communications services in Uganda.[^19]

**Key provisions:**

- **Regulation 6 (Rights of consumers):** The right to access communications services; the right to choose service providers; the right to accurate billing; the right to redress.
- **Regulation 10 (Prohibited advertising):** False, misleading, bait-and-switch advertising is prohibited.
- **Regulation 13 (Denial of access):** Prohibits denial of access except for non-payment or just cause under the Act. Discriminatory treatment in quality of service, pricing, and technology availability is prohibited.
- **Regulation 16 (Protection of consumer information):** Operator may only collect information required for business purposes or as directed by UCC. Information must be "fairly and lawfully collected," processed for clearly identified purposes, accurate, protected against improper disclosure, and not transferred without consumer consent.
- **Regulation 18 (Unsolicited and harmful content):** Operators must protect consumers against spam, scams, unsolicited calls, and harmful content. Consumers must have a mechanism to opt out at no cost.
- **Regulation 24 (Service Level Agreements):** Every operator must submit a standard SLA to UCC for approval. Bundled services remain the operator's contractual responsibility.
- **Regulation 25 (Contents of SLA):** Must include scope of service, confidentiality clause, compensation for unmet quality benchmarks, dispute resolution procedures, and terms for suspension or termination.

#### 2.5.4 The Regulation of Interception of Communications Act (RICA)

RICA governs the lawful interception of communications in Uganda. Key provisions:[^20]

- **RICA §2 (Definition of "interception"):** Interception means listening to, recording, monitoring, or otherwise acquiring the content of a communication without the knowledge of the persons communicating.
- **RICA §5 (Warrant requirement):** No interception may take place without a warrant issued by a Judge of the High Court. The warrant must specify the target, duration, and scope of interception.
- **RICA §2 (Definition of "communication"):** Includes "telecommunication" which encompasses internet communications, voice over IP (VoIP), and data transmissions.

**Technical tension with HTTPS:** As noted in §2.3.5 above, even with a valid RICA warrant, the content of HTTPS communications is encrypted. RICA does not explicitly address whether service providers must decrypt communications or provide TLS keys to intercepting authorities.

#### 2.5.5 Cross-Border Data Transfers Under the DPA

Section 19 of the Uganda Data Protection and Privacy Act imposes an **adequacy requirement** on cross-border data transfers:

> "Where a data processor or data controller based in Uganda processes or stores personal data outside Uganda, the data processor or data controller shall ensure that — (a) the country in which the data is processed or stored has adequate measures in place for the protection of personal data at least equivalent to the protection provided for by this Act; or (b) the data subject has consented."

The DPA Regulations, 2021 further specify that adequacy assessments must consider the nature of the data, the purpose of processing, the duration of processing, and the laws of the recipient country. Uganda has not yet published a list of "adequate" jurisdictions, creating legal uncertainty for cloud-dependent businesses.

#### 2.5.6 The Proposed Single Digital Media Law (2026)

In April 2026, the Government of Uganda announced it was drafting a single, overarching statute to consolidate the country's fragmented communications, press, and digital-content regulatory framework. The ICT Minister, Dr. Chris Baryomunsi, stated: "We are writing an overarching legislation so that all issues to do with communication are housed in one law."[^21]

The draft consolidates provisions currently spread across:
- The Uganda Communications Act, 2013 (UCC's mandate, licensing, spectrum)
- The Press and Journalists Act, 1995 (media accreditation, journalist conduct)
- The Computer Misuse Act, 2011 (as amended — cybercrime offences)
- The Data Protection and Privacy Act, 2019 (data protection, cross-border transfers)

**Reported key provisions:**

| Provision | Description |
|-----------|-------------|
| **Unified licensing** | Single registration regime for broadcasters, online publishers, social media platforms, OTT services, and content creators targeting Ugandan audiences |
| **Local representation** | Offshore platforms meeting user or revenue thresholds must appoint a local representative to receive legal notices and cooperate with regulators |
| **Content moderation** | Mandatory notice-and-takedown procedures with response timelines of 24-48 hours for flagged unlawful content; platforms must maintain moderation policies and publish transparency reports |
| **Metadata retention** | Telecoms, ISPs, and platform operators must retain specified categories of metadata for defined periods |
| **Enhanced data transfer controls** | Extends DPA §19 cross-border transfer restrictions with potential data localisation triggers for sensitive data categories |
| **AI and automated decisioning** | Disclosure and human-review requirements for automated content moderation and algorithmic decisioning |
| **Enforcement** | Administrative fines, service suspension, licence revocation, and referral to criminal law frameworks |

**Implications for internet architecture:** The law would introduce obligations that directly intersect with technical infrastructure — metadata retention affects ISPs and hosting providers at the network layer; content moderation obligations affect application-layer services; and local representation requirements affect the jurisdictional mapping of DNS and IP-based services.

The draft bill text had not been publicly gazetted as of mid-2026. Industry observers expect parliamentary introduction in the second half of 2026.[^22]

#### 2.5.7 Regional and Continental Frameworks

**The EAC Framework for Cyberlaws (2009–2010):**

The East African Community was the first region in Africa to adopt a harmonised framework for cyberlaws, developed by the EAC Task Force on Cyberlaws with UNCTAD support. Phase I (adopted 2009, formally signed May 2010) covered: electronic transactions, electronic signatures and authentication, data protection and privacy, consumer protection, and computer crime. The five original partner states — Kenya, Uganda, Tanzania, Rwanda, and Burundi — committed to enacting harmonised national laws.[^23]

Uganda's **Electronic Transactions Act, 2011**, **Computer Misuse Act, 2011**, and **Electronic Signatures Act, 2011** were enacted directly in response to the EAC Framework (bills were submitted to Cabinet in 2009). The **Data Protection and Privacy Act, 2019** later filled the data protection gap identified in the 2012 UNCTAD assessment for Uganda. This means Uganda's internet regulatory stack is substantially consistent with the EAC harmonisation model.

In 2025–2026, the EAC revived harmonisation efforts under the **Eastern Africa Regional Digital Integration Project (EARDIP)** , supported by the World Bank. A Cross-Border Data Flows Framework was validated in June 2026 to enable secure data movement across the region.

**The African Union Malabo Convention (2014, in force June 2023):**

The African Union Convention on Cyber Security and Personal Data Protection (Malabo Convention) is the continent's only binding treaty on data protection. It entered into force on 8 June 2023 after Mauritania deposited the 15th instrument of ratification. The Convention has three pillars:[^24]

1. **Electronic Transactions** — legal recognition of electronic contracts, signatures, and payments.
2. **Personal Data Protection** (Articles 8–22) — mandates independent data protection authorities, six basic processing principles (consent, lawfulness, purpose specification, accuracy, transparency, confidentiality/security), data subject rights (information, access, objection, erasure), and cross-border transfer restrictions requiring authorisation from the national DPA.
3. **Cybersecurity and Cybercrime** — criminalises hacking, identity theft, cyber fraud; obliges states to adopt national cybersecurity policies and create CERTs.

**Uganda's status:** Uganda has **not signed or ratified** the Malabo Convention. However, Uganda's DPA 2019 already satisfies most of the Convention's mandates (independent PDPO, consent-based processing, data subject rights, cross-border adequacy requirement), so ratification would not require major legislative changes. Among East African states, only **Rwanda** has ratified the Convention (ratified 14 November 2019).[^25]

**Practical relevance for legal practitioners:** The Malabo Convention provides the continental benchmark against which Uganda's data protection framework is measured. When assessing adequacy under DPA §19 for transfers to other African countries, the recipient country's ratification of the Malabo Convention may be relevant evidence of adequate protection — though Uganda has not issued formal guidance on this point.

---

### 2.6 Legal Challenges in Internet Regulation

#### 2.6.1 OTT Regulation

Over-the-Top (OTT) services — WhatsApp, Telegram, Zoom, Netflix — transmit data over the internet without direct involvement of traditional telecommunications operators. Uganda's regulatory framework (UCC Content Regulations, Consumer Protection Regulations) was designed primarily for broadcasting and telecommunications, raising the question of whether OTT services fall within its scope.

Key issues for legal practitioners:
- **Content liability:** If a user posts defamatory or prohibited content on an OTT platform, is the OTT provider a "content provider" under the UCC Content Regulations?
- **Consumer protection:** Do UCC Consumer Protection Regulations apply to OTT services that consumers pay for separately (e.g., Netflix subscriptions via internet data)?
- **Data localisation:** Does the DPA require OTT providers to store Ugandan users' data locally?

#### 2.6.2 Content Moderation

The UCC Content Regulations, 2019 impose content obligations on operators (Regulation 8), including prohibitions on offensive language, incitement, and material contrary to public morality. For internet-based platforms, this creates tension between:
- The operator's obligation to remove prohibited content.
- The user's right to freedom of expression under Article 29 of the Constitution of Uganda.
- The operator's need for safe harbour from liability for user-generated content (which Uganda lacks a specific statutory framework for, unlike Section 230 of the US Communications Decency Act or the EU Digital Services Act).

#### 2.6.3 Data Localisation and the Adequacy Gap

DPA §19 requires adequate data protection in recipient countries but does not explicitly mandate local storage. However, the practical difficulty of establishing adequacy means many organisations opt for local storage. This creates challenges:

1. **Cloud infrastructure:** Uganda has limited local cloud infrastructure (no local AWS or Azure regions).
2. **Cost:** Local hosting is typically more expensive than cloud alternatives.
3. **Performance:** Services hosted locally may lack the redundancy and CDN distribution of global providers.

---

### 2.7 Weekly Practice Task: Technical Deposition — Internet Layer Tracing

**The Scenario:**

Your client, a Ugandan e-commerce company, suffered a data breach. Customer payment data was intercepted during transmission. The logs show:

1. The customer's browser connected to `https://www.shopuganda.com` (port 443).
2. The DNS resolution for `www.shopuganda.com` was performed via MTN Uganda's local DNS server.
3. The server was hosted on AWS EC2 (Cape Town region).
4. The breach was detected when traffic was observed routing through an unknown IP address in Dubai before reaching the Cape Town server.

**Your Task:**

As lead counsel, draft a **Technical Deposition Questionnaire** (maximum 10 questions) directed at the company's IT security officer. Your questions must isolate:

1. At which **TCP/IP layer** did the interception occur? (Layer 3 — IP routing hijack? Layer 4 — TCP session hijack? Or Layer 2 — local network ARP spoofing?)
2. Whether the HTTPS/TLS encryption was properly implemented (was the connection actually HTTPS or did it fall back to HTTP via a downgrade attack?).
3. Whether the DNS resolution was compromised (DNS spoofing or cache poisoning?).
4. Which regulatory implications apply under the **DPA (cross-border transfer)**, **UCC Consumer Protection Regulations (protection of consumer information, reg. 16)**, and **RICA (lawful interception)**.

**Sample Questions:**

> "Can you confirm whether the TLS certificate presented by the server to the customer's browser was valid, self-signed, or mismatched, and whether the browser generated a certificate warning?"

> "Did the DNS query for `www.shopuganda.com` return the legitimate IP address of the AWS EC2 instance, or an IP address in a different jurisdiction?"

---

### Chapter Summary

| Concept | Key Takeaway for Legal Practice |
|---------|-------------------------------|
| 5-Layer TCP/IP Model | Data interception occurs at a specific layer; each layer reveals different jurisdictional information |
| DNS Resolution | The chain of DNS queries can establish jurisdiction over domain registration and identify whether a domain was spoofed |
| HTTP vs. HTTPS | Encrypted vs. plaintext communications determine what data is accessible under a RICA warrant |
| Web Applications and Cloud | Cloud jurisdiction depends on where servers are physically located and whether the DPA §19 adequacy test is satisfied |
| UCC Licensing Regulations | Foundational framework — determines who may operate (licence categories for telecoms, broadcasting, radio, postal, VAS); sets fees, application process, conditions, enforcement (fines up to 10% of annual turnover, suspension, revocation) |
| Comparative Licensing Regimes | Uganda (person-based), Kenya (tiered ULF), UK/EU (General Authorisation), and US (equipment-based) represent four distinct regulatory philosophies; the choice of model determines who may lawfully operate at each TCP/IP layer |
| UCC Content Regulations | Apply broadly to internet-based content; operators must retain records for 60 days and comply with content standards |
| UCC Consumer Protection | ISPs and OTT operators must protect consumer information, provide SLAs, and maintain complaint mechanisms |
| DPA §19 | Cross-border data transfers require adequate protection in the recipient country or data subject consent |
| Single Digital Media Law 2026 | Proposed consolidated framework for digital platforms: unified licensing, content moderation, metadata retention, local representation |
| EAC Cyberlaw Framework | Uganda's ETA, CMA, and DPA derive from EAC harmonisation; revived cross-border data flows project underway |
| Malabo Convention | Continental benchmark for data protection; Uganda has not ratified but DPA already meets its core standards |

---

### References

[^1]: James Kurose and Keith Ross, *Computer Networking: A Top-Down Approach* (8th ed., Pearson, 2021), Section 1.5, pp. 46–57 (Protocol Layers and Their Service Models).

[^2]: Ibid., Section 1.5.1 (Encapsulation).

[^3]: Ibid., Section 1.2 (The Network Edge) and Section 1.3 (The Network Core), pp. 18–42.

[^4]: Ibid., Section 1.3.1 (Packet Switching), pp. 26–34.

[^5]: Ibid., Section 2.4 (DNS — The Internet's Directory Service), pp. 153–176.

[^6]: Ibid., Section 2.4.2 (Overview of How DNS Works), pp. 156–159.

[^7]: Ibid., pp. 158–159 (Local DNS Server).

[^8]: Ibid., pp. 159–162 (DNS Resolution Example).

[^9]: Ibid., Section 2.4.1 (Services Provided by DNS), pp. 154–155.

[^10]: The Uganda Communications (Content) Regulations, 2019 (Statutory Instrument 2019 No. 91), Regulations 3, 5, and 7.

[^11]: Kurose and Ross, *Computer Networking*, Section 2.2 (HTTP), pp. 96–129.

[^12]: Ibid., Section 2.2.3 (HTTP Message Format), pp. 104–112.

[^13]: Ibid., Section 2.2.4 (HTTP Status Codes), pp. 108–110.

[^14]: Ibid., Section 2.2.5 (User-Server Interaction: Cookies), pp. 112–115.

[^15]: Ibid., Section 2.2.7 (HTTPS), pp. 118–123.

[^16]: The Data Protection and Privacy Act (Uganda), No. 9 of 2019, Section 19.

[^17]: The Uganda Communications Act, 2013, Act 1 of 2013, Sections 5, 45, 56, 57, and 93.

[^17a]: The Uganda Communications (Licensing) Regulations, 2019, Statutory Instrument 2019 No. 95.

[^17b]: The Uganda Communications (Fees and Fines) Regulations, 2019, Statutory Instrument 2019 No. 94, as amended by the Uganda Communications (Fees and Fines) (Amendment) (No. 2) Regulations, 2020, Statutory Instrument 2020 No. 111.

[^18]: The Uganda Communications (Content) Regulations, 2019, Regulations 1(2), 3, 5, 7, 8, 38, and 45.

[^19]: The Uganda Communications (Consumer Protection) Regulations, 2019 (Statutory Instrument 2019 No. 87), Regulations 6, 10, 13, 16, 18, 24, and 25.

[^20]: The Regulation of Interception of Communications Act (Uganda), No. 19 of 2010, Sections 2, 5, and related provisions.

[^21]: Isaac Ssejjombwe, "Govt drafts single law to govern media, digital space," *Daily Monitor*, 27 April 2026. See also Global Law Experts, "Uganda's Single Digital Media Law 2026: Practical Compliance Guide for Businesses" (May 2026), available at globallawexperts.com.

[^22]: Chambers and Partners, "TMT 2026 — Uganda" (Global Practice Guides, February 2026), authored by Kirunda & Co Advocates (Robert Kirunda, Olga Karungi, Michelle Grace Mawanda, Dean Michael Mwondha).

[^23]: UNCTAD, "Harmonizing Cyberlaws and Regulations: The Experience of the East African Community" (UNCTAD/DTL/STICT/2012/4, 2012), principal consultant Prof. Ian Walden. See also UNCTAD Press Release UNCTAD/PRESS/IN/2010/023 (21 June 2010).

[^24]: African Union Convention on Cyber Security and Personal Data Protection (Malabo Convention), adopted 27 June 2014, entered into force 8 June 2023, Articles 8–22 (data protection chapter).

[^25]: African Union, "List of Countries Which Have Signed, Ratified/Acceded to the African Union Convention on Cyber Security and Personal Data Protection" (status as of 2 February 2026).

---

### Further Reading

1. James Kurose and Keith Ross, *Computer Networking: A Top-Down Approach* (8th ed., Pearson, 2021) — Sections 1.5 (Protocol Layers), 2.2 (HTTP), and 2.4 (DNS).
2. The Uganda Communications (Licensing) Regulations, 2019, Statutory Instrument 2019 No. 95 — the full licensing framework including procedures, fees, forms, and conditions.
3. The Uganda Communications (Fees and Fines) Regulations, 2019, Statutory Instrument 2019 No. 94, as amended — prescribed fees for all licence categories.
3a. Kenya Information and Communications Act, 1998 (Cap. 411A), and the Kenya Communications Regulations, 2020 (Unified Licensing Framework) — Kenya's tiered licensing model.
3b. Directive 2018/1972 of the European Parliament and of the Council (European Electronic Communications Code), Articles 12–15 (General Authorisation regime).
3c. Communications Act of 1934 (United States), as amended by the Telecommunications Act of 1996, Title I (no ISP licensing requirement); 47 CFR Part 15 (equipment authorisation for unlicensed devices).
4. The Uganda Communications (Content) Regulations, 2019, Statutory Instrument 2019 No. 91.
5. The Uganda Communications (Consumer Protection) Regulations, 2019, Statutory Instrument 2019 No. 87.
6. The Data Protection and Privacy Act, No. 9 of 2019 (Uganda), Section 19.
7. The Regulation of Interception of Communications Act, No. 19 of 2010 (Uganda), Sections 2 and 5.
8. RFC 1034 and RFC 1035 (Domain Names — Concepts and Facilities and Implementation).
9. RFC 7230–7235 (HTTP/1.1 Message Syntax and Routing).
10. RFC 8446 (TLS 1.3 Protocol).
11. UNCTAD, "Harmonizing Cyberlaws and Regulations: The Experience of the East African Community" (2012) — EAC Framework for Cyberlaws and Uganda's alignment.
12. African Union Convention on Cyber Security and Personal Data Protection (Malabo Convention, 2014, in force 2023) — Articles 8–22 on data protection.
13. Global Law Experts / Brian Kalule (Af Mpanga Advocates), "Uganda's Single Digital Media Law 2026" — compliance guides and analysis.
14. DLA Piper Africa (Paul Mbuga, Ruth Muhawe), "Uganda's Data Protection Regulator Clarifies Compliance Requirements for Offshore Entities" (July 2025) — analysis of *Ssekamwa Frank & 3 Ors v. Google LLC*, PDPO Complaint No. 08/11/24/6683.
