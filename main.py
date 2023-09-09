# Main.py using pandas

import pandas as pd


def GDP(data):
    GDPfile = pd.read_csv(data)
    summary = GDPfile.describe()
    return summary
