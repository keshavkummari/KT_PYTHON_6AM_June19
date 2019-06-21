redhat=1

while (redhat<10):# True condition and it will execute until false condition encounters
    print (f"{redhat}")
    if redhat == 5:
        print(f"Condition is met {redhat}")
        break
    else:
        print("I am executing else block")
        redhat=redhat+1

print ("")
print ("We are out of the while block")  
