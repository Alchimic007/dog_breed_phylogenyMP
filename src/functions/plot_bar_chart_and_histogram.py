from Bio import Phylo
import seaborn as sns
import matplotlib.pyplot as plt
import os

def plot_bar_chart_and_histogram(df_closeness, dog_output_directory, filename_without_extension):
    """
    Plot bar chart and histogram of distance data and save them as images.

    Args:
        df_closeness (DataFrame): DataFrame containing distance data.
        dog_output_directory (str): Path to the output directory.
        filename_without_extension (str): Filename without extension.
    """
    # Plot bar chart
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Breed', y='Distance to unknown', data=df_closeness, palette='viridis')
    plt.xticks(rotation=90)
    plt.xlabel('Breed')
    plt.ylabel('Distance to unknown')
    plt.title('Distance to Unknown Breed')
    plt.tight_layout()
    plot_output_file = os.path.join(dog_output_directory, f"{filename_without_extension}_closeness_distribution_with_names.png")
    plt.savefig(plot_output_file)
    plt.close()

    # Plot histogram
    plt.figure(figsize=(10, 6))
    sns.histplot(list(df_closeness['Distance to unknown']), kde=True)
    plt.xlabel('Distance to unknown')
    plt.ylabel('Frequency')
    plt.title('Distribution of Distance to Unknown Breed')
    plot_output_file = os.path.join(dog_output_directory, f"{filename_without_extension}_distance_distribution.png")
    plt.savefig(plot_output_file)
    plt.close()
