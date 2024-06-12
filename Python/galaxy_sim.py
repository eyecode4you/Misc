#galaxy_sim.py
import tkinter as tk
from random import randint, uniform, random
import math

SCALE = 255
#set up display canvas
root = tk.Tk()
root.title("Milky Way Galaxy")
c = tk.Canvas(root, width=1000, height=800, bg='black')
c.grid()
c.configure(scrollregion=(-500, -400, 500, 400))

#Milky Way dimensions (light years)
DISC_RADIUS = 50000
DISC_HEIGHT = 1000
DISC_VOL = math.pi * DISC_RADIUS**2 * DISC_HEIGHT

#Scaling the Galaxy
def scale_galaxy():
	"""Scale galaxy dimensions based on radio bubble size (scale)"""
	disc_radius_scaled = round(DISC_RADIUS / SCALE)
	bubble_vol = 4/3 * math.pi * (SCALE / 2)**3
	disc_vol_scaled = DISC_VOL/bubble_vol
	return disc_radius_scaled, disc_vol_scaled
	
#Using Polar Coordinates
def random_polar_coordinates(disc_radius_scaled):
	"""Generate a uniform random (x, y) point within a disc for 2D display"""
	r = random()
	theta = uniform(0, 2 * math.pi)
	x = round(math.sqrt(r) * math.cos(theta) * disc_radius_scaled)
	y = round(math.sqrt(r) * math.sin(theta) * disc_radius_scaled)
	return x, y
	
#Building Spiral Arms
def spirals(b, r, rot_fac, fuz_fac, arm):
	"""Build spiral arms for tkinter display using logarithmic spiral equation
	
	b = arbitrary constant in logarithmic spiral equation
	r = scaled galactic disc radius
	rot_fac = rotation factor
	fuz_fac = random shift in star position in arm - fuzz variable
	arm = spiral arm (0 = main arm, 1 = trailing stars)
	"""
	
	spiral_stars = []
	fuzz = int(0.030 * abs(r))# randomly shift star locations
	theta_max_degrees = 520
	for i in range(theta_max_degrees): #range(0, 600, 2) for no black hole
		theta = math.radians(i)
		x = r * math.exp(b * theta) * math.cos(theta + math.pi * rot_fac)\
			+ randint(-fuzz, fuzz) * fuz_fac
		y = r * math.exp(b * theta) * math.sin(theta + math.pi * rot_fac)\
			+ randint(-fuzz, fuzz) * fuz_fac
		spiral_stars.append((x, y))
	for x, y in spiral_stars:
		if arm == 0 and int(x % 2) == 0:
			c.create_oval(x-2, y-2, x+2, y+2, fill='purple', outline='')
		elif arm == 0 and int(x % 2) != 0:
			c.create_oval(x-1, y-1, x+1, y+1, fill='yellow', outline='')
		elif arm == 1:
			c.create_oval(x, y, x, y, fill='red', outline='')
			
			
#Scattering Star Haze
def star_haze(disc_radius_scaled, density):
	"""Randomly distribute faint tkinter stars in galactic disc
	disc_radius_scaled = galactic disc radius scaled to radio bubble diameter
	density = multiplier to vary no. of stars posted
	"""
	
	for i in range(0, disc_radius_scaled * density):
		x, y = random_polar_coordinates(disc_radius_scaled)
		c.create_text(x, y, fill='green', font=('Helvetica', '7'), text='.')
		
#Defining the main() Function
def main():
	"""Calculate detection probability & post galaxy display & stats"""
	for i in range(250):
		disc_radius_scaled, disc_vol_scaled = scale_galaxy()
			
		#build 4 main spiral arms & 4 trailing arms
		spirals(b=-0.3, r=disc_radius_scaled, rot_fac=2, fuz_fac=1.5, arm=0)    
		spirals(b=-0.3, r=disc_radius_scaled, rot_fac=1.91, fuz_fac=1.5, arm=1)    
		spirals(b=-0.3, r=-disc_radius_scaled, rot_fac=2, fuz_fac=1.5, arm=0)    
		spirals(b=-0.3, r=-disc_radius_scaled, rot_fac=-2.09, fuz_fac=1.5, arm=1)    
		spirals(b=-0.3, r=-disc_radius_scaled, rot_fac=0.5, fuz_fac=1.5, arm=0)    
		spirals(b=-0.3, r=-disc_radius_scaled, rot_fac=0.4, fuz_fac=1.5, arm=1)    
		spirals(b=-0.3, r=-disc_radius_scaled, rot_fac=-0.5, fuz_fac=1.5, arm=0)    
		spirals(b=-0.3, r=-disc_radius_scaled, rot_fac=-0.6, fuz_fac=1.5, arm=1)    
		star_haze(disc_radius_scaled, density=8)
					
		#run tkinter loop
		#root.mainloop()
		root.update()
		root.update_idletasks()
		c.delete('all')
		print("a")
		
if __name__ == "__main__":
	main()
	
