import random

import matplotlib.pyplot as plt
from numpy import arange


class SinglePlayerRuin:
    def __init__(self, capital, possibility, max):
        self.capital = capital
        self.possibility = possibility
        self.max = max

    def calculate(self):
        while 0 < self.capital < self.max:
            if decision(self.possibility):
                self.capital = self.capital + 1
            else:
                self.capital = self.capital - 1
        return self.capital == self.max

    def calculate_length_of_game(self):
        length = 0
        while 0 < self.capital < self.max:
            length = length + 1
            if decision(self.possibility):
                self.capital = self.capital + 1
            else:
                self.capital = self.capital - 1
        return length


# B
class TestMultipleGames:

    def same_capital_progressive_probability(self, capital, amount):
        probabilities = arange(0.05, 1.00, 0.05)
        losses = []
        for probabilityCount in range(0, probabilities.size):
            losses.append(0)
            for game in range(0, 100, 1):
                if not SinglePlayerRuin(capital, probabilities[probabilityCount], amount).calculate():
                    losses[probabilityCount] += 1
        result = list(map(lambda x: x / 100, losses))
        # print(list(result))
        # print(probabilities)
        analitic = list(map(lambda x: cal(x, capital, amount), probabilities))
        print(analitic)
        plt.figure()
        plt.bar(probabilities, result, width=0.02)
        plt.bar(list(map(lambda x: x + 0.02, probabilities)), analitic, width=0.02)
        plt.xlabel('prawdopodobieństwo wygrania w jednej grze')
        plt.ylabel('prawdopodobieństwo przegrania całości')
        plt.show()

    # C
    def progressive_capital_same_probability(self):
        losses = []
        capitalRange = list(range(0, 100))
        for capital in capitalRange:
            losses.append(0)
            for game in range(0, 100, 1):
                if not SinglePlayerRuin(capital, 0.5, 100).calculate():
                    losses[capital] += 1
        result = list(map(lambda x: x / 100, losses))
        #print(capitalRange)
        analitic = list(map(lambda x: cal_for_same_probability(x, 100), capitalRange))
        #print(capitalRange)
        #print(result)
        plt.figure()
        plt.bar(capitalRange, result, width=0.5)
        plt.bar(list(map(lambda x: x + 0.5, capitalRange)), analitic, width=0.5)
        plt.xlabel('kapitał')
        plt.ylabel('prawdopodobieństwo przegrania całości')
        plt.show()

    # D
    def length_of_rounds_to_end(self, capital, probability, amount):
        lengths = []
        repeats = []
        games = 1000
        sum_of_all_rounds = 0
        for i in range(0, games, 1):
            length_of_game = SinglePlayerRuin(capital, probability, amount).calculate_length_of_game()
            sum_of_all_rounds = sum_of_all_rounds + length_of_game
            if length_of_game in lengths:
                index = lengths.index(length_of_game)
                repeats[index] = repeats[index] + 1
            else:
                lengths.append(length_of_game)
                repeats.append(1)
        avg = sum_of_all_rounds / games
        probabilities = list(map(lambda x: x / 1000, repeats))
        print(lengths)
        print(probabilities)
        plt.figure()
        plt.bar(lengths, probabilities)
        plt.xlabel('Liczba rund')
        plt.ylabel('Prawdopodobieństwo długości rozgrywki')
        plt.title('PRW A ' + str(probability) + ' Średnia liczba rund = ' + str(avg))
        plt.show()

    # E
    def maximum_length_of_game_with_probability(self, capital, probability, amount):
        max_length = 0
        for game in range(0, 1000):
            length = SinglePlayerRuin(capital, probability, amount).calculate_length_of_game()
            if length > max_length:
                max_length = length
        return max_length

    def maximum_length_of_game_with_progressive_probability(self, capital, amount):
        probabilities = arange(0.00, 1.05, 0.05)
        length = []
        for probabilityCount in range(0, probabilities.size):
            length.append(0)
            for game in range(0, 100, 1):
                length[probabilityCount] = SinglePlayerRuin(capital, probabilities[probabilityCount],
                                                            amount).calculate_length_of_game()
        print(length)
        print(probabilities)
        plt.figure()
        plt.bar(probabilities, length, width=0.01)
        plt.xlabel('prawdopodobieństwo wygrania w jednej grze')
        plt.ylabel('długość rozgrywki')
        plt.show()

    # F do skonczenia
    def probability_of_capital_at_step(self, capital, probability, amount):
        games = []
        capital_copy = capital
        for i in range(0, 1000, 1):
            capital = capital_copy
            round = -1
            while 0 < capital < amount:
                round = round + 1
                if decision(probability):
                    capital = capital + 1
                else:
                    capital = capital - 1
                if len(games) <= i:
                    games.append([])
                if len(games[i]) <= round:
                    games[i].append([])
                games[i][round] = capital
        print(games)

    # G
    def trajectory(self, capital, probability, amount, games):
        capital_copy = capital
        plt.figure()
        for i in range(0, games, 1):
            wins = []
            capital = capital_copy
            round = -1
            while 0 < capital < amount:
                round = round + 1
                if len(wins) <= round:
                    if round == 0:
                        wins.append(0)
                    else:
                        wins.append(wins[round - 1])
                if decision(probability):
                    capital = capital + 1
                    wins[round] = wins[round] + 1
                else:
                    capital = capital - 1
            plt.plot(range(0, len(wins), 1), wins)

        plt.title('Capital: ' + str(capital_copy) + ' probability ' + str(probability) + ' amount ' + str(amount))
        plt.xlabel("single game number")
        plt.ylabel("cumulative wins")
        plt.show()


def decision(probability):
    return random.random() < probability


def cal(p, capital, amount):
    if p == 0.5:
        return cal_for_same_probability(capital, amount)
    else:
        return cal_for_diff_probability(p, capital, amount)


def cal_for_same_probability(capital, amount):
    return 1 - capital / amount


def cal_for_diff_probability(p, capital, amount):
    q = 1 - p
    prop = q / p
    return (prop ** capital - prop ** amount) / (1 - (prop ** amount))


if __name__ == "__main__":
    # singleGame = SinglePlayerRuin(50, 1.0, 100)
    # print(singleGame.calculate())
    # B
    # TestMultipleGames().same_capital_progressive_probability(50,100)
    # B porownanie
    TestMultipleGames().same_capital_progressive_probability(20, 100)
    TestMultipleGames().same_capital_progressive_probability(50, 100)
    TestMultipleGames().same_capital_progressive_probability(70, 100)
# print(cal_for_diff_probability(0.2, 50, 100))
# print(cal_for_same_probability(60, 100))
# C
# TestMultipleGames().progressive_capital_same_probability()
# D
# TestMultipleGames().length_of_rounds_to_end(50, 0.8, 100)
# E
# TestMultipleGames().maximum_length_of_game_with_progressive_probability(50, 100)
# F
# TestMultipleGames().probability_of_capital_at_step(50, 0.2, 100)
# G
# TestMultipleGames().trajectory(50, 0.5, 100, 2)
