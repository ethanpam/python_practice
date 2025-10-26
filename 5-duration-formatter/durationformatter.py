def format(seconds: int) -> str:
    """
    Return the seconds into format of hours:minutes:seconds

    Parameters:
        seconds (int): The number of seconds

    Returns:
        str: hours:minutes:seconds
    """
    hours = 0
    minutes = 0
    while seconds > 3600:
        seconds = seconds - 3600
        hours += 1
    while seconds > 60:
        seconds = seconds - 60
        minutes += 1
    if seconds < 10:
        seconds = str(0)+str(seconds)
    if hours != 0:
        if minutes < 10:
            minutes = str(0)+str(minutes)
        return (f"{hours}:{minutes}:{seconds}")
    elif hours == 0:
        return (f"{minutes}:{seconds}")

def main():
    seconds = int(input("How many seconds?: "))
    print(format(seconds))

if __name__ == "__main__":
    main()