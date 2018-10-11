# To jest komentarz :D, tego komputer nie czyta
# Typu podstawowe w Pythonie (są 4)
# String's (ciągi znaków) i odrazu zmienne
owca1 = 'To jest napis'
owca2 = "i to tez jest napis"
# operacje na napisach i wpisywanie do konsoli 
# napisy można łączyć
print("napis" + "napis")
# zwracanie długoci napisu
len("napis napis napis")
# wybieranie czesci napisu
owca1[0:5] # wyciągnie kawałek napisu od 1 znaku do 4 znaku
print(owca1[0:5])
# liczby
# Są dwa typy -> całkowite(int) oraz rzeczywiste(float) np 1.5 lub 1.(3)
7 + 7.5 # To zadziała
# Uwaga
"7" + 7 #Error
print("1" + str(7)) # Zamieni liczbę 7 na napis -> zwróci napis 17
print("1",7) # To zadziała bez funkcji str
# Przydatne operacje na liczbach
2**5 # 32 -> 2 do 5
2e2 # 200 -> 2 * (10 do 2)
2e-1 # 2 * (10 do -1) czyli 1/5
# Typ Boolean prawda fałsz
owcaPrawda = True
owcaFałsz = False