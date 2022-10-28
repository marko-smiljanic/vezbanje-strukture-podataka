class Tacka2D:
    def __init__(self, x, y):
        super().__init__()     #trebalo bi se uvek pisati, jer kao u javi sto je svaka klasa nasledjivala object tako je i ovde
        self.x = x
        self.y = y

    def ispisi_koordinate(self):
        print("Tacka sa koordinatama x: {x}, y: {y}".format(x=self.x, y=self.y), end="")  #moze se i ovako raditi format ne mora po indeksiranju, end="" na kraju ispisa stavlja "" i ne prelazi u novi red
        