import random


class GeneratingRandomness:
    def __init__(self):
        self.min_num = 100
        self.result_string = ''
        self.check = ["000", "001", "010", "011", "100", "101", "110", "111"]
        self.balance = 1000

    def take_input(self):
        list_collector = []
        while True:
            random_string = input('Print a random string containing 0 or 1:\n')

            for item in random_string:
                if item == '1' or item == '0':
                    list_collector.append(int(item))

            if len(list_collector) < self.min_num:
                print(f'Current data length is {len(list_collector)}, {self.min_num - len(list_collector)} symbols left')
                continue
            else:
                self.result_string = ''.join(str(k) for k in list_collector)
                print('Final data string:')
                print(self.result_string + '\n')
                break

    def calculate(self):
        string_list = [self.result_string[i:i + 4] for i in range(0, len(self.result_string))]
        res_dict = {}

        for triad_def in self.check:
            # set the default value to (0, 0)
            res_dict.setdefault(triad_def, (0, 0))

        for triad in string_list:
            if triad[:3] in self.check:
                if len(triad) == 4 and triad.endswith('0'):
                    result = (res_dict.get(triad[:3])[0] + 1, res_dict.get(triad[:3])[-1])
                    res_dict.update({triad[:3]: result})
                elif len(triad) == 4 and triad.endswith('1'):
                    result = (res_dict.get(triad[:3])[0], res_dict.get(triad[:3])[-1] + 1)
                    res_dict.update({triad[:3]: result})
        return res_dict

    def prediction(self):
        print("You have $1000. Every time the system successfully predicts your next press, you lose $1.")
        print("Otherwise, you earn $1. Print \"enough\" to leave the game. Let's go!")

        while True:
            entered_string = input('\nPrint a random string containing 0 or 1:\n\n')
            if entered_string.isnumeric():
                prediction_string = random.choice(self.check)

                for i in range(0, len(entered_string) - 3):
                    next_num = '0' if self.calculate().get(entered_string[0 + i:3 + i])[0] > \
                                      self.calculate().get(entered_string[0 + i:3 + i])[1] else '1'

                    prediction_string += next_num[0]
                self.calculate_accuracy(prediction_string, entered_string)
            elif entered_string == 'enough':
                print('Game over!')
                break
            else:
                continue

    def calculate_accuracy(self, prediction_string, entered_string):
        print(f'prediction:\n{prediction_string}\n')

        money = 0
        guessed_counter = 0
        for item in range(3, len(prediction_string)):
            if prediction_string[item] == entered_string[item]:
                guessed_counter += 1
                money += 1
            else:
                money -= 1

        guess_percentage = round(guessed_counter / (len(prediction_string) - 3) * 100, 2)
        self.balance = self.balance - money

        print(f'Computer guessed right {guessed_counter} out of {len(prediction_string) - 3} symbols ({guess_percentage} %)')
        print(f'Your balance is now ${self.balance}')
        return guess_percentage


if __name__ == '__main__':
    rand = GeneratingRandomness()
    rand.take_input()
    rand.prediction()
