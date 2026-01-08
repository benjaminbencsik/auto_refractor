
# Auto-Refactor

A cross-platform CLI tool to scan for 'messy' code and suggest refactors based on a style guide. This tool is designed to help developers maintain a clean and consistent codebase.


## Features

*   **Cross-Platform:** Runs on Windows, macOS, and Linux.
*   **Simple to Use:** Just point it to a directory and it will scan all `.js` files.
*   **Customizable Rules:** The analysis is based on a simple `style-guide.md`, which can be expanded.
*   **Identifies Common Issues:** Currently detects long lines and `console.log` statements.

## Technologies Used

*   **Python:** The core of the application is written in Python.
*   **argparse:** For parsing command-line arguments.

## How to use

1.  Clone this repository:
    ```bash
    git clone https://github.com/benjaminbencsik/auto_refractor.git
    ```
2.  Navigate to the project directory:
    ```bash
    cd auto_refractor
    ```
3.  Run the tool by providing a directory to scan:
    ```bash
    python auto_refactor.py <directory_to_scan>
    ```
    For example, to scan the current directory:
    ```bash
    python auto_refactor.py .
    ```

## How to Contribute

Contributions are welcome! If you have ideas for new features or improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
