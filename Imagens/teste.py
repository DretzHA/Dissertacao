import math
import matplotlib.pyplot  as plt
import pandas as pd
import numpy as np


# ######################################################################################
# #results cAse I

fig, ax = plt.subplots()
metodos = ['2019', '2020', '2021', '2022', '2023', '2024*', '2025*', '2026*', '2027*', '2028*', '2029*', '2030*'] 
resultados = [8.6, 9.76, 11.28, 13.14, 15.14, 17.08, 19.08, 21.09, 23.14, 25.21, 27.31, 29.42]
bar_colors = ['tab:blue' ]
bar_labels = ['2019', '2020', '2021', '2022', '2023', '2024*', '2025*', '2026*', '2027*', '2028*', '2029*', '2030*']
plt.xticks(range(len(metodos)),('2019', '2020', '2021', '2022', '2023', '2024*', '2025*', '2026*', '2027*', '2028*', '2029*', '2030*'), fontsize=11)
ax.bar(metodos, resultados, label=bar_labels, color=bar_colors)
for i in range (len(metodos)):
    plt.text(i, resultados[i]//2, (resultados[i]), ha = 'center')

plt.plot(metodos, resultados, 'k', linewidth=2.0)
ax.set_ylabel('Número de dispositivos IoT, em bilhões.', fontsize=12)

plt.show()


# #Results Case-II
# fig, ax = plt.subplots()
# metodos = ['MLT', 'MLT+KF', 'AoA+RSSI', 'AoA+RSSI+KF', 'AoA', 'AoA+KF', 'ARFL']
# resultados = [360.83, 337.07, 145.04, 130.31, 68.05, 64.97, 60.00]
# bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:blue', 'tab:red', 'tab:blue', 'tab:green' ]
# bar_labels = ['Without Filter', 'With KF', '_Without Filter', '_White KF' ,'_Without Filter', '_KF', 'ARFL']
# plt.xticks(range(len(metodos)),('MLT', 'MLT+KF', 'AoA+RSSI', 'AoA+RSSI+KF', 'AoA', 'AoA+KF', 'ARFL'), rotation=30)
# ax.bar(metodos, resultados, label=bar_labels, color=bar_colors)
# for i in range (len(metodos)):
#     plt.text(i, resultados[i]//2, int(resultados[i]), ha = 'center')

# plt.plot(metodos, resultados, 'k', linewidth=2.0)
# ax.set_ylabel('Distance Error (cm)')
# ax.set_title('Distance Error x Method')
# ax.legend(title='Method')

# plt.show()

