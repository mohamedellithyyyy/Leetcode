import os

ext_map = {
    ".java": "Java",
    ".sql": "PostgreSQL",
    ".sh": "Bash",
    ".py": "Python",
    ".js": "JavaScript"
}

def scan_repo():
    lang = {}
    total = 0

    for root, _, files in os.walk("."):
        for f in files:
            for ext, name in ext_map.items():
                if f.endswith(ext):
                    lang[name] = lang.get(name, 0) + 1
                    total += 1

    return total, lang


def build_stats(total, lang):
    text = f"""
- 🧩 Total Problems (Repo): **{total}**

- 💻 Languages:
"""

    for k, v in lang.items():
        text += f"  - {k}: {v}\n"

    return text


def update_readme(content):
    with open("README.md", "r", encoding="utf-8") as f:
        data = f.read()

    start = "<!-- STATS_START -->"
    end = "<!-- STATS_END -->"

    if start not in data or end not in data:
        print("Missing README markers")
        return

    new_data = data.split(start)[0] + start + "\n" + content + data.split(end)[1]

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(new_data)


if __name__ == "__main__":
    total, lang = scan_repo()
    stats = build_stats(total, lang)
    update_readme(stats)

    print("README updated")