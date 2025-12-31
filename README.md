# pyname

Pinyin utilities for filenames with Chinese characters.

## Overview

pyname provides command-line utilities for working with Chinese characters in filenames:
- **test-zh**: Check if filenames contain Chinese characters
- **pinyinize**: Convert Chinese text to pinyin
- **ren2py**: Rename files containing Chinese characters to pinyin
- **mkpylink**: Create symlinks/hardlinks for files with Chinese names using pinyin

## Installation

### From Source

```bash
# Install Python dependencies
pip install -r requirements.txt

# Install the utilities
make install

# Or install symlinks (requires sudo)
make install-symlinks
```

The `install` target respects `DESTDIR` and `PREFIX` environment variables:
```bash
PREFIX=/usr DESTDIR=/tmp/staging make install
```

### Bash Completion

Bash completion is automatically installed to `/etc/bash_completion.d/` or `~/.bash_completion.d/`:

```bash
make install  # Completion files are installed automatically
```

To enable completion, source the file or restart your shell:
```bash
source /etc/bash_completion.d/pyname
```

### Man Pages

Man pages are installed automatically with `make install`:

```bash
man test-zh
man pinyinize
man ren2py
man mkpylink
```

### Symlink Installation

For development, you can create symlinks instead of copying files:

```bash
# Install symlinks for binaries, completion, and man pages
make install-symlinks
```

This creates symlinks in `/usr/bin`, `/etc/bash_completion.d`, and `/usr/share/man/man1` pointing to the project directory.

## Usage

### test-zh

Check if filenames contain Chinese characters.

```bash
# Check if any filename contains Chinese characters (default)
test-zh file1.txt 你好.txt

# Check if all filenames contain only Chinese characters
test-zh -f -a 你好.txt 世界.txt

# Check if any filename contains Chinese characters
test-zh -a file1.txt 你好.txt
```

**Options:**
- `-f, --full`: Check if filename contains only Chinese characters
- `-a, --all`: All files must match (default)
- `-1, --one`: At least one file must match
- `-h, --help`: Show help message
- `--version`: Show version

### pinyinize

Convert Chinese text to pinyin.

```bash
# Basic conversion (PascalCase by default)
echo "你好世界" | pinyinize
# Output: NiHaoShiJie

# With tone numbers
pinyinize -t 你好世界
# Output: Ni3Hao3Shi4Jie4

# Camel case
pinyinize -c 你好世界
# Output: niHaoShiJie

# Kebab case
pinyinize -k 你好世界
# Output: ni-hao-shi-jie

# Snake case (underscore)
pinyinize -u 你好世界
# Output: ni_hao_shi_jie

# Space separated
pinyinize -s 你好世界
# Output: ni hao shi jie

# Uppercase
pinyinize -U 你好世界
# Output: NIHAOSHIJIE

# Lowercase
pinyinize -l 你好世界
# Output: nihaoshijie
```

**Options:**
- `-p, --pascal`: Convert to PascalCase (default)
- `-c, --camel`: Convert to camelCase
- `-u`: Add underscore separator
- `-k, --kebab`: Add hyphen separator
- `-s, --space`: Add space separator
- `-U, --uppercase`: Convert to UPPERCASE
- `-l, --lowercase`: Convert to lowercase
- `-t`: Include tone numbers
- `-h, --help`: Show help message
- `--version`: Show version

### ren2py

Rename files containing Chinese characters to pinyin.

```bash
# Rename files
ren2py 你好.txt 世界.txt

# Dry run (show what would be renamed)
ren2py -n 你好.txt

# With formatting options
ren2py -k -l 你好.txt  # kebab-case, lowercase
ren2py -c 你好.txt     # camelCase
ren2py -u 你好.txt     # snake_case

# Verbose output (shows conversion progress and elapsed time)
ren2py -v 你好.txt

# Quiet mode
ren2py -q 你好.txt
```

**Options:**
- All `pinyinize` options (`-p`, `-c`, `-u`, `-k`, `-s`, `-U`, `-l`, `-t`)
- `-n, --dry-run`: Show what would be renamed without actually renaming
- `-q, --quiet`: Suppress informational messages
- `-v, --verbose`: Show detailed progress (including elapsed time for conversion)
- `-h, --help`: Show help message
- `--version`: Show version

### mkpylink

Create symlinks/hardlinks for files with Chinese characters using pinyin names.

```bash
# Create symlink
mkpylink 你好.txt
# Creates: NiHao.txt -> 你好.txt

# Create hard link
mkpylink --hard 你好.txt

# Dry run
mkpylink -n 你好.txt

# Force overwrite existing links
mkpylink -f 你好.txt

# With formatting options
mkpylink -k -l 你好.txt  # Creates: ni-hao.txt -> 你好.txt

# Verbose output (shows conversion progress and elapsed time)
mkpylink -v 你好.txt

# Quiet mode
mkpylink -q 你好.txt
```

**Options:**
- All `pinyinize` options (`-p`, `-c`, `-u`, `-k`, `-s`, `-U`, `-l`, `-t`)
- `-f, --force`: Overwrite existing links
- `-n, --nop`: Show what would be done without actually creating links
- `--hard`: Create hard links instead of symbolic links
- `-q, --quiet`: Suppress informational messages
- `-v, --verbose`: Show detailed progress (including elapsed time for conversion)
- `-h, --help`: Show help message
- `--version`: Show version

## Performance

The pinyin conversion uses `jieba` for Chinese word segmentation, which may be slow on first use (dictionary loading). Subsequent conversions are faster. Use `-v` (verbose) to see elapsed time for each conversion.

## Requirements

- Python 3.6+
- pypinyin
- jieba

Install with:
```bash
pip install -r requirements.txt
```

## Development

```bash
# Run tests
make test

# Or directly
pytest tests/ -v
```

## License

GPL-3.0+ (see LICENSE file)

## Author

Lenik <pyname@bodz.net>
