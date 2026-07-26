# Module 1: Digital Technology Fundamentals
## Week 2: Internet Architecture — Formative Assessment

**Total Marks:** 50  
**Time Allowed:** 1 Hour  
**Instructions:** Answer all questions. Where statutory provisions are cited, quote the provision verbatim and state the source.

---

### Section A: Multiple Choice (10 Marks)

*Circle the correct answer. Each question carries 2 marks.*

**1. Which of the following is the correct order of encapsulation from the application layer downward in the TCP/IP model?**

(a) HTTP Header + Body → IP Header → TCP Header → Ethernet Header  
(b) HTTP Header + Body → TCP Header → IP Header → Ethernet Header + Trailer  
(c) TCP Header → HTTP Header → IP Header → Ethernet Header  
(d) Ethernet Header → IP Header → TCP Header → HTTP Header + Body  

*(2 marks)*

**2. A DNS query returns the IP address of www.example.com. Which type of DNS server is the final authority for that mapping?**

(a) Root DNS server  
(b) Top-Level Domain (TLD) server  
(c) Authoritative DNS server  
(d) Local DNS server  

*(2 marks)*

**3. Under the UCC Consumer Protection Regulations, 2019, within how many days must an operator resolve a consumer complaint?**

(a) 14 days  
(b) 21 days  
(c) 30 days  
(d) 60 days  

*(2 marks)*

**4. Which section of the Uganda Data Protection and Privacy Act requires adequate measures in the recipient country before personal data may be processed or stored outside Uganda?**

(a) Section 17  
(b) Section 18  
(c) Section 19  
(d) Section 20  

*(2 marks)*

**5. An HTTP response with status code 403 indicates:**

(a) The server could not find the requested resource  
(b) The server understood the request but refuses to authorise it  
(c) The request was successful  
(d) The server encountered an internal error  

*(2 marks)*

---

### Section B: Short Answer (20 Marks)

*Answer in the space provided. Each question carries 5 marks.*

**6. Explain the difference between the network edge and the network core.**  
Identify which side a lawful interceptor under RICA would most likely target and why.

*(5 marks)*

**7. Describe the role of the local DNS server in the DNS resolution process.**  
Why is the local DNS server significant for establishing jurisdiction in an internet fraud investigation?

*(5 marks)*

**8. Quote verbatim Section 19 of the Data Protection and Privacy Act (Uganda, 2019).**  
Explain the two alternative conditions under which personal data may be processed or stored outside Uganda.

*(5 marks)*

**9. Under UCC Content Regulations, 2019, Regulation 7, how long must an operator retain records of broadcast content?**  
State the three characteristics the retained records must possess.

*(5 marks)*

---

### Section C: Problem Question (20 Marks)

**10. Read the following fact pattern and answer the questions that follow.**

**Fact Pattern:**

KampalaPay Ltd, a Ugandan fintech company licensed by the Bank of Uganda, processes mobile money transactions through a web application hosted on AWS servers in Frankfurt, Germany. Customers access the service via `https://www.kampalapay.co.ug`. On 15 June 2026, a customer alleges that during a transaction:

- The browser displayed a "Your connection is not private" warning before the customer clicked "Proceed anyway."
- The transaction data was intercepted.
- The DNS resolution for `www.kampalapay.co.ug` returned an IP address registered to a server in Amsterdam, not Frankfurt.
- KampalaPay Ltd had not obtained explicit consent from customers to store their personal data in Germany.

**Questions:**

**(a)** At which TCP/IP layer(s) could the interception have occurred? Identify at least two possible layers and explain what evidence you would examine to confirm each.  
*(6 marks)*

**(b)** Under the UCC Consumer Protection Regulations, 2019, identify two provisions that KampalaPay Ltd may have breached in relation to the protection of customer information. Quote the relevant regulation numbers.  
*(4 marks)*

**(c)** Does KampalaPay Ltd's use of AWS Frankfurt servers comply with Section 19 of the DPA? Explain why or why not, and state what steps KampalaPay Ltd should take to achieve compliance.  
*(6 marks)*

**(d)** If the unauthorised interception was performed by a third party who obtained a RICA warrant, would the warrant authorise the interception of HTTPS communications? Explain the technical limitation and cite the relevant RICA provision.  
*(4 marks)*

---

**END OF ASSESSMENT**
