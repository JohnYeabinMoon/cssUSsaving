def minCdist(thetaVec, data):
	nPers=2;
	
	# Note that thetaVec starts at the initialValues
	
	scaleFac0_mho=thetaVec[0];
	scaleFac1_mho=thetaVec[1];
	scaleFac0_CEA=thetaVec[2];
	scaleFac1_CEA=thetaVec[3];
	thetaBase=thetaVec[4];
	
	wyRatSeries = data['wyRatSeries']
	mhoSeries= data['mhoSeries']
	CEAseries = data['CEAseries']
	saving_rate = data['saving_rate']
	
	steadyStateMC=[]; 
	steadyStateMCexPDVdebt=[];

	debtLimPDVrescaled=scaleFac0_CEA+scaleFac1_CEA*CEAseries; # equation (7)	
	mhoRescaled=scaleFac0_mho+scaleFac1_mho*mhoSeries;  # equation (8)
	
	for k in range(len(wyRatSeries)):   
		print "Calculating Quarter"
		print k
		mhoBase = mhoRescaled[k];
		
		# Need to handle the following#####
		initializeParams;
    		scriptmEBase = scriptmE;
    		scriptcEBase = scriptcE;
    		##############################
    	
	    	debtLimPDV=debtLimPDVrescaled[k];
    
