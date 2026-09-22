import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = REPO_ROOT / "src"


def run_app(inputs: str) -> str:
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_src = Path(temp_dir) / "src"
        shutil.copytree(SRC_DIR, temp_src)

        result = subprocess.run(
            [sys.executable, str(temp_src / "main.py")],
            input=inputs,
            text=True,
            capture_output=True,
            check=False,
            cwd=temp_src,
        )
        return result.stdout


class BackNavigationTests(unittest.TestCase):
    def test_list_menu_back_returns_to_main_menu(self):
        output = run_app("1\n4\n3\n")

        self.assertIn("==== List Actions ====", output)
        self.assertGreaterEqual(output.count("============ Menu ============"), 2)

    def test_task_menu_back_returns_to_list_menu_and_allows_multiple_actions(self):
        output = run_app(
            "1\n"  # Show lists
            "2\n"  # Open list
            "1\n"  # Open list ID 1
            "1\n"  # Create task
            "Task A\n"
            "Description\n"
            "1\n"  # Low priority
            "4\n"  # Mark task in same opened list
            "1\n"  # Task ID
            "2\n"  # Mark as done
            "5\n"  # Back to list menu
            "4\n"  # Back to main menu
            "3\n"  # Exit
        )

        self.assertIn("Task created successfully.", output)
        self.assertIn("\nSuccess\n\n", output)
        self.assertEqual(output.count("Enter list ID to open:"), 1)
        self.assertGreaterEqual(output.count("==== List Actions ===="), 2)


if __name__ == "__main__":
    unittest.main()
