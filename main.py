# Main.py using pandas

import pandas as pd


def GDP(data):
    GDPfile = pd.read_csv(data, dtype={"GDP rate": float})
    summary = GDPfile.describe()
    return summary
