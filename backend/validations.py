

def ans_input_validation(ans: int) -> bool:
    if type(ans) != int:
        return False
    elif ans < 1 or ans > 5:
        return False
    return True
