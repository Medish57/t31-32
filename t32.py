class Footbalist:
    def __init__(self, first_name, last_name, number, height, weight):
        self.first_name = first_name
        self.last_name = last_name
        self.number = number
        self.height = height
        self.weight = weight

    def player_first_name(self):
        return 'The player first name: ' + self.first_name
    
    def player_number(self):
        return 'The ' + str(self.first_name) + ' ' + str(self.last_name) + ' number is ' + str(self.number)

class Goalkeeper(Footbalist):
    pass

class Defenders(Footbalist):
    pass

# ایجاد بازیکنان
player_1 = Footbalist('Ali', 'Hasani', 8, 186, 91)
player_2 = Goalkeeper('Ahmad', 'Nameni', 5, 189, 24)
player_6 = Defenders('Ebrahim', 'Alipoor', 1, 177, 76)

# نمایش اطلاعات
print(player_1.player_first_name())
print(player_1.player_number())