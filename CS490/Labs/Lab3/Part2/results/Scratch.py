import matplotlib.pyplot as plt 

def read_in_file(file):
    data = []
    with open(file, 'r') as f:
        next(f)
        for line in f:
            l = line.split(',')
            data.append(float(l[2]))
    return data



#Data = read_in_file('1stRun.csv')

#Data = read_in_file('2ndRun.csv')

Data = read_in_file('C:\\Users\\thoma\\Desktop\\Lab3\\Part2\\results\\6thRun.csv')
steps = []
for x in range (0,len(Data)):
    steps.append(x * 1000)


#plt.plot(steps, Data, label="Adam")
#plt.plot(steps, Data, label="RMSProp", color="red")
plt.plot(steps, Data, label="Gradient", color='green')
plt.ylabel("Loss")
plt.xlabel("Steps")
plt.legend()
plt.show()