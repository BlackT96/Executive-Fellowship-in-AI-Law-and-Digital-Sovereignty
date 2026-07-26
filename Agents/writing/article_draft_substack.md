# The Abstraction Layer Problem in Ugandan Tech Regulation

*Why Uganda's laws need to see the computer as a stack, not a monolith*

---

## 1. The Problem

Ugandan law does not know what a computer is.

This is not a flippant statement. Open the Computer Misuse Act, 2011 (as amended). Read Section 12 on unauthorised access. Read Section 14 on access with intent. The Act speaks of "a computer" and "a computer system" as if these were single, indivisible things — black boxes that either work or do not work, that either were accessed or were not accessed.

Open the Sale of Goods and Supply of Services Act, Cap. 79. Sections 40–42 imply terms as to quality and fitness for purpose for "goods." A server is goods. A software licence is a service. But where does the operating system sit? Where does a firmware update fall? The Act does not say.

This is the abstraction layer problem: Ugandan law regulates "the computer" as a monolith, while the technology it regulates is a stack of distinct, separable, and independently accountable layers.

Every computer system rests on four pillars:

| Layer | Components | Typical Vendor |
|-------|-----------|----------------|
| Hardware | CPU, RAM, storage, motherboard, cables | Hardware manufacturer or refurbisher |
| Operating System | Kernel, device drivers, process scheduler, memory manager | Microsoft, Apple, Linux distributor, or system integrator |
| Application Software | The program the user actually interacts with | Software developer or SaaS provider |
| Network | Routers, switches, protocols, internet connectivity | ISP, network equipment vendor, or in-house IT |

A system failure originates at exactly one of these layers. The others merely transmit or react to the failure. A CPU cache physically overheats (hardware layer). The OS detects the fault and throws a kernel panic (OS layer — symptom, not cause). The application crashes (software layer — secondary effect). The network logs the server going offline (network layer — tertiary effect).

Ugandan law, as currently structured, struggles to distinguish the originating layer from the symptomatic layers. This has real consequences for litigants, regulators, and policymakers.

---

## 2. Why the Abstraction Layer Problem Matters

### 2.1 Product Liability Becomes a Guessing Game

Consider a typical Ugandan scenario. A company in Kampala buys a server assembled from refurbished components. Six months later, it crashes during peak hours, destroying operational data.

The software vendor says: "Refurbished hardware overheated."

The hardware vendor says: "The OS configuration overloaded the processor threads."

The OS integrator says: "The application had a memory leak."

Current law gives the litigant no doctrinal tool to decide who is right. The result is practice-direction litigation — the plaintiff sues everyone and lets the court sort it out. This is inefficient, expensive, and unpredictable.

A layer-aware framework would tell the court: determine which abstraction layer the failure originated at, then apply the liability rules specific to that layer. Hardware defects engage the Sale of Goods Act. OS misconfiguration engages the service contract with the system integrator. Software bugs engage the software licence or the Consumer Protection Act.

### 2.2 Criminal Liability Under the Computer Misuse Act

The Computer Misuse Act criminalises "unauthorised access" to a computer system. But what counts as overcoming a "secure system device"?

Consider two attacks:

- **Attack A:** An attacker exploits a user-mode buffer overflow to execute code within an application's memory space. The OS kernel access controls remain intact.
- **Attack B:** An attacker exploits a kernel privilege escalation vulnerability to bypass the OS's user-mode/kernel-mode boundary entirely.

Both are "unauthorised access" under Section 12. But they are technically very different. Attack A exploits an application vulnerability within the OS's permission framework. Attack B exploits a flaw in the OS's core security mechanism.

A layer-aware statute would distinguish these. Attack A might be a software vulnerability actionable against the developer. Attack B might be an OS-level defect with different liability implications. Currently, the law treats them identically — and in doing so, loses the granularity needed to assign responsibility accurately.

### 2.3 Electronic Evidence Admissibility

Section 8(5) of the Electronic Transactions Act (Cap. 99) requires evidence that a "computer system was operating properly" at the material time for electronic records to be admissible.

But what does "operating properly" mean when a system has multiple layers? If the hardware layer was functioning but the OS layer had a memory leak, was the system "operating properly"? If the application crashed but the OS continued running, are the OS logs admissible even though the application logs are unreliable?

The courts of Uganda have not yet had to answer these questions in detail. When they do, they will need a framework that distinguishes which layer's proper operation is relevant to the specific record being tendered.

---

## 3. Comparative Approaches

### 3.1 The European Union: AI Liability Directive

The EU's proposed Artificial Intelligence Liability Directive (2022) introduces a tiered liability framework distinguishing between:

- Hardware defects (product liability under the Product Liability Directive)
- Software defects (strict liability for AI systems under the new directive)
- Operator fault (fault-based liability for human oversight failures)

This is precisely the kind of layer-aware regulation Uganda lacks. The EU approach recognises that a failure in an AI system's training data (software layer) is doctrinally different from a failure in its sensor hardware (hardware layer), and allocates liability differently for each.

### 3.2 The United Kingdom: Product Security and Telecommunications Infrastructure Act 2022

The UK's PSTI Act imposes different security duties on:

- Manufacturers of internet-connectable products (hardware layer)
- Software vendors who provide updates (software layer)
- Network providers (network layer)

Each duty is separately enforceable by different regulators. This is a statutory recognition that security is a layered responsibility and cannot be assigned to a single "computer" duty-bearer.

### 3.3 Kenya: Computer Misuse and Cybercrimes Act, 2017

Kenya's Act, like Uganda's, largely treats "computer" as a monolithic term. However, Kenya has moved further in subsidiary legislation — the Data Protection Act, 2019 and its regulations distinguish between data controllers and data processors by technical layer (e.g., cloud infrastructure vs. application-level processing), providing a useful reference point for Uganda.

---

## 4. Policy Recommendations

### 4.1 Amend the Computer Misuse Act to Define Technical Layers

Parliament should consider introducing definitions that distinguish between:

- "Hardware layer" — the physical components of a computer system
- "Operating system layer" — the software managing hardware resources and enforcing access controls
- "Application layer" — software providing user-facing functionality
- "Network layer" — the infrastructure connecting computer systems

A provision stating that "unauthorised access" must be identified by the specific layer at which access controls were overcome would give courts a clear analytical framework.

### 4.2 Introduce a Technology Product Liability Framework

The Sale of Goods and Supply of Services Act should be amended or supplemented with a Technology Product Liability Act that:

- Imposes strict liability on hardware manufacturers for physical defects (existing framework)
- Imposes fault-based liability on software vendors for code defects
- Imposes fault-based liability on system integrators for configuration errors
- Requires the claimant to identify the originating layer of the failure as a pleading requirement

### 4.3 Issue a Practice Direction on Electronic Evidence

The Chief Justice should consider a practice direction under the Electronic Transactions Act establishing a "layer-by-layer" admissibility test for electronic records. The test would require the party tendering electronic evidence to specify:

- Which layer of the system generated the record
- Whether that layer was operating properly at the material time
- Whether a malfunction in another layer affected the integrity of the record from the relevant layer

### 4.4 Establish a Technology and Law Reform Committee

The Uganda Law Reform Commission should establish a standing committee on technology and law reform, including computer scientists and systems engineers alongside lawyers, to ensure that future technology legislation is technically literate and layer-aware.

---

## 5. Conclusion

Uganda is at an inflection point. The National Digital Transformation Strategy, the emerging AI policy framework, and the ongoing review of the Computer Misuse Act all present opportunities to build technical literacy into the fabric of Ugandan regulation.

The abstraction layer model is not just a computer science concept. It is a liability map. Every layer has a different manufacturer, a different vendor, a different contract, and a different legal relationship with the end user. A law that cannot distinguish the layers cannot assign responsibility accurately.

The choice is straightforward. Continue regulating the computer as a black box — and accept that every system failure case will be a litigation lottery. Or adopt a layer-aware framework — and give Ugandan courts, litigants, and regulators the tools they need to decide who is actually responsible when the system goes down.

---

*This article is for informational purposes only and does not constitute legal advice. The state of the law is as of July 2026.*

---

**SOURCES**

- The Computer Misuse Act, No. 2 of 2011 (Uganda), as amended
- The Sale of Goods and Supply of Services Act, Cap. 79 (Uganda)
- The Electronic Transactions Act, Cap. 99 (Uganda)
- European Commission, Proposal for a Directive on Adapting Non-Contractual Civil Liability Rules to Artificial Intelligence (AI Liability Directive), COM(2022) 496 final
- UK Product Security and Telecommunications Infrastructure Act 2022
- Kenya Data Protection Act, No. 24 of 2019
- Uganda National Digital Transformation Strategy, 2023–2028
- Matthew Justice, *How Computers Really Work* (No Starch Press, 2021), Chapters 1–3
- Andrew S. Tanenbaum and Herbert Bos, *Modern Operating Systems* (5th ed., Pearson, 2023), Chapter 1
