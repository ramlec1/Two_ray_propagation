# Two ray propagation models

A script demonstrating the two ray propagation model in various forms of difficulty.

1. The "simple" model follows the standard derivation of the two ray model including the condition that d >> h_TX and d >> h_RX, where the reflection causes a phase flip (gamma=-1). The two rays are added coherently in the way that they are assumed parallel to eachother.
2. The coherent addition model adds a reflection coefficient.
3. The "advanced" model takes the different angles of incidence on the receiver into account. This is done by directly calculating the cross product in the Poynting vector. Also the actual reflection coefficients are calculated.

See the accompanying PDF for the derivations and further explanation.

# NOTICE
The E-field notebook is not finished and should not be used. It is a work in progress to add E-field vector as an output. The other script give a scalar power at receiver result. This would make it possible to add antenna gain into the equation. 
