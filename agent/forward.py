from typing import Dict

import numpy as np
from numpy import bool_

import habitat
from habitat.core.simulator import Observations
from habitat.sims.habitat_simulator.actions import HabitatSimActions

class ForwardOnlyAgent(habitat.Agent):
    def __init__(self, success_distance: float, goal_sensor_uuid: str) -> None:
        self.dist_threshold_to_stop = success_distance
        self.goal_sensor_uuid = goal_sensor_uuid

    def reset(self) -> None:
        pass

    def is_goal_reached(self, observations: Observations) -> bool_:
        dist = observations[self.goal_sensor_uuid][0]
        return dist <= self.dist_threshold_to_stop
    
    def act(self, observations: Observations) -> Dict[str, int]:
        if self.is_goal_reached(observations):
            return HabitatSimActions.stop
        else:
            action = HabitatSimActions.move_forward
        return {"action": action}