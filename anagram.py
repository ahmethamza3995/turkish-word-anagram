import sqlite3
from collections import Counter

def are_anagrams(word1, word2):
    return Counter(word1) == Counter(word2)

con = sqlite3.connect("v12.gts.sqlite3.db")
cur = con.cursor()
cur.execute("SELECT madde FROM madde")

kelime = input("Anagramı kontrol edilecek kelimeyi giriniz: ").lower()

sozluk_kelimesi_bulundu = False
anagramlar = []
for row in cur.fetchall():
    sozluk_kelimesi = row[0].lower()
    if kelime == sozluk_kelimesi:
        sozluk_kelimesi_bulundu = True
    elif are_anagrams(kelime, sozluk_kelimesi) and sozluk_kelimesi not in anagramlar:
        anagramlar.append(sozluk_kelimesi)

if sozluk_kelimesi_bulundu:
    if anagramlar:
        print("Girdiğiniz kelimenin anagramları:")
        for anagram in anagramlar:
            print(anagram)
    else:
        print("Girdiğiniz kelimenin sözlükte anagramı bulunamadı.")
else:
    print("Girdiğiniz kelime sözlükte bulunamadı.")

con.close()
