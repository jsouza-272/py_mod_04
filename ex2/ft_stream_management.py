import sys


def main() -> None:
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")
    sys.stdout.write("Intput Stream active. Enter archivist ID: ")
    sys.stdout.flush()
    arch_id = sys.stdin.readline()
    sys.stdout.write("Intput Stream active. Enter status report: ")
    sys.stdout.flush()
    arch_status = sys.stdin.readline()
    print()
    sys.stdout.write("[STANDARD] Archive status from "
                     + f"{arch_id[:-1]}: {arch_status[:-1]}\n")
    sys.stderr.write("[ALERT] System diagnostic: "
                     + "Communication channels verified\n")
    sys.stdout.flush()
    sys.stderr.flush()
    sys.stdout.write("[STANDARD] Data transmission complete\n")
    sys.stdout.flush()
    print("\nThree-channel communication test successful.")


if __name__ == "__main__":
    main()
