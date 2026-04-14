# lap_timer_client.py
# Programa cliente que lee tiempos de vuelta de un archivo
# e imprime la racha decreciente mas larga.

import lap_timer


def main():
     
    filename = input()
    f = open(filename, "r")
    n = int(f.readline().strip())
    timer = lap_timer.init(n)

   
    


if __name__ == "__main__":
    main()
