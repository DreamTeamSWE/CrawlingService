import os

if __name__ == '__main__':
    os.system('coverage run -m unittest discover -p "Test*.py"')
    os.system('coverage html --omit=*testing*,*__init__*')
    os.system('.\\htmlcov\\index.html')
