from game_controller import GameController

SPACE = {'width': 700, 'height': 750}

game_controller = GameController(SPACE, 6, 7)

def setup():
    size(SPACE['width'], SPACE['height'])
    colorMode(RGB, 1)


def draw():
    background(0.95)
    game_controller.update()


def mousePressed():
    if game_controller.playable:
        game_controller.show_disk(mouseX, mouseY)

def mouseDragged():
    if game_controller.playable:
        game_controller.show_disk(mouseX, mouseY)

def mouseReleased():
    if game_controller.playable:
        game_controller.drop_disk()
