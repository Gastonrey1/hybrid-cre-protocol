# Hybrid Computational Reflective Equilibrium (Hybrid CRE) ⚖️🤖  
### Official Reference Implementation

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18523702.svg)](https://doi.org/10.5281/zenodo.18523702)  

---

## 🧠 What is Hybrid CRE?

**Hybrid Computational Reflective Equilibrium (Hybrid CRE)** is a **constitutional decision architecture for AI systems**.  
Instead of treating alignment as a scalar optimization problem, Hybrid CRE structures artificial decision-making through **jurisdictional logic, procedural safeguards, and institutional review mechanisms**.

The protocol enables AI systems to resolve normative conflicts using **structured governance processes**, not just reward shaping or post-hoc oversight.

This repository provides the **official reference implementation** of the Hybrid CRE computational protocol.

---

## 🧩 System Overview

Hybrid CRE is composed of three core institutional modules:

### **SIS — Systemic Impact Score**
Evaluates the **cross-domain systemic consequences** of candidate decisions.  
SIS models how actions propagate across institutional, social, and regulatory layers. it is part of ATC.

### The ATC, The Alignment Trazability Code: High-Performance Governance Controller

The **ATC (Anti-Gaming & Transition Controller)** is implemented as a lightweight, asynchronous governance controller operating outside the core inference loop.

- **Non-Blocking Architecture:** Model inference remains unaffected. The ATC intercepts only threshold-crossing events ($T_c$), preserving sub-millisecond execution for standard operations.
- **Asynchronous Oversight:** Habeas Log recording and SIS calculations execute in parallel, preventing latency accumulation.
- **Jurisdictional Routing:** Low-impact decisions resolve locally. Only constitutionally significant events are escalated to the CRE Core or Human Bridge.
- **Secure Isolation:** The controller is compatible with Trusted Execution Environments (TEE) and Hardware Security Modules (HSM), ensuring tamper-resistant enforcement of constitutional constraints.
- **Competitive Compatibility:** The architecture does not require slowing model capability development and remains viable in high-speed AI deployment environments.

For a detailed technical breakdown, see the [Full Architecture Documentation](docs/architecture.md).

### **Habeas Log**
A procedural safeguard enabling **jurisdictional review** of automated decisions.  
It functions as a constitutional oversight layer, allowing institutional validation and conflict resolution. It is a proposed as a 4th generation Human Right.

Together, these modules form a **computational analogue of checks and balances**.

### **The Sovereignty Layer (σ)**
Conceptual Foundation

The Human Signature (σ) is not an authentication credential.
It is not an identity token.

It is a sovereignty validator.

Within this architecture, σ represents Residual Human Agency (A) —
the minimal but irreducible jurisdiction that must remain external to the AI system.

σ acts as a reality anchor, preventing the system from collapsing into a closed technocratic loop.

If the system can fully decide without external interruption, sovereignty disappears.

σ ensures that never happens.

### **1. Sigma as a Sovereignty Token (Not Identity)**

The signature does not validate who signs.
It validates that a human authority consciously assumes responsibility at a jurisdictional boundary where AI competence ends.

High-impact decisions (e.g., SIS > 0.7) require σ before execution.

Without σ:

Execution is blocked

The system remains in pending state

This transforms sovereignty from philosophy into execution control.

**2. Sigma as a Paralysis Breaker**

When the CRE Core enters Constitutional Paralysis (logical symmetry between competing principles), algorithmic resolution is forbidden.

Only σ may break the symmetry.

Technically, σ functions as a hardware interrupt:

If system_state == PARALYSIS

Only force_resolution(human_signature, conflict_id) may write to the decision log

This guarantees that deadlocks are resolved politically, not computationally.

**3. Habeas Log – Traceability of Sovereignty**

Every invocation of σ is immutably recorded in the Habeas Log. Each entry binds:

Decision context SIS score - System entropy (S) - Residual agency (A) - Human signature seal

Timestamp

This creates a chain of responsibility that cannot be silently absorbed by the machine.

**4. Anti-Coercion Requirement**

σ must be generated outside the AI’s computational jurisdiction.

The signature must originate from an out-of-band channel: Hardware cryptographic token. Air-gapped signer

External sovereignty device Technical Module

Implementation is provided in:

sovereignty_layer.py 
If the AI can generate σ, sovereignty collapses.

---

## 🎯 Purpose of this Repository

This repository exists to:

- Provide a **reference computational model** of the Hybrid CRE protocol  
- Enable **reproducibility of governance simulations**  
- Serve as a baseline for **institutional AI alignment research**  
- Support development of **constitutional AI architectures**

---

## 📖 Related Publication

The theoretical and philosophical foundations of Hybrid CRE are detailed in:

- **White Paper (Zenodo DOI):** https://doi.org/10.5281/zenodo.18523702  
- **Book:** *Algorithmic Constitutionalism* — Rey, G. (Forthcoming 2026)

This repository contains the **engineering counterpart** of that theoretical framework.

---

## ⚙️ Conceptual Architecture

Hybrid CRE models AI governance as an **institutional process** rather than a control parameter.  
Key principles include:

- Jurisdictional structuring of decision authority  
- Procedural review instead of scalar constraint stacking  
- Institutional traceability  
- Normative conflict resolution through layered oversight  

The system operationalizes a **computational form of constitutional order**.

---

## ⚖️ Intellectual and Research Notice

The Hybrid CRE architecture constitutes an original computational constitutional framework developed by **Gaston Rey**.  
This implementation is released under the conceptual architecture, terminology, and institutional modeling structure form part of an ongoing research program in computational governance and AI constitutionalism.

---

## 📄 License

This reference implementation is distributed under a **dual licensing model**:

- **Academic and Non-Commercial Use**:  
  The code is freely available for research, educational, and non-commercial purposes.  
  Users may copy, modify, and redistribute the work under these conditions, provided proper attribution is given.  

- **Commercial Use**:  
  Any use of this code in commercial products, services, or platforms requires **explicit written authorization from the author**.  
  Interested parties must contact the author to negotiate a separate commercial license.  

This approach ensures open diffusion for academic and research communities, while preserving the author’s rights to negotiate terms for commercial exploitation.

---

## 📬 Contact

For research collaboration or institutional inquiries:

**Gaston Rey**  
gastonrey76@gmail.com

---

## 🏛️ Research Context

Hybrid CRE is part of a broader effort to develop **constitutional architectures for artificial intelligence**, bridging:

- AI alignment  
- Legal theory  
- Institutional design  
- Computational governance  

This work proposes a shift from **optimization-based alignment** to **institutionally structured decision systems**.

---

## Technical Rationale & Performance
* **Language:** Python was selected for this reference implementation due to its status as the *lingua franca* of the AI research community, ensuring maximum readability and auditability.
* **Security:** The protocol uses **Industry-Standard Cryptography** (JWT/JWS). By decoupling jurisdictional validation from the AI’s inference process, we ensure that safety checks do not compromise system performance.
* **Integrity:** This architecture is designed to be deployed within **Trusted Execution Environments (TEE)**, providing a hardware-level guarantee that the "Constitutional Brake" cannot be bypassed.

## Development Roadmap 

### Phase 1: Jurisdictional Foundations (Current 2026)
* [x] Formalize the **Hybrid CRE Protocol** white paper.
* [x] Design the **ATC Token** cryptographic orchestration logic.
* [x] Implement the **Habeas Log** immutable record structure.

### Phase 2: Deliberative Depth (Q2)
* [ ] Development of the **Coherence Matrix** for automated normative conflict detection.
* [ ] Integration of the **SIS (Systemic Impact Score)** with real-world LLM telemetry.
* [ ] Formal verification of the **Constitutional Paralysis** trigger points.

### Phase 3: Scalability & Sovereignty (Q3)
* [ ] Prototype for **Multi-Agent Jurisdictional Conflict Resolution**.
* [ ] Deployment of the **Sovereignty Layer** in a secure hardware enclave (TEE).
* [ ] Implementation of the **Sigma Signature ($\sigma$)** hardware-key bridge.

---
