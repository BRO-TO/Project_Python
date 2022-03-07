import csv
import random
import time

with open("Soal.csv","r") as user:
    user_csv = user.readlines()
    random.shuffle(user_csv)

#------------------------------------------------------------------------------------------------

def new_quiz():
    print("+-----------------------------------------------------------------------------------------------------------------------------------------------+")
    print("|                                                        Simulasi Ujian Harian HSI                                                              |")
    print("|                                                               Quiz Level 1                                                                    |")
    print("+-----------------------------------------------------------------------------------------------------------------------------------------------+")

    print("")
    nama = input("Masukkan nama anda : ")
    print("")
    
    correct_guesses = 0
   

    for i in range(2):
        x = user_csv[i].strip()
        data = x.split("#") 
        correctAnswer = data[4]
       
        print("")
        print(f"{i+1}) {data[0]}\n\n   A.{data[1]}\n\n   B.{data[2]}\n\n   C.{data[3]}")
        print("")
        answer = input("   Jawaban : ")
        print("")
        answer = answer.upper()
        correct_guesses  += checkAnswer(correctAnswer,answer, data[5])

    display_score(correct_guesses, 4, nama)

#------------------------------------------------------------------------------------------------
   
def checkAnswer(cAnswer, ans, d5):

        if (cAnswer != "" and cAnswer == ans):
            print("   BENAR")
            print("")
            print(">>> Jawaban yang benar : " + cAnswer + "." + " " + d5 + " <<<")
            print("")
            print("========================================================================")
            print("========================================================================")
            return 2  
        elif(cAnswer != "" and cAnswer != ans):
            print("   SALAH")
            print("")
            print(">>> Jawaban yang benar : " + cAnswer + "." + " " + d5 + " <<<")
            print("")
            print("========================================================================")
            print("========================================================================")
            return -1
        else:
            print("Waktu anda habis")

#------------------------------------------------------------------------------------------------

def display_score(correct_guesses, totalPoint, nama):
    
    print("-------------------------")
    print("          HASIL          ")
    print("-------------------------")

    if correct_guesses == -2:
        print("")
        print("Total Jawaban Benar Anda: " + str(0))
        print("")
        score = int((0/totalPoint)*100)
        return print("Nilai anda adalah : " + str(score)+ "%" +"," + f" Maaf saudara {nama} belum lulus")
    else:
        print("")
        print("Total Jawaban Benar Anda: " + str(correct_guesses))
        print("")
        score = int((correct_guesses/totalPoint)*100)
        return print("Nilai anda adalah : " + str(score)+ "%" + "," + f" Selamat saudara {nama} lulus")

#------------------------------------------------------------------------------------------------

      
# def simulasi():

#     t = 240

#     while t:
#         mins = t // 60
#         sec = t % 60
#         timer = '{:02d}:{:02d}'.format(mins, sec)
#         print(timer, end="\r")
#         time.sleep(1)
#         t -= 1

      
# simulasi()
new_quiz()





   


    
    


   
   