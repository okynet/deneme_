MDK = {
      "CRINGE": "Garip ya da utandırıcı bir şey",
      "LOL": "Komik bir şeye verilen cevap",
      "NP": "problem yok/sorun yok"}
    
soru = input("hangi kelimeyi arıyorsun NOT:büyük harfle yaz")
if soru in MDK.keys():
    print(MDK[soru],"anlamı budur")
    
else:
    print("aradığınız kelime listede yok")
