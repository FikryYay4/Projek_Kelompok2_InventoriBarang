import file_handler as fh

INVENTORY_FILE = "inventory.csv"

def generate_id(items):
    """Menghasilkan ID unik untuk barang baru secara otomatis."""
    if not items:
        return "BRG-001"
    
    # Ambil angka dari ID terakhir
    # Asumsi format ID selalu "BRG-XXX"
    max_id = 0
    for item in items:
        try:
            current_id_code = item['id']
            # Split berdasarkan '-' dan ambil bagian angka, lalu convert ke int
            number = int(current_id_code.split('-')[1])
            if number > max_id:
                max_id = number
        except (IndexError, ValueError):
            continue
            
    new_number = max_id + 1
    return f"BRG-{new_number:03d}"

def add_item():
    fh.clear_screen()
    print("="*40)
    print("TAMBAH BARANG BARU")
    print("="*40)
    
    items = fh.load_data(INVENTORY_FILE)
    
    # Auto Generate ID
    new_id = generate_id(items)
    print(f"ID Barang Otomatis: {new_id}")
    
    nama = input("Masukkan Nama Barang: ")
    jenis = input("Masukkan Jenis Barang: ")
    try:
        harga = int(input("Masukkan Harga Barang: "))
        stok = int(input("Masukkan Stok Barang: "))
    except ValueError:
        print("\nHarga dan Stok harus berupa angka!")
        input("Tekan Enter untuk kembali...")
        return

    new_item = {
        "id": new_id,
        "nama": nama,
        "jenis": jenis,
        "harga": harga,
        "stok": stok
    }
    
    items.append(new_item)
    fh.save_data(INVENTORY_FILE, items)
    
    print("\nBarang berhasil ditambahkan!")
    input("Tekan Enter untuk melanjutkan...")

def view_items():
    fh.clear_screen()
    print("="*40)
    print("DAFTAR BARANG")
    print("="*40)
    
    items = fh.load_data(INVENTORY_FILE)
    
    if not items:
        print("Belum ada data barang.")
    else:
        print(f"{'ID':<10} | {'Nama':<20} | {'Jenis':<15} | {'Harga':<10} | {'Stok':<5}")
        print("-" * 75)
        for item in items:
            print(f"{item['id']:<10} | {item['nama']:<20} | {item['jenis']:<15} | {item['harga']:<10} | {item['stok']:<5}")
            
    input("\nTekan Enter untuk melanjutkan...")

def update_item():
    fh.clear_screen()
    print("="*40)
    print("UPDATE BARANG")
    print("="*40)
    
    items = fh.load_data(INVENTORY_FILE)
    
    if not items:
        print("Belum ada data barang untuk diupdate.")
        input("Tekan Enter untuk kembali...")
        return
        
    view_items_simple(items)
    target_id = input("\nMasukkan ID Barang yang ingin diupdate: ")
    
    found = False
    for item in items:
        if item['id'] == target_id:
            print(f"\nData Lama: {item['nama']} | {item['jenis']} | {item['harga']} | {item['stok']}")
            print("Isi data baru (kosongkan jika tidak ingin mengubah):")
            
            nama = input(f"Nama [{item['nama']}]: ")
            if nama: item['nama'] = nama
            
            jenis = input(f"Jenis [{item['jenis']}]: ")
            if jenis: item['jenis'] = jenis
            
            harga_input = input(f"Harga [{item['harga']}]: ")
            if harga_input:
                try:
                    item['harga'] = int(harga_input)
                except ValueError:
                    print("Input harga tidak valid, menggunakan harga lama.")
                    
            stok_input = input(f"Stok [{item['stok']}]: ")
            if stok_input:
                try:
                    item['stok'] = int(stok_input)
                except ValueError:
                    print("Input stok tidak valid, menggunakan stok lama.")
                    
            found = True
            break
            
    if found:
        fh.save_data(INVENTORY_FILE, items)
        print("\nData barang berhasil diupdate!")
    else:
        print("\nBarang dengan ID tersebut tidak ditemukan.")
        
    input("Tekan Enter untuk melanjutkan...")

def delete_item():
    fh.clear_screen()
    print("="*40)
    print("HAPUS BARANG")
    print("="*40)
    
    items = fh.load_data(INVENTORY_FILE)
    
    if not items:
        print("Belum ada data barang untuk dihapus.")
        input("Tekan Enter untuk kembali...")
        return
        
    view_items_simple(items)
    target_id = input("\nMasukkan ID Barang yang ingin dihapus: ")
    
    new_items = [item for item in items if item['id'] != target_id]
    
    if len(new_items) < len(items):
        fh.save_data(INVENTORY_FILE, new_items)
        print("\nBarang berhasil dihapus!")
    else:
        print("\nBarang dengan ID tersebut tidak ditemukan.")
        
    input("Tekan Enter untuk melanjutkan...")

def view_items_simple(items):
    """Helper untuk menampilkan daftar sederhana."""
    print(f"{'ID':<10} | {'Nama':<20}")
    print("-" * 35)
    for item in items:
        print(f"{item['id']:<10} | {item['nama']:<20}")

def menu_inventory(user):
    while True:
        fh.clear_screen()
        print("="*40)
        print(f"MENU INVENTORY (User: {user})")
        print("="*40)
        print("1. Tambah Barang")
        print("2. Lihat Daftar Barang")
        print("3. Update Barang")
        print("4. Hapus Barang")
        print("5. Logout")
        print("="*40)
        
        choice = input("Pilih menu (1-5): ")
        
        if choice == '1':
            add_item()
        elif choice == '2':
            view_items()
        elif choice == '3':
            update_item()
        elif choice == '4':
            delete_item()
        elif choice == '5':
            print("\nLogout berhasil.")
            return
        else:
            print("\nPilihan tidak valid!")
            input("Tekan Enter untuk mencoba lagi...")
