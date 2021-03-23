from time import sleep


class TrafficLight:
    __color = ['\033[41m  STOP  \033[0m', '\033[43m  Ready \033[0m', '\033[42m   GO   \033[0m']

    def running(self):
        i = 0
        while i != 3:
            print(TrafficLight.__color[i])
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(2)
            elif i == 2:
                sleep(5)
            i += 1


t = TrafficLight()
t.running()
