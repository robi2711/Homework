import lib as m
lotto = m.fr("Task 3.csv")
lottoList = lotto.split("\n")
lottoList.sort()
f1, f2 = m.freq(lottoList)
