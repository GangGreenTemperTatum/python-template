#!/usr/bin/python3
import argparse
import sys
import tomllib

from jinja2 import Environment, FileSystemLoader


def load_project_settings():
    with open("pyproject.toml", "rb") as f:
        pyproject = tomllib.load(f)
    return {
        **pyproject["project"],
        **pyproject.get("tool", {}).get("readme", {}),
    }


def read_file(path: str) -> str:
    with open(path, "r") as f:
        return f.read()


def write_file(path: str, content: str) -> None:
    with open(path, "w") as f:
        f.write(content)


def get_section_content(content: str, start_marker: str, end_marker: str) -> tuple[str, int, int]:
    start_idx = content.find(start_marker)
    if start_idx == -1:
        return "", -1, -1
    end_idx = content.find(end_marker, start_idx)
    if end_idx == -1:
        return "", -1, -1
    return (content[start_idx : end_idx + len(end_marker)], start_idx, end_idx + len(end_marker))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--dry-run", action="store_true", help="Print to stdout instead of writing file"
    )
    # Ignore unknown arguments (like filenames passed by pre-commit)
    args, _ = parser.parse_known_args()

    # Setup Jinja environment
    env = Environment(
        loader=FileSystemLoader("templates"), trim_blocks=True, lstrip_blocks=True, autoescape=True
    )
    template = env.get_template("README.md.j2")

    # Load project settings
    settings = load_project_settings()

    # Default values
    context = {
        "project_name": settings.get("name", "Project Name"),
        "description": settings.get("description", "A Python Project"),
        "github_org": settings.get("github_org", "organization"),
        "repo_name": settings.get("name", "repository"),
        "emoji": settings.get("emoji", "🐍"),
        "logo_url": settings.get("logo_url") or None,
        "tagline": settings.get("tagline", "with batteries included 🔋"),
    }

    # Render template
    new_content = template.render(**context)

    # Read existing README
    try:
        existing_content = read_file("README.md")
    except FileNotFoundError:
        existing_content = ""

    # Find auto-generated sections and replace
    for marker_pair in [
        ("<!-- BEGIN_AUTO_BADGES -->", "<!-- END_AUTO_BADGES -->"),
        # Add other marker pairs here as needed
    ]:
        start_marker, end_marker = marker_pair
        new_section, start_idx, end_idx = get_section_content(new_content, start_marker, end_marker)
        if not new_section:
            continue

        existing_section, existing_start, existing_end = get_section_content(
            existing_content, start_marker, end_marker
        )
        if existing_start >= 0:
            # Replace existing section
            existing_content = (
                existing_content[:existing_start] + new_section + existing_content[existing_end:]
            )
        else:
            # Add new section at the top after the first heading
            first_heading_end = existing_content.find("\n", existing_content.find("#"))
            if first_heading_end >= 0:
                existing_content = (
                    existing_content[: first_heading_end + 1]
                    + "\n"
                    + new_section
                    + "\n"
                    + existing_content[first_heading_end + 1 :]
                )

    if args.dry_run:
        print(existing_content)
    else:
        write_file("README.md", existing_content)


if __name__ == "__main__":
    sys.exit(main())
