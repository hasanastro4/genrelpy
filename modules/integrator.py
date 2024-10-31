from abc import ABC, abstractmethod

#base class 
class integrator(ABC):
    @abstractmethod
    def step(x,p,dt):
       pass


#derived class -> leapfrog
class leapfrog(integrator):
    def __init__(self, sptm):
        self.sptm = sptm
    def step(self, x, p, dt):
        p = p - 0.5* self.sptm.dHdx(x,p)*dt
        x = x +      self.sptm.dHdp(x,p)*dt
        p = p - 0.5* self.sptm.dHdx(x,p)*dt
        return x,p

