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

lane4 = [1116.2,
1106.9,
1097.64,
1088.39,
1082.16,
1075.95,
1067.75,
977.62,
972.17,
967.74,
962.95,
957.97,
955.29,
950.99,
947.7,
944.44,
941.19,
938.02,
935.8,
932.6,
930.41
]


lane3 = [993.92,
985.48,
977.14,
968.86,
962.55,
956.26,
949.99,
933.01,
928.04,
924.07,
919.1,
915.12,
912.16,
908.2,
905.24,
902.28,
899.33,
896.41,
894.46,
891.51,
889.56
]

lane2=[874.91,
866.2,
857.6,
849.07,
842.55,
836.09,
829.73,
828.45,
823.06,
818.69,
813.37,
809.06,
805.79,
801.53,
798.29,
795.07,
791.86,
788.66,
786.52,
783.35,
781.19
]

lane1=[858.07,
849.31,
841.34,
834.07,
827.4,
821.27,
815.6,
810.36,
805.49,
800.96,
796.73,
792.77,
789.06,
785.57,
782.29,
779.2,
776.27,
773.51,
770.89,
768.41,
766.05
]

lane4_NOSCA=[1451.19,
1288.74,
1177.46,
1156.68,
1138.88
]

lane3_NOSCA=[1390.56,
1285.27,
1122.41,
1098.28,
1079.46
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
plt.title("T_PUSH=30 & M=120", x=0.5, y=1.03 , fontsize=30)
plt.xlabel("SPEED (km/h)", fontsize=20, labelpad=15)
plt.ylabel("DELAY (s)", fontsize=20, labelpad=20)
plt.ylim([700,2000])

plt.legend(loc="best", fontsize=22)

plt.show()