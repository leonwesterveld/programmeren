from ntpath import join
import random



def my_function(original):
  randomised = ''.join(random.sample(original, len(original)))
  return randomised

print(my_function(original = input("type iets\n")))