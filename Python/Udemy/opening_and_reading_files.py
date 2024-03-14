import os

# Print the current working directory
print("Current Working Directory: ", os.getcwd())

# Change the current working directory to where the file is located
# Adjust the path as per your file's location
os.chdir('C:/Users/LUSCHNIG/OneDrive_privat/OneDrive/Leistung/CISCO/ENCOR_LAB/Python/Udemy')

# Now, try opening the file
f = open('configuration.txt', 'rt')
content = f.read()
print(content)

f.close()  # It's a good practice to close the file after reading
