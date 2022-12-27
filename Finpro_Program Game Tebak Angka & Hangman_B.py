import random
import string

def kembali():
  while(True):
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("\n            PROGRAM PERMAINAN TEBAK ANGKA & HANGMAN                \n")
    print("\n                     By : Fadlila Agustina                         \n")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    main = int(input("\nGame apa yg ingin km mainkan? \n1. Tebak Angka \n2. Hangman \n3. Keluar \njawab: "))
    if(main == 1):
      TebakAngka()
    elif(main == 2):
      GameHangman()
    else:
      Keluar()
      break

def Keluar():
  print("\n=======================================================================")
  print("\n                     Thank youu and See uu!                        \n")
  print("=======================================================================")

def TebakAngka():
    #GAME TEBAK ANGKA
    #looping program berjalan
    while(True): 
      print("\n=======================================================================")
      print("\n            Selamat bermain di permainan Tebak Angka!              \n")
      print("=======================================================================")
      print("\n                         range angka :                               ")
      print("                         level mudah  = (1-10)                         ")
      print("                         level sedang = (1-20)                         ")
      print("                         level sulit  = (1-30)                         ")
      print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
      level = input("\nMau coba level apa? [mudah/sedang/sulit]: ")
      while (level != "mudah" and level != "sedang" and level != "sulit"):
        level = input("\nMaaf inputan anda tidak ada di opsi \nPilih level yg ada di opsi [mudah/sedang/sulit] : ")

      if level == "mudah":
        kesempatan = int(input("Berapa kesempatan yang km inginkan? "))
        angka_rahasia = random.randint(1,10)
      elif level == "sedang":
        kesempatan = int(input("Berapa kesempatan yang km inginkan? "))
        angka_rahasia = random.randint(1,20)
      elif level == "sulit":
        kesempatan = int(input("Berapa kesempatan yang km inginkan? "))
        angka_rahasia = random.randint(1,30)

      print("\nlevel yg km pilih", level, "dengan kesempatan", kesempatan, "kali")
      print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

      #looping tebak angka
      while (kesempatan >= 0) :
        if kesempatan == 0 :
          print("\nAngka yang benar adalah:", angka_rahasia)
          print("Maaf km gagal dalam permainan tebak angka:(")
          break
        else:
          print("\nSisa kesempatanmu tinggal: ", kesempatan)
          tebakan = int(input("\nMasukkan angka tebakanmu: "))
          if tebakan == angka_rahasia:
            print("\nWahh keren selamat tebakanmu benarr")
            break
          elif tebakan > angka_rahasia:
            print("Clue: angkanya kurang dari", tebakan)
            kesempatan -= 1
          elif tebakan < angka_rahasia:
            print("Clue: angkanya lebih dari", tebakan)
            kesempatan -=1

      #untuk mengkonfirmasi ulang
      ulang = input("\nApakah mau main tebak angka lagi? (y/n): ")
      while(ulang != "y" and ulang != "n"):
        ulang = input("\nMaaf inputan anda tidak ada di opsi \nMau main tebak angka lagi?: ")
      if ulang == "y":
        print("\nHayyuk main lagii \n")
      elif ulang == "n":
        print("\nThank youu uda main tebak angka \n")
        break
        kembali()
    return

def GameHangman():
  while(True):
    print("\n=======================================================================")
    print("\n               Selamat bermain di permainan Hangman!                 \n")
    print("=======================================================================\n")
    print("Kita sudah menyediakan beberapa kata sifat untuk ditebak")

    kata = ["malas", "cantik", "ganteng", "rajin", "pintar", "wangi", "rapi", "kaya"]
    kesempatan = {
        0: """
               ____________
              | /         |
              |/         ( )
              |          _|_
              |           |
              |          / \\
              |
             _|_
            |_ _|  Tebaklah kata sifatnya!
          """,
        1: """
              ____________
             | /         |
             |/         ( )
             |          _|_
             |          
             |         
             |
            _|_
           |_ _|  Tebaklah kata sifatnya!
          """,
        2: """
              ____________
             | /         |
             |/         ( )
             |         
             |          
             |         
             |
            _|_
           |_ _|  Tebaklah kata sifatnya!
          """,
        3: """
              ____________
             | /         |
             |/        
             |         
             |          
             |         
             |
            _|_
           |_ _|  Tebaklah kata sifatnya!
          """,
        4: """
              ____________
             | /        
             |/        
             |         
             |          
             |         
             |
            _|_
           |_ _|  Tebaklah kata sifatnya!
          """,
        5: """
             |        
             |       
             |         
             |          
             |         
             |
            _|_
           |_ _|  Tebaklah kata sifatnya!
          """,
      }

    def kata_tebakan(kata):
      kalimat = random.choice(kata)  #digunakan untuk mengacak sebuah kata dari suatu daftar kata
      while "-" in kalimat or " " in kalimat:
        kalimat = random.choice(kata)

      return kalimat.upper()

    def hangman():
      kalimat = kata_tebakan(kata)
      huruf = set(kalimat) #huruf dalam kata
      alfabet = set(string.ascii_uppercase)
      huruf_pengguna = set() #huruf yg sudah ditebak oleh pengguna
      nyawa = 5

      #input dari pengguna
      while len(huruf) > 0 and nyawa > 0:
        #huruf yg digunakan
        #" ".join(["a", "b", "cd"]) --> "a b cd"
        print("km mempunyai", nyawa, "kesempatan yg tersisa dan huruf yg sudah km tebak adalah huruf", huruf_pengguna)

        #arah dari pemasukan kata misal C _ N T I K
        daftar_huruf = [letter if letter in huruf_pengguna else "_" for letter in kalimat]
        print(kesempatan[nyawa])
        print("Kata saat ini: ", " ".join(daftar_huruf))

        huruf_dipakai = input("Masukkan 1 huruf yg km tebak: ").upper()
        if huruf_dipakai in alfabet - huruf_pengguna:
          huruf_pengguna.add(huruf_dipakai)
          if huruf_dipakai in huruf:
            huruf.remove(huruf_dipakai)
            print(" ")

          else:
            nyawa = nyawa - 1 #mengurangi nyawa jika salah
            print("huruf, ", huruf_dipakai, "tidak ada dalam kata")

        elif huruf_dipakai in huruf_pengguna:
          print("km sudah menggunakan huruf itu, masukkan huruf tebakan yg lain")

        else:
          print("Huruf yg km tebak tidak ada dalam kata tebakan")
                    
      #saat nyawa sudah habis atau saat berhasil menebak kata
      if nyawa == 0:
        print(kesempatan[nyawa])
        print("Maaf, km kalah:( \nKata yg benar adalah", kalimat)
        hangmanlagi()
      else:
        print("Yeayy km menang, km berhasil menebak kata", kalimat)
        hangmanlagi()

    def hangmanlagi():
        lagi = input("\nApakah mau main hangman lagi? (y/n): ")
        while(lagi != "y" and lagi != "n"):
            lagi = input("\nMaaf inputan anda tidak ada di opsi \nMau main hangman lagi?: ")
        
        if lagi == "y":
            print("\nHayyuk main lagii \n")
            GameHangman() 
        elif lagi == "n":
            print("\nThank youu uda main hangman \n")
        return
        kembali()
    
    if __name__ == "__main__":
      hangman()
      break
        
kembali()
