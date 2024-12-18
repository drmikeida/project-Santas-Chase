import pyxel

class App:
    def __init__(self):
        # Initialize the Pyxel window (width, height)
        pyxel.init(160, 120)

        self.my_resource = pyxel.load("my_resource.pyxres")
        
        self.my_resource_x = 80
        self.my_resource_y = 60
        self.my_resource_dx = 1
        self.my_resource_dy = 1
        self.my_resource_sx = 70
        self.my_resource_sy = 70

        self.score = 0
        
        # Start the game loop
        pyxel.run(self.update, self.draw)

    def update(self):
        # Update Santa's position based on arrow keys
        if pyxel.btn(pyxel.KEY_UP):
            self.my_resource_sy -= 2
        if pyxel.btn(pyxel.KEY_DOWN):
            self.my_resource_sy += 2
        if pyxel.btn(pyxel.KEY_LEFT):
            self.my_resource_sx -= 2
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.my_resource_sx += 2

        # Update present1's position
        self.my_resource_x += self.my_resource_dx
        self.my_resource_y += self.my_resource_dy

        # Bounce present1
        if self.my_resource_x <= 0 or self.my_resource_x >= 146:
            self.my_resource_dx *= -1
        if self.my_resource_y <= 0 or self.my_resource_y >= 106:
            self.my_resource_dy *= -1

        if abs(self.my_resource_x - self.my_resource_sx) <= 5 and abs(self.my_resource_y - self.my_resource_sy) <= 5:
            self.score += 1
            
    def draw(self):
        # Clear the screen with color 16
        pyxel.cls(14)

        pyxel.text(5, 5, f"Score: {self.score}", 7)
        pyxel.blt(self.my_resource_x, self.my_resource_y, 0, 0, 0, 16, 16, 0)
        pyxel.blt(self.my_resource_sx, self.my_resource_sy, 1, 0, 0, 16, 16, 0 )


# Run the game
App()