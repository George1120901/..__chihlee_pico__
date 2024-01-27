from machine import Timer,Pin,ADC


def fun10(t:Timer | None = None):
    print('10秒了')
    led.toggle()
    
led = Pin(15, Pin.OUT)
light = ADC(Pin(28))
timer10 = Timer(period=10000, mode=Timer.PERIODIC, callback=fun10)
fun10()




while True:
    print(light.read_u16())
