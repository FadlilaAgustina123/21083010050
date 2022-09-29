#!/bin/bash 

echo "Masukkan bilangan: "
read bil

echo "Maka, bilangan positif kelipatan ganjilnya adalah: "
while [ $bil -gt 0 ]
do
  echo $bil
  bil=$((bil-2))
done
