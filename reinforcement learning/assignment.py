# Assignment One train RL agent to navigate to cross the road with action right, left, right
import numpy as np
import random



# Environment setup
road_length = 5  # Positions: 0 (start) to 4 (goal)
actions = ["left", "right", "right"]
state = 0  # Starting position
path = []
# Create a Q-table with states (positions) and actions (left/right)

Q = np.zeros((road_length, len(actions)))
episodes = 1000  
learning_rate = 0.8 
gamma = 0.9  
epsilon = 0.3 


print("Agent's manually guided path to cross the road:\n")

for i, action in enumerate(actions):
    if action == "left":
        state = max(0, state - 1)
    else:
        action == "right"
        state = min(road_length - 1, state + 1)
    path.append(action)
    print(f"Step {i+1}: Move {action} → Position {state}")

# Final output
if state == road_length - 1:
    print(f"\nGoal reached in {len(actions)} steps!")
else:
    print(f"\nGoal NOT reached. Final position: {state}")
print(f"Final path: {' → '.join(path)}")

#the q table is not showing