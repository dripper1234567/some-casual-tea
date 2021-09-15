import sense_emu as sense_hat  # FOR USE IN EXTERNAL DEVELOPMENT
import Pyalog
import Advance

Sense = sense_hat.SenseHat()  # sense hat call name
Timer = Advance.AdTime(0.3)  # Calls in more methods
Vector2 = Advance.Vector2([0, 0])  # calls V2


def Main():
    MainLoop()


def MainLoop():
    global Timer
    global Sense
    global Vector2
    while True:
        for event in Sense.stick.get_events():
            Vector2.Set(event.direction)
            if Timer.DeltaTime():
                print(Vector2.X())


'''
    Pyalog()

sense.clear()
        sense.set_pixel(0, Clamp(vector2[0]), [255, 255, 255])
'''

if __name__ == "__main__":
    Main()
