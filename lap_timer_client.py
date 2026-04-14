# lap_timer_client.py
# Programa cliente que lee tiempos de vuelta de un archivo
# e imprime la racha decreciente mas larga.

import lap_timer


def main():
     
    filename = input()
    f = open(filename, "r")
    n = int(f.readline().strip())
    timer = lap_timer.init(n)

    for _ in range(n):
        time = float(f.readline().strip())
        timer = lap_timer.add_lap(timer, time)

    f.close()

   
    print(lap_timer.longest_decreasing_streak(timer))

if __name__ == "__main__":
    main()
