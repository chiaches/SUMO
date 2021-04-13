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

lane4 = [489.7,
481.03,
472.53,
464.09,
457.65,
451.6,
445.35,
434.6,
429.42,
425.27,
419.66,
416.04,
412.43,
408.36,
405.29,
402.23,
399.18,
396.14,
394.11,
391.12,
389.11
]

lane3 = [459.26,
451.19,
443.2,
435.19,
429.23,
423.24,
417.28,
408.17,
403.17,
399.16,
394.16,
390.15,
387.14,
383.14,
380.14,
377.14,
374.14,
371.14,
369.14,
366.17,
364.17
]

lane2 = [404.4,
394.93,
385.52,
377.15,
369.84,
363.53,
356.63,
358.03,
352.78,
347.56,
342.33,
338.21,
333.97,
328.87,
325.71,
322.58,
319.46,
316.36,
314.23,
310.17,
308.06
]

lane1 = [394.07,
385.31,
377.34,
370.07,
363.4,
357.27,
351.6,
346.36,
341.49,
336.96,
332.73,
328.77,
325.06,
321.57,
318.29,
315.2,
312.27,
309.51,
306.89,
304.41,
302.05
]

lane4_NOSCA=[641.84,
508.87,
477.23,
460.68,
448.95,
]

lane3_NOSCA=[581.81,
453.51,
421.37,
402.28,
396.19
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
plt.title("T_PUSH=30 & M=40", x=0.5, y=1.03 , fontsize=30)
plt.xlabel("SPEED (km/h)", fontsize=20, labelpad=15)
plt.ylabel("DELAY (s)", fontsize=20, labelpad=20)
plt.ylim([250,1000])

plt.legend(loc="best", fontsize=22)

plt.show()

