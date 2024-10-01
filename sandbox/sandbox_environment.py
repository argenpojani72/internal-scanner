import shutil
import os

class SandboxEnvironment:
    def __init__(self):
        self.sandbox_path = "/tmp/sandbox"  # Temporary directory for the sandbox

    def clone_system(self, system_folder):
        # Clone the system to sandbox
        print("Cloning system into sandbox...")
        shutil.copytree(system_folder, self.sandbox_path)

    def run_sandbox(self):
        # Run the cloned system in sandbox
        print("Running cloned system...")
        os.system(f"python {self.sandbox_path}/scanner/system_scanner.py")

    def dispose_sandbox(self):
        # Safely dispose of the sandbox
        print("Disposing of sandbox...")
        shutil.rmtree(self.sandbox_path)
