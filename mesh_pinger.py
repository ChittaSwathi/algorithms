import ping3
import netifaces
import nmap
import networkx as nx
import matplotlib.pyplot as plt

# Get network interfaces and IP addresses
interfaces = netifaces.interfaces()
for iface in interfaces:
    addrs = netifaces.ifaddresses(iface)[netifaces.AF_INET]
    for addr in addrs:
        ip = addr['addr']

# Scan network for active devices
nm = nmap.PortScanner()
nm.scan(hosts=ip + '/24', arguments='-sP')

# Ping discovered devices
G = nx.Graph()
for host in nm.all_hosts():
    G.add_node(host)
    rtt = ping3.ping(host)
    if rtt:
        G.add_edge(ip, host)

# Visualize network performance
node_colors = [rtt['avg'] if rtt else 0 for node in G.nodes()]
nx.draw(G, node_color=node_colors, with_labels=True)
plt.show()