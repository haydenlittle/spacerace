import gym
import numpy as np
env = gym.make('SpaceInvaders-ram-v0')
# print(env.action_space.n)
# print(env.observation_space)
states = np.zeros(128)
print(states)
for i in range(1000) :
    observation = env.reset()
    for _ in range(10000):
        env.render()
        # env.step(env.action_space.sample()) # take a random action
        # # print(observation)
        # states.append(observation)
        # print(states)
        # if observation in states :
        #     print('oooooOooOOOo')
        # states.append(observation)
        # print(observation)
        for state in states :
            if np.array_equal(observation, state) :
                'litty'
        states = np.vstack((states, observation))
        # print(states)
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        # print(reward)
        if done :
            print('Episode finished after %d timesteps' % _)
            break
    env.close()
