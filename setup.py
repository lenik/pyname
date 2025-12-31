"""Setup configuration for pyname.

Copyright (C) 2026 Lenik <pyname@bodz.net>
License: GPL
"""

from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read() if fh.read() else ""

setup(
    name="pyname",
    version="0.1.0",
    author="Lenik",
    author_email="pyname@bodz.net",
    description="Pinyin utilities for filenames with Chinese characters",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lenik/pyname",
    py_modules=[],
    scripts=["test-zh", "pinyinize", "ren2py", "mkpylink"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.7",
    install_requires=[
        "pypinyin>=0.49.0",
        "jieba>=0.42.1",
    ],
    license="GPL-3.0+",
)

