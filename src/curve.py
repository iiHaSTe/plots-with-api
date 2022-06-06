
import matplotlib.pyplot as plt
from dbMannager import DataBaseManager

conn = DataBaseManager("../data/users.sqlite")


my_credits = []
ages = []
levels = []

rows = conn.getRows("user")

for row in rows:
	my_credits.append(row[-1])
	levels.append(row[-2])


plt.subplot(3, 1, 2)
plt.plot(levels)
plt.xlabel("levels")

plt.subplot(3, 1, 1)
plt.plot(my_credits)
plt.xlabel("credits")

plt.show()
