import profile
import random
from Map import Map


def profileTest():
    test_map = Map([[random.choice([0, 1]) for _ in range(1000)] for _ in range(1000)])
    test_map.get_cell(0, 0)
    test_map.set_cell(0, 0, 1)
    test_map.flip_cell(0, 0)
    test_map.Update()


if __name__ == "__main__":
    profile.run("profileTest()")