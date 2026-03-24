import copy
def sarsa_update(q_table, state, action, reward, next_state, next_action, alpha, gamma):
    """
    Perform one SARSA update and return the updated Q-table.
    """
    new_q = copy.deepcopy(q_table)
    
    # 2. Compute the Temporal Difference (TD) error 
    # We use the ORIGINAL q_table values here as per the hint
    td = reward + (gamma * q_table[next_state][next_action]) - q_table[state][action]
    
    # 3. Update the COPY
    # The original q_table remains unchanged for other simultaneous updates
    new_q[state][action] += alpha * td
    return new_q