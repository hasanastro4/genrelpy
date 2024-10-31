from abc import ABC, abstractmethod

# base class
class spacetime(ABC):
    @abstractmethod
    def H(x,p):
        pass

    @abstractmethod
    def dHdx(x,p):
        pass

    @abstractmethod
    def dHdp(x,p):
        pass

# derived class -> schwarzschild
class schwarzschild(spacetime):
    def __init__(self, M):
        self.M = M
        self.rs = 2*M

    def Ms(self):
        return self.M

    def Rs(self):
        return self.rs

    def H(self, x, p):
        ir   = 1/x[1]        # 1/r
        irq  = ir*ir         # 1/r^2
        rsor = self.rs/x[1]  # 2M/r
        umrs = 1 - rsor      # 1 - 2M/r
        iumr = 1/umrs        # 1/(1-2M/r)
        return 0.5*(-iumr*p[0]*p[0] + umrs*p[1]*p[1] + irq*(p[2]*p[2] +
                    p[3]*p[3]/sin(x[2])**2))

    def dHdx(self, x, p, const=0):
        ir   = 1/x[1]        # 1/r
        irq  = ir*ir         # 1/r^2
        rsor = self.rs/x[1]  # 2M/r
        umrs = 1 - rsor      # 1 - 2M/r
        iumr = 1/umrs        # 1/(1-2M/r)
        iumq = iumr*iumr     # 1/(1-2M/r)^2
        dHdx0 = 0.
        dHdx1 = self.M * irq * (iumq*p[0]*p[0]+ p[1]*p[1]) - ir*irq*(p[2]*p[2] +
                                                         p[3]*p[3]/sin(x[2])**2)
        dHdx2 = - irq*p[3]*p[3]/sin(x[2])**2/tan(x[2])
        dHdx3 = 0.
        return np.array([dHdx0, dHdx1, dHdx2, dHdx3])

    def dHdp(self, x, p, const=0):
        ir   = 1/x[1]        # 1/r
        irq  = ir*ir         # 1/r^2
        rsor = self.rs/x[1]  # 2M/r
        umrs = 1 - rsor      # 1 - 2M/r
        iumr = 1/umrs        # 1/(1-2M/r)
        dHdp0 = -iumr*p[0]
        dHdp1 =  umrs*p[1]
        dHdp2 =  irq *p[2]
        dHdp3 =  irq *p[3]/sin(x[2])**2
        return np.array([dHdp0, dHdp1, dHdp2, dHdp3])
