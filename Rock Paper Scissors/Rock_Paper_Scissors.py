import random
class Game():
    def __init__(self):
        self.options = {1: "Rock", 2: "Paper", 3: "Scissors"}
        self.file = None
        
    def computer_num(self):
        comp_num = random.randint(1, 3)
        computer = self.options[comp_num]
        print(computer)
        return comp_num

    def actually_the_game(self, comp_num, user_num):
        if comp_num == user_num:
            print("Draw!\n")
            return 2
        elif user_num - 1 == comp_num or user_num + 2 == comp_num:
            print("You win!\n")
            return 0
        else:
            print("You lose!\n")
            return 1

    def stats(self):
        self.check_for_stats_file()
        stats = self.file.readlines()
        self.file.close()
        if len(stats) == 0:
            self.create_new_csv()
            
        self.file = open("Stats.csv", "r")
        for line in self.file:
            temp_line = line.strip("\n")
            temp_line = temp_line.replace(",", " ")
            print(temp_line)
        self.file.close()

    def add_to_stats(self, comp_num, user_num, result):
        self.check_for_stats_file()
        stats = self.file.readlines()
        self.file.close()
        if len(stats) == 0:
            self.create_new_csv()
            
        stats = []
        self.file = open("Stats.csv", "r")
        for line in self.file:
            stat = line.split(",")
            stats.append(stat)
        self.file.close()
        
        prev_value = stats[result][1]
        prev_value = int(prev_value)
        new_value = prev_value + 1
        stats[result][1] = str(new_value)
        
        temp_store = stats[comp_num + 5][1]
        temp_store = int(temp_store) + 1
        stats[comp_num + 5][1] = str(temp_store)
        
        temp_store = stats[user_num + 2][1]
        temp_store = int(temp_store) + 1
        stats[user_num + 2][1] = str(temp_store)

        self.file = open("Stats.csv", "w")
        for stat in stats:
            new_stat = stat[0] + "," + str(stat[1]) + "," + stat[2]
            self.file.write(new_stat)
        self.file.close()

    def check_for_stats_file(self):
        try:
            self.file = open("Stats.csv", "r")
        except FileNotFoundError:
            self.create_new_csv()
            self.file = open("Stats.csv", "r")
            
    def choice(self):
        print("""1. Play game
2. View stats
3. Quit""")
        while True:
            try:
                user_choice = int(input("Enter a number: "))
                break
            except:
                print("You did not enter a number")
        return user_choice

    def user_input(self):
        cor_inp = False
        while cor_inp == False:
            user = input("Enter Rock, Paper or Scissors. ")
            user = user.title()
            user = user.strip()
            for option in self.options:
                if user == self.options[option]:
                    cor_inp = True
                    user_num = option
                    return user_num
            if cor_inp == False:
                print("You did not enter a valid input")

    def create_new_csv(self):
        stats = ("Wins:,", "Losses:,", "Draws:,", "User Rocks:,",
                 "User Papers:,", "User Sciccors:,", "Computer Rocks:,",
                 "Computer Papers:,", "Computer Sciccors:,")
        file = open("Stats.csv", "w")
        for stat in stats:
            file.write(stat + "0" + ",\n")
        file.close()
        
            
def main():
    while True:
        g = Game()
        user_choice = g.choice()
        if user_choice == 1:
            user_num = g.user_input()
            comp_num = g.computer_num()
            result = g.actually_the_game(comp_num, user_num)
            g.add_to_stats(comp_num, user_num, result)
        elif user_choice == 2:
            g.stats()
        elif user_choice == 3:
            break
        else:
            print("You did not enter a valid number")
        game = Game()
        print("\n")
main()
