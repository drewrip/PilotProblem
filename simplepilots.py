import random
import matplotlib.pyplot as plt

# Number of simulations to run
trials = 1000000

# Defining the procedure for the simulation
def sim():
    # Representation of the hat that holds the male/female papers
    hat = ['m', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f']
    num_males = 0
    for i in range(1, 9):
        pick = random.randint(0,len(hat)-1)
        if(hat[pick] == 'm'):
            num_males += 1

        del hat[pick]
    return {"males": num_males, "females": 8-num_males}

#distribution of simulations (in number of females)
distribution = dict([(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0)])
for i in range(1,1000000):
    data = sim()
    distribution[data["females"]] += 1

for i in range(1, 9):
    print(str(i) + " Females: " + str(distribution[i]))

lists = sorted(distribution.items()) # sorted by key, return a list of tuples

x, y = zip(*lists) # unpack a list of pairs into two tuples
plt.plot(x, y)
plt.ylabel("# of Simulations")
plt.xlabel("# of Females")
plt.title(str(trials) + " Simulations Of The Pilot Problem")
plt.show()
