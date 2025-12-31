# Makefile for pyname
# Copyright (C) 2026 Lenik <pyname@bodz.net>
# License: GPL

PREFIX ?= /usr
DESTDIR ?=
PROJECT_DIR := $(shell pwd)
BIN_DIR := $(DESTDIR)$(PREFIX)/bin
MAN_DIR := $(DESTDIR)$(PREFIX)/share/man/man1
COMPLETION_DIR := $(DESTDIR)/etc/bash_completion.d
USER_COMPLETION_DIR := $(HOME)/.bash_completion.d

.PHONY: all install install-symlinks install-completion install-man clean test

all:
	@echo "pyname - Pinyin utilities for filenames with Chinese characters"
	@echo "Run 'make install' to install or 'make install-symlinks' for symlinks"

install: install-completion install-man
	install -d $(BIN_DIR)
	install -m 755 test-zh $(BIN_DIR)/test-zh
	install -m 755 pinyinize $(BIN_DIR)/pinyinize
	install -m 755 ren2py $(BIN_DIR)/ren2py
	install -m 755 mkpylink $(BIN_DIR)/mkpylink

install-symlinks: install-completion-symlinks install-man-symlinks
	@echo "Installing symlinks to /usr/bin (requires sudo)"
	sudo install -d /usr/bin
	sudo ln -sf $(PROJECT_DIR)/test-zh /usr/bin/test-zh
	sudo ln -sf $(PROJECT_DIR)/pinyinize /usr/bin/pinyinize
	sudo ln -sf $(PROJECT_DIR)/ren2py /usr/bin/ren2py
	sudo ln -sf $(PROJECT_DIR)/mkpylink /usr/bin/mkpylink

install-completion-symlinks:
	@echo "Installing symlinks for bash completion to /etc/bash_completion.d (requires sudo)"
	sudo install -d /etc/bash_completion.d
	sudo ln -sf $(PROJECT_DIR)/bash-completion/pyname /etc/bash_completion.d/pyname

install-man-symlinks:
	@echo "Installing symlinks for man pages to /usr/share/man/man1 (requires sudo)"
	sudo install -d /usr/share/man/man1
	sudo ln -sf $(PROJECT_DIR)/man/test-zh.1 /usr/share/man/man1/test-zh.1
	sudo ln -sf $(PROJECT_DIR)/man/pinyinize.1 /usr/share/man/man1/pinyinize.1
	sudo ln -sf $(PROJECT_DIR)/man/ren2py.1 /usr/share/man/man1/ren2py.1
	sudo ln -sf $(PROJECT_DIR)/man/mkpylink.1 /usr/share/man/man1/mkpylink.1

install-completion:
	@if [ -w /etc/bash_completion.d ] 2>/dev/null; then \
		install -d $(COMPLETION_DIR); \
		install -m 644 bash-completion/pyname $(COMPLETION_DIR)/pyname; \
		echo "Bash completion installed to $(COMPLETION_DIR)"; \
	elif [ -d $(HOME)/.bash_completion.d ] 2>/dev/null || mkdir -p $(USER_COMPLETION_DIR) 2>/dev/null; then \
		install -d $(USER_COMPLETION_DIR); \
		install -m 644 bash-completion/pyname $(USER_COMPLETION_DIR)/pyname; \
		echo "Bash completion installed to $(USER_COMPLETION_DIR)"; \
		echo "Add 'source ~/.bash_completion.d/pyname' to your ~/.bashrc"; \
	else \
		echo "Warning: Could not install bash completion. Install manually:"; \
		echo "  install -m 644 bash-completion/pyname /etc/bash_completion.d/pyname"; \
	fi

install-man:
	install -d $(MAN_DIR)
	install -m 644 man/test-zh.1 $(MAN_DIR)/test-zh.1
	install -m 644 man/pinyinize.1 $(MAN_DIR)/pinyinize.1
	install -m 644 man/ren2py.1 $(MAN_DIR)/ren2py.1
	install -m 644 man/mkpylink.1 $(MAN_DIR)/mkpylink.1
	@echo "Man pages installed to $(MAN_DIR)"

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true

test:
	python3 -m pytest tests/ -v

