from matplotlib import pyplot as plt
from math import factorial
n_exams =6 # напишите ваш код здесь: сколько экзаменов надо сдать?
failure_rate =15  # напишите ваш код здесь: какова вероятность завалить один экзамен?
distr = [] # создайте список distr, в котором будете хранить значения распределения
p=0.9
q=0.1
Q=0
for k in range(1, n_exams + 1):
    failure_rate=int(failure_rate/100)
    choose = factorial(n_exams) / (factorial(failure_rate) * factorial(n_exams - failure_rate))

    prob = choose* p **(k*1)* q**(k * (1-failure_rate)*(n_exams-failure_rate))
    Q=1-prob
    distr.append(Q)
# построение гистограммы распределения вероятностей
#plt.bar(range(1, n_exams+1), distr)
#print(plt.bar(range(0, n_exams + 1), distr))
print(plt.bar(range(1, n_exams+1), distr))
print(distr)
      
