# main.py

import file_handler as fh

def run_demo():
    filename = "demo.txt"

    print("Creating and writing to file...")
    fh.write_file(filename, "Hello world!\nThis is a demo file.\nPython is fun.\n")

    print("\nAppending text...")
    fh.append_to_file(filename, "Let's learn file handling together. \n")

    print("\nReading file content:")
    content = fh.read_file(filename)
    if content:
        print(content)
    print("Line count:", fh.count_lines(filename))
    print("Word count:", fh.count_words(filename))

    print("Searching for 'Python':")
    matches = fh.search_in_file(filename, "Python")
    print(matches)

    print("\nFile exists?:", fh.file_exists(filename))

    print("\nDeleting file...")
    fh.delete_file(filename)


if __name__ == "__main__":
    run_demo()
