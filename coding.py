import pandas as pd
import numpy as np

# format long?

minimizeObjFuncInd = 0; # Actually I don't get it this part.

dataOrig = pd.read_excel('cssussavingdata_selection_20110831.xls')
time = dataOrig.t
saving_rate = dataOrig.saving_rate
wyRat = dataOrig.wyRat
CEA = dataOrig.CEA
unemp_pred = dataOrig.unemp_pred

wyRatSeries = wyRat[24:202];
mhoSeries=unemp_pred[25:203]/100;
CEAseries=CEA[25:203];
time=time[25:203];
thetaBase=0.05;

# cExAll=[]; cEyAll=[]; mcPathAll=[]; scriptmEBaseAll=[]; steadyStateMC=[]; PiAll=[];

data = np.array([wyRatSeries, mhoSeries, CEAseries, saving_rate[25:203]])



initialValues = np.array([0, .0003, 1, 4, .01]) 
initialValues.shape = (5,1)
