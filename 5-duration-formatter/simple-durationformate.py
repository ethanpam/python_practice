def format(seconds: int) -> str:
    """
    Return the seconds into format of hours:minutes:seconds

    Parameters:
        seconds (int): The number of seconds

    Returns:
        str: hours:minutes:seconds
    """
    hours = seconds//3600
    minutes = (seconds%3600)//60
    secs = seconds % 60

    secs_str = f"{secs:02}"

    if hours != 0:
        return (f"{hours}:{minutes:02}:{secs_str}")
    else:
        return (f"{minutes}:{secs_str}")

def main():
    seconds = int(input("How many seconds?: "))
    print(format(seconds))

if __name__ == "__main__":
    main()