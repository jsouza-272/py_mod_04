def main() -> None:
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")

    print("Initiating secure vault access...")
    try:
        with open("classified_data.txt", "r") as file:
            print("Vault connection established with failsafe protocols\n")
            print("SECURE EXTRACTION:")
            print(file.read())

        with open("security_protocols.txt", "r") as file:
            print("\nSECURE PRESERVATION:")
            print(file.read())

        print("Vault automatically sealed upon completion")

    except FileNotFoundError:
        print("Vault not found")

    print("\nAll vault operations completed with maximum security.")


if __name__ == "__main__":
    main()
