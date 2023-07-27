from mypy_extensions import TypedDict
import warnings

Rtd_Dict = TypedDict(
    "Rtd_Dict",
    {
        "rate": float,
        "distance": float,
        "time": float
    }
)

def rtd(**keywords: float) -> Rtd_Dict:
    """
    Calculate the missing value in a rate-time-distance (RTD) calculation.

    Given any two known values among rate, distance, and time, this function computes
    the missing value and returns a dictionary with all three values.

    Parameters:
    **keywords (float): Keyword arguments representing the known values in the RTD calculation.
                        Provide any two of the following:
                            - rate (float): The rate of speed or velocity.
                            - distance (float): The distance traveled.
                            - time (float): The time taken.

    Returns:
    dict: A dictionary containing the calculated values.
          The dictionary will have the following keys:
            - 'distance' (float): The distance traveled.
            - 'rate' (float): The rate of speed or velocity.
            - 'time' (float): The time taken.

    Raises:
    TypeError: If more than two known values are provided as keyword arguments.
    Warning: If insufficient information is provided (less than two known values).

    Usage:
    Example 1:
    >>> result = rtd(rate=60, time=2.5)
    >>> print(result)  # Output: {'distance': 150.0, 'rate': 60, 'time': 2.5}

    Example 2:
    >>> result = rtd(distance=400, time=10)
    >>> print(result)  # Output: {'distance': 400, 'rate': 40.0, 'time': 10}

    Example 3:
    >>> result = rtd(rate=55, distance=275)
    >>> print(result)  # Output: {'distance': 275, 'rate': 55, 'time': 5.0}

    Example 4:
    >>> result = rtd(rate=60)
    >>> # Warning: Not enough information to solve for distance, rate, and time.
    """
    rate = keywords.pop('rate', None)
    time = keywords.pop('time', None)
    distance = keywords.pop('distance', None)
    if keywords: raise TypeError(
			f"Invalid keyword parameter: {', '.join(keywords.keys())}")
    else:
        if distance is None and rate is not None and time is not None:
            distance = rate * time
        elif rate is None and distance is not None and time is not None:
            rate = distance / time
        elif time is None and distance is not None and rate is not None:
            time = distance / rate
        else:
            warnings.warn("Not enough information to solve for distance, rate, and time.")
    result: Rtd_Dict = {
        "distance": distance, 
        "rate": rate, 
        "time": time
        }
    return result
