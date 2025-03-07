import pandas as pd
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier 
from sklearn.metrics import accuracy_score

df = pd.read_excel("karar_agaci_veri_100.xlsx")

X = df[["Yas","Kan_Basinci","Kolesterol"]]
y = df["Hastalik"]

classifier = DecisionTreeClassifier(max_depth=1, min_samples_split=2,min_samples_leaf=2)
classifier.fit(X,y) 


#Eksik veri kontrolü
if  df.isnull().sum().sum() > 0:
    print("Veri kümesinde eksik değerler var!!!")


def kullanici_girisi():
    print("Lütfen tahmin için aşağıdaki bilgileri giriniz:")
    yas = int(input("Yas: "))
    kan_basinci = float(input("Kan Basıncı: "))
    kolesterol = float(input("Kolesterol: "))

    return pd.DataFrame([[yas,kan_basinci,kolesterol]], columns=["Yas","Kan_Basinci","Kolesterol"])


yeni_veri = kullanici_girisi()
tahmin = classifier.predict(yeni_veri)


#tahmin sonucunu kullanıcıya göster

if tahmin[0] == 1:
    print("Tahmin: Hastalık Var")
else:
    print("Tahmin: Hastalık Yok")