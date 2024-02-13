import random
import time
import os

global current_reward_maksimum, buffer_with_reward_maksimum, max_reward_can_get
global list_of_sequence, jumlah_sequence, metode_input
global row_col, matriks_of_token, buffer_size, current_buffer
# current_reward_maksimum : int
# buffer_with_reward_maksimum : list of (string, int, int) -------> (token, baris, kolom)
# buffer_size : int
# row_col : (int, int)
# matriks_of_token : matriks of string
# jumlah_sequence : int
# list_of_sequence : list of (string, int)
# max_reward_can_get : int
# current_buffer : list of (string, int, int) -------> (token, baris, kolom)
# metode_input : string

current_reward_maksimum = 0
buffer_with_reward_maksimum = []

################################################ FUNGSI/PROSEDUR ################################################
def get_row_col(width_height):
# mengubah masukan menjadi tuple baris dan kolom
# width_height : string
# return : (int, int) -------> (baris, kolom)
    for i in range(len(width_height)):                                  # width = kolom, height = baris
        if width_height[i] == " ":
            return (int(width_height[i+1:]), int(width_height[:i]))

def get_row_of_token(string_of_token, column_of_matriks):
# mengubah baris masukan menjadi 1 baris elemen matriks token
# string_of_token : string
# column_of_matriks : int
# return : list of string
    row_of_token = [[' ', 0] for i in range(column_of_matriks)]
    column = 0

    string_without_space = string_of_token.replace(" ", "")
    
    if (len(string_without_space) % 2 != 0) or (len(string_without_space)/2 != column_of_matriks):
    # terdapat token yang panjangnya tidak sama dengan 2
        print()
        print("Terdapat token yang tidak valid pada matriks token.")
        print("Silahkan perbaiki terlebih dahulu file txt-nya!")
        exit()

    for i in range(0,len(string_of_token),3):
        row_of_token[column][0] = string_of_token[i:(i+2)]
        column += 1
    return row_of_token

def buffer_to_string(buffer):
# mengubah isi token pada buffer menjadi string token
# buffer : list of (string, int, int) -------> (token, baris, kolom)
# return : string 
    string_buffer = ''
    for i in range(buffer_size):
        string_buffer += buffer[i][0]
    return string_buffer

def hitung_reward(buffer):
# menghitung reward dari token-token yang ada pada buffer
# buffer : list of (string, int, int) -------> (token, baris, kolom)
# return : integer
    hasil_buffer = buffer_to_string(buffer)
    reward = 0
    for i in range(jumlah_sequence):
        if list_of_sequence[i][0] in hasil_buffer:
            reward += list_of_sequence[i][1]
    return reward

def copy_buffer(buffer):
# mengcopy isi buffer ke buffer lain
# buffer : list of (string, int, int) -------> (token, baris, kolom)
# return : list of (string, int, int) -------> (token, baris, kolom)
    buffer_copy = [('', -999, -999) for i in range(buffer_size)]
    for i in range(buffer_size):
        buffer_copy[i] = buffer[i]
    return buffer_copy

def generate_random_sequence(jumlah_token_unik, list_token, ukuran_maksimum_sequence):
# menghasilkan sequence secara random
# jumlah_token_unik : int
# list_token : list of string -------> daftar token unik
# ukuran_maksikum_sequence : int
    global max_reward_can_get, list_of_sequence, jumlah_sequence
    max_reward_can_get = 0

    list_of_sequence = [' ' for i in range(jumlah_sequence)]
    for i in range(jumlah_sequence):
        panjang_sequence = random.randint(2, ukuran_maksimum_sequence)
        string_sequence = ''
        for j in range(panjang_sequence):
            string_sequence += list_token[random.randint(0, jumlah_token_unik-1)]
        list_of_sequence[i] = (string_sequence, random.randint(-10, 10)*5)
        
        if list_of_sequence[i][1] > 0:
            max_reward_can_get += list_of_sequence[i][1]

def is_sequence_unik(list_of_sequence):
# mengecek apakah sequence unik
# list_of_sequence : list of (string, int) -------> (sekuens, reward)
# return : boolean
    global jumlah_sequence
    for i in range(jumlah_sequence):
        for j in range(0,i):
            if list_of_sequence[j][0] == list_of_sequence[i][0]:
                return False
    return True

def membaca_input(cara_input):
# prosedur membaca masukan dari pengguna
# cara_input : string
    global buffer_size, row_col, matriks_of_token, jumlah_sequence, list_of_sequence
    global max_reward_can_get, current_buffer, metode_input

    metode_input = cara_input
    max_reward_can_get = 0

    if cara_input == "1":                                                         # membaca input dari file txt
        print()
        print("========================= INPUT =========================")
        
        print("Pastikan file txt berada pada folder test")
        nama_file = input("Masukkan nama file (ex: test.txt): ")
        
        while not os.path.exists("test/" + nama_file):
            print("File tidak ditemukan! Silahkan masukkan nama file lainnya.")
            nama_file = input("Masukkan nama file (ex: test.txt): ")

        f = open("test/" + nama_file, "r")
        
        buffer_size = int(f.readline().replace("\n", ""))
        current_buffer = [('', -999, -999) for i in range(buffer_size)]

        row_col = get_row_col(f.readline().replace("\n", ""))
        matriks_of_token = [' ' for i in range(row_col[0])]
        for i in range(row_col[0]):
            matriks_of_token[i] = get_row_of_token(f.readline().replace("\n", ""), row_col[1])

        jumlah_sequence = int(f.readline().replace("\n", ""))
        list_of_sequence = [' ' for i in range(jumlah_sequence)]
        for i in range(jumlah_sequence):
            sequence = f.readline().replace("\n", "")
            jumlah_spasi = sequence.count(" ")
            seq_without_space = sequence.replace(" ", "")

            if (len(seq_without_space) % 2 != 0) or (len(seq_without_space)/2 != jumlah_spasi+1):
            # terdapat token yang panjangnya tidak sama dengan 2
                print()
                print("Terdapat token yang tidak valid pada sequence.")
                print("Silahkan perbaiki terlebih dahulu file txt-nya!")
                exit()
            
            if i >= 1:
                for j in range(0,i):
                    if list_of_sequence[j][0] == seq_without_space:
                        print()
                        print("Terdapat 2 sequence yang sama pada file txt.")
                        print("Silahkan perbaiki terlebih dahulu file txt-nya!")
                        exit()

            list_of_sequence[i] = (seq_without_space, int(f.readline().replace("\n", "")))
            if list_of_sequence[i][1] > 0:
                max_reward_can_get += list_of_sequence[i][1]
        f.close()

    elif cara_input == "2":                                                       # membaca input via cli
        print()
        print("========================= INPUT =========================")

        jumlah_token_unik = int(input("Masukkan jumlah token unik                        : "))
        while (jumlah_token_unik < 1):
            print("Jumlah token unik tidak valid!")
            jumlah_token_unik = int(input("Masukkan jumlah token unik                        : "))
        
        list_token = ['' for i in range(jumlah_token_unik)]
        unik = False
        while (unik == False):
            token = input("Masukkan token unik                               : ")
            total_space = token.count(" ")
            token_without_space = token.replace(" ", "")

            if (len(token_without_space) % 2 == 0) and (len(token_without_space)/2 == jumlah_token_unik) and (total_space == jumlah_token_unik-1):
                for i in range(0,len(token_without_space),2):
                    list_token[i//2] = token_without_space[i:(i+2)]
                if len(list_token) == len(set(list_token)):
                    unik = True

            if (unik == False):
                print("Token yang dimasukkan tidak valid/tidak unik.")
                print("Silahkan masukkan token unik kembali!")

        buffer_size = int(input("Masukkan ukuran buffer                            : "))
        while (buffer_size < 1):
            print("Ukuran buffer tidak valid!")
            buffer_size = int(input("Masukkan ukuran buffer                            : "))

        row_col = get_row_col(input("Masukkan lebar (kolom) dan tinggi (baris) matriks : "))
        while (row_col[0] < 1) or (row_col[1] < 1):
            print("Jumlah baris dan kolom tidak valid!")
            row_col = get_row_col(input("Masukkan lebar (kolom) dan tinggi (baris) matriks : "))

        jumlah_sequence = int(input("Masukkan jumlah sequence                          : "))
        while (jumlah_sequence < 1):
            print("Jumlah sequence tidak valid!")
            jumlah_sequence = int(input("Masukkan jumlah sequence                          : "))

        ukuran_maksimum_sequence = int(input("Masukkan ukuran maksimum sequence                 : "))
        while (ukuran_maksimum_sequence < 2):
            print("Ukuran maksimum sequence tidak valid!")
            ukuran_maksimum_sequence = int(input("Masukkan ukuran maksimum sequence                 : "))

        current_buffer = [('', -999, -999) for i in range(buffer_size)]

        matriks_of_token = [[[' ', 0] for i in range(row_col[1])] for j in range(row_col[0])]
        for i in range(row_col[0]):
            for j in range(row_col[1]):
                matriks_of_token[i][j][0] = list_token[random.randint(0, jumlah_token_unik-1)]

        generate_random_sequence(jumlah_token_unik, list_token, ukuran_maksimum_sequence)
        while not is_sequence_unik(list_of_sequence):
            generate_random_sequence(jumlah_token_unik, list_token, ukuran_maksimum_sequence)
    
    else:
        ulangi = input("Input tidak valid, apakah anda ingin mengulangi input? (y/n) : ")
        if ulangi == "y" or ulangi == "Y":
            cara_input = input("Masukkan metode yang diinginkan (pastikan memasukkan 1/2): ")
            membaca_input(cara_input)
        elif ulangi == "n" or ulangi == "N":
            exit()
        else:
            membaca_input(3)

def write_to_file(ingin_menyimpan):
# menuliskan hasil ke file txt
# ingin_menyimpan : string
    if ingin_menyimpan == "y" or ingin_menyimpan == "Y":
        nama_file = input("Masukkan nama file (ex: output.txt): ")
        
        while os.path.exists("test/" + nama_file):
            print("File dengan nama tersebut sudah ada! Silahkan masukkan nama file lainnya.")
            nama_file = input("Masukkan nama file (ex: output.txt): ")

        f = open("test/" + nama_file, "w")

        f.write(f"{current_reward_maksimum}\n")

        if current_reward_maksimum > 0:
            for i in range(buffer_size):
                f.write(f"{buffer_with_reward_maksimum[i][0]} ")
            f.write("\n")
            for i in range(buffer_size):
                f.write(f"{buffer_with_reward_maksimum[i][2]+1}, {buffer_with_reward_maksimum[i][1]+1}\n")
            f.write("\n")
        else:
            f.write("No Solution\n\n")
        
        f.write(f"{waktu_eksekusi*1000} ms\n")
        f.close()

        print("Solusi berhasil disimpan pada file", nama_file)

    elif ingin_menyimpan == "n" or ingin_menyimpan == "N":
        exit()
    else:
        ingin_menyimpan = input("Input tidak valid, apakah anda ingin kembali menyimpan solusi? (y/n): ")
        write_to_file(ingin_menyimpan)

def vertical(current_buffer_position):
# proses brute force
# melakukan pencarian token secara vertikal pada matriks token
# current_buffer_position : int
    global current_reward_maksimum, buffer_with_reward_maksimum
    
    if current_reward_maksimum == max_reward_can_get:                                       # basis, saat reward maksimum sudah tercapai
        return
    else:
        if current_buffer_position == buffer_size:                                          # basis, saat buffer sudah terisi penuh
            reward = hitung_reward(current_buffer)
            if reward > current_reward_maksimum:
                current_reward_maksimum = reward
                buffer_with_reward_maksimum = copy_buffer(current_buffer)
            return
        else:
            for i in range(1, row_col[0]):                                                  # rekurens, melakukan pencarian token secara vertikal
                row = (current_buffer[current_buffer_position-1][1]+i)%row_col[0]
                column = current_buffer[current_buffer_position-1][2]
                if matriks_of_token[row][column][1] == 0:                                   # token belum pernah diambil    
                    current_buffer[current_buffer_position] = (matriks_of_token[row][column][0], row, column)
                    matriks_of_token[row][column][1] = 1
                    horizontal(current_buffer_position+1)
                    matriks_of_token[row][column][1] = 0                                    # mengembalikan nilai token yang diambil menjadi 0 agar bisa diambil pada iterasi selanjutnya

def horizontal(current_buffer_position):
# proses brute force
# melakukan pencarian token secara horizontal pada matriks token
# current_buffer_position : int
    global current_reward_maksimum, buffer_with_reward_maksimum
    
    if current_reward_maksimum == max_reward_can_get:                                       # basis, saat reward maksimum sudah tercapai
        return
    else:
        if current_buffer_position == buffer_size:                                          # basis, saat buffer sudah terisi penuh
            reward = hitung_reward(current_buffer)
            if reward > current_reward_maksimum:
                current_reward_maksimum = reward
                buffer_with_reward_maksimum = copy_buffer(current_buffer)
            return
        else:
            for i in range(1, row_col[1]):                                                  # rekurens, melakukan pencarian token secara horizontal
                row = current_buffer[current_buffer_position-1][1]
                column = (current_buffer[current_buffer_position-1][2]+i)%row_col[1]
                if matriks_of_token[row][column][1] == 0:                                   # token belum pernah diambil
                    current_buffer[current_buffer_position] = (matriks_of_token[row][column][0], row, column)
                    matriks_of_token[row][column][1] = 1
                    vertical(current_buffer_position+1)
                    matriks_of_token[row][column][1] = 0                                    # mengembalikan nilai token yang diambil menjadi 0 agar bisa diambil pada iterasi selanjutnya

################################################ MAIN PROGRAM ################################################
print("========================================================")
print("=== Selamat Datang di Cyberpunk 2077 Breach Protocol ===")
print("========================================================\n")

print("========================= MENU =========================")
print("Metode input:")
print("   1. File txt")
print("   2. Input manual")
cara_input = input("Masukkan metode yang diinginkan: ")
membaca_input(cara_input)

time_start = time.time()
for i in range(row_col[1]):                # melakukan pencarian sequence yang dimulai pada setiap token pada baris pertama
    current_buffer[0] = (matriks_of_token[0][i][0], 0, i)
    matriks_of_token[0][i][1] = 1
    vertical(1)
time_end = time.time()

waktu_eksekusi = time_end - time_start

# output
print()
print("======================== OUTPUT =========================")
if metode_input == "2":                                  # jika input via cli, maka menampilkan matriks token dan sequence
    print("Matriks of token: ")
    for i in range(row_col[0]):
        for j in range(row_col[1]):
            print(matriks_of_token[i][j][0], end=" ")
        print()
    
    print()
    print("Sequence: ")
    for i in range(jumlah_sequence):
        for j in range(0,len(list_of_sequence[i][0]),2):
            print(list_of_sequence[i][0][j:(j+2)], end=" ")
        print()
        print(f"Reward: {list_of_sequence[i][1]}")
    print()

print(current_reward_maksimum)
if current_reward_maksimum > 0:
    for i in range(buffer_size):
        print(buffer_with_reward_maksimum[i][0], end=" ")
    print()
    for i in range(buffer_size):                        # format output :       kolom, baris
        print(f"{buffer_with_reward_maksimum[i][2]+1}, {buffer_with_reward_maksimum[i][1]+1}")
else:
    print("No Solution")

print()
print(waktu_eksekusi*1000, "ms\n")

cara_simpan = input("Apakah ingin menyimpan solusi? (y/n): ")
write_to_file(cara_simpan)