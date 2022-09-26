from random import randrange

metiens = ""
metieni_kopa = 0
for _ in range(10):
    secigi_metieni = 1
    metieni = 0
    metiens = ""
    while secigi_metieni < 3:
        jaunais_metiens = randrange(0, 2)
        if jaunais_metiens == metiens:
            secigi_metieni += 1
        else:
            secigi_metieni = 1
        metiens = jaunais_metiens
        metiens_burts = "C" if jaunais_metiens == 0 else "Ģ"
        metieni += 1
        print(metiens_burts, end=" ")
    else:
        metieni_kopa += metieni
        print(metieni, " ")
        
print(metieni_kopa / 10)
