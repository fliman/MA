import numpy as np

#Monge-Ampere equation solver




class grid:
	def __init__(self, xgrid, ygrid=[0.0, 0.0, 1.0] ,zgrid=[0.0, 0.0, 1.0]):
		self.xgrid = xgrid
		self.ygrid = ygrid
		self.zgrid = zgrid
		self.dx = self.xgrid[2]
		self.dy = self.ygrid[2]
		self.dz = self.zgrid[2]	
		
class MASolver:
	def __init__(self, grid):
		self.grid = grid
		self.X, self.Y = np.meshgrid(np.arange(self.grid.xgrid[0], self.grid.xgrid[1], self.grid.xgrid[2]), 
			                         np.arange(self.grid.ygrid[0], self.grid.ygrid[1], self.grid.ygrid[2]))

		self.u = np.zeros(self.X.shape)

	def initialize(self):
		self.u =np.zeros(self.X.shape)	

	def printInfo(self):
		print "dx %s, dy %s, dz %s\n"%(self.grid.dx, self.grid.dy, self.grid.dz)

	def Dxx(self):
		shape = self.u.shape
		res = np.zeros(shape)
		res[:,1:shape[1]-2] = (self.u[:,0:shape[1] - 3] + self.u[:,2:shape[1]-1] - 2.0 * self.u[:,1:shape[1]-2]) / self.grid.dx /self.grid.dx
		return res	

	def Dyy(self):
		shape = self.u.shape
		res = np.zeros(shape)
		res[1:shape[0]-2,:] = (self.u[0:shape[0] - 3,:] + self.u[2:shape[0]-1,:] - 2.0 * self.u[1:shape[0]-2,:]) / self.grid.dy / self.grid.dy
		return res	

	def Dxy(self):
		shape = self.u.shape
		res = np.zeros(shape)
		res[1:shape[0]-2, 1:shape[1]-2] = (self.u[0:shape[0] - 3, 0:shape[1]-3] - self.u[0:shape[0] - 3, 2:shape[1]-1]  + 
			                               self.u[2:shape[0] - 1, 2:shape[1]-1] - self.u[2:shape[0] - 1, 0:shape[1]-3] ) / self.grid.dy / self.grid.dx / 4.0
		return res

	def Dx(self):
		shape = self.u.shape
		res = np.zeros(shape)
		res[:, 1:shape[1]-2] = (self.u[:, 2:shape[1] - 1] - self.u[:, 0:shape[1] - 3]) / self.grid.dx / 2.0
		return res				
	
	def Dy(self):
		shape = self.u.shape
		res = np.zeros(shape)
		res[1:shape[0]-2, :] = (self.u[2:shape[0] - 1, :] - self.u[0:shape[0] - 3, :]) / self.grid.dy / 2.0
		return res		

	def solve(self):
		print self.Dxx().shape
		print self.Dxy().shape
