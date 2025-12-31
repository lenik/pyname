"""Tests for test-zh command."""

import subprocess
import sys


def test_test_zh_contains_mode():
    """Test test-zh with contains mode."""
    # Should pass: contains Chinese
    result = subprocess.run(
        [sys.executable, "test-zh", "你好.txt"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    
    # Should fail: no Chinese
    result = subprocess.run(
        [sys.executable, "test-zh", "hello.txt"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 1
    
    # Should pass: any has Chinese
    result = subprocess.run(
        [sys.executable, "test-zh", "-1", "hello.txt", "你好.txt"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0


def test_test_zh_full_mode():
    """Test test-zh with full mode."""
    # Should pass: only Chinese (no extension)
    result = subprocess.run(
        [sys.executable, "test-zh", "-f", "你好"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0


def test_test_zh_help():
    """Test test-zh help."""
    result = subprocess.run(
        [sys.executable, "test-zh", "--help"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "test-zh" in result.stdout
