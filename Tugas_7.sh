#!/bin/bash

Panjang() {
	echo "Masukkan Panjang :"
	read p
	Lebar
}
Lebar() {
	echo "Masukkan Lebar  :"
	read l
	let Luas_Persegi=$p*$l
	echo "Luas Persegi :" 
	echo "$Luas_Persegi"
}
Panjang 
