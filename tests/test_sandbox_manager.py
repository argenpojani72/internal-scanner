import unittest
from sandbox.docker_manager import SandboxManager

class TestSandboxManager(unittest.TestCase):
    def setUp(self):
        self.manager = SandboxManager()

    def test_sandbox_creation(self):
        sandbox = self.manager.create_sandbox()
        self.assertIsNotNone(sandbox, "Sandbox should be created.")
        self.manager.destroy_sandbox(sandbox)

if __name__ == "__main__":
    unittest.main()
