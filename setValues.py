mybeta = 1/(1+theta);    # from resetParams.py
bigR = littleR + 1; 	 # from resetParams.py
bigG = littleG + 1; 	 # from resetParams.py

biggamma = bigG;
scriptR = bigR/biggamma; # net interest factor (R normalized by wage growth)
Lambda = (bigR**(-1))*(bigR*mybeta)**(1/rho);  # from resetParams.py  # lambda -> Lambda
kappa = 1-Lambda; 


# Various impatience factors
scriptPGrowth = (bigR*mybeta)**(1/rho)/biggamma;
scriptPReturn = (bigR*mybeta)**(1/rho)/bigR;
scriptpgrowth = math.log(scriptPGrowth);
scriptpreturn = maht.log(scriptPReturn);


# Check for Gamma Impatience###########
if scriptPGrowth >= 1:
	print '(bigR*mybeta)^(1/rho)/biggamma = %d' % ((bigR*mybeta)**(1/rho)/biggamma)
	print 'bigR = %d' % bigR
	print 'mybeta = %d' % mybeta
	print 'biggamma = %d' % biggamma
	print 'Aborting: Employed Consumer Not Growth Impatient.' # need to change the color RED

# Check for BigR impatience
if scriptPReturn >= 1:
	print 'Aborting: Employed Consumer Not Return Impatient.' # need to change the color RED
########################################


Pi = (1+(scriptPGrowth^(-rho)-1)/mho)**(1/rho);
littleH = (1/(1-bigG/bigR));
myZeta = scriptR*kappa*Pi;

# The steady state values for the employed and unemployed consumer
scriptmE = 1+(bigR/(biggamma+myZeta*biggamma-bigR));
scriptcE = (1-scriptR**(-1))*scriptmE+scriptR**(-1);
scriptaE = scriptmE - scriptcE;
scriptbE = scriptaE*scriptR;
scriptyE = scriptaE*(scriptR-1)+1;
scriptxE = scriptyE - scriptcE;
scriptbU = scriptbE;
scriptmU = (scriptmE - scriptcE) * scriptR;
scriptcU = scriptmU * kappa;

littleV = 1/(1-mybeta*((bigR*mybeta)**((1/rho)-1)));


## Define CRRA function##############
def CRRA(scriptc,rho):
    if rho == 1:
        u = math.log(scriptc); 
    else: 
        u = (scriptc**(1-rho))/(1-rho); 
    return u
#####################################

## Define vUPF function ############
def vUPF(scriptm,rho,kappa,littleV,bigR,mybeta):
	temp = CRRA(kappa * scriptm,rho) * littleV
	if rho ==1:
		temp = temp + math.log(bigR * mybeta) * (mybeta/((mybeta-1)**2));
	return temp
#####################################


scriptvU = CRRA(scriptcU,rho)*littleV;
scriptvE = (CRRA(scriptcE,rho) + mybeta*(biggamma**(1-rho))*mho*vUPF(scriptaE * scriptR,rho,kappa,littleV,bigR,mybeta))/(1-mybeta*(biggamma**(1-rho)*(1-mho)));

Beth = scriptR * mybeta * biggamma**(1-rho);


## Find the limiting MPC as assets approach zero
# Define kappaLim0Find function #####
# Define naturalFuncLim0 function

def naturalFuncLim0(kEt,Beth,scriptR,mho,kappa,rho):
	return Beth * scriptR * mho * (kappa * scriptR * ((1-kEt)/kEt))**(-rho-1) * kappa;

def kappaLim0Find(Beth,scriptR,mho,kappa,rho,Lambda):
	gothisdeep = 100;
	counter = 0;
	searchAt = 0.5;
	found = 0;
	
	while counter <= (gothisdeep and found == 0):
		if searchAt < naturalFuncLim0(searchAt,Beth,scriptR,mho,kappa,rho)/(1 + naturalFuncLim0(searchAt,Beth,scriptR,mho,kappa,rho)):
			searchAt = searchAt - 2**(-counter)*(Lambda-0.5);
   		if searchAt > naturalFuncLim0(searchAt,Beth,scriptR,mho,kappa,rho)/(1 + naturalFuncLim0(searchAt,Beth,scriptR,mho,kappa,rho)):
   			searchAt = searchAt + 2**(-counter)*(Lambda-0.5);
   		if searchAt == naturalFuncLim0(searchAt,Beth,scriptR,mho,kappa,rho)/(1 + naturalFuncLim0(searchAt,Beth,scriptR,mho,kappa,rho)):
   			found = 1;
   		count += 1;
   	return searchAt
############################

kappaEMax = kappaLim0Find(Beth,scriptR,mho,kappa,rho,Lambda);


# These functions find the MPC and its derivatives at the steady state.
# Define CRRApp function
# Define CRRAppp function
# Define CRRApppp function
# Define CRRAppppp function
# Define kappaEFind function
# Define kappaEPFind function
# Define kappaEPPFind function
# Define kappaEPPPFind function


def CRRApp(scriptc,rho):
	return -rho * scriptc**(-rho-1);
	
def CRRAppp(scriptc,rho):
	return -rho * (-rho-1) * scriptc**(-rho-2)
	
def CRRApppp(scriptc,rho):
	return -rho * (-rho-1) * (-rho-2) * scriptc**(-rho-3)

def CRRAppppp(scriptc,rho):
	return -rho * (-rho-1) * (-rho-2) * (-rho-3) * scriptc**(-rho-4)
	
def kappaEFind(rho,mho,kappa,scriptR,Beth,scriptcE,scriptcU):
    gothisdeep = 100; 
    counter = 0;
    searchAt = 0;
    found = 0;
    while counter <= (gothisdeep and found == 0):
        scriptcEP = searchAt;
        LHS = scriptcEP * CRRApp(scriptcE,rho);
        RHS = Beth * ((1 - mho) * (1 - scriptcEP)* scriptcEP * scriptR * CRRApp(scriptcE,rho) + kappa * mho * (1 - scriptcEP)* scriptR * CRRApp(scriptcU,rho));
        if LHS > RHS:
            searchAt = searchAt + 2**(-counter);
        if LHS < RHS:
            searchAt = searchAt - 2**(-counter);
        if LHS == RHS:
            found = 1;
        counter += 1;
    return scriptcEP

def kappaEPFind(kappaE,kappa,rho,mho,Beth,scriptR,scriptcE,scriptcU):
	gothisdeep = 100; 
	counter = 0;
	searchAt = 0;
	found = 0;
	scriptcEP = kappaE;
	while counter <= (gothisdeep and found == 0):
		scriptcEPP = searchAt;
    	LHS = scriptcEPP * CRRApp(scriptcE,rho) + scriptcEP**2 * CRRAppp(scriptcE,rho);
	    RHS = Beth * (-(1 - mho) * scriptcEP * scriptcEPP * scriptR * CRRApp(scriptcE,rho) + (1 - mho) * (1 - scriptcEP)**2 * scriptcEPP * scriptR**2 * CRRApp(scriptcE,rho) - kappa * mho * scriptcEPP * scriptR * CRRApp(scriptcU,rho) + (1 - mho) * (1 - scriptcEP)^2 * scriptcEP**2 * scriptR**2 * CRRAppp(scriptcE,rho) + kappa**2 * mho * (1 - scriptcEP)**2 * scriptR**2 * CRRAppp(scriptcU,rho));
    	if LHS > RHS:
	        searchAt = searchAt + 2**(-counter);
		if LHS < RHS:
	        searchAt = searchAt - 2**(-counter);
    	if LHS == RHS:
	        found = 1;
    	counter += 1;
	return scriptcEPP

def kappaEPPFind(rho,mho,scriptR,kappa,kappaE,kappaEP,Beth,scriptcE,scriptcU):
	gothisdeep = 100; 
	counter = 0;
	searchAt = 0;
	found = 0;
	scriptcEP = kappaE;
	scriptcEPP = kappaEP;
	while counter <= (gothisdeep and found == 0):
		scriptcEPPP = searchAt;
		LHS = scriptcEPPP * CRRApp(scriptcE,rho) + 3 * scriptcEP * scriptcEPP * CRRAppp(scriptcE,rho) + scriptcEP**3 * CRRApppp(scriptcE,rho);
    	RHS = Beth * (-(1 - mho) * scriptcEP * scriptcEPPP * scriptR * CRRApp(scriptcE,rho) - 3 * (1 - mho) * (1 - scriptcEP) * scriptcEPP**2 * scriptR**2 * CRRApp(scriptcE,rho) + (1 - mho) * (1 - scriptcEP)**3 * scriptcEPPP * scriptR**3 * CRRApp(scriptcE,rho) - kappa * mho * scriptcEPPP * scriptR * CRRApp(scriptcU,rho) - 3 * (1 - mho) * (1 - scriptcEP) * scriptcEP**2 * scriptcEPP * scriptR**2 * CRRAppp(scriptcE,rho) + 3 * (1 - mho) * (1 - scriptcEP)^3 * scriptcEP * scriptcEPP * scriptR**3 * CRRAppp(scriptcE,rho) - 3 * kappa**2 * mho * (1 - scriptcEP) * scriptcEPP * scriptR**2 * CRRAppp(scriptcU,rho) + (1 - mho) * (1 - scriptcEP)**3 * scriptcEP**3 * scriptR**3 * CRRApppp(scriptcE,rho) + kappa**3 * mho * (1 - scriptcEP)**3 * scriptR**3 * CRRApppp(scriptcU,rho));
    	if LHS > RHS:
	        searchAt = searchAt + 2**(-counter);
	    if LHS < RHS:
	        searchAt = searchAt - 2**(-counter);
	    if LHS == RHS:
	        found = 1;
	    counter += 1;
	return scriptcEPPP;

def kappaEPPPFind(rho,mho,kappa,kappaE,kappaEP,kappaEPP,Beth,scriptR,scriptcE,scriptcU):
	gothisdeep = 100; 
	counter = 0;
	searchAt = 0;
	found = 0;
	scriptcEP = kappaE;
	scriptcEPP = kappaEP;
	scriptcEPPP = kappaEPP;
	while counter <= (gothisdeep and found == 0):
		scriptcEPPPP = searchAt;
	    LHS = scriptcEPPPP * CRRApp(scriptcE,rho) + 3 * scriptcEPP**2 * CRRAppp(scriptcE,rho) + 4 * scriptcEP * scriptcEPPP * CRRAppp(scriptcE,rho) + 6 * scriptcEP**2 * scriptcEPP * CRRApppp(scriptcE,rho) + scriptcEP**4 * CRRAppppp(scriptcE,rho);
    	RHS = Beth * (-(1 - mho) * scriptcEP*  scriptcEPPPP * scriptR * CRRApp(scriptcE,rho) + 3 * (1 - mho) * scriptcEPP**3 * scriptR**2 * CRRApp(scriptcE,rho) - 4 * (1 - mho) * (1 - scriptcEP) * scriptcEPP * scriptcEPPP * scriptR**2 * CRRApp(scriptcE,rho) - 6 * (1 - mho) * (1 - scriptcEP)**2 * scriptcEPP * scriptcEPPP * scriptR**3 * CRRApp(scriptcE,rho) + (1 - mho) * (1 - scriptcEP)**4 * scriptcEPPPP * scriptR**4 * CRRApp(scriptcE,rho) - kappa * mho * scriptcEPPPP * scriptR * CRRApp(scriptcU,rho) + 3 * (1 - mho) * scriptcEP**2 * scriptcEPP**2 * scriptR**2 * CRRAppp(scriptcE,rho) - 4 * (1 - mho) * (1 - scriptcEP) * scriptcEP**2 * scriptcEPPP * scriptR**2 * CRRAppp(scriptcE,rho) - 18 * (1 - mho) * (1 - scriptcEP)**2 * scriptcEP * scriptcEPP**2 * scriptR**3 * CRRAppp(scriptcE,rho) + 3 * (1 - mho) * (1 - scriptcEP)**4 * scriptcEPP**2 * scriptR**4 * CRRAppp(scriptcE,rho) + 4 * (1 - mho) * (1 - scriptcEP)**4 * scriptcEP * scriptcEPPP * scriptR**4 * CRRAppp(scriptcE,rho) + 3 * kappa**2 * mho * scriptcEPP**2 * scriptR**2 * CRRAppp(scriptcU,rho) - 4 * kappa**2 * mho * (1 - scriptcEP) * scriptcEPPP * scriptR**2 * CRRAppp(scriptcU,rho) - 6 * (1 - mho) * (1 - scriptcEP)**2 * scriptcEP**3 * scriptcEPP * scriptR**3 * CRRApppp(scriptcE,rho) + 6 * (1 - mho) * (1 - scriptcEP)**4 * scriptcEP**2 * scriptcEPP * scriptR**4 * CRRApppp(scriptcE,rho) - 6 * kappa**3 * mho * (1 - scriptcEP)**2 * scriptcEPP * scriptR**3 * CRRApppp(scriptcU,rho) + (1 - mho) * (1 - scriptcEP)**4 * scriptcEP**4 * scriptR**4 * CRRAppppp(scriptcE,rho) + kappa**4 * mho * (1 - scriptcEP)**4 * scriptR**4 * CRRAppppp(scriptcU,rho));
    	if LHS > RHS:
	        searchAt = searchAt + 2**(-counter);
        if LHS < RHS:
	        searchAt = searchAt - 2**(-counter);
    	if LHS == RHS:
	        found = 1;
    	counter += 1;
	return scriptcEPPPP;

kappaE = kappaEFind(rho,mho,kappa,scriptR,Beth,scriptcE,scriptcU);
kappaEP = kappaEPFind(kappaE,kappa,rho,mho,Beth,scriptR,scriptcE,scriptcU);
kappaEPP = kappaEPPFind(rho,mho,scriptR,kappa,kappaE,kappaEP,Beth,scriptcE,scriptcU);
kappaEPPP = kappaEPPPFind(rho,mho,kappa,kappaE,kappaEP,kappaEPP,Beth,scriptR,scriptcE,scriptcU);


## Need to check the dimension...#########################
SteadyStateVals = [scriptbE scriptmE scriptcE scriptaE kappaE kappaEP scriptvE];
##########################################################


if VerboseOutput==1:
    print 'All variables set, consumer is sufficiently impatient.'


