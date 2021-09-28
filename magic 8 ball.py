import random

answerq = ("Absolutely!", "No way Pedro!", "Go for it tiger.", "sure", "nah")
lenght = len(answerq)
print("""Welcome to the Magic 8 Ball game.
Use it to answer your questions...""")

question = input("""Ask me for any advice and I’ll help you out.
Type in your question and then press Enter for an answer.
 > """)

print("shaking.... \n" * 4)

choice=random.randint(0,lenght-1)
answer = answerq[choice]
print(answer)