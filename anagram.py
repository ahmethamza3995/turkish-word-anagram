import sqlite3
from collections import Counter

def are_anagrams(word1, word2):
    
    return Counter(word1) == Counter(word2)

con = sqlite3.connect("v12.gts.sqlite3.db")
cur = con.cursor()
cur.execute("SELECT madde FROM madde")

kelime = input("Anagramı kontrol edilecek kelimeyi giriniz: ").lower()

anagramlar = []
for row in cur.fetchall():
    sozluk_kelimesi = row[0].lower()
    if kelime != sozluk_kelimesi and are_anagrams(kelime, sozluk_kelimesi):
        anagramlar.append(sozluk_kelimesi)

if anagramlar:
    print("Girdiğiniz kelimenin anagramları:")
    for anagram in anagramlar:
        print(anagram)
else:
    print("Girdiğiniz kelimenin anagramı sözlükte bulunamadı.")

con.close()
