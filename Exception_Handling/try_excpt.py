
import sys
import os

def platform_check():
	assert('darwin' in sys.platform), "This Code Executes Only on Linux Operating System"
	print("Welcome to Python World")

try:
	platform_check()
except:
	print(f"This is not a Linux OS {os.uname}")
	print(f"sys.platform()")
