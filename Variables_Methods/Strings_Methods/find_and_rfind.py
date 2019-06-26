
"""
1	find(str, beg=0, end=len(string))
	Search a substring in a given variable or string from left to right.

2	rfind(str, beg=0, end=len(string))
	Search a substring in a given variable or string from right to left.
"""
            #012345678910                         3738
cloud_env = "AWS AZURE GCP Digital Ocean"

substring = "is"

print(cloud_env,len(cloud_env))
print(cloud_env.find(substring))
print(cloud_env.rfind(substring))
