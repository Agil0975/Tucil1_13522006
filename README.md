# Tucil1_13522006
Tugas Kecil Mata Kuliah IF2211 Strategi Algoritma 2024 - Cyberpunk 2077 Breach Protocol

## **Table of Contents**
* [Deskripsi Singkat](#deskrips-singkat)
* [Requirements](#requirements)
* [Cara Menjalankan Program](#cara-menjalankan-program)
* [Struktur Program](#struktur-program)
* [Author](#author)

## **Deskripsi Singkat**
<em> Cyberpunk 2077 Breach Protocol <em> adalah minigame meretas pada permainan video Cyberpunk 2077.
Minigame ini merupakan simulasi peretasan jaringan local dari ICE (Intrusion Countermeasures
Electronics) pada permainan Cyberpunk 2077. 

Komponen pada permainan ini antara lain adalah:
1. Token – terdiri dari dua karakter alfanumerik seperti E9, BD, dan 55.
2. Matriks – terdiri atas token-token yang akan dipilih untuk menyusun urutan kode.
3. Sekuens – sebuah rangkaian token (dua atau lebih) yang harus dicocokkan.
4. Buffer – jumlah maksimal token yang dapat disusun secara sekuensial. 

Aturan permainan Breach Protocol antara lain:
1. Pemain bergerak dengan pola horizontal, vertikal, horizontal, vertikal (bergantian) hingga 
   semua sekuens berhasil dicocokkan atau buffer penuh.
2. Pemain memulai dengan memilih satu token pada posisi baris paling atas dari matriks.
3. Sekuens dicocokkan pada token-token yang berada di buffer.
4. Satu token pada buffer dapat digunakan pada lebih dari satu sekuens.
5. Setiap sekuens memiliki bobot hadiah atau reward yang variatif.
6. Sekuens memiliki panjang minimal berupa dua token.

## **Requirements**
Untuk menjalankan program ini, kamu perlu menginstal **Python** pada perangkat yang kamu gunakan.

## **Cara Menjalankan Program**
1. Clone repositori ini. <br>
`$ git clone  https://github.com/Agil0975/Tucil1_13522006.git `
2. Pindah ke direktori 'Tucil1_13522006'. <br>
`$ cd Tucil1_13522006 `
3. Jalankan program dengan mengetikkan: <br>
`$ python src/main.py `
4. Pastikan file txt berada di folder 'test' (jika input via file .txt).

## **Struktur Program**
```
.
│   .gitignore
│   README.md
|
├───bin
|   └───.gitignore
|
├───doc
|   └───Tucil1_K2_13522006_Agil Fadillah Sabri.pdf
|
└───src
|    |
|    └───main.py
|
└───test
     |
     └───hasil_manual1.txt
         hasil_manual2.txt
         hasil_manual3.txt
         hasil_manual4.txt
         hasil_manual5.txt
         hasil_test1.txt
         hasil_test2.txt
         hasil_test3.txt
         hasil_test4.txt
         hasil_test5.txt
         test1.txt
         test2.txt
         test3.txt
         test4.txt
         test5.txt
```

## **Author**

| **NIM**  |       **Nama**        | **Kelas** |       
| :------: | :-------------------: | :------:  | 
| 13522006 |  Agil Fadillah Sabri  |   K02