import random
# ----------------------------
def new_game():
    
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("")
        print(key)
        print("")
        for i in options[question_num-1]:
            print(i)
        guess = input("Jawab (A, B, atau C): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key),guess)
        question_num += 1

        print(correct_guesses)

    display_score(correct_guesses, guesses)

# ----------------------------

def check_answer(answer, guess):
    
    if answer == guess:
        print(f"Jawaban {guess} BENAR") 
        return 1
    else:
        print(f"Jawaban {guess} SALAH")
        return 0
       
# ----------------------------

def display_score(correct_guesses, guesses):
    print("-------------------------")
    print("HASIL : ")
    print("-------------------------")

    print("Jawaban Benar: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Jawaban Anda: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Nilai anda adalah : " + str(score)+ "%")

# ----------------------------

def play_again():
    
    response = input("Apakah anda mau mencoba lagi ? (y) atau (n): ")
    response = response.upper()

    if response == "Y":
        return True
    else:
        return False
# ----------------------------


questions = {
    "1. Apa hukum mempelajari tauhid ? " : "A",
    "2. Cara mencari berkah yang dibenarkan dari seorang yang shaleh adalah ? " : "C",
    "3. Mengimani adanya syafa'at di akhirat adalah ? " : "C",
    "4. Hukum mendatangi dukun/paranormal adalah ? " : "A",
    "5. Tumbal dengan sembeli seekor kerbau dan menanam kepalanya di sungai supaya tidak diganggu oleh jin penunggu sungai, ini termasuk ? " : "B"
}

options = [["   A. Wajib", "   B. Sunnah (dianjurkan)", "   C. Mubah (boleh)"],
          ["   A. Meminum bekas minumnya", "   B. Mengambil tanah kuburannya", "   C. Menuntut ilmu darinya"],
          ["   A. Syirik", "   B. Bid'ah", "   C. Wajib"],
          ["   A. Haram", "   B. Boleh bila memang perlu", "   C. Makruh"],
          ["   A. Syirik kecil", "   B. Syirik besar", "   C. Bid'ah"]]

new_game()

while play_again():
    new_game()

print("")

