import gym


class Agent:
    def __init__(self, env) -> None:
        pass

    def decide(self, observation):
        pos, vel = observation
        lb = min(-0.09 * (pos + 0.25) ** 2 + 0.03,
                 0.3 * (pos + 0.9) ** 4 - 0.008)
        ub = -0.07 * (pos + 0.38) ** 2 + 0.07
        if lb < vel < ub:
            action = 2
        else:
            action = 0
        return action

    def learn(self, *args):
        pass

def play(env, agent, render=False, train=False):
    episode_reward = 0.
    observation = env.reset()
    while True:
        if render:
            env.render()
        action = agent.decide(observation)
        next_observation, reward, done, _ = env.step(action)
        episode_reward += reward
        if train:
            agent.learn(observation, action, reward, done)
        if done:
            break
        observation = next_observation
    return episode_reward


def main():
    env = gym.make('MountainCar-v0')

    myAgent = Agent(env)
    env.seed(0)
    episode_reward = play(env, myAgent, True)
    print('回合奖励 = {}'.format(episode_reward))
    env.close() # 此语句可关闭图形界面

if __name__ == '__main__':
    main()