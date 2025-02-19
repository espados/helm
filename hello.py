import os
import sys

def main():
    print_message = os.getenv("PRINT_MESSAGE", "error").lower()

    if print_message == "deployment":
        i = 0
        while i == 0:
            print("v5: This is the actual service deployment...")
    elif print_message == "job":
        print("This is the post sync hook job...")
    else:
        sys.stderr.write("ERROR: PRINT_MESSAGE is not set to 'error' probably. Exiting...\n")
        sys.exit(1)

if __name__ == "__main__":
    main()
