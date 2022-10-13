#!/bin/bash

echo "Banyaknya nilai yang ingin dimasukkan:"
read ipk

jumlah=0;
ipk_mhs=0;

for ((i=1; i<=ipk; i++))
do
	echo "Nilai ke-$i :"
	read isi[$i]
	let jumlah=$jumlah+${isi[i]};
	let ipk_mhs=$jumlah/$ipk;
done

echo "IPS mhs =" $jumlah / $ipk
echo "IPK mhs =" $ipk_mhs
