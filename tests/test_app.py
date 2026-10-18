
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from app import make_message, student_info


class TestStudentApplication(unittest.TestCase):
    def test_student_information(self):
        info = student_info()
        self.assertTrue(info["name"])
        self.assertTrue(info["surname"])
        self.assertTrue(info["group"])
        self.assertTrue(info["id"])

    def test_success_message(self):
        self.assertIn(
            "Application is running successfully!",
            make_message()
        )


if __name__ == "__main__":
    unittest.main()
