""" ex_4_3.py """
import os

try:
    from src.ex_4_0 import get_shutdown_events
    from src.ex_4_2 import logstamp_to_datetime
    from src.util import get_data_file_path
except ImportError:
    from ex_4_0 import get_shutdown_events
    from ex_4_2 import logstamp_to_datetime
    from util import get_data_file_path

# Use this FILENAME variable to test your function.
FILENAME = get_data_file_path("messages.log")
# >>>> DO NOT MODIFY CODE ABOVE <<<<


def time_between_shutdowns(logfile):
    """
    Your docstring here.  Replace the pass keyword below with your implementation.
    """
    shutdown_entries = get_shutdown_events(logfile)
    first_sd = shutdown_entries[0]
    last_sd = shutdown_entries[-1]

    first_date = first_sd.split('')[1]
    last_date = last_sd.split('')[1]
    
    return logstamp_to_datetime(last_date) - logstamp_to_datetime(first_date)
    

# >>>> The code below will call your function and print the results
if __name__ == "__main__":
    print(f'{time_between_shutdowns(FILENAME)=}')
