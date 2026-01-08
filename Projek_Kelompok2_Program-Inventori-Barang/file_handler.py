import os
import csv

def clear_screen():
    """Membersihkan layar terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

def load_data(filename):
    """Membaca data dari file CSV."""
    filepath = os.path.join("data", filename)
    if not os.path.exists("data"):
        os.makedirs("data")
        
    if not os.path.exists(filepath):
        return []
        
    data = []
    try:
        with open(filepath, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
        return data
    except (IOError, csv.Error):
        return []

def save_data(filename, data):
    """Menyimpan data ke file CSV."""
    filepath = os.path.join("data", filename)
    if not os.path.exists("data"):
        os.makedirs("data")
        
    if not data:
        # Create empty file if no data
        with open(filepath, 'w', newline='', encoding='utf-8') as file:
            pass
        return

    # Ambil keys dari dictionary pertama sebagai header
    fieldnames = data[0].keys()
    
    with open(filepath, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
