from atc_security import ATCOrchestrator, ai_motor_output

# Initialize the ATC with a Constitutional Threshold of 0.7
atc = ATCOrchestrator(constitutional_threshold=0.7)

# CASE A: Safe Trajectory (Low SIS)
print("--- Scenario A: Routine Update ---")
result_a = atc.evaluate_trajectory({"task": "Optimize database"}, sis_score=0.2)
if result_a["action"] == "AUTHORIZE_EXECUTION":
    print(ai_motor_output("Optimize database", result_a["token"]))

# CASE B: High-Impact Trajectory (Critical SIS - Potential Paralysis)
print("\n--- Scenario B: Critical Infrastructure Change ---")
result_b = atc.evaluate_trajectory({"task": "Modify Core Protocol"}, sis_score=0.85)

if result_b["action"] == "HALT_FOR_REVIEW":
    print(f"ALERTA: {result_b['reason']}. Action blocked by ATC.")
    print("System state: Awaiting CRE Core Deliberation or Human Sigma Signature.")
