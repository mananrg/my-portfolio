
# Python program to explain os.rmdir() method 
    
# importing os module 
import os
  
# Directory name
directory = "my-portfolio"
  
# Parent Directory
parent = "/var/www/html"
  
# Path
path = os.path.join(parent, directory)
  
  
# Remove the Directory
# "ihritik"
try:
    #os.rmdir(path)
    #print("Directory '%s' has been removed successfully" %directory)
    os.system("sudo rm -rf my-portfolio")
    print("Directory '%s' has been removed successfully" %directory)
    print("Cloning directory from github")
    os.system("sudo git clone https://github.com/mananrg/my-portfolio.git")
    print("Cloned!!!!!")
    print("Restarting Server")
    os.system("sudo service apache2 restart")
    print("Apache Restarted")
except OSError as error:
    print(error)
    print("Directory '%s' can not be removed" %directory)
