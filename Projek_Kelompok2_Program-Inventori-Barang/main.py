import auth
import inventory
import file_handler as fh

def main():
    fh.clear_screen()
    print("="*40)
    print("SELAMAT DATANG")
    print("SISTEM INVENTORI BARANG")
    print("="*40)
    input("\nTekan Enter untuk melanjutkan...")
    
    user = auth.menu_auth()
    
    if user:
        inventory.menu_inventory(user)
    
    fh.clear_screen()
    print("\n" + "="*40)
    print("PROGRAM SELESAI")
    print("="*40)

if __name__ == "__main__":
    main()