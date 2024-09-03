import numpy as np
import matplotlib.pyplot as plt


def main():
    # input parameters
    h_tx = 2 # transmitter height (meter)
    h_rx = 1 # receiver height (meter)
    d = np.linspace(10, 100, 100001) # horizontal seperation distance (meter)
    f = 30 * 1e9 # frequency (MHz)
    P_t = 1 # transmitter power EIRP (Watt)
    e_r = 15 # relative permittivity of the soil (only real part) ITU-R P.527-4 & Wireless communications principles and practice 2nd edition, theodore rappaport

    # calculate parameters
    c0 = 299792458. # speed of light
    Z0 = 376.73 # free space impedance
    r_los = np.sqrt(d**2 + (h_tx-h_rx)**2) # distance RX-TX of LOS wave
    r_ref = np.sqrt(d**2 + (h_tx+h_rx)**2) # distance RX-TX of reflected wave
    t = r_los/c0 # set t=0 wrt los e field
    E_1m = np.sqrt(Z0 * P_t / (4*np.pi)) # E-field strength coefficient from P_eirp
    theta = np.arctan((h_tx+h_rx) / d) # angle of incidence
    gamma_par = (-e_r * np.sin(theta) + np.sqrt(e_r - np.cos(theta)**2)) / (e_r*np.sin(theta) + np.sqrt(e_r - np.cos(theta)**2)) # reflection los parallel polarization check theodore book eq 3.24 and 3.25 
    gamma_trans = (np.sin(theta) - np.sqrt(e_r - np.cos(theta)**2)) / (np.sin(theta) + np.sqrt(e_r - np.cos(theta)**2)) # reflection los transverse polarization
    gamma = gamma_par + gamma_trans # reflection loss

    E_los =  E_1m / r_los * np.cos(2*np.pi*f * (t - r_los/c0)) # E-field at RX from LOS wave
    E_ref = E_1m / r_ref * gamma * np.cos(2*np.pi*f * (t - r_ref/c0)) # E-field at RX from reflected wave

    fig, ax = plt.subplots()
    ax.plot(d, (E_los+E_ref)**2)
    ax.set_xscale('log')
    ax.set_yscale('log')
    plt.show()

    print(E_los)
    



if __name__ == "__main__":
    main()