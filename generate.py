import os

ext_map = {
    ".java": "Java",
    ".sql": "PostgreSQL",
    ".sh": "Bash",
    ".py": "Python",
    ".js": "JavaScript"
}

def detect_language(file):
    for ext, lang in ext_map.items():
        if file.endswith(ext):
            return lang
    return "Unknown"


def scan_files():
    problems = []

    for root, _, files in os.walk("."):
        for f in files:
            if any(f.endswith(ext) for ext in ext_map):
                # skip system folders
                if ".git" in root:
                    continue

                problem_id = f.split(".")[0]
                lang = detect_language(f)
                path = os.path.join(root, f).replace("./", "")

                problems.append((problem_id, f, lang, path))

    return sorted(problems)


def build_table(problems):
    table = """
## 🧩 LeetCode Solutions Table

| # | Problem | Language | Solution |
|--|--------|----------|----------|
"""

    for pid, file, lang, path in problems:
        table += f"| {pid} | {file} | {lang} | [view]({path}) |\n"

    return table


def update_readme(table):
    with open("README.md", "r", encoding="utf-8") as f:
        data = f.read()

    start = "<!-- STATS_START -->"
    end = "<!-- STATS_END -->"

    if start not in data or end not in data:
        print("Missing README markers")
        return

    new_data = data.split(start)[0] + start + "\n" + table + "\n" + data.split(end)[1]

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(new_data)


if __name__ == "__main__":
    problems = scan_files()
    table = build_table(problems)
    update_readme(table)

    print("Table generated 🚀")