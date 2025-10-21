import traci
import numpy as np
import os
from rl_package.rl_logic.annexe import calculate_reward

class EnvironnementSumo:
    def __init__(self, sumoCmd,window=2000):
        if traci.isLoaded():
            traci.close()
        traci.start(sumoCmd)  # Start SUMO once
        self.window=window
        self.lanes_ids = traci.lane.getIDList()
        self.trafficlights_ids = traci.trafficlight.getIDList()


    def queue(self,lane_ids):
        return [traci.lane.getLastStepHaltingNumber(lane_id) for lane_id in lane_ids]

    def get_lane_no_intersection(self,lane_ids=None):
        if not lane_ids:
            lane_ids=self.lanes_ids
        return [lane_id for lane_id in lane_ids if not lane_id.startswith(':')]


    def get_state(self,lane_ids):
        return [traci.lane.getLastStepHaltingNumber(lane_id) for i,lane_id in enumerate(lane_ids) ]+\
        [traci.lane.getLastStepVehicleNumber(lane_id) for i,lane_id in enumerate(lane_ids)]

    def get_total_number_vehicles(self):
        return len(traci.vehicle.getIDList())


    def get_phase_without_yellow(self,traffic_light):
        "return phases of trafific_light without yellow phase"
        phases = traci.trafficlight.getAllProgramLogics(traffic_light)[0].phases
        long_phases = []
        position = []
        for i,phase in enumerate(phases):
            if "y" not in phase.state:
                long_phases.append(phase)
                position.append(i)
        return long_phases, position


    def step(self,actions):
        ###CODER UN STEP qui prend une action en argument
        #utiliser un modele, renvoyer next state: array, reward:int, done :
        states = [self.get_states_per_traffic_light(traffic_light) for traffic_light in self.trafficlights_ids]
        for i,traffic_light in enumerate(self.trafficlights_ids):
            traci.trafficlight.setPhase(traffic_light,2*actions[i])

        for _ in range(self.window):
            traci.simulationStep()

        next_states = [self.get_states_per_traffic_light(traffic_light) for traffic_light in self.trafficlights_ids]

        rewards = [calculate_reward(states[i],next_states[i]) for i in range(len(actions))]

        return next_states,rewards

    def full_simul(self,agent):
        lanes = self.get_lane_no_intersection()
        state = np.array(self.get_state(lanes))
        action=1
        for step in range(130000): ## TO CHANGED
            if step%2000 == 0:
                state=np.array(self.get_state(lanes))
                action = agent.epsilon_greedy_policy(state,0)*2
                traci.trafficlight.setPhase(self.trafficlights_ids[0],action)
            traci.simulationStep()



    def close(self):
        if traci.isLoaded():
            traci.close()  # Properly close SUMO
            os.system("pkill -f sumo")
            os.system("pkill -f sumo-gui")


    def get_number_of_junction(self):
        return traci.junction.getIDCount()


    def control_lanes(self, traffic_light):
        lane_ids = traci.trafficlight.getControlledLinks(traffic_light)
        values = []
        for value in lane_ids:
            for j in value:
                for k in j:
                    values.append(k)
        lane_ids = values
        return [lane for lane in lane_ids if not lane.startswith(':')]

    def get_states_per_traffic_light(self, traffic_light):
        # initialisation d'un dictionnaire vide

        lane_ids = traci.trafficlight.getControlledLinks(traffic_light)
        values = []
        for value in lane_ids:
            for j in value:
                for k in j:
                    values.append(k)
        lane_ids = values
        cleaned_lane_ids = [lane for lane in lane_ids if not lane.startswith(':')]
        print(cleaned_lane_ids)
        print(len(cleaned_lane_ids))
        # on met ça dans le dico
        return [traci.lane.getLastStepHaltingNumber(lane_id) for lane_id in cleaned_lane_ids] +\
        [traci.lane.getLastStepVehicleNumber(lane_id) for lane_id in cleaned_lane_ids]
