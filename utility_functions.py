import math
import matplotlib.pyplot as plt

def round_to_base(in_val, base):
    """
    Round the in_val value to the nearest base.
    E.g. base 5
        2  -> 0
        9  -> 10
        12 -> 10
        13 -> 15
    
    :param in_val: Value to round
    :param base: Base to round to
    :return: Rounded value
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
    
    :param in_val: Value to round
    :param range_val: Range to floor to
    :return: Rounded value range
    """
    
    floored_val = math.floor(in_val/range_val) * range_val
    
    return f"{floored_val} - {floored_val + range_val - 1}"

def find_column_names(df, find_column_name):
    """
    Find all columns in a dataframe based on a prefix (find_column_name) and return as a list.
    E.g. columns: ["a_a", "a_b", "b_a", "c"] and find_column_name: "a"
        ["a_a", "a_b"]
    
    :param df: Input data frame
    :param find_column_name: Prefix of column name
    :return: Rounded value range
    """
    
    return [column_name for column_name in df.columns if f"{find_column_name}_" in column_name ]

def fetch_columns_on_name_list(df, find_column_name_list):
    """
    Find all subsets of the prefixes provided in find_column_name_list and form a list of these.
    The columns are found with find_column_names.
    
    :param df: Input data frame
    :param find_column_name_list: List of prefix column names
    :return: Rounded value range
    """
    
    return [name for name_group in [find_column_names(df, column_name) for column_name in find_column_name_list] for name in name_group]

def plot_result(df, x_axis_component, y_axis_component, target_name, title="component plot"):
    """
    Plot the provided data_frame (shape 3xn) on a 2D plotgraph.
    
    :param df: Input data frame
    :param x_axis_component: Name for x axis component
    :param y_axis_component: Name for y axis component
    :param target: Name for target data
    :param title: Title of the plotted data
    """

    fig = plt.figure(figsize = (8,8))
    ax = fig.add_subplot(1,1,1) 

    ax.set_xlabel(x_axis_component, fontsize = 15)
    ax.set_ylabel(y_axis_component, fontsize = 15)
    ax.set_title(title, fontsize = 20)

    targets = [True, False]
    colors = ['r', 'g']

    for target, color in zip(targets,colors):
        indicesToKeep = df[target_name] == target
        ax.scatter(df.loc[indicesToKeep, x_axis_component], df.loc[indicesToKeep, y_axis_component], c = color, s = 50)


    ax.legend(targets)
    ax.grid()