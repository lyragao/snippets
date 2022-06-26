# i want to pick a random point in a circle.
# NOT MY CODE THIS CODE WAS STOLEN FROM BELOW.
# code stolen from nubdobdev: https://www.youtube.com/watch?v=4y_nmpv-9lI 

import random

# METHOD 1: REJECTION SAMPLING.
# pick a random x and y coordinate inside a square.
# if it's outside of the circle, try again. 
def rejection_sampling(): 
  while True: 
    x = random() * 2 - 1
    y = random() * 2 - 1
    if x * x + y * y < 1: 
      return x, y

# METHOD 2: POLAR COORDINATES. 
# this produces points concentrated in the center. 
def random_polar(): 
  theta = random() * 2 * pi
  r = random()
  return r * cost(theta), r * sin(theta)

# METHOD 3: INVERSE TRANSFORM SAMPLING.
# fix the problem of greater density in the center by applying 
# an inverse pdf, which in this case is sqrt(r). 
def sqrt_dist(): 
  theta = random() * 2 * pi
  r = sqrt(random())
  return r * cos(theta), r * sin(theta)

# METHOD 4: TRIANGLES
# view circle as infinitely many isoceles triangles. 
# to select a random point, pick a random triangle and a 
# random point in the triangle. 
def sum_dist(): 
  theta = random() * 2 * pi
  r = random() + random()
  if r >= 1: 
    r = 2 - r
  return r * cos(theta), r * sin(theta) 

# METHOD 5: MAX OF 2 UNIFORM RVS
  theta = random() * 2 * pi
  r = random()
  x = random()
  if x > r: 
    r = x
  return r * cos(theta), r * sin(theta)
