from random import random

#직관적인 답 

mine =input("가위 바위 보 중 하나를 선택하시오.")
com = ""
result = ""

rnd = random()
if rnd > 0.66 :
    com = "가위"
elif rnd > 0.33 :
    com ="바위"
else :
    com ="보"
    
if com == "가위" and mine == "가위" : result = "비김"
if com == "가위" and mine == "바위" : result = "이김"
if com == "가위" and mine == "보" : result = "짐"

if com == "바위" and mine == "가위" : result = "짐"
if com == "바위" and mine == "바위" : result = "비김"
if com == "바위" and mine == "보" : result = "이김"
 
if com == "보" and mine == "가위" : result = "이김"
if com == "보" and mine == "바위" : result = "짐"
if com == "보" and mine == "보" : result = "비김"

print("나: ",mine)
print("컴: ",com)
