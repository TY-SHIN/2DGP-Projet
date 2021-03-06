from pico2d import *
import game_framework
import load_state
import main_state
import server


image = None

def enter():
    global image
    server.life = 3
    image = load_image('resource\\title.png')
    server.font = load_font('ENCR10B.TTF', int(32*main_state.window_height/600))
def handle_events():
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
        elif event.type == SDL_KEYDOWN:
                game_framework.change_state(load_state)

def exit():
    pass

def update():
    pass
def draw():
    w,h = main_state.window_width, main_state.window_height
    clear_canvas()

    image.clip_draw(0,0,256,240,w/2,h/2,w,h)
    server.font.draw(w/4,3*h/8,'press any key to start',(255,255,255))
    update_canvas()