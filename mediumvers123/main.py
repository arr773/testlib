
# Import Multiplication from your library
from medium_multi.multi import Multiplication

# Instantiate a Multiplication object
multiplication = Multiplication(2)

# Call the multiply method
print(multiplication.multiply(5))

#Steps to publish the library
#create the dist file
#python setup.py sdist bdist_wheel
#python -m twine check dist/*
#python -m twine upload dist/*
# username=TestLib
# password=test_lib