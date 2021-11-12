"""Visualize the sets using the supervenn package."""

from typing import List
from typing import Set

from supervenn import supervenn  # type: ignore
import matplotlib.pyplot as plot  # type: ignore

import sys


def visualize_sets(sets: List[Set[str]]):
    """Create a visualization of sets."""
    # create a matplotlib figure space
    plot.figure(figsize=(16, 8))
    # compute all of the subsets and then visualize them
    supervenn_plot = supervenn(
        sets, side_plots=True, widths_minmax_ratio=1, sets_ordering="minimize gaps"
    )
    # save the visualization in the output/ directory
    # NOTE: if you want to make the program more configurable, please
    # consider making this directory and file name a parameter to
    # the program instead of being hard-coded as a string
    file_name = sys.argv[2]
    split = file_name.split("/")[1]
    sliced = split.split(".")[0]
    sliced_again = sliced.split("_")[0]
    # NOTE: you are not required to complete this task; however,
    # adding this feature to the program will make it easier for
    # you to complete the analysis of the text files using sets
    plot.savefig(f"graphics/set-visualization-{sliced_again}.png")
    # return the dictionary of chunks for visualization purposes
    return supervenn_plot.chunks
