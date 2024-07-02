import sys
import json
import argparse

def py_to_snippet(py_file_path, snippet_file_path):
    with open(py_file_path, 'r') as f:
        code_lines = f.readlines()

    file_name = py_file_path.split("/")[-1]
    prefix = '!' + file_name.split(".")[0]

    snippet = {
        prefix: {
            "scope": "python",
            "prefix": prefix,
            "body": code_lines,
            "description": f"{prefix} snippet"
        }
    }

    with open(snippet_file_path, 'w') as f:
        json.dump(snippet, f, indent=4)

def main():
    parser = argparse.ArgumentParser(description='Convert a Python file to a VS Code snippet.')
    parser.add_argument('command', help='The command to run.')
    parser.add_argument('input_file', help='The input Python file.')
    parser.add_argument('--output', help='The output snippet file. If not provided, defaults to the input file name with a .code-snippets extension.')

    args = parser.parse_args()

    if args.command != 'run':
        print("Unknown command. Use 'tosnippets run <input_file>'")
        sys.exit(1)

    if args.output:
        snippet_file_path = args.output
    else:
        snippet_file_path = args.input_file.replace('.py', '.code-snippets')

    py_to_snippet(args.input_file, snippet_file_path)
    print(f"Snippet has been saved to {snippet_file_path}")

if __name__ == "__main__":
    main()
