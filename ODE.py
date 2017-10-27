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
        error.append(explicitEulerSpring( x0,v0,t,h0 / i))
        h.append(h0/i)
    plt.plot(h,error)
    plt.title("Absolute Error vs h")
    plt.xlabel("h")
    plt.ylabel("Absolute Error")
    plt.show()

explicit = explicitEulerSpring(0,20,50,.05)
implicit = implicitEulerSpring(0,20,50,.05)
symplectic = symplecticEulerSpring(0,20,50,.05)

plt.plot(implicit[1],implicit[2])
plt.title("Phase Space")
plt.xlabel("Position [m]")
plt.ylabel("Velocity [m/s]")
plt.show()
