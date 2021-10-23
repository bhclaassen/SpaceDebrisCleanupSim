# Space Debris Celanup Sim
# 2021-10-23
# BHC

#####################
# !! PSUEDO CODE !! #
#####################

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# Libraries #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# Data Dictionary#

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
headingTP -> Heading (theta, phi); 0 <= theta < 360 for (theta,phi) <https://en.wikipedia.org/wiki/Spherical_coordinate_system>
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


# def initDebris(numObjects, boundingBoxDimensions,overrideDebrisInfo_Matrix = 0):
    # Create matrix [# of objects] x length(ID, locationXYZ, ifCollected)]

    # Create object ID
    # Set location randomly within bounding box
    # Set ifCollected = 0 to start

    # Output debrisInfo_Matrix


# def initDebrisRTree():
    # NOT USING FOR NOW, DOING BRUTE FORCE SEARCH TO START
    # Output debrisRTree

# def initInstances():


## BEGIN MAIN ##
# def debrisCollection_runInstance(droneInfo_Matrix, debrisInfo_Matrix, debrisRTree, shipCollectionRange, numTicks):
    # MAIN - Run simulation instance

    # Set random heading for each drone
    
    # Loop over number of ticks
        # Loop over each drone
            # Check if have debris
                # If so, check if within [shipCollectionRange]
                    # If so, dock
                        # Update drone and ship parameters
                # If have debris but not within [shipCollectionRange]
                    # Change heading to return to origin
                    # Move
            # Check if debris detected
                # Check if debris within [droneCollectionRange]
                    # If so, collect debris
                # If debris detected but not in range
                    # Orient heading towards debris
                    # Move
            
            # If not have debris and not detect debris
                # check if change heading
                    # If so, change heading
                # Move

        # END drone loop
    # END ticks loop

    # Output drone characteristics matrix and 'succses' score

## END MAIN ##

# def simulationSuccessCalculation(droneInfo_Matrix, debrisInfo_Matrix, numTicks):
    # Calculate 'success' score based on inputs
    # Output score

# def droneCharacteristicsRecombination(droneInformation_Matrix, shipInformation_Matrix):
    # 


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# MAIN #

# Specify starting parameters
# Initialize debris field creation
# Initialize debris R Tree for nearest neighbor search <https://en.wikipedia.org/wiki/R-tree>

##-> Begin generation loop <-##
#Loop over number of generations
    
    ##-> Begin instance loop <-##
    # Loop over number of instances per generation

        # Initialize drone creation
        
        # Run simulation instance

        # Calculate 'success' score
        # Output and store drone characteristics and 'success' score

    ##-> End instance loop <-##

    # Recombine drone characteristics based on 'success' score

##-> End generation loop <-##

# Output


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#                                    END                                       #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#