import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Black Hole Mass
M = 1

def geodesic_eqs(t, y, L):
    """
    Returns the derivatives for (r, phi, pr) with respect to the
    affine parameter (t) for a test particle orbiting a Schwarzschild black hole.

    Parameters
    ----------
    t : float
        Affine parameter (often denoted as τ).
    y : array_like
        State vector [r, phi, pr], where:
            r   = radial coordinate,
            phi = angular coordinate,
            pr  = dr/dτ
    L : float
        Angular momentum of the test particle.

    Returns
    -------
    dydt : list of floats
        Derivatives [dr/dτ, dphi/dτ, dpr/dτ].
    """
    r, phi, pr = y

    # d(phi)/dτ Angular velocity
    dphi_dt = L / r**2

    # dr/dτ Raidal velocity
    dr_dt = pr
    
    # d(pr)/dτ Radial accelaration
    dpr_dt = -M/r**2 + L**2/r**3 - 3*M*L**2/r**4

    return [dr_dt, dphi_dt, dpr_dt]


def simulate_orbit(L, label, t_range, pr0=0.0, r0=10.0, phi0=0.0):
    """
    Solve the geodesic equations for given angular momentum L and label.

    Parameters
    ----------
    L : float
        Angular momentum.
    label : str
        Description for the orbit (for plotting/legend).
    pr0: float
        Initial radial velocity dr/dτ.
    r0 : float
        Initial radius.
    phi0 : float
        Initial angle.
    t_range : float
        Range of affine parameter for integration.

    Returns
    -------
    x, y, r : arrays
        Cartesian coordinates (x, y) and radial coordinate r over the solution.
    """
    # Initial kinematic state
    y0 = [r0, phi0, pr0]

    # Integrate with solve_ivp
    solution = solve_ivp(
        fun=geodesic_eqs,
        t_span=t_range,
        y0=y0,
        args=(L,),
        dense_output=True,
        max_step=0.1
    )

    # Extract r, phi from the solution
    r, phi = solution.y[0], solution.y[1]

    # Convert to cartesian for plotting
    x = r * np.cos(phi)
    y = r * np.sin(phi)

    return x, y, r


def plot_orbit(x, y, orbit_label, orbit_color):
    """
    Plots a single orbit in its own figure.
    
    Parameters
    ----------
    x : array
        x-coordinates of the orbit.
    y : array
        y-coordinates of the orbit.
    orbit_label : str
        Label for the orbit.
    orbit_color : str
        Color to plot the orbit.
    """
    plt.figure(figsize=(8, 8))
    plt.plot(x, y, label=orbit_label, color=orbit_color)
    
    # Draw the black hole (event horizon at r = 2M)
    black_hole = plt.Circle((0, 0), 2*M, color='black', zorder=10)
    plt.gca().add_artist(black_hole)
    
    # Aesthetics
    plt.title(f"Orbit: {orbit_label}")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.gca().set_aspect('equal', adjustable='box')
    plt.grid(True)
    plt.legend()
    plt.xlim(-30, 30)
    plt.ylim(-30, 30)
    plt.show()


def main():
    # List of orbits: L, label, color, and initial radial velocity
    orbits = [
        {'L': 3.780, 'label': 'Circular',   'color': 'green',  'pr0': 0.0, 't_range': [0,1000], 'r0': 10},
        {'L': 3.536, 'label': 'Precessing', 'color': 'blue',  'pr0': 0.0, 't_range': [0,1000], 'r0': 10},
        {'L': 30.500, 'label': 'Scattering', 'color': 'orange', 'pr0': -5.01, 't_range': [0,1000], 'r0': 1000},
        {'L': 3.535, 'label': 'Plunging',   'color': 'red',    'pr0': 0.0, 't_range': [0,1000], 'r0': 10},
    ]

    plt.figure(figsize=(8, 8))

    for orbit in orbits:
        x, y, r = simulate_orbit(
            L=orbit['L'],
            label=orbit['label'],
            pr0=orbit['pr0'],
            t_range=orbit['t_range'],
            r0=orbit['r0']
        )
        plot_orbit(x, y, orbit['label'], orbit['color'])


if __name__ == "__main__":
    main()

