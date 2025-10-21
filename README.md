# Traffic Light RL

A reinforcement learning project exploring how to optimize traffic light control across multiple intersections using deep RL and SUMO simulation.

## Overview

This repository contains the codebase and experimentation framework developed for a student project in reinforcement learning, focusing on traffic light coordination. The objective was to train agents to dynamically adjust signal timings in order to improve traffic flow and reduce congestion.

We explored various RL algorithms (notably DQN and its variants), deployed multi-agent setups, and evaluated their performance using microscopic traffic simulations in **SUMO** (Simulation of Urban Mobility).

> **Note**: This codebase was developed collaboratively as part of a student research project. Some components (especially notebooks) are exploratory drafts, preserved here for traceability and reproducibility.

## Repository Structure

```
Traffic/                   SUMO XML files for the road network, routes, and simulation setup
models/                    Saved model checkpoints
notebooks/                 Experiment drafts and exploratory tests
rl_package/                Packaged Python code for training and simulation
├── rl_algorithms/         DQN, Double DQN, etc.
├── rl_logic/              Environment logic and reward computation
├── interface/             SUMO / TraCI communication interface
└── params.py              Hyperparameters and configuration
setup.py                   Project setup
requirements.txt           Dependencies
.env.sample / .envrc       Local environment variables (for direnv)
README.md                  This file
```

## Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/Arsenecl/traffic-light-rl.git
cd traffic-light-rl
pip install -r requirements.txt
```

Make sure **SUMO** is installed and accessible in your environment.  
You can download it here: [SUMO Download](https://sumo.dlr.de/docs/Downloads.html)

If you use `direnv`, you can copy `.env.sample` to `.envrc` and adjust the paths.

## Running Experiments

To run training or evaluation scripts, use the entry point from the `rl_package`.  
Example:

```bash
python -m rl_package.main
```

You can modify the parameters from `rl_package/params.py`.

## Notebooks

The `notebooks/` folder contains exploratory work, rough experiments, and intermediate results. These are not clean pipelines but were kept for documentation and traceability purposes.

## Demo

A video demonstration showcasing the traffic simulation and the decisions made by the RL agent is available here:  
👉 [Demo Video](https://drive.google.com/your-demo-link)

## Authors

This project was initially developed by a team of students as part of a reinforcement learning course.  
This version is maintained and cleaned up by [@Arsenecl](https://github.com/Arsenecl).
