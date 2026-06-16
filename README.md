# Python Project Template 🐍

<div align="center">

**A Modern Python Project Scaffold**

_... with batteries included_ 🔋

</div>

<!-- BEGIN_AUTO_BADGES -->

[![Tests](https://github.com/GangGreenTemperTatum/python-template/actions/workflows/tests.yaml/badge.svg)](https://github.com/GangGreenTemperTatum/python-template/actions/workflows/tests.yaml)
[![Pre-Commit](https://github.com/GangGreenTemperTatum/python-template/actions/workflows/pre-commit.yaml/badge.svg)](https://github.com/GangGreenTemperTatum/python-template/actions/workflows/pre-commit.yaml)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)

<!-- END_AUTO_BADGES -->

- [Python Project Template 🐍](#python-project-template-)
  - [🚀 Quick Start](#-quick-start)
  - [📦 What's Included](#-whats-included)
  - [📁 Project Structure](#-project-structure)
  - [🛠️ Development](#️-development)
    - [Prerequisites](#prerequisites)
    - [Common Commands](#common-commands)
    - [VSCode Integration](#vscode-integration)
  - [📚 Documentation](#-documentation)
    - [Using This Template](#using-this-template)
    - [Template Development](#template-development)
  - [🤝 Contributing](#-contributing)
  - [📄 License](#-license)
  - [🔐 Security](#-security)

## 🚀 Quick Start

1. Click the green `Use this template` button at the top of this page
1. Name your repository and select options
1. Clone your new repository:

   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

1. Initialize with your preferred package manager:

   ```bash
   # Using pip
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install -e ".[dev]"

   # Using uv
   uv venv --python 3.11 # Optional: specify Python version
   source .venv/bin/activate
   uv pip install -e ".[dev]"

   # Using poetry
   poetry install
   ```

1. Set up pre-commit hooks:

   ```bash
   pre-commit install
   ```

## 📦 What's Included

- 📝 Modern `pyproject.toml` configuration
- 🧪 Testing setup with pytest
- 🔍 Code quality tools:
  - Black (code formatting)
  - Ruff (fast linting)
  - mypy (type checking)
  - pre-commit hooks
- 📚 Documentation template
- 🔄 GitHub Actions workflows
- 🔒 Security policy template
- 👥 CODEOWNERS template

## 📁 Project Structure

```bash
.
├── CODEOWNERS          # Repository access control
├── LICENSE            # Apache License 2.0
├── README.md          # This file
├── SECURITY.md        # Security policy
├── Taskfile.yaml      # Task automation
├── docs/              # Documentation
├── examples/          # Usage examples
├── pyproject.toml     # Python project config
└── tests/             # Test suite
```

## 🛠️ Development

### Prerequisites

- Python 3.11+
- One of: pip, uv, or poetry
- [pre-commit](https://pre-commit.com/)
- [Task](https://taskfile.dev/installation/) (optional, but recommended)

### Common Commands

```bash
# Run tests
task test  # or: pytest

# Format code
task format  # or: black .

# Run linting
task lint  # or: ruff check .

# Type checking
task types  # or: mypy .

# Run all checks
task check
```

### VSCode Integration

1. Open `python.code-workspace` in VSCode
1. Install recommended extensions when prompted
1. Enjoy automated formatting and linting!

## 📚 Documentation

The project uses MkDocs for documentation with automated builds via pre-commit
hooks.

### Using This Template

For step-by-step instructions on creating a new project using this template, see
our [Project Setup Guide](docs/topics/project-from-template.md).

### Template Development

If you're contributing to the template itself:

1. Set up documentation tools:

   ```bash
   pip install -e ".[dev]"
   pre-commit install
   ```

1. (Optional) Install social card dependencies:

   ```bash
   # macOS
   brew install cairo freetype2 libffi

   # Ubuntu/Debian
   apt-get install libcairo2-dev libfreetype6-dev libffi-dev

   # Then uncomment social-cards plugin in mkdocs.yaml
   ```

1. Preview documentation locally:

   ```bash
   mkdocs serve
   ```

Documentation is automatically built before each commit via pre-commit
hooks.

## 🤝 Contributing

Contributions are welcome!
Please see our [Contributing Guide](docs/contributing.md).

## 📄 License

This project is licensed under the Apache License 2.0 - see the
[LICENSE](LICENSE) file for details.

## 🔐 Security

See our [Security Policy](SECURITY.md) for reporting vulnerabilities.
