import numpy as np


def calc_crsr_index(df, ii):
    """
    Function to calculate the CRS-R index (Annen*, Filippini* et al., (2019)).

    Takes a pandas dataframe as input and returns the CRS-R index. The input dataframe should contain
    the CRS-R subscores (Auditory, Visual, Motor, Oromotor, Arousal). Because usually the CRS-R is
    performed multiple times, the function can be used in a loop to calculate the CRS-R index for every CRS-R.
    Column names should in any case be numbered like so: CRSR_ii_type  (e.g., CRSR_1_Motor).
    Read file with CRS-R subscores (with column names Auditory, Visual, Motor, Oromotor, Arousal).Items for a
    diagnosis of EMCS are excluded.

    Usage:
    crsr_index = calc_crsr_index(dataframe, ii))"""

    # Initialize the transposition matrix to calculate the CRS-R index (Annen*, Filippini* et al., (2019)),
    # same as from CRS-R modified score (Sattin et al., 2015).
    RBvalue = np.array([1.00, 0.86, 0.71, 0.57, 0.43, 0.29, 0.14, 0.00])
    CMBvalue = np.array([0.00, 0.09, 0.18, 0.27, 0.36, 0.45, 0.55, 0.64, 0.73, 0.82, 0.91, 1.00])
    MSmatrix = np.array([[7.29, 15.63, 23.97, 32.31, 40.64, 48.98, 57.32, 65.65, 73.99, 82.33, 90.66, 99.00],
                         [6.25, 14.59, 22.93, 31.26, 39.60, 47.94, 56.27, 64.61, 72.95, 81.28, 89.62, 97.96],
                         [5.21, 13.55, 21.88, 30.22, 38.56, 46.89, 55.23, 63.57, 71.91, 80.24, 88.58, 96.92],
                         [4.17, 12.51, 20.84, 29.18, 37.52, 45.85, 54.19, 62.53, 70.86, 79.20, 87.54, 95.87],
                         [3.13, 11.46, 19.80, 28.14, 36.47, 44.81, 53.15, 61.48, 69.82, 78.16, 86.49, 94.83],
                         [2.08, 10.42, 18.76, 27.09, 35.43, 43.77, 52.11, 60.44, 68.78, 77.12, 85.45, 93.79],
                         [1.04, 9.38, 17.72, 26.05, 34.39, 42.73, 51.06, 59.40, 67.74, 76.07, 84.41, 92.75],
                         [0.00, 8.34, 16.67, 25.01, 33.35, 41.68, 50.02, 58.36, 66.69, 75.03, 83.37, 91.71]])

    # Use this if highest score per subscale is provided. This is appropriate to calculate the
    # CRS-R index as proposed by Annen*, Filippini* et al., (2019).
    mydata = dict()
    # auditory
    if df['CRSR_' + str(ii) + '_Auditory'].values > 2:
        mydata['AuditoryRB'] = 2
    else:
        mydata['AuditoryRB'] = df['CRSR_' + str(ii) + '_Auditory'].values

    if df['CRSR_' + str(ii) + '_Auditory'].values < 3:
        mydata['AuditoryCMB'] = 0
    else:
        mydata['AuditoryCMB'] = df['CRSR_' + str(ii) + '_Auditory'].values - 2

    # visual
    if df['CRSR_' + str(ii) + '_Visual'].values > 1:
        mydata['VisualRB'] = 1
    else:
        mydata['VisualRB'] = df['CRSR_' + str(ii) + '_Visual'].values

    if df['CRSR_' + str(ii) + '_Visual'].values < 2:
        mydata['VisualCMB'] = 0
    else:
        mydata['VisualCMB'] = df['CRSR_' + str(ii) + '_Visual'].values - 1

    # motor
    if df['CRSR_' + str(ii) + '_Motor'].values > 2:
        mydata['MotorRB'] = 2
    else:
        mydata['MotorRB'] = df['CRSR_' + str(ii) + '_Motor'].values

    if df['CRSR_' + str(ii) + '_Motor'].values < 3:
        mydata['MotorCMB'] = 0
    else:
        mydata['MotorCMB'] = df['CRSR_' + str(ii) + '_Motor'].values - 2

    # oromotor
    if df['CRSR_' + str(ii) + '_Oromotor'].values > 2:
        mydata['OromotorRB'] = 2
    else:
        mydata['OromotorRB'] = df['CRSR_' + str(ii) + '_Oromotor'].values

    if df['CRSR_' + str(ii) + '_Oromotor'].values < 3:
        mydata['OromotorCMB'] = 0
    else:
        mydata['OromotorCMB'] = df['CRSR_' + str(ii) + '_Oromotor'].values - 2

    # Obtain the reflexive behavior and cognitively mediated behavior value
    mydata['CommunicationCMB'] = df['CRSR_' + str(ii) + '_Communication'].values
    mydata['ArousalMS'] = df['CRSR_' + str(ii) + '_Arousal'].values * (1 / 3)

    #
    mydata['RB'] = (mydata['AuditoryRB'] + mydata['VisualRB'] + mydata['MotorRB'] + mydata['OromotorRB']) / 7
    mydata['CMB'] = (mydata['AuditoryCMB'] + mydata['VisualCMB'] + mydata['MotorCMB'] +
                mydata['OromotorCMB'] + mydata['CommunicationCMB']) / 11

    mydata['index_rb'] = np.where(np.round(mydata['RB'], 2) == RBvalue)
    mydata['index_cmb'] = np.where(np.round(mydata['CMB'], 2) == CMBvalue)
    mydata['MS_value'] = MSmatrix[mydata['index_rb'], mydata['index_cmb']]

    # Calculate the CRS-R index
    crsr_index = mydata['MS_value'] + mydata['ArousalMS']

    return crsr_index
