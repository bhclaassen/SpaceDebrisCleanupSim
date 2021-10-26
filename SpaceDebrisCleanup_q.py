# Space Debris Celanup Sim
# 2021-10-24
# BHC

#######################
##  !! IMPORTANT !!  ##
## STARTING WITH 2-D ##
#######################

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# Libraries #
import math
from os import TMP_MAX
import pandas as pd
import numpy as np



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# Data Dictionary #

'''
~ GENERAL ~
boundingBoxDimensions -> (X,Y,Z) coordinates of outermost point for all positive
    values. Full box side length = 2*Var. Full box centered at (0,0,0)
numTicks -> Number of ticks per instance; t < 0
debrisRTree -> R-tree search tree for nearest neighbor debris object search


~ DRONE/SHIP ~
numDrones -> Number of drones
shipCollectionRange -> range drone must be to dock with ship
totalCost -> fcn(   
    droneParameters(
        passive sense range,
        movement speed,
        drone collection range
        ), 
    shipParameters(
        numDebrisCollected,
        numDrones,
        shipCollectionRange
        ),
    droneCost
    )
    )
ifDocked -> Drone char(bool): 1 is docked, 0 is not
ifSenseDebris -> Drone char(bool): 1 is debris sensed, 0 is not
ifHaveDebris -> Drone char(bool): 1 is debris is possessed, 0 is not
droneInformation_Matrix -> Matrix used to override random generation of drone chars
locationXYZ -> Drone location (x,y,z) around origin (0,0,0); -X < x < X for (x,y,z)
headingTP -> Heading (theta, phi); 0 <= theta < 360 for (theta,phi)
        <https://stackoverflow.com/questions/23856489/pvector-heading-for-3d-rotation>
        <https://en.wikipedia.org/wiki/Spherical_coordinate_system>
droneInfo_Matrix -> Matrix containing all drone information
droneParameters ->  movement speed,
                    passive sense range,
                    percent chance to change heading,
                    debris collection range
shipParameters ->   numDebrisCollected,
                    numDrones


~ DEBRIS ~
numObjects -> Number of pieces of debris
ifCollected -> Debris char(bool): 1 is collected, 0 is not
debrisInformation_Matrix -> Matrix used to override random generation of debris chars
locationXYZ -> Debris location (x,y,z) around origin (0,0,0); -X < x < X for (x,y,z)
debrisInfo_Matrix -> Matrix containing all debris information


'''

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# Functions #

'''

## Initialization functions
initDroneMatrix -> (# of drones, # of parameters, parameter names, total cost allocation, overrideDroneInfo_Matrix = 0)
initDebris -> (# of objects, bounding box dimensions, overrideDebrisInfo_Matrix = 0)
initDebrisRTree -> (debrisInformation_Matrix, bounding box dimensions)
initInstances -> (drone and ship characteristics)


## Simulation instance functions
debrisCollectionInstance -> (droneInformation_Matrix)
simulationSuccessCalculation -> ()
droneCharacteristicsRecombination -> (droneInformation_Matrix, shipInformation_Matrix)

'''


# def initShipMatrix():

# def initDroneMatrix(numDrones, numParameters, parameterNames, totalCost, overrideDroneInfo_Matrix = 0):
    # Create matrix [# of drones] x [# of parameters] + length(ID, locationXYZ, headingTP, ifDocked, ifSenseDebris, ifHaveDebris)]

    # Create drone ID
    # Fill drone parameters
        # Parameters: Movement speed, passive sense range, percent chance to change heading, debris collection range
    # Set ifDocked = 1 to start
    # Set locationXYZ = (0,0,0) to start
    # Set headingTP = (0,0) to start
    # Set ifSenseDebris = 0 to start
    # Set ifHaveDebris = 0 to start

    # Output droneInfo_Matrix


def initDebris(numObjects, boundingBoxDimensions, tmpSeed = 0, overrideDebrisInfo_Matrix = 0):

    # Create matrix [# of objects] x length(ID, locationXYZ, ifCollected)]
    if(tmpSeed != 0):
        np.random.seed(tmpSeed)

    debrisInfo_Matrix = pd.DataFrame(
        {
            'ID': np.array(list(range(numObjects))) + 1
            ,'locX': boundingBoxDimensions * 2 * np.random.random_sample(numObjects) - boundingBoxDimensions # Set location randomly within bounding box: (b-a) rand + a; <https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.random.random.html>
            ,'locY': boundingBoxDimensions * 2 * np.random.random_sample(numObjects) - boundingBoxDimensions
            ,'ifCollected': [0] * numObjects # Set ifCollected = 0 to start
        }
    )
    
    # Output debrisInfo_Matrix
    return(debrisInfo_Matrix)


# def initDebrisRTree():
    # NOT USING FOR NOW, DOING BRUTE FORCE SEARCH TO START
    # Output debrisRTree


# def initInstances():


def doMove_X(tmp_X, tmp_Heading, tmp_MoveSpeed):
    # cos(theta) * hypotenuse = adjacent side length
    # add movement on the x-axis to current x location
    newTmp_X = math.cos(tmp_Heading) * tmp_MoveSpeed + tmp_X
    return(newTmp_X)

def doMove_Y(tmp_Y, tmp_Heading, tmp_MoveSpeed):
    # sin(theta) * hypotenuse = opposite side length
    # add movement on the y-axis to current y location
    newTmp_Y = math.sin(tmp_Heading) * tmp_MoveSpeed + tmp_Y
    return(newTmp_Y)
    
 
# def simulationSuccessCalculation(droneInfo_Matrix, debrisInfo_Matrix, numTicks):
    # Calculate 'success' score based on inputs
    # Output score


# def droneCharacteristicsRecombination(droneInformation_Matrix, shipInformation_Matrix):
    # 

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

## BEGIN INSTANCE ##
def debrisCollection_runInstance(tmp_shipInfo_Matrix, tmp_droneInfo_Matrix, tmp_debrisInfo_Matrix, tmp_numTicks, tmpSeed = 0, tmp_debrisRTree = 0):
    # MAIN - Run simulation instance
    print(tmp_shipInfo_Matrix)
    print(tmp_droneInfo_Matrix)
    print(tmp_debrisInfo_Matrix)
    print(tmp_numTicks)

    if(tmpSeed != 0):
        np.random.seed(tmpSeed)

    # Loop over number of ticks
    for tick in range(tmp_numTicks):
        print(f'Tick #: {tick}')

        # Loop over each drone
        for drone in range(tmp_droneInfo_Matrix.shape[0]):
            print(f'Drone #: {drone}')

            #Pull current drone characteristics
            tmpDroneChars = pd.DataFrame(tmp_droneInfo_Matrix.loc[drone, :])
            print(tmpDroneChars)
            print(tmpDroneChars.shape)
            print(type(tmpDroneChars))
            print(tmpDroneChars.loc['ifDocked'].bool())


            # ? If docked?
            if tmpDroneChars.loc['ifDocked'].bool() == True:
                # Docked: {update attributes, choose random heading, move}
                # If have debris
                if tmpDroneChars.loc['ifHaveDebris'].bool() == True:
                    tmp_shipInfo_Matrix['numDebrisCollected'] = tmp_shipInfo_Matrix['numDebrisCollected'] + 1
                    tmpDroneChars.loc['ifHaveDebris'] = False

                # Choose random heading
                tmpDroneChars.loc['headingT'] = np.random.random_sample(1) * (2 * math.pi)
                tmpDroneChars.loc['locX'] = 0
                tmpDroneChars.loc['locY'] = 0

                tmpX = tmpDroneChars.loc['locX']
                tmpY = tmpDroneChars.loc['locY']
                tmpHeading = tmpDroneChars.loc['headingT']
                tmpMoveSpeed = tmpDroneChars.loc['moveSpeed']

                tmpDroneChars.loc['locX'] = doMove_X(tmpX, tmpHeading, tmpMoveSpeed)
                tmpDroneChars.loc['locY'] = doMove_Y(tmpY, tmpHeading, tmpMoveSpeed)
## <- Ends here, for the moment

                print(tmpDroneChars)

                
            # ? Have debris?
                # Have debris:
                # ? In ship collection range?
                    # In ship collection range: {dock, update parameters}
                # Have debris, not in collection range: orient to (0,0,0), move
            
            # ? Sense debris?
                # Sense debris: ? debris in collection range?
                    # Debris in collection range: {collect}
                # Sense debris, not in collection range: {orient to debris, move}

            # ? New heading?
                # New heading: set new random heading, move
                # No new heading: move

        # END drone loop
    # END ticks loop

    # 'Success' score
#   shipSuccessScore = shipInfo_Matrix -> numDebrisCollected
#   return(shipSuccessScore)
    return(1)

## END INSTANCE ##

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# MAIN #

# Specify starting parameters
numDebris = 3 # Number of pieces of debris
numDrones = 2 #10 # Number of drones
debrisBoxHalfSide_Length = 2 #10 # Bounding box 2 times as wide/deep/tall
droneMovementSpeed = 2 # Drone distance moved per tick
droneSenseRange_Radius = 6 # Radius of drone sense range
droneCollectionRange_Radius = 2 # Radius of drone collection range
ticks = 1 # 100 # Number of time steps
shipCollectionRange_Radius = 2 # Radius of ship collection range
generalSeed = 2 # Set seed if desired. Can be ommitted or set to 0 for no seed 
numGenerations = 1 # Set number of generations. 1 means no recombination
numInstances = 1 # Set number of instances, i.e. number of ship/debris colletion versions to run





# Initialize debris field creation
debrisInfo_Matrix = initDebris(numDebris, debrisBoxHalfSide_Length, tmpSeed = generalSeed, overrideDebrisInfo_Matrix = 0)
#print(debrisInfo_Matrix)

# Initialize debris R Tree for nearest neighbor search <https://en.wikipedia.org/wiki/R-tree>

##-> Begin generation loop <-##
#Loop over number of generations
for gen in range(numGenerations):
    print(f'Generation #: {gen}')

    ##-> Begin instance loop <-##
    for inst in range(numInstances):
        print(f'Instance #: {inst}')

        #Intialize ship creation
        #initShipMatrix()
        shipInfo_Matrix = pd.DataFrame(
            {
                'numDronesDocked': [numDrones]
                ,'numDebrisCollected': [0]
                ,'shipCollectionRadius': [1]
                ,'successScore': [0]
            }
        )
        #print(shipInfo_Matrix)

        # Initialize drone creation
        #initDroneMatrix(numDrones, numParameters, parameterNames, totalCost, overrideDroneInfo_Matrix = 0)
        droneInfo_Matrix = pd.DataFrame(
            {
                'ID': np.array(list(range(numDrones))) + 1
                ,'locX': [0] * numDrones
                ,'locY': [0] * numDrones
                ,'headingT': [0] * numDrones
                ,'moveSpeed': [droneMovementSpeed] * numDrones
                ,'senseRadius': [droneSenseRange_Radius] * numDrones
                ,'collectionRadius': [droneCollectionRange_Radius] * numDrones
                ,'ifDocked': [1] * numDrones
                ,'ifSenseDebris': [0] * numDrones
                ,'ifHaveDebris': [0] * numDrones
            }
        )

        droneInfo_Matrix['locX'] = droneInfo_Matrix['locX'].astype(float)
        droneInfo_Matrix['locY'] = droneInfo_Matrix['locY'].astype(float)
        droneInfo_Matrix['headingT'] = droneInfo_Matrix['headingT'].astype(float)
        droneInfo_Matrix['moveSpeed'] = droneInfo_Matrix['moveSpeed'].astype(float)
        droneInfo_Matrix['senseRadius'] = droneInfo_Matrix['senseRadius'].astype(float)
        droneInfo_Matrix['collectionRadius'] = droneInfo_Matrix['collectionRadius'].astype(float)
        droneInfo_Matrix['ifDocked'] = droneInfo_Matrix['ifDocked'].astype(bool)
        droneInfo_Matrix['ifSenseDebris'] = droneInfo_Matrix['ifSenseDebris'].astype(bool)
        droneInfo_Matrix['ifHaveDebris'] = droneInfo_Matrix['ifHaveDebris'].astype(bool)

        

        print(droneInfo_Matrix.dtypes)

        #print(droneInfo_Matrix)

        # Run simulation instance
        shipInstance_SuccessScore = debrisCollection_runInstance(shipInfo_Matrix, droneInfo_Matrix, debrisInfo_Matrix, ticks, generalSeed)
        print(shipInfo_Matrix)
        # Calculate 'success' score
        # Output and store drone characteristics and 'success' score


    ##-> End instance loop <-##

    # Recombine drone characteristics based on 'success' score

##-> End generation loop <-##

# Output


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#                                    END                                       #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#