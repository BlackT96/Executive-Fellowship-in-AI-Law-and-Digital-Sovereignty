# Data Localisation vs Cloud Adoption: The Bind Facing Ugandan Tech Startups

*Uganda's startups are told to scale globally but store data locally — the law is not making it easy*

---

## 1. The Bind

A Kampala fintech startup raises its seed round. It builds on AWS because that is where the talent knows how to deploy, where the credit card works, and where the compliance certifications already exist. Six months later, the startup's lawyer reads the Data Protection and Privacy Act, 2019 and discovers that transferring customer data to AWS's South Africa region may require an adequacy determination that Uganda has not yet made.

This is the bind: Uganda has no explicit data localisation law, but its cross-border transfer rules under DPA Section 26 create the practical equivalent — without the clarity.

Section 26 permits transfers only if:
- The recipient country has adequate data protection (no official list published by NITA-U as of mid-2026)
- The data subject consents
- The transfer is necessary for contract performance
- Other limited exceptions apply

The result is legal uncertainty. Startups cannot confidently choose between a Rwandan sovereign cloud, AWS Cape Town, or a server under a desk in Kampala — because the law has not told them which choice is compliant.

---

## 2. The Regional Drift Toward Localisation

Uganda's hesitation sits within an East African region that is moving — unevenly — toward data localisation.

| Jurisdiction | Position |
|---|---|
| **Uganda** | No explicit localisation law. DPA Section 26 restricts cross-border transfers without adequacy or consent. Adequacy list unpublished. |
| **Kenya** | Data Protection Act Section 50 requires processing through a local server for public interest data. Cloud Policy 2025 mandates localisation for certain categories. |
| **Rwanda** | Enforced localisation. MTN Rwanda fined FRw 7.03 billion (USD 8.2M) for transferring data outside Rwanda without authorisation under RURA Regulations 2016. |
| **Tanzania** | No explicit localisation law under the PDPC Act 2022. |
| **EAC (Draft)** | Developing a harmonised data protection framework — direction of travel is toward managed cross-border flows, not blanket localisation. |
| **AfCFTA Digital Trade Protocol** | Article 22 prohibits mandatory data localisation, with exceptions for legitimate public policy and national security. Not yet ratified by Uganda. |

The region is pulling in two directions. Rwanda says store it here. The AfCFTA says do not block data flows. Uganda sits in the middle with a law that restricts cross-border transfers but no administrative apparatus to tell startups how to comply.

---

## 3. Why Startups Use Global Cloud Providers

Ugandan startups do not choose AWS, Azure, or Google Cloud out of disloyalty. They choose them because:

- **Ecosystem talent.** Developers trained on these platforms are readily available.
- **Certifications.** ISO 27001, SOC 2, PCI-DSS — the certifications that enterprise customers and investors require — come bundled.
- **Cost.** Hyperscaler pricing beats building a Tier III data centre in Kampala by orders of magnitude.
- **Reliability.** AWS Cape Town offers 99.99% uptime SLAs. A local server on unreliable grid power does not.
- **Global integration.** Payment gateways, identity providers, and downstream APIs are already on these platforms.

A mandatory localisation requirement would force startups to choose between compliance and competitiveness.

---

## 4. What the Law Actually Requires

The DPA's cross-border transfer framework (Section 26, read with Regulations 31-33) does not say "store data in Uganda." It says:

1. Ensure the recipient country has adequate protection (Regulation 31 — factors include the rule of law, independent oversight, international obligations)
2. Or obtain the data subject's consent (Regulation 32)
3. Or demonstrate that the transfer is necessary for contract performance, or for reasons of public interest, legal claims, or vital interests
4. Document the transfer assessment

For a fintech startup using AWS Cape Town, the practical path is either:
- **Adequacy.** But Uganda has not listed South Africa as adequate. South Africa has POPIA, which is broadly comparable to Uganda's DPA, so a case can be made — but there is no official determination.
- **Consent.** Obtain explicit, informed consent from each data subject for cross-border transfer. This is operationally heavy and may not cover all processing purposes.
- **SCCs.** Adopt standard contractual clauses with the cloud provider — a recognised transfer mechanism under global practice, though Uganda's DPA Regulations do not explicitly provide for SCCs the way the GDPR does.

The uncertainty is not that the law prohibits cloud adoption. It is that the law does not clearly authorise it either.

---

## 5. What Startups Should Do Now

1. **Document the adequacy assessment.** Even without an official list, Regulation 31 provides criteria. Assess South Africa's POPIA framework against those criteria and document the analysis. A reasoned, good-faith adequacy assessment is better than no assessment at all.

2. **Insist on a DPA with your cloud provider.** DPA Section 21 requires a contract between controller and processor. The cloud provider's standard terms should be supplemented with a Data Processing Agreement that specifies security measures, restricts sub-processing, and addresses cross-border transfer mechanisms.

3. **Use data residency controls.** AWS permits customers to restrict data to a specific region. Configure the account to store and process data only in the Africa (Cape Town) region, with replication disabled across regions. Document this configuration.

4. **Monitor the adequacy list.** NITA-U has indicated it will publish a list of adequate jurisdictions. When South Africa, Kenya, or Rwanda appear on the list, the transfer assessment becomes straightforward.

5. **Engage with NITA-U.** The Personal Data Protection Office under NITA-U is receptive to industry input. A joint submission from the startup community requesting expedited adequacy determinations for key cloud regions would serve the entire ecosystem.

---

## 6. The Bottom Line

Uganda does not need a data localisation law to protect its startups' data. It needs a functional cross-border transfer framework — clear adequacy determinations, model contractual clauses, and guidance that startups can actually follow.

The alternative is a silent tax on every Ugandan tech startup: the cost of legal uncertainty, the delay of bespoke compliance advice, and the risk of enforcement action for doing what every startup in the world does — using the best cloud infrastructure available.

Startups will store data where the law is clear. Uganda has a chance to make that answer "wherever the best infrastructure is, with appropriate safeguards." The window will not stay open forever.

---

*This article is for informational purposes only and does not constitute legal advice. The state of the law is as of July 2026.*

**SOURCES**

- Data Protection and Privacy Act, 2019 (Uganda), Sections 21, 26
- Data Protection and Privacy Regulations, 2021, Regulations 31-33
- Kenya Data Protection Act, 2019, Section 50
- Kenya Cloud Policy, May 2025
- MTN Rwanda fine — RURA Regulations 2016 enforcement action
- AfCFTA Digital Trade Protocol, Article 22 (not yet ratified)
- EAC Data Protection Framework (Draft)
- NITA-U Personal Data Protection Office guidance notes
- AWS Africa (Cape Town) Region — data residency documentation
