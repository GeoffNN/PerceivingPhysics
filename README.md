# PerceivingPhysics
Integrating a Physics Engine with Deep Neural Networks

## Pipeline

Our work is separated in several step:

 - Physics Simulator for a simple pendulum. This is used both for having a perfect baseline dataset, and for the MCMC approach of evaluating the physical parameters.

 We based our work on the two following websites:
http://www.petercollingridge.co.uk/pygame-physics-simulation/boundaries for Pygame physics simulation and code by Craig Wm. Versek here: https://gist.github.com/cversek/98dead0521677d0b7d4d4162715704be.

 - Recognizing the mass. This uses a CNN using Hypercolumn features.

 - Using the mass's center positions as input for an MCMC to get physical caracteristics of the system (length of the cord).

## Installation