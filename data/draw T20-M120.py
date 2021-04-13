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

lane4 = [1254.28,
1235.75,
1277.88,
1269.87,
1208.85,
1202.85,
1196.85,
1149.85,
1144.85,
1139.85,
1095.87,
1090.87,
1082.86,
1070.85,
1032.87,
1029.87,
1024.87,
1020.87,
1019.87,
1015.87,
1011.87
]

lane3 = [1102.64,
1085.28,
1080.7,
1072.59,
1018.45,
1012.31,
1006.19,
959.17,
954.06,
949.95,
938.78,
934.7,
893.73,
886.68,
880.59,
877.52,
872.46,
867.28,
867.36,
862.19,
833.45
]

lane2=[740.87,
744.92,
736.9,
728.61,
725.4,
719.07,
712.75,
709.61,
704.36,
699.16,
692.1,
687.91,
681.48,
675.57,
672.91,
669.81,
675.37,
672.27,
670.12,
667.06,
664.02
]

lane1=[
748.07,
739.31,
731.34,
724.07,
717.4,
711.27,
705.6,
700.36,
695.49,
690.96,
686.73,
682.77,
679.06,
675.57,
672.29,
669.2,
666.27,
663.51,
660.89,
658.41,
656.05
]

lane4_NOSCA=[1825.38,
1786.48,
1478.3,
1267.73,
1192.28]

lane3_NOSCA=[1778.88,
1739.14,
1431,
1219.54,
1141.2,]

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
plt.title("T_PUSH=20 & M=120", x=0.5, y=1.03 , fontsize=30)
plt.xlabel("SPEED (km/h)", fontsize=20, labelpad=15)
plt.ylabel("DELAY (s)", fontsize=20, labelpad=20)
plt.ylim([500,2600])

plt.legend(loc="best", fontsize=22)

plt.show()