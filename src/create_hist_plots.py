import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from sklearn.manifold import TSNE
import seaborn as sns

# Parameters
SAMPLE_SIZE = 15
SEED = 42

# Paths
ROOT = Path(__file__).parent.parent
DATA_PATH = ROOT / 'data' / 'histograms.csv'
METADATA_PATH = ROOT / 'data' / 'correct_recordings.txt'
OUTPUT_PATH = ROOT / 'plots' / 'histograms'


def create_histogram_plot(hist: pd.Series):
    """Creates plot of precomputed histogram

    Args:
        hist - Pandas Series containing precomputed histogram with index being bin-labels

    Returns:
        fig, ax: Figure and axes with plotted histogram
    """
    fig = plt.figure()
    ax = fig.add_subplot()

    ax.bar(height=np.array(hist), x=list(hist.index))

    return fig, ax


def tsne_dimension_reduction(df: pd.DataFrame) -> pd.DataFrame:
    """Performs TSNE dimension reduction to dimension 2

    Args:
        df: DataFrame with heights of histogram bins as columns

    Returns:
        DataFrame with TSNE components called tsne_1, tsne_2 and with index of original dataframe
    """


    n_components = 2

    tsne = TSNE(n_components)
    tsne_result = pd.DataFrame(tsne.fit_transform(df))

    # Set index and columns
    tsne_result.index = df.index
    tsne_result.columns = ['tsne_1', 'tsne_2']

    return tsne_result


def create_tsne_plot(df: pd.DataFrame):
    """Creates plot of TSNE reduced data (takes first two columns!)

    Args:
        df: DataFrame with tsne-reduced data to dimension 2
        should contain column 'correct' indicating if measurement is correct

    Returns:
        fig, ax: Figure and axes with the scatterplot
    """

    fig, ax = plt.subplots(1)
    sns.scatterplot(x=df.columns[0], y=df.columns[1], hue='correct', data=df, ax=ax)

    return fig, ax


def main():

    df = pd.read_csv(DATA_PATH, index_col='measure_id', header=0)
    correct_recordings = pd.read_csv(METADATA_PATH).iloc[:, 0]  # Correct recordings ids are in the first column


    # Add column with correct recordings
    df['correct'] = df.index.isin(correct_recordings)

    # Prepare sample
    sample_df = df.groupby('correct').sample(SAMPLE_SIZE, random_state=SEED)

    # Prepare plots for sample
    figures = []
    for idx, row in sample_df.iterrows():
        hist = row[~(row.index == 'correct')]
        fig, ax = create_histogram_plot(hist)

        ax.set_title(f'Measure ID = {idx}; Correct = {row['correct']}')
        figures.append(fig)

    # Prepare TSNE embedding
    tsne_df = tsne_dimension_reduction(df.drop(columns='correct'))
    tsne_df = tsne_df.join(df[['correct']])

    # Prepare TSNE plot
    tsne_fig, tsne_ax = create_tsne_plot(tsne_df)
    tsne_ax.set_title('TSNE dimension reduction of histograms.')


    # Save files
    OUTPUT_PATH.mkdir(exist_ok=True, parents=True)

    # TSNE plot
    tsne_fig.savefig(OUTPUT_PATH / 'tsne.png')

    # Histogram plots
    for idx, fig in enumerate(figures):
        fig.savefig(OUTPUT_PATH / f'hist_{idx}.png')


if __name__ == '__main__':
    main()
