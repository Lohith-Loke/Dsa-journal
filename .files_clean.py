import os

dir_name = "D:\intern\leetcode"
test = os.listdir(dir_name)

for item in test:
    if item.endswith(".exe"):
        os.remove(os.path.join(dir_name, item))