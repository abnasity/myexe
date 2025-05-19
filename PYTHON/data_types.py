# data types in python
Lists = []
tuples = ()
sets = {}
dictionaries = {}
int = 45
float = 5.7
bool = True, False
char = 'A'
string = "Hello"

# Lets talk about dictionaries
# In dictionaries we have both keys and values both in quotes separated by a colon
# Key Features
# 	Key-value pairs, keys are unique, no duplicates, Unordered
Phone = {
    "model": "Samsung",
    "Processor" : "Mediatek",
    "Android version" : "15",
    "Specs" : "Storage 256 Ram 8gb"
}

# List example
# key features
# Ordered, indexable, can contain duplicates
list = ["Mango", "Banana", "Orange"]

# Tuple example
# Key features
# Ordered, immutable, can contain mixed data types
MyTuple = ("Mango", "Banana", "Orange")

# Sets example
# *****Key features*****
# Unordered
# No duplicate elements

MySet = {1, 2, 3, 4, 5}

# Summary key features
# *****💡 Summary by Feature*******
# Feature	Applies To
# Ordered -	List, Tuple, String, Array
# Unordered - 	Set, Dict, Map
# Allows Duplicates	- List, Tuple, Array
# No Duplicates -	Set, Dict keys
# Immutable	- Tuple, String (in Python)
# Mutable -	List, Set, Dict
# Indexed Access - List, Tuple, String, Array
# Keyed Access	- Dict, Map
# Numeric Operations - Int, Float, Decimal
# Text Operations -	String, Char
# Logical Operations -	Boolean
# Date Arithmetic - Date, Time, DateTime