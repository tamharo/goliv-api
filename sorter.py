from flask import request,jsonify
import json


from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp



#get data from uri query and init vehicule count and depot(start point)
def get_data():
    """Stores the data for the problem."""
    data = {}
    data['distance_matrix'] = json.loads(str(request.args['round']))
    data['num_vehicles'] = 1
    data['start'] = [int(request.args['start'])]
    data['end'] = [int(request.args['end'])]
    return data

#init resp to array with solution
def resp(manager, routing, solution):
    index = routing.Start(0)
    output = []
    while not routing.IsEnd(index):
        output.append(int(format(manager.IndexToNode(index))))
        index = solution.Value(routing.NextVar(index))
    output.append(int(format(manager.IndexToNode(index))))
    print(output)
    return output


def sorter():
    #get data from Uri query (round)
    data = get_data()

    #create the routing index manager
    manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']),
                                           data['num_vehicles'], data['start'], data['end'])

    #create Routing Model
    routing = pywrapcp.RoutingModel(manager)


    def distance_callback(from_index, to_index):
        """Returns the distance between the two nodes."""
        # Convert from routing variable Index to distance matrix NodeIndex.
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return data['distance_matrix'][from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)

    # Define cost of each arc.
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Setting first solution heuristic.
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

    # Solve the problem.
    solution = routing.SolveWithParameters(search_parameters)

    # Print solution on console.
    if solution:
        return jsonify(resp(manager, routing, solution))
