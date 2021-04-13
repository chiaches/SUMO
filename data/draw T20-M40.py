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

lane4 = [535.12,
525.97,
515.77,
507.64,
494.19,
488.16,
482.13,
471.11,
466.09,
462.08,
429.42,
424.38,
420.34,
416.31,
411.29,
408.27,
404.26,
401.25,
399.24,
396.24,
393.25
]


lane3 = [473.77,
463.71,
418.8,
410.64,
402.55,
396.41,
390.28,
383.17,
378.06,
373.95,
368.86,
363.8,
359.73,
355.65,
350.58,
347.52,
344.46,
341.41,
339.36,
336.31,
333.3
]

lane2=[
365.86,
357.4,
352.92,
344.61,
337.99,
331.66,
325.2,
319.91,
314.96,
310.42,
305.31,
301.14,
297.48,
293.41,
288.29,
285.2,
282.27,
279.51,
276.89,
274.41,
272.05,
]

lane1=[
364.07,
355.31,
347.34,
340.07,
333.4,
327.27,
321.6,
316.36,
311.49,
306.96,
302.73,
298.77,
295.06,
291.57,
288.29,
285.2,
282.27,
279.51,
276.89,
274.41,
272.05
]

lane4_NOSCA=[761.84,
723.54,
605.7,
499.33,
482.34
]

lane3_NOSCA=[713.55,
674.87,
558.04,
450.94,
436.15
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
plt.title("T_PUSH=20 & M=40", x=0.5, y=1.03 , fontsize=30)
plt.xlabel("SPEED (km/h)", fontsize=20, labelpad=15)
plt.ylabel("DELAY (s)", fontsize=20, labelpad=20)
plt.ylim([200,1200])

plt.legend(loc="best", fontsize=22)

plt.show()





