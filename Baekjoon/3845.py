# Constants
 FIELD_WIDTH = 100
 FIELD_HEIGHT = 75

 # This will be a list of dictionaries
 inputs = []

 def read_inputs():

     inp = {}

     # Read n_x, n_y, and w on one line
     params = input().split()

     if len(params) < 3:
         exit("Not enough parameters")

     inp["nx"] = int(params[0])
     inp["ny"] = int(params[1])
     inp["width"] = float(params[2])

     # Return if n_x, n_y, and w are all 0
     if inp["nx"] == 0 and inp["ny"] == 0 and inp["width"] == 0.0: return

     # Read x and y values
     inp["x_values"] = list(map(float, input().split()))

     if len(inp["x_values"]) != inp["nx"]: 
         exit("Wrong number of x values!")

     inp["y_values"] = list(map(float, input().split()))

     if len(inp["y_values"]) != inp["ny"]:
         exit("Wrong number of y values!")

     # Append the new input to the input list
     inputs.append(inp)

     # Recursive call
     read_inputs()

 # ==========================================

 read_inputs()
 print(inputs)
 # Write an algorithm to process each input in the dictionary...