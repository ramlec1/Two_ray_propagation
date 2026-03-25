# Two ray propagation models

A script demonstrating the two ray propagation model in various forms of difficulty.
1. The "simple" model follows the standard derivation of the two ray model including the condition that d >> h_TX and d >> h_RX, where the reflection causes a phase flip (gamma=-1). The two rays are added coherently in the way that they are assumed parallel to eachother.
2. The coherent addition model adds an reflection coefficient.
3. The "advanced" model takes the different angles of incidence on the receiver into account. This is done by directly calculating the cross product in the Poynting vector. Also the actual reflection coefficients are calculated.

See the accompanying PDF for the derivations and further explanation.

Currently still working out some stuff with the reflection coefficients...
The derivation including the complex part (Jordan's book) gives some weird out of phase answers between polarizations in the advanced model.
Jordan's equations implementation also results in a return to 1/d**2 behaviour at a distance beyond r_break.
For now the equations by Kraus and Carver seems to work fine.

