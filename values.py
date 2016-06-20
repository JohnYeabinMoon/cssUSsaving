# Values...

# initializedParams
epsilon = 0.01;
littleRBase = 0.04/4;  
littleGBase = 0.01/4;
rhoBase = 2;
VerboseOutput = 0;

# resetParams
mho = mhoBase;
theta = thetaBase;
littleR = littleRBase;
littleG = littleGBase;
rho = rhoBase;

# setValues

mybeta = 1/(1+theta);   # individual's time discount factor
bigR = littleR + 1; 	# interest factor
bigG = littleG + 1;     # wage growth factor
biggamma = bigG;
scriptR = bigR/biggamma; # net interest factor (R normalized by wage growth)
Lambda = (bigR**(-1))*(bigR*mybeta)**(1/rho); # MPS for a perfect foresight consumer
kappa = 1-Lambda; # MPC for a perfect foresight consumer



scriptPGrowth = (bigR*mybeta)**(1/rho)/biggamma;
scriptPReturn = (bigR*mybeta)**(1/rho)/bigR;
scriptpgrowth = log(scriptPGrowth);
scriptpreturn = log(scriptPReturn);

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

Pi = (1+(scriptPGrowth**(-rho)-1)/mho)**(1/rho);
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
