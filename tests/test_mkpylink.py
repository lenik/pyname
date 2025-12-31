"""Tests for mkpylink command."""

import os
import subprocess
import sys
import tempfile
from pathlib import Path


def test_mkpylink_nonexistent_file():
    """Test mkpylink with non-existent file."""
    result = subprocess.run(
        ["bash", "mkpylink", "-v", "nonexistent.txt"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 1
    output = result.stdout + result.stderr
    assert "File not found" in output


def test_mkpylink_no_chinese():
    """Test mkpylink with file without Chinese characters."""
    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = Path(tmpdir) / "hello.txt"
        test_file.write_text("test")
        result = subprocess.run(
            ["bash", "mkpylink", "-v", "-n", str(test_file)],
            capture_output=True,
            text=True,
        )
        # Should return 0 but not create any links
        assert result.returncode == 0
        output = result.stdout + result.stderr
        # With verbose, might show processing info


def test_mkpylink_dry_run():
    """Test mkpylink dry run mode."""
    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = Path(tmpdir) / "你好.txt"
        test_file.write_text("test")
        result = subprocess.run(
            ["bash", "mkpylink", "-v", "-n", str(test_file)],
            capture_output=True,
            text=True,
        )
        # Should return 0 in dry run
        assert result.returncode == 0
        # Should show what would be done (capture stdout & stderr together)
        output = result.stdout + result.stderr
        assert "Would create" in output or "symlink" in output.lower()
        # With verbose, should show conversion info
        assert "Converting" in output


def test_mkpylink_create_symlink():
    """Test mkpylink creates symlink."""
    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = Path(tmpdir) / "你好.txt"
        test_file.write_text("test")
        result = subprocess.run(
            ["bash", "mkpylink", "-v", str(test_file)],
            capture_output=True,
            text=True,
        )
        # Should return 0
        assert result.returncode == 0
        # Should create symlink with PascalCase name
        link_path = Path(tmpdir) / "NiHao.txt"
        assert link_path.is_symlink() or link_path.exists()
        # Original file should still exist
        assert test_file.exists()
        # Should show creation message (capture stdout & stderr together)
        output = result.stdout + result.stderr
        assert "Created" in output or "symlink" in output.lower()
        # With verbose, should show conversion info
        assert "Converting" in output


def test_mkpylink_force_overwrite():
    """Test mkpylink with force option."""
    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = Path(tmpdir) / "你好.txt"
        test_file.write_text("test")
        # Create first link
        result1 = subprocess.run(
            ["bash", "mkpylink", "-v", str(test_file)],
            capture_output=True,
            text=True,
        )
        assert result1.returncode == 0
        # Try to create again with force
        result2 = subprocess.run(
            ["bash", "mkpylink", "-v", "-f", str(test_file)],
            capture_output=True,
            text=True,
        )
        # Should succeed with force
        assert result2.returncode == 0
        # Should show creation message (capture stdout & stderr together)
        output2 = result2.stdout + result2.stderr
        assert "Created" in output2 or "symlink" in output2.lower()


def test_mkpylink_camel_case():
    """Test mkpylink with camelCase option."""
    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = Path(tmpdir) / "你好.txt"
        test_file.write_text("test")
        result = subprocess.run(
            ["bash", "mkpylink", "-v", "-c", str(test_file)],
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        # Should create symlink with camelCase name
        link_path = Path(tmpdir) / "niHao.txt"
        assert link_path.is_symlink() or link_path.exists()
        # Should show creation message (capture stdout & stderr together)
        output = result.stdout + result.stderr
        assert "Created" in output or "symlink" in output.lower()


def test_mkpylink_kebab_separator():
    """Test mkpylink with kebab separator."""
    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = Path(tmpdir) / "你好.txt"
        test_file.write_text("test")
        result = subprocess.run(
            ["bash", "mkpylink", "-v", "-k", str(test_file)],
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        # Should create symlink with kebab-case name
        link_path = Path(tmpdir) / "ni-hao.txt"
        assert link_path.is_symlink() or link_path.exists()
        # Should show creation message (capture stdout & stderr together)
        output = result.stdout + result.stderr
        assert "Created" in output or "symlink" in output.lower()


def test_mkpylink_hard_link():
    """Test mkpylink with hard link option."""
    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = Path(tmpdir) / "你好.txt"
        test_file.write_text("test")
        result = subprocess.run(
            ["bash", "mkpylink", "-v", "--hard", str(test_file)],
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        # Should create hard link
        link_path = Path(tmpdir) / "NiHao.txt"
        assert link_path.exists()
        # Should be a hard link (same inode)
        if os.name != 'nt':  # Skip on Windows
            assert link_path.stat().st_ino == test_file.stat().st_ino
        # Should show creation message (capture stdout & stderr together)
        output = result.stdout + result.stderr
        assert "Created" in output or "hard link" in output.lower()


def test_mkpylink_help():
    """Test mkpylink help."""
    result = subprocess.run(
        ["bash", "mkpylink", "-h"],
        capture_output=True,
        text=True,
    )
    # Help may exit with 0 or show usage
    assert result.returncode == 0 or "mkpylink" in result.stdout or "mkpylink" in result.stderr

