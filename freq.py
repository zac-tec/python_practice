data=input("enter a list")
data=data.split()
freq={}
for i in data:
     if i in freq:
         freq[i]=freq[i]+1
     else:
         freq[i]=1       
         
print(freq)         