# main.py

from ai_model.vulnerability_detector import VulnerabilityDetector
from ai_model.system_fixer import SystemFixerAI
from sandbox.sandbox_environment import SandboxEnvironment
from interface.local_interface import LocalInterface

def main():
    # Initialize components
    system_folder = "/company_systems/example_system"
    sandbox = SandboxEnvironment(system_folder)
    detector = VulnerabilityDetector()
    fixer = SystemFixerAI()
    interface = LocalInterface()

    # Clone system to sandbox
    sandboxed_system = sandbox.clone_system()

    # Simulate system scan (hypothetical system report)
    system_report = "Sample system report with logs..."
    report = detector.generate_report(system_report)

    # Display report to the user
    interface.display_report(report)

    # Ask for user approval to apply fixes
    if interface.approve_fixes():
        fixes = fixer.suggest_fixes(report["vulnerabilities"])
        fixer.apply_fixes(sandboxed_system, fixes)

    # Dispose of sandbox
    sandbox.dispose_sandbox()

if __name__ == "__main__":
    main()
