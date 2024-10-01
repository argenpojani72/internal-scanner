from sandbox.docker_manager import DockerManager

def main():
    docker_manager = DockerManager()
    sandbox = docker_manager.create_sandbox()

    try:
        docker_manager.setup_python_env_in_sandbox(sandbox)
        docker_manager.execute_command_in_sandbox(sandbox, '/sandbox/venv/bin/python /sandbox/scanner/system_scanner.py')
        docker_manager.execute_command_in_sandbox(sandbox, '/sandbox/venv/bin/python /sandbox/ethical_hacking/ethical_hacking/tools/ethical_hacking.py')
    finally:
        docker_manager.destroy_sandbox(sandbox)

if __name__ == "__main__":
    main()
