from time import sleep
import gym
import random
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 


env_name = "CartPole-v1"
env = gym.make(env_name)
print("Observation space:", env.observation_space)
print("Action space:", env.action_space)
class Agent():
    def __init__(self, env):
        self.action_size = env.action_space.n
        print("Action size:", self.action_size)
        
    def get_action(self, state):
        action = random.choice(range(self.action_size))
        pole_angle = state[2]
        action = 0 if pole_angle < 0 else 1 #0 Push cart to the left #1 Push cart to the right
        return action

agent = Agent(env)
state = env.reset()
print(state)

for _ in range(100):
    # action = env.action_space.sample()
    action = agent.get_action(state)
    state, reward, done, info = env.step(action)
    print(reward,state,done)
    env.render()
    if reward<1:
        sleep(3)
        break
env.close()

