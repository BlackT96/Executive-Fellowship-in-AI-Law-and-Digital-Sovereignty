# Interpretive Opinion: Section 29(2)(a) of the Electronic Transactions Act, Cap. 99

## Question Presented

Does Section 29(2)(a) of the Electronic Transactions Act, Cap. 99 (Uganda) remove a service provider's entire Section 29(1) liability exemption upon entering into a contractual API agreement, or does the exemption continue to apply to third-party claims while merely not overriding the parties' contractual obligations?

## Short Answer

**Section 29(2)(a) does not remove the Section 29(1) exemption.** It does something narrower: it prevents the exemption from being used as a defence *between the contracting parties* to excuse performance of what they freely agreed. The exemption continues to protect the service provider against third-party claims (tort, infringement, statutory liability) regardless of whether a contract exists.

---

## 1. Textual Analysis

### The provision

**Section 29(1):**
> A service provider is not liable for third-party material to which it merely provides access, if the liability is founded on—
> (a) making, publication, dissemination or distribution of the material; or
> (b) infringement of any rights in the material.

**Section 29(2):**
> However, this exemption does not affect—
> (a) contractual obligations;
> (b) obligations under a licensing or regulatory framework;
> (c) obligations imposed by law or court order to remove, block, or deny access.

### Key textual features

| Word / Phrase | Significance |
|---|---|
| **"this exemption"** | Refers to the entire S.29(1) rule — the proposition that the service provider "is not liable" for third-party material. |
| **"does not affect"** | The exemption does **not nullify**, **override**, or **displace** contractual obligations. The exemption and the contract coexist. |
| **"contractual obligations"** | Obligations that arise **from a contract** — promises the service provider made to a specific counterparty. |

### What the text does NOT say

The provision does **not** say:
- "This exemption **does not apply** where a contractual obligation exists"
- "This exemption **ceases to have effect** in respect of any matter covered by a contract"
- "A service provider who enters into a contract **loses** the protection of subsection (1)"

Parliament chose the phrase "does not affect" rather than "does not apply." This choice is significant. Under the canon *expressio unius est exclusio alterius* (the expression of one thing is the exclusion of another), the deliberate omission of language that would remove the exemption altogether implies that Parliament did not intend that result.

### Plain meaning

The plain meaning of S.29(2)(a) is:

> *If a service provider has a contractual obligation (e.g., "I will keep the API running at 99.9% uptime"), the S.29(1) exemption does not excuse non-performance of that obligation. But the exemption still protects the service provider against claims from third parties who are not party to that contract.*

---

## 2. Contextual Analysis — Part V Read as a Whole

Part V (Sections 29–33) creates a **safe harbour** framework for service providers — modelled on the US Digital Millennium Copyright Act (DMCA s.512), the EU E-Commerce Directive (Articles 12–15), and similar provisions in Kenya (KICA s.72B–D) and South Africa (ECTA s.72–78).

| Section | Function |
|---|---|
| **S.29** | **Mere conduit / access** — no liability for transmitting or providing access to third-party material |
| **S.30** | **Information location tools** — no liability for linking to infringing material (conditional on notice/takedown) |
| **S.31** | **Notice and takedown procedure** — procedural mechanism for infringement claims |
| **S.32** | **No duty to monitor** — service providers need not actively police user content |
| **S.33** | **Territorial jurisdiction** — the Part applies where service provider is established in Uganda |

### Contextual argument

If S.29(2)(a) were read as removing the entire exemption upon entering any contract, the consequences would be absurd:

- **Every service provider with Terms of Service** (i.e., virtually every service provider) would lose the exemption. The safe harbour would be meaningless.
- **S.30** (information location tools) would be similarly gutted — because S.30(3) preserves contractual obligations in identical language.
- **S.32** (no duty to monitor) would be undermined, since a contractual obligation to detect infringing content could be manufactured through any API agreement.

Ugandan courts apply the **golden rule**: where a literal interpretation leads to absurdity, the court may depart from the literal meaning. More directly, the **harmonious construction** principle requires that S.29(2)(a) be read in a way that gives effect to the entire Part, not in a way that destroys it.

---

## 3. Legislative Intent — The Mischief S.29 Was Enacted to Remedy

### The mischief

Before S.29, a service provider who merely transmitted or hosted third-party content could be held **secondarily liable** for:
- Defamation (e.g., a user posts a defamatory comment)
- Copyright infringement (e.g., a user uploads infringing material)
- Other tortious content created by users

This created a chilling effect: platforms would either refuse to host user content or would over-censor to avoid liability. The East African Community harmonisation framework and the UNCTAD assessment both identified intermediary liability as a barrier to e-commerce development in Uganda.

### Parliament's purpose

S.29 was enacted to **create a safe harbour** — to say: *if you are merely a conduit or access provider, you are not liable for what your users do.* This is standard intermediary liability reform worldwide.

### What does the mischief tell us about S.29(2)(a)?

The mischief was **third-party claims** against intermediaries for user-generated content. The exemption addresses that mischief. S.29(2)(a) preserves the parties' freedom to **allocate risk by contract** — it means that the exemption does not override the parties' own allocation of responsibility.

If Parliament had intended to remove the exemption entirely upon entering a contract, it would have been defeating the very mischief it set out to remedy — because virtually every commercial relationship involves a contract.

---

## 4. Interpretive Canons Applied

### Literal rule (primary)

The plain words "does not affect" mean the exemption remains in force alongside contractual obligations. It affects neither their validity nor their enforceability.

### Golden rule (absurdity avoidance)

Reading S.29(2)(a) as removing the exemption leads to absurdity: service providers lose protection merely by having a contract, which is the normal state of commercial affairs. This cannot have been intended.

### Mischief rule (Heydon's Case)

The mischief was intermediary liability for user content. The remedy was a safe harbour. A broad reading of S.29(2)(a) would undo the remedy.

### Purposive approach

The purpose of Part V is to limit intermediary liability to promote e-commerce. S.29(2)(a) serves the limited purpose of ensuring that the safe harbour does not become a shield for contractual non-performance. It does not destroy the harbour.

### Reading the statute as a whole

Part V must be read as an integrated safe harbour scheme. S.30 and S.32 would be equally undermined by a broad reading of S.29(2)(a). An interpretation that preserves all three provisions is to be preferred.

### "Always speaking" principle

The ETA is a technology-neutral statute. The concept of "contractual obligations" is generic and accommodates any type of contract, including API agreements. But the principle of technology neutrality cuts both ways: it also means the safe harbour was designed to endure across changing business models, not to be contracted away by implication.

### Harmonious construction with the Data Protection and Privacy Act, 2019

Under the DPA, a data processor (e.g., a cloud API provider) has statutory obligations regardless of contract — security measures (s.20), data breach notification, etc. S.29(2)(a) preserves contractual obligations, but the DPA's statutory obligations are preserved under S.29(2)(b) (regulatory framework) and S.29(2)(c) (obligations imposed by law). This reinforces that S.29(2)(a) is about contractual, not statutory, liability.

---

## 5. Interpretation Stated

### The correct interpretation

**Section 29(2)(a) preserves contractual obligations as between the contracting parties. It does not remove the Section 29(1) exemption in respect of third-party claims.**

Concretely:

| Scenario | Effect |
|---|---|
| A third-party sues the service provider for defamation based on user-generated content transmitted via the API | S.29(1) exemption applies — the service provider is protected. S.29(2)(a) is irrelevant because there is no contract between the service provider and the third party. |
| The startup sues the platform for breach of the API contract (e.g., failure to maintain uptime) | S.29(1) exemption does not apply — the contract is preserved. The platform cannot say "I'm exempt under S.29(1)." S.29(2)(a) prevents this use of the exemption. |
| A third-party sues the service provider for copyright infringement based on infringing material transmitted via the API | S.29(1) exemption applies. The existence of an API contract with the startup does not change this. |
| The startup sues the platform for a statutory data protection breach (DPA s.20) | S.29(2)(b) and (c) preserve regulatory and statutory obligations — not S.29(2)(a). The exemption does not shield the platform from DPA claims, but this is because of S.29(2)(b)/(c), not because the contract exists. |

### Why the alternative interpretation (exemption lost entirely) is rejected

**Alternative Interpretation A — "The exemption is entirely lost if there is any contract"**

This interpretation is rejected for the following cumulative reasons:

1. **Text**: The words "does not affect" cannot bear the meaning "removes." If Parliament intended removal, it would have said "this exemption does not apply where there are contractual obligations."

2. **Absurdity**: It would mean that any service provider with Terms of Service (i.e., every service provider) loses the safe harbour. The safe harbour would protect only truly gratuitous, contract-free arrangements — a category that barely exists in commercial practice.

3. **Surplusage**: If the exemption were entirely lost upon contract, S.29(2)(b) and (c) would be largely redundant — regulatory and statutory obligations would also be preserved, but the exemption would already be gone. Parliament does not legislate in vain.

4. **Defeats the mischief**: The whole point of S.29 was to create a safe harbour for intermediaries. This interpretation would destroy it for any commercial intermediary.

5. **Inconsistent with S.30 and S.32**: S.30(3) and S.32(2) contain identical "does not affect" language. If this interpretation were applied to all three, the entire safe harbour scheme collapses.

**Alternative Interpretation B — "The exemption is partially lost, to the extent of the contractual obligation"**

This is closer to the correct interpretation but still imprecise. The exemption is not "lost" at all — it simply does not excuse the contractual obligation. The exemption continues to exist for non-contractual claims.

### Distinction from the course notes

I note that the existing course notes (Week 4 Reading Notes) state: *"the exemption does not apply if the API provider has a contractual obligation"* and *"lost if contract exists."* These are simplified teaching statements that, while useful for introducing the concept, are legally imprecise. They risk creating the impression that entering a contract destroys the safe harbour entirely. The correct position is more nuanced: the exemption remains for third-party claims; it is merely unavailable as a defence to a contractual claim.

---

## 6. Practical Application to the API Agreement Scenario

### The scenario

A Ugandan startup wants to integrate with a large platform (e.g., SafeBoda, MTN Mobile Money) via API. The platform is concerned that signing an API agreement will trigger S.29(2)(a) and expose it to full liability for anything the startup does with the data.

### Advice to the platform

**The concern is misplaced.** Signing an API agreement does not strip the platform of S.29(1) protection. Here is what actually happens:

1. **Third-party claims (non-contractual):** If a third party sues the platform because the startup misused data obtained via the API, the platform can still invoke S.29(1). The exemption applies. The existence of the API contract is irrelevant to third-party claims.

2. **Claims by the startup (contractual):** If the startup sues the platform for breaching the API agreement (e.g., downtime, data quality, SLA breaches), the platform cannot use S.29(1) as a defence. This is what S.29(2)(a) means — the contract is enforceable despite the exemption.

3. **Statutory claims (DPA, CMA, etc.):** If the startup or a third party sues the platform for violating the Data Protection and Privacy Act (e.g., failure to secure data), S.29(1) does not shield the platform anyway — S.29(2)(b) and (c) preserve regulatory and statutory obligations. But this has nothing to do with the existence of the API contract.

### What the platform should actually worry about

The platform's liability exposure in an API agreement depends on:

| Source of Liability | Protected by S.29(1)? | Notes |
|---|---|---|
| Third-party IP infringement via API | Yes | S.29(1) applies; S.29(2)(a) does not remove it |
| Third-party defamation via API | Yes | Same |
| Breach of contract with startup | No | S.29(2)(a) preserves the contract |
| DPA s.20 security breach | No (S.29(2)(b)/(c)) | Statutory obligation, preserved independently |
| Data localisation violations | No (S.29(2)(b)/(c)) | Regulatory obligation, preserved independently |
| Startup's misuse of data against third parties | Likely protected for platform (S.29(1)) | Unless platform had actual knowledge or control — see S.30 knowledge threshold |

### Practical drafting recommendation

The API agreement should not rely on S.29(1) as a contractual shield. It should set out the platform's liability expressly:

- **For third-party claims**: The platform may wish to include an indemnity from the startup for claims arising from the startup's use of the data (this is contractual allocation of risk, consistent with S.29(2)(a)).
- **For service levels**: The platform should cap its liability for SLA breaches consistent with its exposure under the contract.
- **For data protection**: The platform should comply with DPA obligations regardless of the API agreement or S.29(1).

S.29(2)(a) does not prevent the platform from limiting its contractual liability through standard clauses (liability caps, exclusions, disclaimers). What it prevents is the platform saying: *"I have no contractual liability because S.29(1) exempts me."*

---

## 7. Summary

| Element | Conclusion |
|---|---|
| **Does S.29(2)(a) remove the S.29(1) exemption entirely?** | **No.** The exemption continues to apply to third-party claims. |
| **What does S.29(2)(a) do?** | It preserves contractual obligations — the exemption cannot be used as a defence to a claim for breach of contract. |
| **Can a service provider still rely on S.29(1) after signing an API agreement?** | **Yes,** for claims by persons not party to that agreement. |
| **Can the startup still sue the platform for breach of the API agreement?** | **Yes.** S.29(1) is no defence to a contractual claim. |
| **What about statutory claims (DPA, CMA)?** | Preserved under S.29(2)(b) and (c), regardless of contract. |

The safe harbour in S.29(1) is not a fragile thing that disappears the moment paper is signed. It is a statutory protection that operates in the realm of third-party liability — the realm the safe harbour was designed to address. S.29(2)(a) is simply Parliament's way of saying: *"You cannot use this Act to weasel out of a promise you voluntarily made."*
