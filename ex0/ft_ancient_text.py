def main(file_name: str) -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    print(f"\nAccessing Storage Vault: {file_name}")
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            print("Connection established...\n")
            print("RECOVERED DATA:")
            print(file.read())
        print("\nData recovery complete. Storage unit disconnected")
    except FileNotFoundError:
        print("ERROR: Storage vault not found")


if __name__ == "__main__":
    main("ancient_fragment.txt")
