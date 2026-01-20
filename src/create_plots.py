import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Parameters
FREQ = 250
SIGNAL = 'magnitude'
SAMPLE_SIZE = 15
SEED = 42

# Paths
ROOT = Path(__file__).parent.parent
DATA_PATH = ROOT / 'data' / 'eda_anon.pkl'
METADATA_PATH = ROOT / 'data' / 'correct_recordings.txt'
OUTPUT_PATH = ROOT / 'plots' / 'input_signals'


def create_measurement_plot(y: np.ndarray, x: None | np.ndarray = None):
    fig = plt.figure()
    ax = fig.add_subplot()

    if x is None:
        ax.plot(y)
    else:
        ax.plot(x, y)

    return fig, ax

def prepare_recordings_sample(measure_ids: pd.Series, correct_ids: pd.Series):

    measure_df = pd.DataFrame({'measure_ids': measure_ids})
    measure_df['correct'] = measure_df['measure_ids'].isin(correct_ids)

    return measure_df.groupby('correct').sample(SAMPLE_SIZE, random_state=SEED)

def main():

    df = pd.read_pickle(DATA_PATH)
    correct_recordings = pd.read_csv(METADATA_PATH).iloc[:, 0]  # Correct recordings ids are in the first column

    measure_ids = pd.Series(df.index.get_level_values('measure_id').unique())
    measure_sample_df = prepare_recordings_sample(measure_ids, correct_recordings)

    # Prepare plots
    figures = []
    for _, row in measure_sample_df.iterrows():
        signal = df.loc[(row['measure_ids'], FREQ), SIGNAL]
        fig, ax = create_measurement_plot(y = np.array(signal))

        ax.set_title(f'Measure ID = {row['measure_ids']}; Correct = {row['correct']}')
        figures.append(fig)

    # Save files
    OUTPUT_PATH.mkdir(exist_ok=True, parents=True)
    for idx, fig in enumerate(figures):
        fig.savefig(OUTPUT_PATH / f'signal_{idx}.png')


if __name__ == '__main__':
    main()





