import os
import argparse
import sys

def analyze_file(file_path):
    """
    Analyzes a single file for potential style issues.

    Args:
        file_path (str): The path to the file to analyze.

    Returns:
        list: A list of suggestion strings.
    """
    suggestions = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for i, line in enumerate(f, 1):
                # Rule 1: Line length
                if len(line) > 120:
                    suggestions.append(f"Line {i}: Line is longer than 120 characters.")
                
                # Rule 2: No console.log
                if 'console.log' in line:
                    suggestions.append(f"Line {i}: Contains a 'console.log' statement.")
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}", file=sys.stderr)
        return []
    except Exception as e:
        print(f"Error analyzing file {file_path}: {e}", file=sys.stderr)
        return []
        
    return suggestions

def main():
    """
    Main function to parse command-line arguments and scan a directory for .js files.
    """
    parser = argparse.ArgumentParser(description='Auto-Refactor: A tool to find "messy" code.')
    parser.add_argument('directory', type=str, help='The directory to scan for .js files.')
    args = parser.parse_args()

    target_dir = args.directory
    if not os.path.isdir(target_dir):
        print(f"Error: Directory not found at '{target_dir}'", file=sys.stderr)
        sys.exit(1)

    print(f"Scanning for .js files in '{target_dir}'...")
    js_files_found = False
    for root, _, files in os.walk(target_dir):
        for file in files:
            if file.endswith('.js'):
                js_files_found = True
                file_path = os.path.join(root, file)
                print(f"\nAnalyzing {file_path}...")
                suggestions = analyze_file(file_path)
                
                if suggestions:
                    print("Suggestions found:")
                    for suggestion in suggestions:
                        print(f"- {suggestion}")
                else:
                    print("No issues found.")
    
    if not js_files_found:
        print("No JavaScript files found in the specified directory.")

if __name__ == '__main__':
    main()