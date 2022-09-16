#!/bin/bash

#penjumlahan
echo "LINUX JUMLAHIN ANGKA YG KAMU MASUKIN YAA"
echo "Masukkan nilai p: "
read p
echo "Masukkan nilai q: "
read q
let hasil=$p+$q
echo "Jadi, hasil dari penjumlahan $p + $q = $hasil"

sleep 1

#perkalian
echo "SELANJUTNYA LINUX BAKAL KALIIN "
echo "Masukkan nilai a: "
read a
echo "Masukkan nilai b: "
read b
let kali=$a*$b
echo "Jawaban dari perkalian tersebut adalah $kali"

sleep 1

#perbandingan
echo "YANG TERAKHIR BANDINGIN NILAI YAGESYAK"
sleep 1
echo "IYADONG KALO AKU DIBANDINGIN SM MANTAN  KAMU YO NDAK MAMPU HEHE"
echo "Masukin nilai x: "
read x
echo "Masukin nilai y: "
read y
echo "SATU DUA TIGA CLING"
sleep 1

if [ $x -gt $y ]
then
  echo "Nilai x lebih besar dari nilai y"
elif [ $x -lt $y ]
then
  echo "Nilai x lebih kecil dari nilai y"
elif [ $x -eq $y ]
then
  echo "Nilainya sama gaiss"
else
  echo "Maaf coba masukin nilai yg beda yaa"
fi

sleep 1

echo "THANK YOUU"
