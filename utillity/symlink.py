# importing os module  
import os 
  
  
# Source file path 
src = 'g:/vfx/assets/ttp'
  
# Destination file path 
dst = 'f:/vfx/projects/houdini/asset'
  
# Create a symbolic link 
# pointing to src named dst 
# using os.symlink() method 
os.symlink(src, dst) 
  
print("Symbolic link created successfully") 