import random

answerq = ("Absolutely!", "No way Pedro!", "Go for it tiger.", "sure", "nah")
choice = random.randint(0, len(answerq)-1)
answer = answerq[choice]
input("""
Welcome to the Magic 8 Ball game.
Ask me for any advice and I’ll help you out.
Type in your question and then press Enter for an answer.
> """)
print("shaking.... \n" * 4)
print(answer)
exit(0)
