# relativity_coding_project

Modeling Plunging, Scattering, Circular, and Precessing Timelike Geodesics in Schwarzschild Spacetime
by Charles Campbell
ASTR 471
Sean McWilliams
Due: April 16, 2025

 This code models four different timelike geodesics in M=1 Schwarzschild spacetime as a function of initial angular momentum and radial velocity. Scipy.integrate is used to numerically integrate two ODEs that are derived from the effective potential.
	
 The first ODE, the radial acceleration equation, is derived by taking the derivative of the effective potential with respect to the affine parameter.
	
 The second ODE is determined from the observation that the Schwarzschild metric is spherically symmetric, and solving Killing's equation leads to a conserved quantity that governs the angular evolution of the geodesic.

The code shows that varying different values of the angular momentum and initial radial velocity parameters lead to different orbital states. To have a scattering orbit, it was necessary to have very large angular velocities and initial radial velocities. To generate the other orbital states, small nonzero angular momenta were sufficient.

Figures of the code output can be found by running the code. AI was used for generating the initial code architecture, but the mathematical model was written by the student and debugging was performed by the student.




