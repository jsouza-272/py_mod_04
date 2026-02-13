def file_not_found() -> None:
    file_name = "lost_archive.txt"
    print(f"CRISIS ALERT: Attempting access to '{file_name}'...")
    try:
        with open(file_name, "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")


def permission_error() -> None:
    file_name = "classified_vault.txt"
    print(f"CRISIS ALERT: Attempting access to '{file_name}'...")
    try:
        with open(file_name, "r") as file:
            print(file.read())
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")


def normal_operation() -> None:
    file_name = "standard_archive.txt"
    print(f"ROUTINE ACCESS: Attempting access to '{file_name}'...")
    try:
        with open(file_name, "r") as file:
            recoverd = file.read()
            print(f"SUCCESS: Archive recovered - ``{recoverd}''")
        print("STATUS: Normal operations resumed")
    except (FileNotFoundError, PermissionError):
        print("Crisis")


def main() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
    file_not_found()
    print()
    permission_error()
    print()
    normal_operation()
    print("\nAll crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()
