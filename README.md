# System Uptime Script

## Overview
This project contains a Python script that retrieves and displays the system uptime in a cross-platform compatible way.

## Generated Code

### File: `copilot_test.py`

A Python script that prints system uptime information with support for multiple operating systems.

#### Features:
- **Cross-Platform Support**: Works on Windows, macOS, and Linux
- **Windows**: Uses Windows Management Instrumentation Command-line (wmic) to get boot time and calculates uptime
- **macOS/Linux**: Uses the native `uptime` command
- **Detailed Output**: Displays uptime in days, hours, minutes, and seconds format
- **Error Handling**: Includes exception handling for command failures

#### Key Functions:

```python
def get_system_uptime():
```
- Main function that retrieves and prints system uptime
- Detects the operating system automatically
- Calculates uptime based on system boot time
- Prints formatted uptime information

#### Output Example (Windows):
```
System Uptime: 5 days, 3 hours, 45 minutes, 30 seconds
Last Boot Time: 2026-05-29 14:20:15
```

#### Output Example (macOS/Linux):
```
System Uptime (macOS): 14:35  up 5 days,  3:45, 2 users, load average: 1.23, 1.45, 1.67
```

## Usage

### Prerequisites:
- Python 3.x
- Windows: Administrative privileges may be required for `wmic` command
- macOS/Linux: Standard user permissions

### Running the Script:
```bash
python copilot_test.py
```

### Installation:
No additional dependencies required. The script uses only Python standard library modules:
- `subprocess`: For running system commands
- `platform`: For detecting the operating system
- `datetime`: For parsing and calculating time differences

## Error Handling
If the script encounters an error while retrieving uptime:
- An error message will be displayed
- A note about required permissions will be shown
- The script will terminate gracefully without crashing

## Compatibility
- ✅ Windows (Windows 7 and later)
- ✅ macOS (all versions with uptime command)
- ✅ Linux (all distributions with uptime command)
