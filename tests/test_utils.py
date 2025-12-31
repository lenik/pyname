"""Tests for utility functions embedded in scripts."""

import subprocess
import sys


def test_contains_chinese():
    """Test contains_chinese function via test-zh."""
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


def test_pinyin_conversion():
    """Test pinyin conversion via pinyinize."""
    result = subprocess.run(
        [sys.executable, "pinyinize", "你好"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    output = result.stdout.strip()
    assert len(output) > 0
    # Should contain some pinyin output
    assert any(c.isalpha() for c in output)
