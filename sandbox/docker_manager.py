import docker
import os

class DockerManager:
    def __init__(self):
        self.client = docker.from_env()

    def create_sandbox(self):
        print("Creating sandbox...")
        sandbox = self.client.containers.run(
            "kalilinux/kali-rolling",
            command="bash",
            detach=True,
            tty=True,
            volumes={
                os.path.abspath("."): {'bind': '/sandbox', 'mode': 'rw'}
            }
        )
        print("Sandbox created.")
        return sandbox

    def execute_command_in_sandbox(self, sandbox, command):
        print(f"Running command '{command}' inside the sandbox...")
        exec_log = sandbox.exec_run(command)
        print(exec_log.output.decode())
        if exec_log.exit_code != 0:
            print(f"Command failed with exit code {exec_log.exit_code}")
            return False
        return True

    def setup_python_env_in_sandbox(self, sandbox):
        print("Setting up Python virtual environment in sandbox...")

        self.execute_command_in_sandbox(sandbox, 'apt-get update')
        self.execute_command_in_sandbox(sandbox, 'apt-get install -y python3 python3-pip python3-venv')
        self.execute_command_in_sandbox(sandbox, 'python3 -m venv /sandbox/venv')
        self.execute_command_in_sandbox(sandbox, '/sandbox/venv/bin/python -m pip install --upgrade pip')
        self.execute_command_in_sandbox(sandbox, '/sandbox/venv/bin/pip install psutil')

        print("Python environment set up complete.")

    def destroy_sandbox(self, sandbox):
        print("Destroying sandbox...")
        sandbox.stop()
        sandbox.remove()
        print("Sandbox destroyed.")
