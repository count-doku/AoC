import numpy as np
import tqdm
import copy, os, time

# wrong: 1736,

class WalkingGuard():
    def __init__(self, position, direction, map, verbose=False):
        self.position = position
        self.map = map
        self.direction = direction
        self.right_border = np.shape(map)[0] - 1
        self.lower_border = np.shape(map)[1] - 1
        self.left_border = 0
        self.upper_border = 0
        self.look()
        self.verbose = verbose
        self.trail = []

        self.steps = 0
        if verbose:
            self.plot_map()
        self.position_already_in_trail = False
        self.endless_loop = False
    
    def plot_map(self, margin=5):
        for line in self.map[max(0, self.position[0]-margin):min(129, self.position[0]+margin), :]:
            print("".join(line))
        print("".join(["#"]*130))
        
    def look(self):
        if self.direction == ">":
            if self.position[1] + 1 > self.right_border:
                self.steps += 1
                self.sight = "finish"
            else:
                target = [self.position[0], self.position[1] + 1]
                self.sight = self.map[target[0], target[1]]
        elif self.direction == "v":
            if self.position[0] + 1 > self.lower_border:
                self.steps += 1
                self.sight = "finish"
            else:
                target = [self.position[0] + 1, self.position[1]]
                self.sight = self.map[target[0], target[1]]
        elif self.direction == "<":
            if self.position[1] - 1 < self.left_border:
                self.steps += 1
                self.sight = "finish"
            else:
                target = [self.position[0], self.position[1] - 1]
                self.sight = self.map[target[0], target[1]]
        elif self.direction == "^":
            if self.position[0] - 1 < self.upper_border:
                self.steps += 1
                self.sight = "finish"
            else:
                target = [self.position[0] - 1, self.position[1]]
                self.sight = self.map[target[0], target[1]]
        else:
            raise IOError("wrong view direction")

    def step(self):
        self.check_endless_loop()
        if self.direction == ">":
            if self.sight == "#":
                self.trail.append(self.calc_checksum(self.position))
                self.direction = "v"
                self.look()
                if self.sight == "#":
                    self.step()
                else:
                    self.down()
            else:
                self.right()
        elif self.direction == "v":
            if self.sight == "#":
                self.trail.append(self.calc_checksum(self.position))
                self.direction = "<"
                self.look()
                if self.sight == "#":
                    self.step()
                else:
                    self.left()
            else:
                self.down()
        elif self.direction == "<":
            if self.sight == "#":
                self.trail.append(self.calc_checksum(self.position))
                self.direction = "^"
                self.look()
                if self.sight == "#":
                    self.step()
                else:
                    self.up()
            else:
                self.left()
        elif self.direction == "^":
            if self.sight == "#":
                self.trail.append(self.calc_checksum(self.position))
                self.direction = ">"
                self.look()
                if self.sight == "#":
                    self.step()
                else:
                    self.right()
            else:
                self.up()
        else:
            raise IOError("wrong step direction")
    
    def right(self):
        self.map[self.position[0], self.position[1]] = "X"
        self.position[1] += 1
        self.map[self.position[0], self.position[1]] = ">"
        self.steps += 1
        self.look()

    def down(self):
        self.map[self.position[0], self.position[1]] = "X"
        self.position[0] += 1
        self.map[self.position[0], self.position[1]] = "v"
        self.steps += 1
        self.look()

    def left(self):
        self.map[self.position[0], self.position[1]] = "X"
        self.position[1] -= 1
        self.map[self.position[0], self.position[1]] = "<"
        self.steps += 1
        self.look()

    def up(self):
        self.map[self.position[0], self.position[1]] = "X"
        self.position[0] -= 1
        self.map[self.position[0], self.position[1]] = "^"
        self.steps += 1
        self.look()            

    def calc_checksum(self, position):
        return str(position[0]) + str(position[1]) + self.direction
    
    def check_endless_loop(self):
        if self.calc_checksum(self.position) in self.trail:
            if self.position_already_in_trail:
                self.endless_loop = True
            else:
                self.position_already_in_trail = True

if __name__ == "__main__":
    init_map = []
    test = False
    if test:
        path = "2024/06/input_test"
        n = 10
    else:
        path = "2024/06/input"
        n = 130

    with open(path) as file:
        for i in range(n):
            line = file.readline().rstrip()
            init_map.append(list(line))

    init_map = np.array(init_map) # Convert map to np array
    init_position_of_guard = np.squeeze(np.where(init_map=="^"))  # Find guard position

    guardy = WalkingGuard(copy.deepcopy(init_position_of_guard), "^", copy.deepcopy(init_map))

    while guardy.sight != "finish":
        guardy.step()
        # guardy.plot_map()
        # time.sleep(0.1)

    result_1 = np.copy(len(np.where(guardy.map == "X")[0])+1)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"Part One Result: {result_1}")
    
    variations = 0
    max_trials = 1000000000
    possible_endless_loops = 0

    for x in range(len(init_map)):
        for y in range(len(init_map)):
            if init_map[x, y] == "#":
                continue
            elif np.equal(np.array((x, y)), init_position_of_guard).all():
                continue
            else:
                manipulated_map = copy.deepcopy(init_map)
                manipulated_map[x, y] = "#"
            guardy_1 = WalkingGuard(copy.deepcopy(init_position_of_guard), "^", copy.deepcopy(manipulated_map), verbose=False)
            finished = False
            for trial in range(max_trials):
                guardy_1.step()
                if guardy_1.sight == "finish":
                    finished = True
                    break
                if guardy_1.endless_loop:
                    possible_endless_loops += 1
                    break
            if variations%100 == 0:
                print(f"found endless loops: {possible_endless_loops} at {x}, {y} | variations: {variations}/{130*130} | steps gone: {trial}")
            variations += 1

    result_2 = copy.copy(possible_endless_loops)
    print(f"Part Two Result: {result_2}")
    print("finish")