import subprocess
import sys

def test_valid_input():
    result = subprocess.run(
        [sys.executable, "structured.py", "Ananya", "80", "90", "100"],
        capture_output=True,
        text=True
    )

    output = result.stdout

    assert "Student Name: Ananya" in output
    assert "Marks: 80 90 100" in output
    assert "Total: 270" in output
    assert "Average: 90.0" in output


def test_missing_arguments():
    result = subprocess.run(
        [sys.executable, "structured.py", "Ananya", "80"],
        capture_output=True,
        text=True
    )

    assert "Usage: python structured.py" in result.stdout
    assert result.returncode == 1
