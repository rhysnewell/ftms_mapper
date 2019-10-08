class compound:
    """
    Class for a single compound
    """
    def __init__(self):
        mz = None

def read_compounds(filename):
    with open(filename) as f:
        for line in f:
            line = line.strip().split()
