# Fragmentation_depth_model
Script for the prediction of the depth of fragmentation of the metal core of a differentiated planetary embryo during a giant planet forming impact as modelled in Maller et al. 2023.


A bunch of functions are regrouped in the script.
The function "the_model" takes as imputs the Radius of the impactor in km, the Radius of the target planet in km and the ratio of the impact velocity to the escape velocity for the system impactor plus target planet. 
It returns in a string whether there is fragmentation on impact, the depth at which fragmentation is complete, the depth at which fragmentation begins and the center of mass of the crater.
