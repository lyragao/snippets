# approaches to find a random point in a circle.
# code stolen from nubdobdev: https://www.youtube.com/watch?v=4y_nmpv-9lI 

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
