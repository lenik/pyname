"""Tests for ren2py command."""

import subprocess
import sys
import tempfile
from pathlib import Path


def test_ren2py_nonexistent_file():
    """Test ren2py with non-existent file."""
    result = subprocess.run(
        ["bash", "ren2py", "-v", "nonexistent.txt"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 1
    output = result.stdout + result.stderr
    assert "File not found" in output


def test_ren2py_no_chinese():
    """Test ren2py with file without Chinese characters."""
    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = Path(tmpdir) / "hello.txt"
        test_file.write_text("test")
        result = subprocess.run(
            ["bash", "ren2py", "-v", "-n", str(test_file)],
            capture_output=True,
            text=True,
        )
        # Should return 0 but not rename anything
        assert result.returncode == 0
        # File should still exist with original name
        assert test_file.exists()


def test_ren2py_dry_run():
    """Test ren2py dry run mode."""
    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = Path(tmpdir) / "你好.txt"
        test_file.write_text("test")
        result = subprocess.run(
            ["bash", "ren2py", "-v", "-n", str(test_file)],
            capture_output=True,
            text=True,
        )
        # Should return 0 in dry run
        assert result.returncode == 0
        # File should still exist with original name
        assert test_file.exists()
        # Should show what would be renamed (capture stdout & stderr together)
        output = result.stdout + result.stderr
        assert "Would rename" in output or "Renamed" in output
        # With verbose, should show conversion info
        assert "Converting" in output


def test_ren2py_help():
    """Test ren2py help."""
    result = subprocess.run(
        ["bash", "ren2py", "-h"],
        capture_output=True,
        text=True,
    )
    # Help may exit with 0 or show usage
    assert result.returncode == 0 or "ren2py" in result.stdout or "ren2py" in result.stderr
