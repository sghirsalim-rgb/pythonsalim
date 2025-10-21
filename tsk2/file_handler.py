# file_handler.py
"""
File handling utilities:
- read_file(filename)
- write_file(filename, content)
- append_to_file(filename, content)
- count_lines(filename)
- count_words(filename)
- search_in_file(filename, keyword)
- file_exists(filename)
- delete_file(filename)
"""

import os

def read_file(filename: str) -> str | None:
    """Reads the full content of a file and returns it as a string."""
    if not os.path.exists(filename):
        print(f"File '{filename}' does not exist.")
        return None
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()

def write_file(filename: str, content: str) -> None:
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
        print(f"Content written to '{filename}' successfully.")

def append_to_file(filename: str, content: str) -> None:
    with open(filename, "a", encoding="utf-8") as f:
        f.write(content)
        print(f"Content appended to '{filename}' successfully.")

def count_lines(filename: str) -> int:
    if not os.path.exists(filename):
        print(f"File '{filename}' does not exist.")
        return 0
    with open(filename, "r", encoding="utf-8") as f:
        return len(f.readlines())

def count_words(filename: str) -> int:
    if not os.path.exists(filename):
        print(f"File '{filename}' does not exist.")
        return 0
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read()
        words = text.split()
        return len(words)

def search_in_file(filename: str, keyword: str) -> list[str]:
    results = []
    if not os.path.exists(filename):
        print(f"File '{filename}' does not exist.")
        return results
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            if keyword.lower() in line.lower():
                results.append(line.strip())
    return results

def file_exists(filename: str) -> bool:
    return os.path.exists(filename)

def delete_file(filename: str) -> None:
    if os.path.exists(filename):
        os.remove(filename)
        print(f"File '{filename}' successfully deleted.")
    else:
        print(f"File '{filename}' does not exist.")
