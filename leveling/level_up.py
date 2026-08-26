import leveling.get_exp as get_exp

def level_up (won, opponent_level, current_exp):
    # Calculate earned experience (preventing division or zero exp issues)
    exp_gained = max(1, opponent_level // 5)
    if won:
        current_exp += exp_gained

    exp_required = get_exp.get_medium_fast_exp(next_level)
    
    leveled_up = False
    """
        Breaking Out of while loop: Eventually, after leveling up once or multiple times, the player's remaining current_exp will drop below the exp_required threshold.
        When that happens, the while condition becomes False, the loop automatically terminates, and the code moves on to return the final values.
        Exp is cumulative. It does not reset to zero if your hero levels up, even if it does display it that way in the CLI.
    """
    while current_exp >= exp_required:
        current_level = next_level
        leveled_up = True
        next_level = current_level + 1
        exp_required = get_exp.get_medium_fast_exp(next_level)
        
    return current_exp, current_level, leveled_up