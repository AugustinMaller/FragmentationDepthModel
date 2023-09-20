# Fragmentation_depth_model
Script for the prediction of the depth of fragmentation of the metal core of a differentiated planetary embryo during a giant planet-forming impact, as modelled in Maller et al. 2023 in equation (15).

This code is based on Python 3. No specific libraries are required.

The main function is "the_model".
It takes as inputs the radius of the impactor and the radius of the target planet in km and the ratio of the impact velocity to the escape velocity for the system composed of the impactor and the target planet.
It returns whether there is or not fragmentation on impact as a string, the depth at which fragmentation is complete in km, the depth at which fragmentation begins in km, and the centre of mass of the crater in km.

If you have any questions, please feel free to reach out Augustin Maller (maller@ipgp.fr).
If you use this scaling law, pease make sure to cite our paper, Maller et al. 2023 (in press).
