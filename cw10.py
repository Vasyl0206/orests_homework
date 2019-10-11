def enough(cap, on, wait):
    load = cap - on
    if load == wait:
        return 0
    elif load > wait:
        return 0
    elif load < wait:
        res2 = wait - load
        return res2
    # Your code here

# def enough(cap, on, wait):
# return max(0, wait - (cap - on))