"""Tests for pinyinize command."""

import subprocess
import sys


def test_pinyinize_default():
    """Test basic pinyinize (default: PascalCase)."""
    result = subprocess.run(
        [sys.executable, "pinyinize", "你好"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    output = result.stdout.strip()
    # Should produce "NiHao" (PascalCase, default)
    assert output == "NiHao"


def test_pinyinize_underline():
    """Test pinyinize with underline separator."""
    result = subprocess.run(
        [sys.executable, "pinyinize", "-u", "你好"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    output = result.stdout.strip()
    # Should produce "ni_hao" (underscore separator)
    assert output == "ni_hao"


def test_pinyinize_kebab():
    """Test pinyinize with kebab separator."""
    result = subprocess.run(
        [sys.executable, "pinyinize", "-k", "你好"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    output = result.stdout.strip()
    # Should produce "ni-hao" (hyphen separator)
    assert output == "ni-hao"


def test_pinyinize_space():
    """Test pinyinize with space separator."""
    result = subprocess.run(
        [sys.executable, "pinyinize", "-s", "你好"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    output = result.stdout.strip()
    # Should produce "ni hao" (space separator)
    assert output == "ni hao"


def test_pinyinize_uppercase():
    """Test pinyinize with uppercase option."""
    result = subprocess.run(
        [sys.executable, "pinyinize", "-U", "你好"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    output = result.stdout.strip()
    # Should produce "NIHAO" (uppercase, no separator)
    assert output == "NIHAO"


def test_pinyinize_lowercase():
    """Test pinyinize with lowercase option."""
    result = subprocess.run(
        [sys.executable, "pinyinize", "-l", "你好"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    output = result.stdout.strip()
    # Should produce "nihao" (lowercase, no separator)
    assert output == "nihao"


def test_pinyinize_camel_case():
    """Test pinyinize with camelCase option."""
    result = subprocess.run(
        [sys.executable, "pinyinize", "-c", "你好"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    output = result.stdout.strip()
    # Should produce "niHao" (camelCase)
    assert output == "niHao"
    assert " " not in output


def test_pinyinize_uppercase_with_underline():
    """Test pinyinize with uppercase and underline."""
    result = subprocess.run(
        [sys.executable, "pinyinize", "-u", "-U", "你好"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    output = result.stdout.strip()
    # Should produce "NI_HAO" (uppercase with underscore)
    assert output == "NI_HAO"


def test_pinyinize_with_tone():
    """Test pinyinize with tone option."""
    result = subprocess.run(
        [sys.executable, "pinyinize", "-t", "你好"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    output = result.stdout.strip()
    # Should produce pinyin with tone numbers (e.g., "ni3hao3")
    assert len(output) > 0
    # Should contain tone numbers
    assert "ni3" in output or "hao3" in output or "3" in output


def test_pinyinize_multi_word():
    """Test pinyinize with multiple words."""
    result = subprocess.run(
        [sys.executable, "pinyinize", "-c", "你好世界"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    output = result.stdout.strip()
    # Should produce camelCase: "niHaoShiJie"
    assert output == "niHaoShiJie"
    assert " " not in output


def test_pinyinize_kebab_multi_word():
    """Test pinyinize kebab with multiple words."""
    result = subprocess.run(
        [sys.executable, "pinyinize", "-k", "你好世界"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    output = result.stdout.strip()
    # Should produce kebab-case: "ni-hao-shi-jie"
    assert output == "ni-hao-shi-jie"


def test_pinyinize_lowercase_kebab():
    """Test pinyinize with lowercase and kebab separator."""
    result = subprocess.run(
        [sys.executable, "pinyinize", "-l", "-k", "你好"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    output = result.stdout.strip()
    # Should produce "ni-hao" (lowercase with hyphen separator)
    assert output == "ni-hao"


def test_pinyinize_uppercase_space_tone():
    """Test pinyinize with uppercase, space, and tone."""
    result = subprocess.run(
        [sys.executable, "pinyinize", "-U", "-s", "-t", "你好"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    output = result.stdout.strip()
    # Should produce "NI3 HAO3" (uppercase with space and tone numbers)
    assert output == "NI3 HAO3"


def test_pinyinize_help():
    """Test pinyinize help."""
    result = subprocess.run(
        [sys.executable, "pinyinize", "--help"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "pinyinize" in result.stdout
