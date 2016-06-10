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

wyRatSeries = wyRat[24:203];
mhoSeries=unemp_pred[25:204]/100;
CEAseries=CEA[25:204];
time=time[25:204];
thetaBase=0.05;

## Need to reset index to merge 
wyRatSeries = wyRatSeries.reset_index()
mhoSeries = mhoSeries.reset_index()
CEAseries = CEAseries.reset_index()
saving_rate = saving_rate.reset_index()

# merge mhoSeries CEAseries and saving_rate
mhoSeries = mhoSeries.merge(CEAseries)
mhoSeries = mhoSeries.merge(saving_rate)

wyRatSeries = wyRatSeries.wyRat # delete current index
wyRatSeries = wyRatSeries.reset_index() # New index starting at 0
mhoSeries = mhoSeries[['unemp_pred','CEA','saving_rate']] # delete current index
mhoSeries = mhoSeries.reset_index() # New index starting at 0

# Merge wyRatSeries and the rest 
data = wyRatSeries.merge(mhoSeries) 
data = data[['wyRat','unemp_pred','CEA','saving_rate']] # delete index column

# rename labels
data.columns = 'wyRatSeries','mhoSeries','CEAseries','saving_rate'


# cExAll=[]; cEyAll=[]; mcPathAll=[]; scriptmEBaseAll=[]; steadyStateMC=[]; PiAll=[];


initialValues = np.array([0, .0003, 1, 4, .01]) 
initialValues.shape = (5,1)
