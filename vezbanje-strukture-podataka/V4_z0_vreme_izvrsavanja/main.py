#kada pokrecem u terminalu moram navesti putanju do fajla(kao u c++)
# cd .\(copy realite path od foldera)
##moze sve da se pozove i u konzoli sa pprofile .\main.py

for i in range(1000):
    rez = i**2
    print(rez)

rez = None
print(rez)



#T(n) -- ukupno vreme izvrsavanja... racunamo max() od dva bloka.. npr. if se izvrsi n2, else se izvrsi n + 2 puta -- T(n) = n2 ...jer se gleda najgori slucaj... kod if i else gledamo samo sta je u telu i to brojimo
#O(n)  -- maksimalno vreme izvrsavanja, tj. posmatramo kao limes, ako imamo uz n, npr. n + nesto... to nesto ne gledamo
#posmatramo samo najveci eksponent(stepen) uz n, i 2n**2 -- 2 se takodje ignorise i tu posmatramo samo n**2
#kod O(n) = 2n**2 + 3n + 1 --- O(n) = n**2
#return naredba se ne racuna

#do 4 poglavlja u knjizi(bez njega)