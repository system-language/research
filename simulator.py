# simulator.py
def regulatory_effect(regulatory_env):
    if regulatory_env == 0:  # Hostile
        return -0.02  # Decrease growth rate by 2%
    elif regulatory_env == 1:  # Neutral
        return 0  # No change
    elif regulatory_env == 2:  # Friendly
        return 0.02  # Increase growth rate by 2%

def calculate_growth_rate(transaction_fee, marketing_effort, regulatory_env):
    base_growth_rate = 0.05
    reg_effect = regulatory_effect(regulatory_env)
    return base_growth_rate + marketing_effort - transaction_fee + reg_effect


def simulate_one_step(user_count, transaction_fee, marketing_effort, regulatory_env):
    growth_rate = calculate_growth_rate(transaction_fee, marketing_effort, regulatory_env)
    new_users = user_count * growth_rate
    user_count += new_users
    fee_revenue = user_count * transaction_fee
    return user_count, fee_revenue

def run_simulation(steps, user_count, transaction_fee, marketing_effort, regulatory_env):
    user_counts = [user_count]
    fee_revenues = [user_count * transaction_fee]

    for _ in range(steps):
        user_count, fee_revenue = simulate_one_step(user_count, transaction_fee, marketing_effort, regulatory_env)
        user_counts.append(user_count)
        fee_revenues.append(fee_revenue)

    return user_counts, fee_revenues


    
