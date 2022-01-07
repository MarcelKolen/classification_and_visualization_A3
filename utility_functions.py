import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def round_to_base(in_val, base):
    """
    Round the in_val value to the nearest base.
    E.g. base 5
        2  -> 0
        9  -> 10
        12 -> 10
        13 -> 15
    
    :param in_val: Value to round.
    :param base: Base to round to.
    :return: Rounded value.
    """
    
    return round(in_val/base) * base

def floor_range(in_val, range_val):
    """
    Floor the in_val value to the nearest base (range_val). 
    And then indicate a range.
    E.g. base 5
        2  -> 0 - 4
        9  -> 5 - 9
        12 -> 10 - 14
        13 -> 10 - 14
    
    :param in_val: Value to round.
    :param range_val: Range to floor to.
    :return: Rounded value range.
    """
    
    floored_val = math.floor(in_val/range_val) * range_val
    
    return f"{floored_val} - {floored_val + range_val - 1}"

def find_column_names(df, find_column_name):
    """
    Find all columns in a dataframe based on a prefix (find_column_name) and return as a list.
    E.g. columns: ["a_a", "a_b", "b_a", "c"] and find_column_name: "a"
        ["a_a", "a_b"]
    
    :param df: Input data frame.
    :param find_column_name: Prefix of column name.
    :return: Rounded value range.
    """
    
    return [column_name for column_name in df.columns if f"{find_column_name}_" in column_name ]

def fetch_columns_on_name_list(df, find_column_name_list):
    """
    Find all subsets of the prefixes provided in find_column_name_list and form a list of these.
    The columns are found with find_column_names.
    
    :param df: Input data frame.
    :param find_column_name_list: List of prefix column names.
    :return: Rounded value range.
    """
    
    return [name for name_group in [find_column_names(df, column_name) for column_name in find_column_name_list] for name in name_group]

def plot_result(df, x_axis_component, y_axis_component, target_names, title="component plot", num_of_columns=3, size_x=16, size_y=16, c_map_name="cividis"):
    """
    Plot the provided data_frame on a 2D plotgraph with multiple targets.
    
    :param df: Input data frame.
    :param x_axis_component: Name for x axis component.
    :param y_axis_component: Name for y axis component.
    :param target_names: Names for target data (input must be a list).
    :param title: Title of the plotted data.
    :param num_of_columns: Number of columns in the grid representation.
    :param size_x: Horizontal figure size.
    :param size_y: Vertical figure size.
    :param c_map_name: Color map to use.
    """

    num_of_plots = len(target_names)
    num_of_rows = num_of_plots // num_of_columns 
    num_of_rows += num_of_plots % num_of_columns
    
    fig = plt.figure(figsize = (size_x, size_y))
    
    # Create a plot for every target attribute in the dataframe.
    for i, value in enumerate(target_names):
        ax = fig.add_subplot(num_of_rows,num_of_columns,i+1)

        ax.set_xlabel(x_axis_component, fontsize = 15)
        ax.set_ylabel(y_axis_component, fontsize = 15)
        ax.set_title(value, fontsize = 20)

        # Normalize target data.
        target_df = df[value].astype("float")
        min_max_norm_target_df = (target_df-target_df.min())/(target_df.max()-target_df.min())

        pd_plt = pd.concat([df[x_axis_component],df[y_axis_component], min_max_norm_target_df], axis=1)
        pd_plt.columns = ["x", "y", "z"]

        sc = ax.scatter(pd_plt.x, pd_plt.y, c=pd_plt.z, s=50, cmap=c_map_name)
        fig.colorbar(sc)

    fig.suptitle(title, fontsize=24)
    fig.show()
    
def random_selection(size, min_val, max_val, replace=False, sort=True):
    """
    Create a numpy array of random values of size n=size with values between
    min=min_val and max=max_val.
    
    The random list can be returned as a sorted list of random values 
    between min_val and max_val, or as an unsorted list.
    
    The list can contain only unique values or repeated values.
    
    :param size: Number of elements to get. Note that this can be limited.
    to max_val - min_val if its exceeds this difference when replace is false.
    :param min_val: Min boundary of random values (inclusive).
    :param max_val: Max boundary of random values (exclusive).
    :param replace: False, only allow unique values; True, allow values to occur multiple times.
    :param sort: Sort the resulting list.
    :return: List of random integers between min_val and max_val of size n=size.
    """

    # When replacement is not allowed (only unique numbers), limit the size value to the difference of
    # max_val - min_val (difference between the boundaries) if it exceeds this amount.
    if not replace:
        size = size if (dif := max_val - min_val) >= size else dif

    select = np.random.choice(range(min_val, max_val), size, replace=replace)
    
    return np.sort(select) if sort is True else select