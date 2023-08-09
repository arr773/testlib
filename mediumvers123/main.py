
# # Import Multiplication from your library
# from medium_multi.multi import Multiplication

# # Instantiate a Multiplication object
# multiplication = Multiplication(2)

# # Call the multiply method
# print(multiplication.multiply(5))

# #Steps to publish the library
# #create the dist file
# #python setup.py sdist bdist_wheel
# #python -m twine check dist/*
# #python -m twine upload dist/*
# # username=TestLib
# # password=test_lib
import pandas as pd
from medium_multi.stats import reportgeneration
real_data = pd.read_csv("titanic_train.csv")
synthetic_data = pd.read_csv('gretel_titanic_data.csv')
output="test.pdf"
report=reportgeneration(real_data,synthetic_data)
user_name = input("Enter User Name: ")
tool_used = input("Enter the Tool Used for Synthetic Data Generation: ")
# doc = SimpleDocTemplate(output, pagesize=letter)
report.create_pdf_report(output,user_name,tool_used)