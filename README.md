# ESTool

## Train
```
python train.py <environment name> -e <number of episode for each population, reward will be normalized across this batch> -n <number of process> -t <number of worker per each process> -o {cma/openes}
```
Therefore, The population will become n*t. Currently, `-e 4 -n 4 -t 4 -o cma` works fine mostly with `gt_rr` envs.

Possible Env Names:
  - `{hopper, ant, walker2d, swimmer, cheetah, ant, humanoid, reacher, striker, pusher, thrower}`
  - `{(above list})_gt_rr`; ground truth relative reward.
  - `{(above list})_gt_binary_rr`; binarized ground truth relative reward
  - `{(above list})_siamese_rr`; reward as a predicted prob (by siamese network) whether the current traj is better than before.
  - `{(above list})_siamese_binary_rr`; binarized version of the siamese_rr

## Visualization

```
python model.py <environment name> <model file name>
```

To record video, check `record_video` flag in `model.py`.

## Current Results

1. Hopper-v2
  - `_gt_rr` env was trainable with the basic parameters @ 2500 generation (took more than 200 minutes)
  - `python train.py hopper_gt-rr -e 4 -n 4 -t 4`

2. Walker2d-v2
  - on training...

