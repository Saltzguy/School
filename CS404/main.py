#%%
import random
from datetime import datetime
from Graph import Graph

def generate_vehicle(locations: set, num: int) -> list:
    random.seed(datetime.now())
    return random.sample(locations, num)
   

# returns a generator for unlimited request  
def generate_request(locations: set):
       index = 0
       while True:
            index += 1
            random.seed(datetime.now())
            rand_vehicle = random.randint(0,2)
            rand_locations = random.sample(locations,1)
            yield index, rand_vehicle, rand_locations[0]
        
        
def find_closest_vehicle(vehicles: list, destination: int, graph: Graph):
    vehicle_index = -1
    path = []
    dist = 500
    for x in range(len(vehicles)):
       temp_path , temp_dist = graph.shortest_path(vehicles[x],destination)
       if temp_path is not None:
            if dist > temp_dist:
                path = temp_path
                vehicle_index = x
                dist = temp_dist
    if vehicle_index < 0:
        vehicle_index, dist, path = None, None, None
    return vehicle_index, dist, path
        




# set of the available zip codes
locations = {64151, 64152, 64153, 64154, 64155, 64156, 64157, 64158, 64159, 64160,64161, 64162, 64163}
graph = Graph()
graph.add_nodes(locations)
# generate a random undirected connnected graph max weight 5, extra edges 5
graph.generate_random_undirected_graph(5, 5)
print(graph)

# generates request
requests = generate_request(locations)

#number of police , ambulance and firetrucks
vehicle_num = 3

# The list of available vehicles.
firetrucks = generate_vehicle(locations,vehicle_num)
police = generate_vehicle(locations,vehicle_num)
ambulance = generate_vehicle(locations,vehicle_num)

#
history = []

for _ in range(10):
    
    path = [] # not in use right now.
    start = 0
    dist = -1
    start_loc = -1
    index, vehicle_type, request_loc = next(requests)
    
    if vehicle_type == 0:
        vehicle_type = "FireTruck"
        vehicle_index, dist, path = find_closest_vehicle(firetrucks,request_loc,graph)
        
        if vehicle_index is not None:
            start_loc = firetrucks[vehicle_index]
            firetrucks[vehicle_index] = request_loc
    
    elif vehicle_type == 1:     
        vehicle_type = "Police car"
        vehicle_index, dist, path = find_closest_vehicle(police,request_loc,graph)
        
        if vehicle_index is not None:
            start_loc = police[vehicle_index]
            police[vehicle_index] = request_loc

    else:
        vehicle_type = "Ambulance"
        vehicle_index, dist, path = find_closest_vehicle(ambulance,request_loc,graph)
        
        if vehicle_index is not None:
            start_loc = ambulance[vehicle_index]
            ambulance[vehicle_index] = request_loc
    
    history.append([index, vehicle_type, vehicle_index, start_loc, request_loc, dist])
   
    #print("Request for {} to location {}".format(vehicle_type, request_loc))
    #print("{0} {1} at {2} traveling to {3} by way of {4} will take {5} time \n".format(vehicle_type,vehicle_index,start_loc, request_loc,path, dist))

for index in history:
    print(index)