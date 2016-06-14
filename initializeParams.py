# This script defines the base values for parameters in the TBS model.
# It then calls a script to define the working values of these parameters.


epsilon = 0.01;
littleRBase = 0.04/4;


#### Need some help
#if ~exist('prodGbase','var'); littleGBase = 0.01/4;
#else; littleGBase=(prodGbase)/400; 
#    end;
#########
# Thus far I haven't gotten any idea of 'prodGbase' 
#So base line is 
littleGBase = 0.01/4;
#########

rhoBase = 2;
VerboseOutput = 0;

#if ~exist('mean');
#    print(good)
#end

if VerboseOutput == 1:
	print 'Output will be verbose.'
	print 'Parameter base values have been set.'


#resetParams;
