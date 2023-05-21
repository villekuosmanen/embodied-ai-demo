import habitat.gym   # initialise gym environments

import gymnasium as gym

# Naive: get a random action
def get_action(env):
    return env.action_space.sample()

env = gym.make('HabitatRenderPick-v0')# Get number of actions from gym action space
print("Environment creation successful")

# Get the number of state observations
state = env.reset()


print("Agent acting inside environment.")
count_steps = 0
terminal = False
while not terminal:
    action = get_action(env)
    observations, reward, terminal, info = env.step(action)
    count_steps += 1
print("Episode finished after {} steps.".format(count_steps))

# Close the env
env.close()