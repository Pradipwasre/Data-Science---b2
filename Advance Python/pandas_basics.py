# =====================================================
#  GETTING STARTED WITH PANDAS  
# =====================================================

# -----------------------------------------------------
# 1. WHAT IS PANDAS?
# -----------------------------------------------------
# Pandas is a Python library used to work with DATA (tables, like Excel).
# Why we use it:
#   - Read data from files (CSV, Excel)
#   - Clean data, filter data, calculate things quickly
#   - Much easier than writing long loops

# -----------------------------------------------------
# 2. INSTALLING PANDAS  (run in the VS Code terminal, NOT in .py file)
# -----------------------------------------------------
#   pip install pandas
#   pip install numpy
#   pip install openpyxl     <- needed only for Excel files
#
#   (If you use Anaconda:  conda install pandas)

# -----------------------------------------------------
# 3. IMPORTING PANDAS
# -----------------------------------------------------
import pandas as pd   # "pd" is a short nickname everyone uses
import numpy as np    # we need numpy for some examples

# Example: check that pandas is installed
print("Pandas version:", pd.__version__)


# =====================================================
# PART A: PANDAS DATA STRUCTURES
# =====================================================
# Pandas has 2 main structures:
#   Series    -> ONE column of data (1-dimensional)
#   DataFrame -> a full TABLE with rows and columns (2-dimensional)


# =====================================================
# PART B: CREATING A SERIES
# =====================================================

# ---------- B1. Series from a Python list ----------
print("\n--- B1. Series from a list ---")

marks = [80, 90, 70]          # a normal Python list
s1 = pd.Series(marks)         # convert the list into a Series
print(s1)                     # left side = index (0,1,2), right side = values

# ---------- B2. Series from a list with our OWN index ----------
print("\n--- B2. Series with custom index ---")

s2 = pd.Series([80, 90, 70], index=["Ravi", "Sita", "Raju"])
print(s2)                     # now the labels are names, not 0,1,2
print(s2["Sita"])             # get a value using the label -> 90

# ---------- B3. Series from a NumPy array ----------
print("\n--- B3. Series from a NumPy array ---")

arr = np.array([10, 20, 30])  # create a NumPy array
s3 = pd.Series(arr)           # convert the array into a Series
print(s3)

# ---------- B4. Series from a dictionary ----------
print("\n--- B4. Series from a dictionary ---")

fruits = {"Apple": 100, "Banana": 40, "Mango": 80}   # key = label, value = data
s4 = pd.Series(fruits)        # dictionary KEYS become the index automatically
print(s4)


# =====================================================
# PART C: CREATING A DATAFRAME
# =====================================================

# ---------- C1. DataFrame from a list of dictionaries ----------
print("\n--- C1. DataFrame from list of dictionaries ---")

# Each dictionary = ONE ROW of the table
students = [
    {"Name": "Ravi", "Age": 20},
    {"Name": "Sita", "Age": 21},
    {"Name": "Raju", "Age": 19},
]
df1 = pd.DataFrame(students)
print(df1)

# ---------- C2. DataFrame from a dictionary of lists ----------
print("\n--- C2. DataFrame from dictionary of lists ---")

# Each key = COLUMN name, each list = values of that column
data = {
    "Name": ["Ravi", "Sita", "Raju"],
    "Age": [20, 21, 19],
    "City": ["Delhi", "Pune", "Goa"],
}
df2 = pd.DataFrame(data)
print(df2)

# ---------- C3. DataFrame from a NumPy array ----------
print("\n--- C3. DataFrame from NumPy array ---")

arr2 = np.array([[1, 2, 3],
                 [4, 5, 6]])   # 2 rows and 3 columns
# NumPy has no column names, so we give them using columns=[...]
df3 = pd.DataFrame(arr2, columns=["A", "B", "C"])
print(df3)


# =====================================================
# PART D: DATAFRAME FROM EXTERNAL FILES (Brief Intro)
# =====================================================

# First, let's save our small table as a CSV file so we have a file to read
df2.to_csv("students.csv", index=False)   # index=False -> don't save 0,1,2 numbers
print("\nstudents.csv file created in your folder!")

# ---------- D1. Read a CSV file ----------
print("\n--- D1. Reading a CSV file ---")

df_csv = pd.read_csv("students.csv")      # read the file into a DataFrame
print(df_csv)

# ---------- D2. Read an Excel file ----------
print("\n--- D2. Reading an Excel file ---")

df2.to_excel("students.xlsx", index=False)    # save as Excel (needs openpyxl)
df_excel = pd.read_excel("students.xlsx")     # read the Excel file
print(df_excel)

# ---------- D3. Quick look at the data ----------
print("\n--- D3. head() shows first 2 rows ---")

print(df_csv.head(2))     # head(n) = first n rows. Very useful for big files!

# =====================================================
#  END OF CLASS  -  Great job, everyone! 
# =====================================================
