import os
import sys
from datetime import datetime

def display_help():
    """Displays usage instructions."""
    print("=== File Management & Directory Utility ===")
    print("Usage: python file_utility.py <command> [arguments]")
    print("\nCommands:")
    print("  setup <workspace_name>    : Create and navigate to a new workspace directory.")
    print("  scan <.extension>         : List all files with the targeted extension in the current tree.")
    print("  log <message>             : Append a message to 'system_log.txt' using context managers.")
    print("  readlog                   : Safe-read the contents of 'system_log.txt'.")
    print("  info                      : Display current directory structure information.")

def create_workspace(workspace_name):
    """Creates a dynamic workspace folder and navigates into it."""
    try:
        # Create directory (avoids error if it already exists)
        os.makedirs(workspace_name, exist_ok=True)
        print(f"[+] Workspace '{workspace_name}' is ready.")
        
        # Navigate into the new subdirectory
        os.chdir(workspace_name)
        print(f"[+] Navigated into: {os.getcwd()}")
    except OSError as e:
        print(f"[-] Error creating workspace: {e}", file=sys.stderr)

def scan_extensions(target_ext):
    """Inspects directory structure and lists files matching a specific extension."""
    if not target_ext.startswith('.'):
        target_ext = '.' + target_ext
        
    current_dir = os.getcwd()
    print(f"[*] Scanning for '{target_ext}' files starting from: {current_dir}")
    
    match_count = 0
    # os.walk navigates the current directory and all subdirectories
    for root, dirs, files in os.walk(current_dir):
        for file in files:
            if file.endswith(target_ext):
                print(f"    -> {os.path.join(root, file)}")
                match_count += 1
                
    print(f"[*] Total '{target_ext}' files found: {match_count}")

def write_log(message):
    """Creates or appends to a log file using a context manager."""
    log_filename = "system_log.txt"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # The 'with' statement ensures the file is safely closed after writing
    with open(log_filename, 'a', encoding='utf-8') as log_file:
        log_file.write(f"[{timestamp}] {message}\n")
    print(f"[+] Successfully logged message to '{log_filename}'.")

def read_log():
    """Safe-reads the log file using a context manager."""
    log_filename = "system_log.txt"
    
    if not os.path.exists(log_filename):
        print(f"[-] Log file '{log_filename}' does not exist yet.")
        return
        
    print(f"\n--- Contents of {log_filename} ---")
    # The 'with' statement ensures the file is safely closed after reading
    with open(log_filename, 'r', encoding='utf-8') as log_file:
        for line_number, line in enumerate(log_file, start=1):
            # sys.stdout.write is used here to avoid double newlines from print()
            sys.stdout.write(f"{line_number:02d} | {line}")
    print("----------------------------------\n")

def display_info():
    """Inspects and displays the current directory structure."""
    current_dir = os.getcwd()
    print(f"[*] Current Directory: {current_dir}")
    
    items = os.listdir(current_dir)
    folders = [item for item in items if os.path.isdir(os.path.join(current_dir, item))]
    files = [item for item in items if os.path.isfile(os.path.join(current_dir, item))]
    
    print(f"[*] Subdirectories ({len(folders)}): {', '.join(folders) if folders else 'None'}")
    print(f"[*] Files ({len(files)}): {', '.join(files) if files else 'None'}")

def main():
    # Process command-line runtime arguments using sys.argv
    if len(sys.argv) < 2:
        display_help()
        sys.exit(1) # Exit with an error code

    command = sys.argv[1].lower()

    if command == "setup":
        if len(sys.argv) < 3:
            print("[-] Missing argument. Usage: python file_utility.py setup <workspace_name>")
        else:
            create_workspace(sys.argv[2])
            
    elif command == "scan":
        if len(sys.argv) < 3:
            print("[-] Missing argument. Usage: python file_utility.py scan <.extension>")
        else:
            scan_extensions(sys.argv[2])
            
    elif command == "log":
        if len(sys.argv) < 3:
            print("[-] Missing argument. Usage: python file_utility.py log <message>")
        else:
            # Join all subsequent arguments into a single message string
            message = " ".join(sys.argv[2:])
            write_log(message)
            
    elif command == "readlog":
        read_log()
        
    elif command == "info":
        display_info()
        
    else:
        print(f"[-] Unknown command: '{command}'")
        display_help()
        sys.exit(1)

if __name__ == "__main__":
    main()