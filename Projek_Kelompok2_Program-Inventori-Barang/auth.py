import file_handler as fh
import string

def validate_password(password):
    """
    Validasi password:
    1. Minimal 8 karakter.
    2. Harus mengandung minimal satu karakter unik (simbol).
    """
    if len(password) < 8:
        print("\nPassword Gagal: Password harus memiliki minimal 8 karakter.")
        return False
    
    special_chars = string.punctuation
    if not any(char in special_chars for char in password):
        print("\nPassword Gagal: Password harus memiliki minimal satu karakter unik/simbol.")
        return False
        
    return True

def login():
    fh.clear_screen()
    print("="*40)
    print("LOGIN SYSTEM")
    print("="*40)
    username = input("Username: ")
    password = input("Password: ")
    
    users = fh.load_data("users.csv")
    
    for user in users:
        # Strict case sensitivity comparison (default in Python strings)
        if user['username'] == username and user['password'] == password:
            print(f"\nLogin berhasil! Selamat datang, {username}.")
            input("Tekan Enter untuk melanjutkan...")
            return username
            
    print("\nUsername atau password salah!")
    input("Tekan Enter untuk mencoba lagi...")
    return None

def register():
    fh.clear_screen()
    print("="*40)
    print("REGISTRASI USER BARU")
    print("="*40)
    print("Syarat Password:")
    print("- Minimal 8 karakter")
    print("- Minimal 1 karakter unik/simbol")
    print("="*40)
    
    username = input("Masukkan Username baru: ")
    
    users = fh.load_data("users.csv")
    
    # Cek apakah username sudah ada (Case Sensitive Check)
    for user in users:
        if user['username'] == username:
            print("\nUsername sudah digunakan! Silakan pilih yang lain.")
            input("Tekan Enter untuk kembali...")
            return

    password = input("Masukkan Password baru: ")
    
    if not validate_password(password):
        input("Tekan Enter untuk mencoba lagi...")
        return
    
    new_user = {
        "username": username,
        "password": password
    }
    
    users.append(new_user)
    fh.save_data("users.csv", users)
    
    print("\nRegistrasi berhasil! Silakan login.")
    input("Tekan Enter untuk melanjutkan...")

def menu_auth():
    while True:
        fh.clear_screen()
        print("="*40)
        print("MENU UTAMA AUTENTIKASI")
        print("="*40)
        print("1. Login")
        print("2. Register")
        print("3. Keluar Program")
        print("="*40)
        
        choice = input("Pilih menu (1-3): ")
        
        if choice == '1':
            user = login()
            if user:
                return user
        elif choice == '2':
            register()
        elif choice == '3':
            print("\nTerima kasih telah menggunakan program ini.")
            exit()
        else:
            print("\nPilihan tidak valid!")
            input("Tekan Enter untuk mencoba lagi...")
