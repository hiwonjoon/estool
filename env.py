import numpy as np
import gym
"""
import pybullet as p
import pybullet_envs
import pybullet_envs.bullet.minitaur_gym_env as minitaur_gym_env
import pybullet_envs.bullet.racecarGymEnv as racecarGymEnv
import pybullet_envs.bullet.kukaGymEnv as kukaGymEnv
from custom_envs.minitaur_duck import MinitaurDuckBulletEnv
from custom_envs.minitaur_ball import MinitaurBallBulletEnv
"""

def make_env(env_name, seed=-1, render_mode=False):
    """
    if (env_name.startswith("RacecarBulletEnv")):
    print("bullet_racecar_started")
    env = racecarGymEnv.RacecarGymEnv(isDiscrete=False, renders=render_mode)
    elif (env_name.startswith("RocketLander")):
    from box2d.rocket import RocketLander
    env = RocketLander()
    elif (env_name.startswith("BipedalWalker")):
    if (env_name.startswith("BipedalWalkerHardcore")):
        from box2d.biped import BipedalWalkerHardcore
        env = BipedalWalkerHardcore()
    else:
        from box2d.biped import BipedalWalker
        env = BipedalWalker()
    elif (env_name.startswith("MinitaurBulletEnv")):
    print("bullet_minitaur_started")
    env = minitaur_gym_env.MinitaurBulletEnv(render=render_mode)
    elif (env_name.startswith("MinitaurDuckBulletEnv")):
    print("bullet_minitaur_duck_started")
    env = MinitaurDuckBulletEnv(render=render_mode)
    elif (env_name.startswith("MinitaurBallBulletEnv")):
    print("bullet_minitaur_ball_started")
    env = MinitaurBallBulletEnv(render=render_mode)
    elif (env_name.startswith("KukaBulletEnv")):
    print("bullet_kuka_grasping started")
    env = kukaGymEnv.KukaGymEnv(renders=render_mode,isDiscrete=False)
    else:
    if env_name.startswith("Roboschool"):
        import roboschool
    env = gym.make(env_name)
    if render_mode and not env_name.startswith("Roboschool"):
        env.render("human")
    """
    if env_name.endswith('RelativeReward'):
        env_name = env_name.replace('RelativeReward','')

        import sys, os
        sys.path.append('../')
        #sys.path.append(os.path.dirname(os.path.abspath(__file__))+'../')
        import ranker_env_wrapper

        if env_name.endswith('-GT'):
            env_name = env_name.replace('-GT','')
            env = ranker_env_wrapper.RankerEnvGT(
                env_name
            )
        elif env_name.endswith('-GTBinary'):
            env_name = env_name.replace('-GTBinary','')
            env = ranker_env_wrapper.RankerEnvGTBinary(
                env_name
            )
        elif env_name.endswith('-Siamese'):
            from siamese_ranker import Model
            from functools import partial
            import train

            env_name = env_name.replace('-Siamese','')
            env = ranker_env_wrapper.RankerEnv(
                env_name,
                partial(Model,embedding_dims=128,steps=20),
                '%s/%s/last.ckpt'%('../log',env_name)
            )
        elif env_name.endswith('-SiameseBinary'):
            from siamese_ranker import Model
            from functools import partial
            import train

            env_name = env_name.replace('-SiameseBinary','')
            env = ranker_env_wrapper.RankerEnvBinary(
                env_name,
                partial(Model,embedding_dims=128,steps=20),
                '%s/%s/last.ckpt'%('../log',env_name)
            )
        else:
            assert False, 'unsupported'
    else:
        env = gym.make(env_name)

    if (seed >= 0):
        env.seed(seed)
    '''
    print("environment details")
    print("env.action_space", env.action_space)
    print("high, low", env.action_space.high, env.action_space.low)
    print("environment details")
    print("env.observation_space", env.observation_space)
    print("high, low", env.observation_space.high, env.observation_space.low)
    assert False
    '''
    return env
