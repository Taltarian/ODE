import numpy as np, matplotlib.pyplot  as plt, math


def explicitEulerSpring(x0,v0,t,h):
    t = np.linspace(0,t,t/h)
    x = [x0]
    v = [v0]
    E = [v0 ** 2 + x0 ** 2]
    xReal = 20 * np.cos(t - np.pi/2)
    vReal = -20 * np.sin(t - np.pi/2)
    xError = []
    vError = []
    for i,e in enumerate(t):
        if i > 0:
            x.append(x[i - 1] + v[i -1] * h)
            v.append(v[i - 1] - x[i -1] * h)
            E.append(v[i] ** 2 + x[i] ** 2)
        xError.append(abs(xReal[i] - x[i]))
        vError.append(abs(vReal[i] - v[i]))
    return (t,x,v,E,xReal,vReal,xError,vError)

def implicitEulerSpring(x0,v0,t,h):
    t = np.linspace(0,t,t/h)
    xReal = x0 * np.cos(t)
    vReal = -x0 * np.sin(t)
    x = [x0]
    v = [v0]
    E = [v0 ** 2 + x0 ** 2]
    xReal = 20 * np.cos(t - np.pi/2)
    vReal = -20 * np.sin(t - np.pi/2)
    xError = []
    vError = []
    for i,e in enumerate(t):
        if i > 0:
            x.append((x[i - 1] + v[i -1] * h) / (1 + h ** 2))
            v.append(v[i - 1] - x[i] * h)
            E.append(v[i] ** 2 + x[i] ** 2)
        xError.append(abs(xReal[i] - x[i]))
        vError.append(abs(vReal[i] - v[i]))
    return (t,x,v,E,xReal,vReal,xError,vError)


def symplecticEulerSpring(x0,v0,t,h):
    t = np.linspace(0,t,t/h)
    x = [x0]
    v = [v0]
    E = [v0 ** 2 + x0 ** 2]
    xReal = 20 * np.cos(t - np.pi/2)
    vReal = -20 * np.sin(t - np.pi/2)
    xError = []
    vError = []
    for i,e in enumerate(t):
        if i > 0:
            x.append(x[i - 1] + v[i -1] * h)
            v.append(v[i - 1] - x[i] * h)
            E.append(v[i] ** 2 + x[i] ** 2)
    xError.append(abs(xReal[i] - x[i]))
    vError.append(abs(vReal[i] - v[i]))
    return (t,x,v,E,xReal,vReal,xError,vError)

def hError(x0, v0, t, h0):
    h = []
    error = []
    for i in range(0,17,2):
        if i == 0:
             i = 1
        xe = explicitEulerSpring(x0,v0,t,h0 / i)
        xe = max(xe[6])
        error.append(xe)
        h.append(h0 / i)
    plt.plot(h, error)
    plt.title("Absolute Error vs h")
    plt.xlabel("h")
    plt.ylabel("Absolute Error")
    plt.savefig('Error_v_h.png')
    plt.close()

explicit = explicitEulerSpring(0,20,50,.05)
implicit = implicitEulerSpring(0,20,50,.05)
symplectic = symplecticEulerSpring(0,20,50,.05)

plt.plot(explicit[0],explicit[1])
plt.title("Position vs Time")
plt.xlabel("Time [s]")
plt.ylabel("Position [m]")
plt.savefig('xvt.png')
plt.close()

plt.plot(explicit[0],explicit[2])
plt.title("Velocity vs Time")
plt.xlabel("Time [s]")
plt.ylabel("Velocity [m/s]")
plt.savefig('vvt.png')
plt.close()

plt.plot(explicit[0],explicit[6])
plt.title("Position Error vs Time")
plt.xlabel("Time [s]")
plt.ylabel("Position Error [m]")
plt.savefig('xerror.png')
plt.close()

hError(0,20,50,.05)

plt.plot(explicit[0],explicit[3])
plt.title("Energy vs Time")
plt.xlabel("Time [s]")
plt.ylabel("Energy")
plt.savefig('ExplicitEnergy.png')
plt.close()

plt.plot(explicit[0],explicit[3])
plt.title("Phase Space")
plt.xlabel("Position [m^2]")
plt.ylabel("Velocity [m/s ^2]")
plt.savefig('ExplicitPhaseSpace.png')
plt.close()

plt.plot(implicit[0],implicit[6])
plt.title("Position Error vs Time")
plt.xlabel("Time [s]")
plt.ylabel("Position Error [m]")
plt.savefig('implicitError.png')
plt.close()

plt.plot(implicit[0],implicit[3])
plt.title("Phase Space")
plt.xlabel("Position [m^2]")
plt.ylabel("Velocity [m/s ^2]")
plt.savefig('ImplicitPhaseSpace.png')
plt.close()

plt.plot(symplectic[0],symplectic[3])
plt.title("Phase Space")
plt.xlabel("Position [m^2]")
plt.ylabel("Velocity [m/s ^2]")
plt.savefig('SymplecticPhaseSpace.png')
plt.close()
