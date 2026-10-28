import traceback
import os

# Custom Exception Hierarchy
class FileProcessingError(Exception):
    """Base exception for file processing."""
    pass

class InvalidFormatError(FileProcessingError):
    """Raised when file content formatting is invalid."""
    pass

def process_file(filepath):
    """Fault-tolerant file parser demonstrating try-except-else-finally."""
    file_obj = None
    try:
        print(f"\n[*] Attempting to process: '{filepath}'")
        file_obj = open(filepath, 'r')
        
        for line_num, line in enumerate(file_obj, 1):
            # Simulated parsing rule: Each line must contain a comma
            if "," not in line and line.strip():
                raise InvalidFormatError(f"Line {line_num} missing comma separator: '{line.strip()}'")
                
    except FileNotFoundError:
        print("[-] Error: The specified file does not exist.")
        
    except InvalidFormatError as e:
        print(f"[-] Format Error Caught: {e}")
        print("[-] Traceback Log:")
        traceback.print_exc() # Logs the full traceback for debugging
        
    except Exception as e:
        print(f"[-] An unexpected error occurred: {e}")
        
    else:
        # Executes ONLY if the try block succeeds without any exceptions
        print("[+] Success: File parsed completely with valid formatting.")
        
    finally:
        # Guarantee resource cleanup regardless of success or failure
        if file_obj and not file_obj.closed:
            file_obj.close()
            print("[*] Cleanup: File resource safely closed.")

if __name__ == "__main__":
    # 1. Create dummy files for demonstration
    valid_file, invalid_file = "valid.txt", "invalid.txt"
    with open(valid_file, "w") as f: f.write("ID,Name\n1,Alice\n2,Bob")
    with open(invalid_file, "w") as f: f.write("ID,Name\n1,Alice\nBadLineWithoutComma")

    # 2. Run the pipeline against different scenarios
    process_file(valid_file)       # Triggers 'else' and 'finally'
    process_file(invalid_file)     # Triggers custom 'except' and 'finally'
    process_file("missing.txt")    # Triggers FileNotFoundError and 'finally'

    # 3. Cleanup dummy files
    os.remove(valid_file)
    os.remove(invalid_file)