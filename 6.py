import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Create fuzzy variables
dirtiness = ctrl.Antecedent(np.arange(11), 'dirtiness')
stain_type = ctrl.Antecedent(np.arange(11), 'stain_type')
washing_time = ctrl.Consequent(np.arange(61), 'washing_time')

# Define membership functions
dirtiness.automf(3)
stain_type.automf(3)
washing_time.automf(3)

# Define rules
rule1 = ctrl.Rule(dirtiness['poor'] & stain_type['poor'], washing_time['poor'])
rule2 = ctrl.Rule(dirtiness['average'] & stain_type['average'], washing_time['average'])
rule3 = ctrl.Rule(dirtiness['good'] & stain_type['good'], washing_time['good'])

# Create control system
washing_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
washing_machine = ctrl.ControlSystemSimulation(washing_ctrl)

# Set input values
washing_machine.input['dirtiness'] = 7
washing_machine.input['stain_type'] = 8

# Compute the result
washing_machine.compute()

# Print the output
print("Washing Time:", washing_machine.output['washing_time'])

# Visualize the result
washing_time.view(sim=washing_machine)
