from numpy import array

LIATconstVisual = ("10 mus", "30 mus", "100 mus", "300 mus", "1 ms", "3 ms",
                   "10 ms", "30 ms", "100 ms", "300 ms", "1 s", "3 s", "10 s",
                   "30 s", "100 s", "300 s", "1 ks", "3 ks", "100 ks", "300 ks"
                   )

tconstliaoutp = array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]);

tconstuseroutp = array([10*1E-6, 30*1E-6, 100*1E-6, 300*1E-6,1*1E-3, 3*1E-3,
                        10*1E-3, 30*1E-3, 100*1E-3, 300*1E-3, 1, 3, 10, 30,
                        100, 300, 1*1E3, 3*1E3, 100*1E3, 300*1E3])

LIASensVisual = ("2 nV", "5 nV", "10 nV", "20 nV", "50 nV", "100 nV", "200 nV",
                 "500 nV", "1 muV", "2 muV", "5 muV", "10 muV", "20 muV",
                 "50 muV", "100 muV", "200 muV", "500 muV", "1 mV", "2 mV", "5 mV",
                 "10 mV", "20 mV", "50 mV", "100 mV", "200 mV", "500 mV", "1 V"
                 )
sensliaoutp = array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,
                     18,19,20,21,22,23,24,25,26]
)

ChopperFrequencyPreset = ('Off', '5 kHz', '10 kHz', '15 kHz', '20 kHz', 
                          '25 kHz', '30  kHz', '35 kHz', '40 kHz', '45 kHz',
                          '50 kHz', '55 kHz', '60 kHz', '65 kHz', '70 kHz', 
                          '75 kHz', '80 kHz', '85 kHz', '90 kHz', '95 kHz', '100 kHz'
                          )

LIAChopperOutpValues = ('0', '0.227', '0.454', '0.682', '0.909', '1.137', 
                        '1.364', '1.592', '1.819', '2.047', '2.274', '2.501',
                        '2.729', '2.956', '3.184', '3.411', '3.639', '3.866',
                        '4.094', '4.321', '4.548'
                        )

DelayLines = ('Group1.Pos', 'Group4.Pos')

rootfolder = 'C:/Users/XY/Programs/ManipControle/Root/'
