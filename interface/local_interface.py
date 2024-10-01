# interface/local_interface.py

class LocalInterface:
    def display_report(self, report):
        # Display report to the user
        print("Vulnerability Report:")
        for vulnerability in report['vulnerabilities']:
            print(f"- {vulnerability}")
        print("Recommendations:")
        for recommendation in report['recommendations']:
            print(f"- {recommendation}")

    def approve_fixes(self):
        # Simulate user approval of fixes
        user_input = input("Approve suggested fixes? (yes/no): ")
        return user_input.lower() == "yes"
