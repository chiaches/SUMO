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

SPEED_NOSCA = [40,
50,
60,
70,
80
]

values = ['40','42','44','46','48', '50','52','54','56','58', '60', '62', '64', '66', '68', '70','72','74','76','78', '80']

lane4 = [1800.28,
1791.31,
1782.37,
1773.43,
1767.49,
1761.55,
1753.61,
1587.85,
1582.74,
1577.64,
1572.55,
1567.47,
1563.39,
1559.31,
1556.24,
1553.18,
1550.12,
1546.07,
1544.02,
1540.97,
1538.93
]


lane3 = [1584.39,
1575.16,
1567,
1557.82,
1551.63,
1545.46,
1538.3,
1457.34,
1452.32,
1448.29,
1443.28,
1439.26,
1436.26,
1432.26,
1429.26,
1426.26,
1423.27,
1420.28,
1418.33,
1415.34,
1413.36
]

lane2=[1322.07,
1313.31,
1305.34,
1298.07,
1291.4,
1285.27,
1279.6,
1274.36,
1269.49,
1264.96,
1260.73,
1256.77,
1253.06,
1249.57,
1246.29,
1243.2,
1240.27,
1237.51,
1234.89,
1232.41,
1230.05
]

lane1=[
1322.07,
1313.31,
1305.34,
1298.07,
1291.4,
1285.27,
1279.6,
1274.36,
1269.49,
1264.96,
1260.73,
1256.77,
1253.06,
1249.57,
1249.29,
1243.2,
1240.27,
1237.51,
1234.89,
1232.41,
1230.05
]

lane4_NOSCA=[2258.16,
2001.61,
1965.8,
1852.68,
1820.08
]

lane3_NOSCA=[2198.22,
1942.81,
1906.05,
1794.28,
1780.16
]

plt.figure(figsize=(25, 15), dpi=100, linewidth=2)

plt.xticks(SPEED,values, fontsize=18)
plt.yticks(fontsize=18)

plt.plot(SPEED_NOSCA, lane4_NOSCA, 's--', color='b', label="Lane4 without SCA")
plt.plot(SPEED_NOSCA, lane3_NOSCA, 'o--', color='r', label="Lane3 without SCA" )
plt.plot(SPEED, lane4, 's-', color='b', label="Lane4 with SCA" )
plt.plot(SPEED, lane3, 'o-', color='r', label="Lane3 with SCA" )
plt.plot(SPEED, lane2, '^-', color='y', label="Lane2 with SCA" )
plt.plot(SPEED, lane1, '*-', color='g', label="Lane1 with SCA" )

x_major_locator=MultipleLocator(10)
plt.title("T_PUSH=30 & M=200", x=0.5, y=1.03 , fontsize=30)
plt.xlabel("SPEED (km/h)", fontsize=20, labelpad=15)
plt.ylabel("DELAY (s)", fontsize=20, labelpad=20)
plt.ylim([1100,2900])

plt.legend(loc="best", fontsize=22)

plt.show()

