import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import aseegg as ag

dane = pd.read_csv(r"C:\Users\Michal i Julia\Desktop\sygnaly3\dane.csv", delimiter=';', engine='python')
mojeDane = dane['Sub11']

czestProbkowania = 256

czestOdciecia1=49
czestOdciecia2=51
czestOdciecia3=3

przefiltrowany = ag.pasmowozaporowy(mojeDane, czestProbkowania, czestOdciecia1, czestOdciecia2)

ag.spektrogram(przefiltrowany, 256, show_plot=False)
plt.xlabel("t [s]")
plt.ylabel("f [Hz]")
plt.title("Ryc 1.  Sygnał po usunięciu zakłóceń o częstotliwości 50 Hz.")
plt.show()



przefiltrowany2 = ag.gornoprzepustowy(przefiltrowany, czestProbkowania, czestOdciecia3)
ag.spektrogram(przefiltrowany2, 256, show_plot=False)
plt.xlabel("t [s]")
plt.ylabel("f [Hz]")
plt.title("Ryc 2.  Sygnał po usunięciu składowych poniżej 3 Hz.")

plt.show()

ag.rysujFFT(przefiltrowany2[5*256:15*256])
