# Traffic Light RL

A reinforcement learning project exploring how to optimize traffic light control across multiple intersections using deep RL and SUMO simulation.

## Overview

This repository contains the codebase and experimentation framework developed during a project at Le Wagon. The aim was to experiment with training agents capable of dynamically adjusting signal timings to improve traffic flow and reduce congestion across multiple intersections.

We explored several variants of Deep Q-Networks (notably DQN, 2DQN and 3DQN), and tested multi-agent setups. Experiments were carried out using microscopic traffic simulations with **SUMO** (Simulation of Urban Mobility).

> Note: Some parts of this repository (especially in `notebooks/`) contain exploratory drafts, preserved for documentation and reproducibility.

## Repository Structure
```
Traffic/ → SUMO XML files for the road network, routes, and simulation setup
models/ → Saved model checkpoints
notebooks/ → Exploratory notebooks and intermediate tests
rl_package/ → Packaged Python code for training and simulation
  ├── rl_algorithms/ → RL algorithms like DQN, Double DQN, 3DQN
  ├── rl_logic/ → Environment logic and reward calculation
  ├── interface/ → Communication interface with SUMO via TraCI
  └── params.py → Centralized configuration and hyperparameters
setup.py → Project setup script
requirements.txt → Python dependencies
.env.sample / .envrc → Environment variables template
README.md → This file
```

## Installation

Clone the repository and install dependencies:

git clone https://github.com/Arsenecl/traffic-light-rl.git
cd traffic-light-rl
pip install -e .

This uses the `setup.py` file to correctly package and install the project dependencies listed in `requirements.txt`.

Make sure SUMO is installed and accessible in your environment.  
You can download it here: https://sumo.dlr.de/docs/Downloads.html

If you use `direnv`, you can copy `.env.sample` to `.envrc` and adjust the paths accordingly.

## Running Experiments

To train or evaluate an agent:

python -m rl_package.main

You can configure the experiment by editing the `params.py` file.

## Notebooks

The `notebooks/` folder contains various drafts and partial tests used during the prototyping phase. These are not clean pipelines but help understand the evolution of the project.

## Demo

A video demonstration showcasing the traffic simulation and the decisions made by the RL agent is available here:  
[Demo Video](https://www.youtube.com/watch?v=bnvSJbV-G6g)
