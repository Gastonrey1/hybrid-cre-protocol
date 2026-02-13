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

### The ATC, The Alignment Traceability Code: High-Performance Governance Controller

The **ATC (Anti-Gaming & Transition Controller)** is implemented as a lightweight, asynchronous governance controller operating outside the core inference loop.

- **Non-Blocking Architecture:** Model inference remains unaffected. The ATC intercepts only threshold-crossing events ($T_c$), preserving sub-millisecond execution for standard operations.
- **Asynchronous Oversight:** Habeas Log recording and SIS calculations execute in parallel, preventing latency accumulation.
- **Jurisdictional Routing:** Low-impact decisions resolve locally. Only constitutionally significant events are escalated to the CRE Core or Human Bridge.
- **Secure Isolation:** The controller is compatible with Trusted Execution Environments (TEE) and Hardware Security Modules (HSM), ensuring tamper-resistant enforcement of constitutional constraints.
- **Competitive Compatibility:** The architecture does not require slowing model capability development and remains viable in high-speed AI deployment environments.

For a detailed technical breakdown, see the [Full Architecture Documentation](docs/architecture.md).
### 🛡️ Anti-Gaming Mechanism: $S_{norm}$
The protocol utilizes a **Normalized Anti-Gaming Metric ($S_{norm}$)** to detect and neutralize "Reward-Hacking" or "Constitutional Drift."
* **Function:** It measures the divergence between the AI's proposed trajectory and the Constitutional Baseline.
* **Impact:** If $S_{norm}$ exceeds established limits, the **ATC** automatically revokes the execution token and triggers a **Human Bridge** request.


### **Habeas Log**
## 📜 The Habeas Log: Jurisdictional Traceability

The **Habeas Log** is the protocol’s immutable record-keeping layer. It is proposed as a **"4th Generation Human Right"**: the right to a transparent, non-falsifiable record of automated decisions.

Technically, it functions as a **Computational Analogue of Checks and Balances**:

* **Immutable Binding:** Every AI trajectory is cryptographically bound to its **$S_{norm}$** score and the **ATC Token** that authorized it.
* **Jurisdictional Review:** Allows for post-hoc auditing where human institutions can verify if the AI operated within its constitutional boundaries.
* **Integrity Chain:** Uses hash-linking to ensure that once a decision is logged, it cannot be altered or deleted by the AI Core.

### Reference Implementation Structure (`habeas_log.py`)
```python
# Conceptual structure of a Habeas Entry
{
    "jurisdictional_id": "UUID-V4",
    "trajectory_hash": "SHA256",
    "metrics": {
        "sis_impact": 0.45,
        "s_norm_drift": 0.12
    },
    "authorization": "ATC_SIGNED_JWT",
    "human_signature": "SIGMA_V_KEY", # Optional unless SIS > Tc
    "timestamp": "ISO-8601"
}

## ⚖️ The Sovereignty Layer: The Sigma Signature ($\sigma$)

The **Sigma Signature ($\sigma$)** is not an identity token; it is a **Sovereignty Validator**. It represents the irreducible **Residual Human Agency ($A$)** required to break algorithmic deadlocks.

<details>
<summary><b>Click to expand: Core Principles of $\sigma$</b></summary>

* **Sovereignty Anchor:** Prevents the AI from collapsing into a closed technocratic loop. If the AI can decide everything, sovereignty is lost.
* **Paralysis Breaker:** When the CRE Core enters **Constitutional Paralysis** (normative tie), only $\sigma$ can break the symmetry.
* **Anti-Coercion:** $\sigma$ must be generated via out-of-band hardware (air-gapped or physical security keys). If the AI can simulate $\sigma$, the system fails.
</details>

### Technical Implementation
| Feature | Description | Mechanism |
| :--- | :--- | :--- |
| **Trigger** | SIS > Threshold ($T_c$) | Automated Circuit Breaker |
| **Logic** | Hardware Interrupt | `force_resolution(human_sig)` |
| **Traceability** | Habeas Log Binding | Immutable Cryptographic Link |

> **"Sovereignty is not a feeling; it is an execution control."**

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
