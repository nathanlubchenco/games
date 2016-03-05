from enum import Enum
import networkx as nx
import matplotlib.pyplot as plt

## Game Constants
STARTING_RESOURCES = 100
NODE_BASE_COST = 5
EDGE_BASE_COST = 3
DISTANCE_1_EFFICIENCY = 100
DISTANCE_2_EFFICIENCY = 90 
DISTANCE_3_EFFICIENCY = 80 
DISTANCE_4_EFFICIENCY = 70 
DISTANCE_5_EFFICIENCY = 50 

class Component(Enum):
    engines = 1
    fuel_pod = 2
    core = 3
    # other components 

def show_ship(ship):
    nx.draw(ship)
    plt.show()
# may want to change this to an ascii version of thingsor if going with a javascript move this to a d3 layer?

def add_component(ship, component, connections):
    ## return new ship
    new_ship = ship
# probably existing method for adding multiple edges in some fashion
    for connection in connections:
        new_ship.add_edge(component, connection)
    return new_ship 

def upkeep(ship):
    ## determine upkeep cost based on ship design
# TODO: consider making upkeep based on increased complexity of a node, 3 edges on a single node cost more than 3 edges on multiple nodes
    cost = ship.order() + ship.size()
    return cost 

def random_event():
    ## disaster or boon
    print "nothing happened"

def new_ship():
    ship = nx.Graph()
    ship.add_node(Component.core)
    return ship

