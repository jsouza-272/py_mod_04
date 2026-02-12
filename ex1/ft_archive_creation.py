def main(file_name: str) -> None:
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    try:
        print(f"Initializing new storage unit: {file_name}")
        with open(file_name, "x+") as file:
            print("Storage unit created successfully...\n")
            print("Inscribing preservation data...")

            print("[ENTRY 001] New quantum algorithm discovered")
            file.write("[ENTRY 001] New quantum algorithm discovered\n")

            print("[ENTRY 002] Efficiency increased by 347%")
            file.write("[ENTRY 002] Efficiency increased by 347%\n")

            print("[ENTRY 003] Archived by Data Archivist trainee")
            file.write("[ENTRY 003] Archived by Data Archivist trainee")

        print("\nData inscription complete. Storage unit sealed.")
        print("Archive 'new_discovery.txt' ready for long-term preservation.")
    except FileExistsError:
        print("Storage unit already exists")


if __name__ == "__main__":
    main("new_discovery.txt")
