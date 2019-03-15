from datetime import datetime

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

# Data to serve with our API
SEQUENCES = {
        "gi\:1034683989": {
            "seguid": "yplrJjECsVqQufeYy0HkDD16z58",
            "timestamp": get_timestamp()
        }
}

# Create a handler for our read (GET) people
def read():
    """
    This function responds to a request for /api/people
    with the complete lists of people

    :return:        sorted list of people
    """
    # Create the list of people from our data
    return [SEQUENCES[key] for key in sorted(SEQUENCES.keys())]
