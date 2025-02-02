from locale import currency
import numpy as np

R = np.matrix([
                [0, -0.04, -0.08, -0.08, -0.12, -0.16, 0.84],
                [-100, 0, -0.04, -0.04, -0.08, -0.12, 0.88],
                [-100, -100, 0, 0, -0.04, -0.08, 0.92],
                [-100, -100, 0, 0, -0.04, -0.08, 0.92],
                [-100, -100, -0.04, -0.04, 0, -0.04, 0.96],
                [-100, -100, -0.08, -0.08, -0.04, 0, 1],
                [-100, -100, -0.12, -0.12, -0.08, -0.04, 0]
             ])

Q = np.matrix(np.zeros([7,7]))

alpha = 0.8

initial_state = 1

def available_actions(state):
    curr_state_row = R[state,]
    av_act = np.where(curr_state_row >= -0.04)[1]
    return av_act

available_act = available_actions(initial_state)

def sample_next_action(available_actions_range):
    next_action = int(np.random.choice(available_act,1))
    return next_action

action = sample_next_action(available_act)

def update(current_state, action, alpha):
    max_index = np.where(Q[action,] == np.max(Q[action,]))[1]

    if (max_index.shape[0] > 1):
        max_index = int(np.random.choice(max_index, size=1))
    else:
        max_index = int(max_index)
    max_value = Q[action, max_index]

    # Q learning formula
    Q[current_state,action] = R[current_state, action] + alpha*max_value

update(initial_state, action, alpha)

# TRAINING
for i in range(10000):
    current_state = np.random.randint(0, int(Q.shape[0]))
    available_act = available_actions(current_state)
    action = sample_next_action(available_act)
    update(current_state, action, alpha)

print("Trained Q matrix :")
print(Q / np.max(Q)* 100)

# TESTING
current_state = 1
steps = [current_state]
while(current_state != 3):
    next_step_index = np.where(Q[current_state,] == np.max(Q[current_state,]))[1]
    if next_step_index.shape[0] > 1:
        next_step_index = int(np.random.choice(next_step_index, size = 1))
    else:
        next_step_index = int(next_step_index)
    steps.append(next_step_index)
    current_state = next_step_index

print("Selected path :")
print(steps)