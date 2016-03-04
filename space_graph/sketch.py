from enum import Enum
import networkx as nx

## Game Constants
STARTING_RESOURCES = 100
NODE_BASE_COST = 5
EDGE_BASE_COST = 3

class Component(Enum):
    engines = 1
    fuel_pod = 2
    # other components 

def show_ship(ship):
    ## render ship
    print ship

def add_component(ship, component, connections):
    ## return new ship
    print ship

def upkeep(ship):
    ## determine upkeep cost based on ship design

def random_event():
    ## disaster or boon
