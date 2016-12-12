
##################################################################
#
# Python script to link between LesHouches events file+pythia+delphes+madanalysis
####################################################################
lhe = 'test_drellyan.lhe'  # put it in the same directory of the running script or 

################################################
#Here the user should define pythia options by on/off

Hadronizatoin = 'on'
Beam_remnants = 'on'
Decay_of_heavy_hadrons = 'on'
Initial_state_radiation = 'on'
Final_state_radiation = 'on'
Multiple_interaction = 'off'

# Other options for the merging&matching algorithm has to be chagned by the user (if needed)  
merging = '0'  # If '0' no matching used. '1' CKKW matching '2' MLM matching

######################################################
# Fo the moment delphes input card is the default CMS one for RUN-II
Delphes = 'on'  # 'on/off' turn on or off delphes
################################################
madanalysis = 'on' 

cross_section = '0.1'  # please add it in Pb
Lumi = '100'           #1/fb
plot = 'M ( l l ) 100 0 200' #Invariant mass plot "you can plot any other variables as defined in MadAnalysis manual"
