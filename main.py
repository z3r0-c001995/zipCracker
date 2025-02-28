import zipfile
import rarfile
import argparse
import pyfiglet
import time
from tqdm import tqdm
from colorama import init, Fore  # Importing colorama for coloring

# Initialize colorama
init()

# Function to display a decorated banner for zipCracker
def generate_banner():
    banner = pyfiglet.figlet_format("☠️ zipCracker ☠️")
    print(banner)
    # Right-align the author name below the banner with color
    print(Fore.GREEN + "by z3r0c001".rjust(50))  # Author's name in green


def count_lines(wordlist):
    """Count total words in the wordlist for progress tracking."""
    try:
        with open(wordlist, 'r', encoding='latin-1') as f:
            return sum(1 for _ in f)
    except FileNotFoundError:
        print(Fore.RED + f"[-] Error: Wordlist file '{wordlist}' not found.")
        exit(1)
    except Exception as e:
        print(Fore.RED + f"[-] Error reading wordlist: {e}")
        exit(1)


def crack_zip(zip_path, wordlist):
    """Attempt to crack a ZIP file password using a wordlist."""
    total_passwords = count_lines(wordlist)
    
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_file:
            with open(wordlist, 'r', encoding='latin-1') as words:
                for i, word in enumerate(tqdm(words, total=total_passwords, desc=Fore.CYAN + "Cracking ZIP", unit=" passwords")):
                    password = word.strip().encode('utf-8')
                    try:
                        zip_file.extractall(pwd=password)
                        print(Fore.GREEN + f"\n[+] Password found: {password.decode()}")
                        return
                    except (RuntimeError, zipfile.BadZipFile):
                        pass
    except FileNotFoundError:
        print(Fore.RED + f"[-] Error: ZIP file '{zip_path}' not found.")
        exit(1)
    except Exception as e:
        print(Fore.RED + f"[-] Error processing ZIP file: {e}")
        exit(1)

    print(Fore.RED + "\n[-] Password not found.")


def crack_rar(rar_path, wordlist):
    """Attempt to crack a RAR file password using a wordlist."""
    # Ensure UnRAR is in the system PATH
    rarfile.UNRAR_TOOL = "unrar"  
    total_passwords = count_lines(wordlist)

    try:
        with rarfile.RarFile(rar_path, 'r') as rar_file:
            with open(wordlist, 'r', encoding='latin-1') as words:
                for i, word in enumerate(tqdm(words, total=total_passwords, desc=Fore.CYAN + "Cracking RAR", unit=" passwords")):
                    password = word.strip()
                    try:
                        rar_file.extractall(pwd=password)
                        print(Fore.GREEN + f"\n[+] Password found: {password}")
                        return
                    except (rarfile.BadRarFile, rarfile.NeedFirstVolume):
                        pass
    except FileNotFoundError:
        print(Fore.RED + f"[-] Error: RAR file '{rar_path}' not found.")
        exit(1)
    except Exception as e:
        print(Fore.RED + f"[-] Error processing RAR file: {e}")
        exit(1)

    print(Fore.RED + "\n[-] Password not found.")


if __name__ == "__main__":
    # Display the banner at startup
    generate_banner()  

    parser = argparse.ArgumentParser(description="Crack ZIP or RAR file passwords using a wordlist.")
    parser.add_argument("file", help="Path to the ZIP or RAR file")
    parser.add_argument("wordlist", help="Path to the password wordlist")

    args = parser.parse_args()

    if args.file.endswith(".zip"):
        crack_zip(args.file, args.wordlist)
    elif args.file.endswith(".rar"):
        crack_rar(args.file, args.wordlist)
    else:
        print(Fore.RED + "[-] Unsupported file format.")

    # Prompt user to press '0' to terminate the program
    while True:
        user_input = input(Fore.YELLOW + "\nPress '0' and hit Enter to terminate the program: ")
        if user_input == '0':
            print(Fore.GREEN + "Exiting program...")
            exit()
