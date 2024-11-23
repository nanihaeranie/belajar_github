from colorama import Fore, init

# Inisialisasi colorama (penting untuk Windows)
init()

# Cetak teks dengan warna berbeda
print(Fore.YELLOW + "Hello World")
print(Fore.RED + "Hello World")
print(Fore.BLUE + "Hello World")
print(Fore.CYAN + "Hello World")
print(Fore.GREEN + "Hello World")

# Reset warna kembali ke default
print(Fore.RESET + "Back to default color")
