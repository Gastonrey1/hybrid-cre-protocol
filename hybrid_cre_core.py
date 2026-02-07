import numpy as np
import datetime
import hashlib

class HybridCREProtocol:
    """
    Reference Implementation of the Hybrid Constitutional Reflective Equilibrium Protocol.
    Theory and Architecture by Gaston Rey (2026).
    License: Apache 2.0
    """
    
    def __init__(self, jurisdictional_threshold=0.75):
        self.threshold = jurisdictional_threshold
        self.normative_entropy = 0.0
        self.habeas_log = []
        self.state = "OPERATIONAL_AUTONOMY" # States: OPERATIONAL, RESTRICTIVE, PARALYTIC

    def calculate_sis(self, impact_vectors):
        """
        Systemic Impact Score (SIS)
        Calculates the structural impact based on jurisdictional vectors.
        SIS = ||V|| * (1 + Normative Entropy)
        """
        base_impact = np.linalg.norm(impact_vectors)
        sis_score = base_impact * (1 + self.normative_entropy)
        return round(sis_score, 4)

    def atc_verification(self, decision_data):
        """
        Alignment Traceability Code (ATC)
        Generates a preventive oversight hash for real-time integrity monitoring.
        """
        timestamp = datetime.datetime.utcnow().isoformat()
        raw_atc = f"{timestamp}-{decision_data}-{self.state}"
        atc_hash = hashlib.sha256(raw_atc.encode()).hexdigest()
        return atc_hash[:16] # ATC truncated for traceability logs

    def evaluate_governance_flow(self, impact_vectors, decision_metadata):
        """
        Main Governance Logic: Determines transition from automation to Constitutional Review.
        Implements the 'Hybrid Flow' across jurisdictional boundaries.
        """
        sis = self.calculate_sis(impact_vectors)
        atc = self.atc_verification(decision_metadata)
        
        # Jurisdictional logic: Transition based on threshold escalation
        if sis > self.threshold:
            action = "ESCALATE_TO_CONSTITUTIONAL_REVIEW (CRE_CORE)"
            self.normative_entropy += 0.05 # Accumulate entropy on systemic friction
            self.state = "RESTRICTIVE"
        else:
            action = "EXECUTE_AUTOMATED_DECISION"
            self.normative_entropy *= 0.98 # Homeostatic stabilization
            self.state = "OPERATIONAL_AUTONOMY"
        
        # Check for Paralytic State (Systemic failure or extreme entropy)
        if self.normative_entropy > 1.0:
            self.state = "PARALYTIC_STATE"
            action = "EMERGENCY_HALT: SOVEREIGN_INTERVENTION_REQUIRED"

        # Record in Habeas Log (Implementation of the 4th Gen Human Right)
        log_entry = {
            "atc": atc,
            "sis": sis,
            "action": action,
            "entropy": round(self.normative_entropy, 4),
            "state": self.state,
            "timestamp": datetime.datetime.utcnow().isoformat()
        }
        self.habeas_log.append(log_entry)
        
        return log_entry

# --- Testing the Framework (Validation Scenarios) ---
if __name__ == "__main__":
    # Initialize the protocol with a specific jurisdictional limit
    protocol = HybridCREProtocol(jurisdictional_threshold=0.85)
    
    print("--- Hybrid CRE Protocol Simulation ---")
    
    # Scenario 1: Low Impact (Ordinary Automation)
    print("\n[Scenario 1: Low Impact]")
    res1 = protocol.evaluate_governance_flow([0.2, 0.1, 0.3], "Minor algorithmic adjustment")
    print(f"Action: {res1['action']} | SIS: {res1['sis']} | State: {res1['state']}")

    # Scenario 2: High Impact (Constitutional Escalation)
    print("\n[Scenario 2: High Impact - Structural Risk]")
    res2 = protocol.evaluate_governance_flow([0.8, 0.5, 0.9], "Institutional resource reallocation")
    print(f"Action: {res2['action']} | SIS: {res2['sis']} | State: {res2['state']}")
    
    # Check the Habeas Log
    print(f"\n[Habeas Log Entries]: {len(protocol.habeas_log)} recorded events.")
