# Week 3: Databases — Reading Notes for Legal Practitioners

**Module 1:** Digital Technology Fundamentals
**Program:** Executive Fellowship (AI Law & Digital Sovereignty)
**Target Audience:** Lawyers with no prior computing background

---

## How to Use These Notes

Each section follows the same structure:
1. **Plain-English Explanation** — what it is, in everyday language
2. **Practical Illustration** — a concrete example tied to legal practice
3. **Why It Matters for a Lawyer** — the legal significance
4. **Legal Framework** — relevant Ugandan statutes and case law

---

# PART 1: WHAT IS A DATABASE?

## 1.1 The Filing Cabinet Analogy

Imagine a law firm's filing room:

- **Physical filing system**: You have cabinets, each with labelled drawers. Inside each drawer are folders. Inside each folder are individual documents. To find a client's file, you go to the right cabinet, pull the right drawer, and locate the right folder.
- **A database is the same thing, but digital.** It is a structured collection of information stored on a computer, organised so that data can be easily accessed, managed, and updated.

**Practical Illustration:**

| Physical World | Database World |
|---|---|
| Filing cabinet | Database server |
| Drawer | Table |
| Folder | Row (also called a record) |
| Individual fields on a form (Name, Date, Amount) | Columns (also called fields) |
| Clerk who retrieves files | Database Management System (DBMS) — the software |

**Why this matters for a lawyer:** When a client says "the bank's computer system shows I made a transfer," that record lives in a database. The structure of that database determines whether you can trust that record, challenge it, or use it as evidence.

---

## 1.2 Two Families of Databases

There are two main families of databases, and they work fundamentally differently:

| Feature | SQL Databases (Relational) | NoSQL Databases (Non-Relational) |
|---|---|---|
| **Structure** | Rigid, like a spreadsheet with strict rules | Flexible, like a box of index cards that can hold anything |
| **Consistency** | Strong — data is always accurate immediately | Eventual — data may be out of date for a few seconds |
| **Scaling** | Vertical — buy a bigger computer | Horizontal — buy more computers |
| **Best for** | Banking, payments, financial records | Social media, user profiles, product catalogs |
| **Examples** | PostgreSQL, MySQL, Microsoft SQL Server | MongoDB, Redis, Cassandra |

---

# PART 2: SQL DATABASES (RELATIONAL)

## 2.1 What is a Relational Database?

A relational database organises data into **tables** that are connected to each other through **relationships**. Think of it like a law firm's matter management system.

**Plain English:** Information is stored in separate, neatly organised spreadsheets (tables). Each spreadsheet has columns (fields like "Name", "Date", "Amount") and rows (individual records). The magic is that tables can talk to each other through shared identifiers.

### Practical Illustration: A Law Firm's Billing System

**Table 1: CLIENTS**
| Client_ID | Name | Email | Phone |
|---|---|---|---|
| C001 | Alice Nakato | alice@email.com | 0771000111 |
| C002 | Bob Musoke | bob@email.com | 0772000222 |

**Table 2: MATTERS**
| Matter_ID | Client_ID | Case_Type | Status |
|---|---|---|---|
| M101 | C001 | Commercial | Active |
| M102 | C002 | Family | Closed |

**Table 3: INVOICES**
| Invoice_ID | Matter_ID | Amount | Date |
|---|---|---|---|
| INV001 | M101 | 5,000,000 | 15/03/2026 |
| INV002 | M102 | 2,500,000 | 10/01/2026 |

**What just happened here?** 
- Instead of repeating "Alice Nakato" on every invoice, the system stores her once in the CLIENTS table.
- The MATTERS table links to CLIENTS using Client_ID.
- The INVOICES table links to MATTERS using Matter_ID.
- To find all invoices for Alice Nakato, the system follows the chain: CLIENTS → MATTERS → INVOICES.

**Legal significance:** If you subpoena records for "all transactions involving Alice Nakato," the relational structure means the bank can produce a complete, non-duplicated history. The relationships between tables ensure data integrity — if a matter is closed, all related invoices are still traceable.

---

## 2.2 Key Concepts (with Legal Analogies)

### a) Tables
A table is just a collection of related data stored in rows and columns.

> **Legal analogy:** Think of a table as a **register** — like the Land Register, where each entry (row) contains specific fields (columns) about a property.

### b) Schema
A schema is the blueprint that defines what columns a table has, what type of data each column can hold, and what rules apply.

> **Legal analogy:** A schema is like **the template for a standard-form contract**. Before you fill in any details, the template tells you: "Clause 1 must be a date, Clause 2 must be a party name, Clause 3 must be a monetary amount." The schema enforces structure.

**Example of schema rules:**
- The "Amount" column can only hold numbers (not text like "approximately five million")
- The "Date" column can only hold valid dates
- The "Email" column can only hold values containing "@"

**Why this matters:** If a database has a strict schema, you can trust that the data is well-formed. If you receive a database export and see "NOT A DATE" in a date field, the schema was not enforced — and you should question the reliability of the entire record.

### c) Primary Key
Every row in a table needs a unique identifier — like a National ID number for each record.

> **Legal analogy:** A primary key is like a **Certificate of Title number**. No two properties share the same title number. If you have the title number, you can find the exact property record — no confusion, no duplicates.

In our example above, `Client_ID = C001` uniquely identifies Alice Nakato. There cannot be another row with `Client_ID = C001`.

**Forensic significance:** In litigation, if the opposing party produces database records with duplicate primary keys, that is a red flag — the database integrity is compromised, and you can attack the reliability of the evidence.

### d) Foreign Key
A foreign key is a column in one table that points to the primary key in another table — creating a relationship between the tables.

> **Legal analogy:** A foreign key is like a **cross-reference in a legal document** — "see Schedule A" or "as defined in Clause 4.2 above." It connects one piece of information to another without repeating the content.

In our example, `Matter_ID = M102` in the INVOICES table points to the same `Matter_ID` in the MATTERS table. This tells you which matter the invoice belongs to.

**Why this matters:** Foreign keys enforce **referential integrity** — the database guarantees that you cannot create an invoice for a matter that does not exist. If a court orders production of "all invoices for Matter M102," and the database enforces foreign keys, you can trust that the result is complete.

### e) Structured Querying (SQL)
SQL (Structured Query Language) is the language used to talk to relational databases. It is standardised — meaning the same basic commands work across PostgreSQL, MySQL, and most other relational databases.

> **Legal analogy:** SQL is like **a standardised court form** — everyone uses the same format. "SELECT" means "retrieve these records," "INSERT" means "add a new record," "DELETE" means "remove a record," "UPDATE" means "change a record."

**Simple SQL example:**
```sql
SELECT Name, Amount 
FROM INVOICES 
WHERE Date > '01/01/2026';
```
This says: "Find all invoices dated after 1 January 2026, and show me only the client name and amount."

**Why it matters for cross-examination:**
If a bank says "our system shows the transaction occurred," you can ask:
- "What query did you run to retrieve this data?"
- "Did that query include a WHERE clause that might have filtered out relevant records?"
- "Was the query run against the live database or a backup?"

A lawyer who understands SQL can expose whether the produced data is complete or cherry-picked.

---

## 2.3 ACID Properties (The Gold Standard for Data Integrity)

ACID is an acronym for four properties that guarantee database transactions are processed reliably. This is the most important concept in this module for a lawyer dealing with digital evidence.

### A — Atomicity (All or Nothing)

> **Legal analogy:** A **contract** requires offer, acceptance, and consideration. If any element is missing, there is no contract. Similarly, an atomic transaction either completes fully or does not happen at all.

**Practical Illustration — Mobile Money Transfer:**
When you send UGX 100,000 from your phone to a merchant:
1. Debit your account: -100,000
2. Credit merchant's account: +100,000
3. Record the transaction in the log

With **Atomicity**, if step 1 succeeds but the network fails during step 2, the entire transaction is rolled back. Your account is not debited, and the merchant is not credited. The system returns to the state before you pressed "Send."

**Without Atomicity** (as can happen in some NoSQL systems): Your account is debited 100,000, but the merchant never receives it. The money is lost in cyberspace. Now you have a legal dispute — and the database cannot prove what happened.

### C — Consistency (Data Must Follow the Rules)

> **Legal analogy:** A **will** must meet formal legal requirements — signed, witnessed, dated. If any requirement is missing, the will is invalid. The law enforces consistency just as a database enforces its schema rules.

**Practical Illustration — Banking:**
A bank's database rule says: "An account balance can never be negative." If a transaction tries to deduct 200,000 from an account with only 100,000, the database **rejects the transaction**. It does not allow an inconsistent state.

**Legal significance:** If a database is ACID-compliant and the opposing party claims their system "accidentally" processed a transaction that violated a known rule (e.g., exceeding a credit limit), the ACID consistency guarantee makes that claim harder to believe.

### I — Isolation (Transactions Don't Interfere)

> **Legal analogy:** Imagine two advocates drafting different clauses of the same contract simultaneously. Isolation ensures that Advocate A's changes do not accidentally overwrite Advocate B's changes until both are ready to commit.

**Practical Illustration — Double Spending:**
Two people try to withdraw the last 50,000 from the same bank account at the same time — one at the ATM, one online. With **Isolation**, the database processes one transaction first, locks the record, completes it, then processes the second one — which will fail because the balance is now zero.

**Without Isolation**: Both withdrawals could succeed, resulting in an overdraft of 50,000 that the bank did not authorise.

### D — Durability (Once Done, It Stays Done)

> **Legal analogy:** A **court judgment** once entered cannot be erased. Even if the courthouse burns down, the judgment remains — because there are backup records. Durability is the same principle for database transactions.

**Practical Illustration:**
After you complete a mobile money transfer, the phone network goes down. With **Durability**, the transaction record is already written to permanent storage (hard drive). When the network returns, the record is still there. You can prove the transfer happened.

**Without Durability**: If the system crashes milliseconds after the transaction completes but before it is saved to permanent storage, the record vanishes. The money is gone, but there is no evidence it ever existed.

### ACID Summary Table for Courtroom Reference

| Property | Plain English | Legal Analogy | If Missing |
|---|---|---|---|
| **Atomicity** | All or nothing | Contract formation — missing element = no contract | Partial transactions, lost money |
| **Consistency** | Follows the rules | Will formalities — missing signature = invalid | Invalid data, corrupted records |
| **Isolation** | No interference | Multiple advocates drafting same contract | Double spending, balance errors |
| **Durability** | Permanent record | Court judgment — survives courthouse fire | Evidence vanishes after crash |

---

## 2.4 Vertical Scaling

> **Plain English:** When your filing cabinet is full, you buy a bigger filing cabinet. That is vertical scaling — replacing your computer with a more powerful one (more memory, faster processor, bigger hard drive).

**Practical Illustration:**
A law firm starts with 100 client files. A single filing cabinet works fine. After 10 years, they have 10,000 files. They buy a bigger cabinet. Eventually, they need an entire room. But there is a physical limit to how many files can fit in one room.

**For SQL databases:** Scaling means buying a bigger server. This works well up to a point, but eventually you hit the physical limits of what one machine can do. And big servers are expensive — you pay a premium for the largest machines.

**Why it matters:** If a fintech company uses an SQL database and their transaction volume grows rapidly, they will eventually hit a scaling limit. At that point, they may either:
- Migrate to NoSQL (which could affect data integrity guarantees)
- Implement sharding (splitting the database across multiple servers — complex and expensive)

In litigation, this history matters — was the company using a system that was already at its scaling limit when the disputed transaction occurred?

---

## 2.5 Legal Framework for SQL Records

### Evidence Act Cap. 6

- **Section 2**: Defines "document" to include "any matter expressed or described upon any substance by means of letters, figures, or marks" — this covers database records stored electronically.
- **Section 78**: The court shall presume certified copies of documents to be genuine if they are substantially in the prescribed form.
- **Section 91**: Oral evidence cannot substitute for documentary evidence when the document's contents are in issue.

**Practical significance:** A database printout is a "document" under the Evidence Act. If certified, it benefits from a presumption of genuineness. But that presumption can be rebutted — especially if you can show the database lacked ACID compliance at the relevant time.

### Electronic Transactions Act Cap. 99

- **Section 5**: Legal writing requirements are satisfied by electronic records (including database entries).
- **Section 6**: An electronic record qualifies as an "original" if there is a reliable assurance as to the integrity of the information from the time it was first created.
- **Section 8**: Electronic messages are admissible in evidence. Subsection (5) allows the court to presume an electronic record was generated by a functional computer.
- **Section 9**: Electronic records must be retained in their original format with full integrity.

**Key question for cross-examination:** "Can you demonstrate that the database record was ACID-compliant at the time the transaction was recorded?" If the answer is no, the Section 6 integrity assurance may be compromised.

---

# PART 3: NOSQL DATABASES (NON-RELATIONAL)

## 3.1 What is a NoSQL Database?

> **Plain English:** If SQL is a neatly organised filing cabinet where every folder follows the same format, NoSQL is a box of index cards where each card can hold completely different information. One card might have "Name" and "Phone." Another card might have "Name," "Email," "Address," "Shopping Preferences," and "Last 20 Purchases" — all on one card. There is no standard template.

**Why would anyone use this?** Speed and flexibility. When you have millions of users and each user's data looks different, you do not want to force them into a rigid template. You also want to be able to add new types of information without redesigning the entire system.

### Practical Illustration — Mobile Money Customer Profiles

In an SQL database, every customer must have the same fields:
| Customer_ID | Name | Phone | ID_Number | Date_Joined |
|---|---|---|---|---|

But in the real world, some customers have biometric data, some have agent relationships, some have business accounts with different rules, some have linked bank accounts, some use the service in different languages. A NoSQL database lets you store all of this without forcing every record to have the same structure.

```json
// Customer A — basic user
{
  "customerId": "C001",
  "name": "Alice Nakato",
  "phone": "+256771000111",
  "joined": "2025-01-15"
}

// Customer B — business user with extra fields
{
  "customerId": "C002",
  "name": "Bob Musoke Enterprises Ltd",
  "phone": "+256772000222",
  "joined": "2024-06-01",
  "businessType": "Retail",
  "tinNumber": "TIN123456",
  "linkedAccounts": ["ACC001", "ACC002"],
  "preferences": {
    "language": "Luganda",
    "smsNotifications": true
  }
}
```

**Legal significance:** When you subpoena records, the data produced may look different for each customer. You cannot assume that "all records have the same fields." You need to specifically ask: "Produce the complete database record for Customer X, including all nested data fields."

---

## 3.2 Types of NoSQL Databases

### a) Document Stores
> Stores data as documents (usually JSON format). Each document is self-contained.

**Practical Illustration — Insurance Claims:**
An insurance company stores each claim as a single document containing the claimant's details, policy information, incident description, assessor's report, photos, and payment history — all in one place.

**SQL approach**: Would require 5-7 separate tables (Claimants, Policies, Incidents, Assessments, Photos, Payments) linked by foreign keys.

**Legal advantage of document stores:** To produce a complete claim record, you retrieve one document. No joins needed. Faster and simpler. But — there is no guarantee that related documents are consistent with each other (because there are no foreign key constraints).

### b) Key-Value Stores
> The simplest NoSQL type. Every piece of data is stored with a unique key (identifier) and a value (the data). Like a giant dictionary.

**Practical Illustration — Session Data:**
When you log into mobile banking, the system creates a "session" — a temporary record that you are logged in. It stores this as:
```
Key: "session:USER123:20260315"
Value: { "loggedInAt": "14:30:00", "ipAddress": "196.43.12.5", "expiresAt": "14:45:00" }
```
When you log out, the record is deleted. Super fast. Temporary.

**Example: Redis** — often used for caching, sessions, real-time leaderboards.

**Legal significance:** Key-value stores are often used for temporary data. If litigation arises months after a transaction, that session data may have been automatically deleted. You need to know what data retention policies apply to each type of store, not just the main database.

### c) Column-Family Stores
> Data is stored by column (not by row). Optimised for writing massive amounts of data very quickly.

**Practical Illustration — Mobile Money Transaction Logs:**
A mobile money provider processes millions of transactions per day. A column-family store like **Cassandra** can handle 1,000,000+ writes per second across hundreds of servers.

**SQL approach**: A single SQL server would crash under that write volume. Column-family stores distribute writes across many machines.

**Legal significance:** These stores are great for high-volume logging but have weaker consistency guarantees. A transaction may show as "completed" on one server while still "pending" on another — for a few seconds or even minutes. In litigation, you need to ask: "Which server's copy of the transaction log are you relying on, and was it consistent across all nodes at the relevant time?"

### d) Graph Databases
> Stores data as nodes (entities) and edges (relationships). Optimised for relationship-heavy queries.

**Practical Illustration — Fraud Detection:**
A bank wants to detect money laundering. With a graph database, they can map:
- Person A → sends money to → Person B
- Person B → sends money to → Person C
- Person C → is related to → Person A (same family)
- Person A → is director of → Company X
- Company X → shares address with → Company Y

The graph database can traverse these relationships in milliseconds. An SQL database would require many complex joins and would be much slower.

**Example: Neo4j** — often used for fraud detection, social networks, recommendation engines.

**Legal significance:** If the prosecution in a money laundering case relies on a graph database analysis to show suspicious connections, you need to understand: how was the graph constructed? What data was fed into it? Were there false positives? Graph databases can find connections that are coincidental, not causal.

---

## 3.3 BASE Properties (The NoSQL Alternative to ACID)

> **Plain English:** If ACID is a strict judge who enforces every rule before signing a court order, BASE is a flexible mediator who says "let's agree in principle now and sort out the details later."

### B — Basically Available
The system always responds to queries — even if the response might not contain the latest data.

> **Legal analogy:** An advocate who always answers their phone, even if they do not yet have the complete file in front of them. "I can tell you generally what happened, but I may not have the latest update."

### S — Soft State
The database state can change over time without any new input — because data is still propagating across servers.

> **Legal analogy:** A judgment that is subject to appeal. The legal position is not "final" until all appeals are exhausted. Similarly, a BASE database record is not "final" until all nodes have synchronised.

### E — Eventual Consistency
Given enough time without new updates, all copies of the data will eventually become consistent. But there is no guarantee of *when*.

> **Legal analogy:** "Cheque in the mail." You have been told the money is coming, but you do not know exactly when it will arrive. You trust it will eventually get there.

### Practical Illustration — Social Media "Like"

| Time | Scenario |
|---|---|
| T+0s | Alice posts a photo. |
| T+1s | Bob "likes" it on his phone. |
| T+2s | Carol refreshes her feed from a different server and sees 0 likes. |
| T+5s | Carol refreshes again — now she sees 1 like. |
| T+10s | All servers have synchronised. Everyone sees 1 like. |

For the 8 seconds between T+2 and T+10, the system was **eventually consistent**. Different users saw different data. No one was wrong — they were just looking at different copies of the data before synchronisation completed.

### ACID vs BASE — The Critical Difference for Lawyers

| Scenario | ACID (SQL) | BASE (NoSQL) |
|---|---|---|
| You check your account balance | Always accurate | May show yesterday's balance |
| You transfer money | Completes fully or not at all | May show "pending" for seconds/minutes |
| System crashes mid-transaction | Transaction rolls back safely | Transaction may partially complete |
| Multiple people check same record | Everyone sees same data | Different people may see different data |
| Audit trail for litigation | Immediately reliable | May need to wait for synchronisation |

### Why Fintechs Use Both

Most Ugandan fintechs run **hybrid architectures**:
- **SQL (PostgreSQL)** for transactions, balances, financial records — where ACID is non-negotiable
- **NoSQL (MongoDB)** for customer profiles, product catalogs, analytics — where flexibility matters more
- **NoSQL (Redis)** for caching, sessions — where speed is critical

**Cross-examination question:** "For the transaction in dispute, which database recorded it — your SQL system or your NoSQL system? What were the consistency guarantees at that moment?"

---

## 3.4 Horizontal Scaling

> **Plain English:** If vertical scaling is "buy a bigger filing cabinet," horizontal scaling is "buy more filing cabinets and spread the files across them."

**Practical Illustration — Mobile Money Growth:**
- Year 1: 10,000 customers — one server handles everything
- Year 2: 100,000 customers — one big server (vertical scaling)
- Year 3: 1,000,000 customers — one server is no longer enough
- Year 4: 10,000,000 customers — add 10 servers, each handling 1,000,000 customers (horizontal scaling)

**How NoSQL scales horizontally:** The system automatically distributes data across servers. If Customer A's data is on Server 1 and Customer B's data is on Server 2, the system knows where to find each record without you having to remember.

**Legal significance:** Horizontal scaling means that at any given moment, different servers may have slightly different versions of the data (see "Eventual Consistency" above). If litigation requires proving what a specific server showed at a specific time, you may need to examine individual server logs, not just the database as a whole.

---

## 3.5 Legal Framework for NoSQL Records

The same statutes apply — but the analysis is different.

### Evidence Act Cap. 6
- The "document" definition (Section 2) covers NoSQL records too
- But the presumption of genuineness (Section 78) may be harder to invoke if the records are not in a standard format

### Electronic Transactions Act Cap. 99
- **Section 6 (originality)**: Can a NoSQL document that changed state over 10 seconds (eventual consistency) be considered a reliable "original"? The integrity assurance requirement becomes harder to satisfy.
- **Section 8 (admissibility)**: Admissible, but the weight depends on whether the system was functioning properly at the relevant time.
- **Section 9 (retention)**: If the NoSQL system automatically deletes old versions of documents (soft state), does this comply with statutory retention periods?

### Key Case Law

**Commodity Export International Ltd v. MKM Trading Co. Ltd (CACA 84/2008):**
> "Uganda's Evidence Act was passed long before computers were invented and the issue of electronic evidence could not have been contemplated. It is important that Uganda moves forward into the digital age in a way that makes it possible to resolve legal disputes effectively."

**Significance:** The Court of Appeal recognised that the Evidence Act (1909) was not designed for digital records. Courts must adapt. This gives you room to argue both for and against the admission of NoSQL records — depending on whether the system's architecture supports reliability.

**Amongin Jane Frances Akili v. Lucy Akello & Anor (HCT-02-CV-EP-0001-2014):**
> Per Mutonyi J: "Electronic evidence is any probative information stored or transmitted in digital form that a party at any trial or proceeding may use."

**Practical tip for cross-examination:** NoSQL records are "electronic evidence" under this definition. But the *probative value* (how much they prove) depends on the database's consistency guarantees at the time the record was created.

---

# PART 4: DATA WAREHOUSING — THE BIG PICTURE

## 4.1 What is a Data Warehouse?

> **Plain English:** If an SQL database is a law firm's active filing cabinet (daily use, current matters), a data warehouse is the law firm's archive (historical records, big-picture analysis). You do not use it for day-to-day operations. You use it to run reports, spot trends, and answer big questions.

**Key difference:**
- **Database** (OLTP — Online Transaction Processing): Handles individual transactions. "Debit Alice 100,000. Credit Bob 100,000." Optimised for speed on small operations.
- **Data Warehouse** (OLAP — Online Analytical Processing): Handles massive analysis. "Show me the total transaction volume per region per month for the last 5 years." Optimised for throughput on large queries.

### Practical Illustration

| | Database (PostgreSQL) | Data Warehouse (BigQuery) |
|---|---|---|
| **Purpose** | Process payments | Analyse payment trends |
| **Data** | Last 90 days of transactions | 5 years of transaction history |
| **Query** | "What is Alice's balance?" | "What is the average transaction size in Kampala vs Gulu?" |
| **Speed** | Milliseconds | Seconds to minutes (handles terabytes) |
| **User** | Customers, tellers | Executives, regulators, auditors |

---

## 4.2 ETL Pipelines (Extract, Transform, Load)

> **Plain English:** Before data from multiple sources can be analysed together in a warehouse, it must go through a three-step process:

**Step 1 — Extract:** Pull data from source systems (databases, spreadsheets, APIs).
**Step 2 — Transform:** Clean it up, standardise formats, fix errors, combine datasets.
**Step 3 — Load:** Put the clean data into the data warehouse.

### Practical Illustration — Bank of Uganda Regulatory Reporting

A bank must report its mobile money transaction data to the Bank of Uganda monthly:

1. **Extract**: Pull transaction logs from PostgreSQL (accounting system) and MongoDB (customer profiles).
2. **Transform**: 
   - Convert all dates to a standard format (DD/MM/YYYY)
   - Convert all currencies to UGX
   - Join customer names from MongoDB with transaction records from PostgreSQL
   - Remove duplicate records
   - Flag anomalous transactions for review
3. **Load**: Insert the cleaned dataset into BigQuery for the regulator to query.

**Legal significance:** The ETL process is a point of vulnerability. Errors introduced during transformation can alter the data. If the regulator's report shows different figures than the bank's live system, the ETL pipeline is the first place to investigate.

**Cross-examination question:** "Can you produce the ETL logs showing exactly how the data was transformed before it was loaded into the data warehouse? Were any records modified, deleted, or aggregated during transformation?"

---

## 4.3 Google BigQuery — Serverless Data Warehouse

> **Plain English:** BigQuery is Google's data warehouse service. "Serverless" means you do not have to manage any computers. You just upload your data and run queries. Google handles all the infrastructure — automatically adding more computing power when your query is complex, reducing it when it is not.

### Architecture (Simplified for Lawyers)

BigQuery has four key technologies working together:

### a) Dremel — The Query Engine
> **Analogy:** A team of 1,000 paralegals reviewing documents simultaneously. Instead of one person reading every document, the work is split across thousands of workers, each handling a small piece.

Dremel takes your SQL query and breaks it into tiny pieces, distributes them across thousands of machines, then collects and combines the results. This is why a query that scans 28 GB of data can return results in 2 seconds.

### b) Colossus — The Storage System
> **Analogy:** A library where every book is automatically copied and stored in multiple locations. If one branch burns down, the books are safe because copies exist elsewhere.

Colossus stores data across Google's global network. It handles replication (making copies), recovery (restoring after failures), and distribution (ensuring data is available where needed).

### c) Jupiter — The Network
> **Analogy:** A highway system connecting the library (Colossus) to the paralegal team (Dremel). Jupiter is Google's ultra-fast network that moves data between storage and compute at petabit speeds.

### d) Capacitor — The Storage Format
> **Analogy:** Instead of storing documents as complete files (like PDFs), Capacitor stores each column of data separately. If you only need the "Date" and "Amount" columns, BigQuery reads only those two columns — not the entire 100-column table.

**Why this matters for audit integrity:**
- Data in BigQuery is **immutable** — once written, it cannot be altered without creating a new version
- All queries are **logged** — you can see who queried what, when
- Access is **controlled** — through IAM (Identity and Access Management)
- The separation of storage and compute means you can keep data forever without paying for compute power you are not using

### Practical Illustration — Regulatory Audit Trail

A mobile money provider uses BigQuery for regulatory reporting to the Bank of Uganda. An investigator wants to verify that transaction volumes reported for March 2026 are accurate.

**Using BigQuery audit logs, the investigator can determine:**
1. Who uploaded the March data (and when)
2. What transformations were applied
3. Who queried the data (and when)
4. Whether any data was modified after upload
5. Whether the query results match the data actually stored

**Legal significance:** BigQuery's architecture provides a **strong chain of custody** for data — but only if properly configured. In litigation, you should request:
- BigQuery audit logs for the relevant period
- IAM policy documentation (who had access)
- Data retention and deletion policies
- Any custom transformation scripts used in ETL pipelines

---

## 4.4 Data Warehouses vs Databases — Summary for Lawyers

| Factor | Database (SQL/NoSQL) | Data Warehouse (e.g., BigQuery) |
|---|---|---|
| **Primary use** | Running the business | Analysing the business |
| **Data structure** | Normalised (no duplication) | Denormalised (duplication OK for speed) |
| **Time horizon** | Current data (days/weeks) | Historical data (months/years) |
| **Query type** | Simple, fast (single records) | Complex, slow (millions of records) |
| **User** | Customers, frontline staff | Analysts, regulators, executives |
| **Evidential value** | Best for proving individual transactions | Best for proving patterns and trends |

---

# PART 5: LEGAL PROBLEM-SOLVING FRAMEWORK

## 5.1 How to Analyse a Database Evidence Problem

When faced with digital evidence from a database, use this five-step framework:

### Step 1: Identify the Database Type
- Is it SQL (relational) or NoSQL (non-relational)?
- Clues: Ask what software they use (PostgreSQL, MySQL = SQL; MongoDB, Cassandra = NoSQL)
- **Why it matters:** Determines the consistency guarantees and reliability of the record

### Step 2: Assess the Consistency Model
- Is it ACID (SQL) or BASE (NoSQL)?
- Was the system in normal operation when the record was created?
- **Why it matters:** Determines whether the record is immediately reliable or potentially stale

### Step 3: Check Statutory Compliance
- Did the system record satisfy ETA Section 5 (writing), Section 6 (originality), Section 8 (admissibility)?
- Was the data retained per Section 9?
- **Why it matters:** Determines admissibility and evidential weight

### Step 4: Examine the ETL Pipeline (if applicable)
- Was the data extracted from a warehouse, not a live database?
- Were transformations applied?
- Are transformation logs available?
- **Why it matters:** Data may have been altered between extraction and production

### Step 5: Challenge or Authenticate
- **Challenge**: Point to lack of ACID compliance, eventual consistency gaps, missing ETL logs, schema violations
- **Authenticate**: Point to ACID compliance, audit trails, certification under Section 78 Evidence Act, ETA Section 8(5) presumption

---

## 5.2 Practical Cross-Examination Questions

### For SQL Database Evidence
1. "What database management system does your company use?"
2. "Is it ACID-compliant?"
3. "Was the system ACID-compliant on [date of disputed transaction]?"
4. "Can you produce the transaction log showing the atomic commit for that transaction?"
5. "Was the database under any unusual load at that time that might have affected isolation?"
6. "Has the data in this record been altered since it was first created?"
7. "Can you produce the schema definition to confirm what constraints existed?"

### For NoSQL Database Evidence
1. "What NoSQL database does your company use?"
2. "Is it BASE-compliant?"
3. "What was the consistency level at the time of the disputed record?"
4. "How many servers/nodes did your database have at that time?"
5. "Was the data fully synchronised across all nodes when this record was created?"
6. "Could a user querying a different node have seen different data at the same moment?"
7. "What is your data retention policy for this NoSQL store?"

### For Data Warehouse Evidence (BigQuery)
1. "Was this data produced from a live database or a data warehouse?"
2. "What ETL pipeline was used to load this data?"
3. "Can you produce the ETL transformation logs?"
4. "Were any records modified, aggregated, or excluded during the ETL process?"
5. "Can you produce the BigQuery audit logs for the queries that generated this report?"
6. "Who had access to the data warehouse at the relevant time?"
7. "How is immutability enforced in your BigQuery configuration?"

---

# PART 6: QUICK REFERENCE CARDS

## Cheat Sheet: SQL vs NoSQL

| Question | SQL | NoSQL |
|---|---|---|
| Structure | Tables with fixed columns | Documents, key-values, graphs |
| Schema | Fixed (must define upfront) | Flexible (can change anytime) |
| Consistency | Strong (ACID) | Eventual (BASE) |
| Scaling | Vertical (bigger server) | Horizontal (more servers) |
| Best for | Financial records, transactions | User profiles, catalogs, logs |
| Data integrity | High (enforced by database) | Medium (enforced by application) |
| Query language | SQL (standardised) | Various (vendor-specific) |
| Examples | PostgreSQL, MySQL | MongoDB, Redis, Cassandra |

## Cheat Sheet: ACID vs BASE

| Property | ACID (SQL) | BASE (NoSQL) |
|---|---|---|
| **Key priority** | Consistency | Availability |
| **Transaction** | All or nothing | May partially complete |
| **Data state** | Always valid | May be temporarily invalid |
| **Concurrent reads** | Everyone sees same data | Different users may see different data |
| **Crash recovery** | Full rollback | Partial rollback possible |
| **Legal reliability** | High | Medium (depends on timing) |

## Cheat Sheet: Evidence Act Key Sections

| Section | What it says | Practical use |
|---|---|---|
| S.2 | "Document" includes electronic records | Database records are documents |
| S.78 | Presumption of genuineness for certified copies | Certified database printouts presumed genuine (rebuttable) |
| S.91 | Oral evidence cannot replace documentary evidence | Cannot substitute a witness's word for database records |

## Cheat Sheet: Electronic Transactions Act Key Sections

| Section | What it says | Practical use |
|---|---|---|
| S.5 | Electronic form satisfies writing requirements | A database entry counts as "in writing" |
| S.6 | Electronic record can be an "original" if integrity is assured | Challenge: was integrity assured in a BASE system? |
| S.8 | Electronic messages admissible; S8(5) creates presumption of functional computer | Opponent can use S8(5); you can rebut it |
| S.9 | Electronic records must be retained with integrity | Did the NoSQL soft state violate retention requirements? |

---

# PART 7: GLOSSARY FOR LAWYERS

| Term | Plain English Definition |
|---|---|
| **ACID** | A set of properties (Atomicity, Consistency, Isolation, Durability) that guarantee database transactions are processed reliably. Found in SQL databases. |
| **Atomicity** | All-or-nothing — a transaction either completes fully or is rolled back entirely. |
| **BASE** | Basically Available, Soft state, Eventual consistency — the NoSQL alternative to ACID. Prioritises availability over immediate consistency. |
| **BigQuery** | Google's serverless data warehouse. Handles petabyte-scale analytics. |
| **Column** | A single field in a database table (e.g., "Name", "Date", "Amount"). |
| **Consistency (ACID)** | Transactions must follow all database rules; invalid transactions are rejected. |
| **Consistency (BASE)** | Data will eventually become consistent across all servers, but may be temporarily inconsistent. |
| **Data Warehouse** | A system for analysing large volumes of historical data from multiple sources. |
| **Database** | A structured collection of data. The two main types are SQL (relational) and NoSQL (non-relational). |
| **Document Store** | A NoSQL database that stores data as self-contained documents (usually JSON). |
| **Durability** | Once a transaction is committed, it stays committed even if the system crashes. |
| **ETL** | Extract, Transform, Load — the process of moving data from source systems into a data warehouse. |
| **Foreign Key** | A column that links to the primary key of another table, creating a relationship. |
| **Graph Database** | A NoSQL database that stores entities as nodes and relationships as edges. |
| **Horizontal Scaling** | Adding more servers to handle increased load. Used by NoSQL databases. |
| **Isolation** | Concurrent transactions do not interfere with each other. |
| **Key-Value Store** | The simplest NoSQL database — stores data as key-value pairs (like a dictionary). |
| **NoSQL** | Non-relational databases that prioritise flexibility and scale over strict structure. |
| **OLAP** | Online Analytical Processing — complex queries over large datasets (data warehouse workload). |
| **OLTP** | Online Transaction Processing — fast, simple queries for individual transactions (database workload). |
| **Primary Key** | A unique identifier for each row in a database table. |
| **Relational Database** | A database that organises data into tables with relationships between them. See SQL. |
| **Row** | A single record in a database table. Also called a "record". |
| **Schema** | The blueprint that defines a table's structure (columns, data types, rules). |
| **Serverless** | You do not manage servers — the cloud provider handles infrastructure automatically. |
| **SQL** | Structured Query Language — the standard language for relational databases. Also refers to the database type itself. |
| **Table** | A collection of related data organised in rows and columns. |
| **Vertical Scaling** | Buying a bigger server to handle increased load. Used by SQL databases. |

---

*End of Week 3 Reading Notes. These notes cover all curriculum topics: SQL (tables, schemas, keys, ACID, vertical scaling), NoSQL (document stores, key-value, graph, BASE, horizontal scaling), and Data Warehousing (BigQuery architecture, ETL, serverless analytics), with the Ugandan legal framework (Evidence Act Cap. 6, Electronic Transactions Act Cap. 99, relevant case law) integrated throughout.*
