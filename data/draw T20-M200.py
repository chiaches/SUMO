import matplotlib.pyplot as plt

from matplotlib.pyplot import MultipleLocator

SPEED = [40,
42,
44,
46,
48,
50,
52,
54,
56,
58,
60,
62,
64,
66,
68,
70,
72,
74,
76,
78,
80
]

values = ['40','42','44','46','48', '50','52','54','56','58', '60', '62', '64', '66', '68', '70','72','74','76','78', '80']

lane4 = [2007.28,
1963.31,
1990.93,
1981.92,
1877.92,
1871.91,
1865.92,
1781.19,
1776.17,
1771.16,
1722.15,
1717.15,
1696.99,
1661.15,
1641.03,
1638.05,
1606.19,
1601.2,
1601.22,
1596.25,
1591.27
]


lane3 = [1719.32,
1674.02,
1709.8,
1701.64,
1602.55,
1596.41,
1590.28,
1535.17,
1530.06,
1525.95,
1476.89,
1471.81,
1461.72,
1416.68,
1409.62,
1406.55,
1400.46,
1364.49,
1362.36,
1359.23,
1349.31
]

lane2 = [
1138.35,
1130.64,
1120.9,
1112.61,
1109.8,
1103.46,
1097.17,
1092.49,
1087.26,
1083,
1078.94,
1073.81,
1065.48,
1066.29,
1064.68,
1061.54,
1056.56,
1052.55,
1051.32,
1047.36,
1043.44
]

lane1 = [1132.07,
1123.31,
1115.34,
1108.07,
1101.4,
1095.27,
1089.6,
1084.36,
1079.49,
1074.96,
1070.73,
1066.67,
1063.06,
1059.57,
1059.29,
1053.2,
1050.27,
1047.51,
1044.89,
1042.41,
1040.05
]

plt.figure(figsize=(25, 15), dpi=100, linewidth=2)

plt.xticks(SPEED,values, fontsize=18)
plt.yticks(fontsize=18)

plt.plot(SPEED, lane4, 's-', color='b', label="Lane4 with SCA" )
plt.plot(SPEED, lane3, 'o-', color='r', label="Lane3 with SCA" )
plt.plot(SPEED, lane2, '^-', color='y', label="Lane2 with SCA" )
plt.plot(SPEED, lane1, '*-', color='g', label="Lane1 with SCA" )

x_major_locator=MultipleLocator(10)
plt.title("T_PUSH=20 & M=200", x=0.5, y=1.03 , fontsize=30)
plt.xlabel("SPEED (km/h)", fontsize=20, labelpad=15)
plt.ylabel("DELAY (s)", fontsize=20, labelpad=20)
plt.ylim([800,2300])

plt.legend(loc="best", fontsize=22)

plt.show()


