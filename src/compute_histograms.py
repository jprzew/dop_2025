import pandas as pd
import numpy as np
from pathlib import Path

BINS = 20
HIST_RANGE = (0.0, 40000.0)
FREQ = 250

# Paths
ROOT = Path(__file__).parent.parent
DATA_PATH = ROOT / 'data' / 'eda_anon.pkl'
METADATA_PATH = ROOT / 'data' / 'correct_recordings.txt'
OUTPUT_PATH = ROOT / 'data' / 'histograms.csv'


def compute_histogram(data: pd.Series, bins: int = 20,
                      hist_range: tuple[float, float] = (0.0, 40000.0)):
    """Computes histogram for one series of data"""

    return np.histogram(np.array(data), bins=bins, range=hist_range)


def compute_all_histograms(df: pd.DataFrame) -> pd.DataFrame:
    """Compute histograms for all measurements in df.
       Limits computation to frequency=FREQ (param of this script)

    Args:
        df: DataFrame with multiindex ('measure_id' 'freq', 'timestamp')
            and column 'magnitude'
    Returns:
        DataFrame with index 'measure_id' and columns being bins of computed histograms

    """

    desired_freq_df = df.xs(FREQ, level=1)

    def _hist_from_measure_df(measure_df: pd.DataFrame):
        hist = compute_histogram(measure_df['magnitude'],
                                 bins=BINS, hist_range=HIST_RANGE)[0]  # First element of the tuple contains histogram
        return pd.Series(hist)


    result = (desired_freq_df
              .groupby('measure_id')
              .apply(_hist_from_measure_df)
              )

    return result


def main():

    # Read input data
    df = pd.read_pickle(DATA_PATH)
    correct_recordings = pd.read_csv(METADATA_PATH).iloc[:, 0]  # Correct recordings ids are in the first column

    # Compute histograms
    histograms_df = compute_all_histograms(df)

    # Write histograms to file
    histograms_df.to_csv(OUTPUT_PATH)

if __name__ == '__main__':
    main()
