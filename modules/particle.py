import numpy as np

class particle():
    def __init__(self, x, p, m=1):
        if isinstance(x,list):
            x = np.array(x)
        if isinstance(p,list):
            p = np.array(p)
        self.__mass= m
        self.__coor = x
        self.__mome = p

    def get_mass(self):
        return self.__mass

    def get_pos(self):
        return self.__pos

    def get_mom(self):
        return self.__mome

    def set_mass(self,m):
        self.__mass = m

    def set_pos(self,x):
        self.__coor = x

    def set_mom(self,p):
        self.__mome = p

    def set_phase_space(self, x, p):
        self.set_pos(x)
        self.set_mom(p)

class particles():
    r"""class representing a bunch of particles (N-part)
        
    """
    def __init__(self):
        self.__N=0
        self.__member=[]
	
    def add(self, b):
        r""" append a particle to particles
        
        """
        self.__member.append(b)
        self.__N +=1
		
    def member(self):
        r""" return a list of particle to particles
        
        """
        return self.__member

    def number(self):
        r""" return number of particles
        
        """
        return len(self.__member)

#friends
def mass(part):
    return part.get_mass()

def pos(part):
    return part.get_pos()

def mom(part):
    return part.get_mom()

