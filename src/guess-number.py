import random

# ======== Intro Game ======== 
print(("=" * 21) + " Game Tebak Angka " + ("=" * 21))
print("               Selamat datang di Game Tebak Angka")
print("\n   Kamu memiliki 7 kesempatan untuk menebak antara 1-50\n")
print("-" * 60)

# ======== Validasi Variabel ======== 
num = random.randrange(1,50) # Mencari angka random dengan library random
correct = 0 # Vaiabel jumlah tebakan yang benar

# ======== Loop Tempat Game Berjalan ======== 
for i in range(7): # Looping untuk mengatur kesempatan Player untuk menjawab
    try:
        guess = int(input("Masukan Tebakan Antara 1-50: ")) # Input Tebakan Player
    except ValueError: # Error handling jika Player memasukan jawaban selain angka
        print("Whoops! Input bukan angka. Coba lagi.")
        continue
    
    # Percabangan jika jawaban benar atau salah
    if guess > num: # Jika tebakan lebih besar dari jawaban
        print("Kebesaran! Coba angka yang lebih kecil.")
    elif guess < num: # Jika tebakan lebih kecil dari jawaban
        print("Kekecilan! Coba angka yang lebih besar.")
    else: # Jika Tebakan Benar
        guess += 1 # Mengubah Nilai variabel correct
        break

# ======== Output Setelah Game Selesai ========
# Percabangan output keberhasilan Player 
if correct == 1: # Jika Player berhasil menebak
    print("\nHoree! Kamu Berhasil Menebaknya.")
else: # Jika Player gagal menebak
    print("\nSayang sekali, kamu gagal Menebaknya.")