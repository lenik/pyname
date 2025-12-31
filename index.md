# pyname - Pinyin Utilities for Chinese Filenames

## Project Overview

pyname is a collection of command-line utilities for working with Chinese characters in filenames. It provides tools to check for Chinese characters, convert them to pinyin, rename files, and create symlinks with pinyin names.

## Architecture

The project consists of four standalone command-line utilities:

1. **test-zh** (Python script): Checks if filenames contain Chinese characters
2. **pinyinize** (Python script): Converts Chinese text to pinyin with various formatting options
3. **ren2py** (Bash script): Renames files containing Chinese characters to pinyin
4. **mkpylink** (Bash script): Creates symlinks/hardlinks for files with Chinese names using pinyin

## Key Components

### Python Scripts

- **test-zh**: Uses regex to detect Chinese characters (Unicode range \u4e00-\u9fff)
- **pinyinize**: Uses `jieba` for word segmentation and `pypinyin` for pinyin conversion

### Bash Scripts

- **ren2py** and **mkpylink**: Use shlib framework for option parsing and logging
- Both call `pinyinize` and `test-zh` as external commands
- Support `-q/--quiet` and `-v/--verbose` options with `_log*` functions
- Show elapsed time for slow pinyin conversion operations

## Dependencies

- Python 3.6+
- pypinyin (for pinyin conversion)
- jieba (for Chinese word segmentation)
- shlib (for bash scripts, typically in /usr/lib/shlib)

## Build System

- **Makefile**: Handles installation, bash completion, and testing
- **setup.py**: Python package metadata (legacy, scripts are now standalone)
- **debian/**: Debian packaging files

## Testing

All utilities have comprehensive test suites in `tests/`:
- `test_test_zh.py`: Tests for test-zh
- `test_pinyinize.py`: Tests for pinyinize
- `test_ren2py.py`: Tests for ren2py
- `test_mkpylink.py`: Tests for mkpylink

Run tests with: `make test` or `pytest tests/ -v`

## Installation

```bash
make install  # Installs to PREFIX/bin (default: /usr/local/bin)
make install-symlinks  # Creates symlinks in /usr/bin
```

Bash completion is automatically installed to `/etc/bash_completion.d/` or `~/.bash_completion.d/`.

## Usage Patterns

### Basic Workflow

1. Check for Chinese characters: `test-zh file.txt`
2. Convert to pinyin: `pinyinize "你好"`
3. Rename files: `ren2py 你好.txt`
4. Create symlinks: `mkpylink 你好.txt`

### Formatting Options

All pinyin conversion tools support:
- PascalCase (default): `NiHao`
- camelCase: `niHao`
- kebab-case: `ni-hao`
- snake_case: `ni_hao`
- UPPERCASE: `NIHAO`
- lowercase: `nihao`

### Performance Considerations

- First pinyin conversion is slow (jieba dictionary loading)
- Subsequent conversions are faster
- Use `-v` to see elapsed time: `Result: 你好 -> NiHao (0s 783.820ms)`

## File Structure

```
pyname/
├── test-zh          # Python script
├── pinyinize        # Python script
├── ren2py           # Bash script
├── mkpylink         # Bash script
├── Makefile         # Build system
├── setup.py         # Python package metadata
├── requirements.txt # Python dependencies
├── bash-completion/ # Bash completion files
├── debian/          # Debian packaging
├── tests/           # Test suite
└── README.md        # User documentation
```

## Development Notes

- All scripts are standalone (no package imports)
- Bash scripts use shlib for consistent option parsing
- Logging uses `_log*` functions for `-q/-v` support
- Symlinks use relative paths when in same directory
- Error handling uses `_error` function (always shown)

## License

GPL-3.0+

## Author

Lenik <pyname@bodz.net>

