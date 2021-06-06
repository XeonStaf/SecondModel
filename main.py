import math
import matplotlib.pyplot as plt


config = {}
with open('config.txt', 'r') as f:
    for i in f.readlines():
        inp = i.replace(' ', '').replace('\n', '').split('=')
        config[inp[0]] = float(inp[1])

V_x = config["ElectronSpeed"]
V_y = float(0)

FREQUENCY = 1000
Q = -1.6e-19
M = 9.1e-31
R_1 = config["outCilinderRadius"] - config["distBetweenPlate"]
r = (R_1 + config["outCilinderRadius"]) / 2
x = float(0)
y = r - R_1
a = float(0)

graph_x = []
graph_y = []
graph_t = []
graph_v = []
graph_a = []

dt = int(0)

while x <= config["CondenserLenght"] and r < config["outCilinderRadius"] and r > R_1:

    if dt % FREQUENCY == 0:
        graph_x.append(x)
        graph_y.append(y)
        graph_v.append(math.sqrt(V_x * V_x + V_y * V_y))
        graph_t.append(dt / FREQUENCY)
        graph_a.append(a)
    a = (Q * config["voltage"] / (r * math.log(config["outCilinderRadius"] / (config["outCilinderRadius"] - config["distBetweenPlate"])))) / M
    V_y += a / FREQUENCY
    r += V_y / FREQUENCY
    x += V_x / FREQUENCY
    y = r - R_1
    dt += 1

plt.title("y(x)")
plt.plot(graph_x, graph_y)
plt.savefig('y(x).png')
plt.clf()

plt.title("y(t)")
plt.plot(graph_t, graph_y )
plt.savefig('y(t).png')
plt.clf()

plt.title("v(t)")
plt.plot(graph_t, graph_v)
plt.savefig('v(t).png')
plt.clf()

plt.title("a_y(t)")
plt.scatter(graph_t, graph_a)
plt.savefig('a_y(t).png')


