import traci
import sys
import math

def create_Stopped_vehicle():
    try:
        print("Starting SUMO simulation...")
        traci.start(["sumo-gui", "-c", "osm.sumocfg","--time-to-teleport", "-1"])

        lane_id = "1101404059#0_0"
        edge_id = "24242838#2"
       
        traci.simulationStep()  # Required before adding
        traci.vehicle.add("blocker1", "blockerRoute", typeID="veh_passenger")
        traci.vehicle.setStop("blocker1", edgeID=edge_id, laneIndex=0, pos=10, duration=1000, flags=0)

        max_steps = 5000
        step = 0

        print("Running simulation loop...")
        while traci.simulation.getMinExpectedNumber() > 0 and step < max_steps:
            traci.simulationStep()
            step += 1

        print(f"Simulation completed after {step} steps")

    except traci.exceptions.TraCIException as e:
        print(f"TraCI error: {e}")
    except Exception as e:
        print(f"General error: {e}")
    finally:
        print("Closing SUMO...")
        traci.close()

def main():
    print("STOPPED VEHICLE")
    print("=" * 50)
    try:
        import sumolib
        print("SUMO libraries found")
        create_Stopped_vehicle()
    except ImportError:
        print("Warning: SUMO libraries not found")

if __name__ == "__main__":
    main()
