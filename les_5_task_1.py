# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа)
# для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
from collections import *


class Firm:
    def __init__(self):
        self.firm_name = input(f'Введите название фирмы: ')
        self.q1_profit = float(input('Введите прибыль за 1 квартал: '))
        self.q2_profit = float(input('Введите прибыль за 2 квартал: '))
        self.q3_profit = float(input('Введите прибыль за 3 квартал: '))
        self.q4_profit = float(input('Введите прибыль за 4 квартал: '))
        self.year_profit = self.q1_profit + self.q2_profit + self.q3_profit + self.q4_profit

    def is_profitable(self, avg_profit_by_year: float) -> bool:
        return self.year_profit >= avg_profit_by_year

    def avgProfit(firms: deque) -> float:
        sum_profit = 0
        for firm in firms:
            sum_profit += firm.year_profit
        return sum_profit / len(firms)


    def get_profit_firm_names(firms: deque, avg_year_profit: float) -> list:
        profit_firm_names = []
        for firm in firms:
            if firm.is_profitable(avg_year_profit):
                profit_firm_names.append(firm.firm_name)
        return profit_firm_names

    def get_unprofit_firm_names(firms: deque, avg_year_profit: float) -> list:
        unprofit_firm_names = []
        for firm in firms:
            if not firm.is_profitable(avg_year_profit):
                unprofit_firm_names.append(firm.firm_name)
        return unprofit_firm_names


firm_cnt = int(input('Введите количество предприятий: '))

if firm_cnt < 1:
    print("До свидания")
    exit(0)
firms = deque()
for i in range(0, firm_cnt):
    firms.append(Firm())

avg_profit = Firm.avgProfit(firms)
print("Средняя прибыль по предприятиям: %f" % avg_profit)
print("Прибыльные фирмы: ", Firm.get_profit_firm_names(firms, avg_profit))
print("Убыточные фирмы: ", Firm.get_unprofit_firm_names(firms, avg_profit))
