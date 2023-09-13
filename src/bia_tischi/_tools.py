from langchain.tools import StructuredTool, tool
from ._machinery import _context
from ._utilities import make_variable_name, find_image

if _context.verbose:
    print("Setting up tools")

@_context.tools.append
@tool
def load_image(filename: str):
    """Useful for loading an image file and storing it under a given variable name."""
    from skimage.io import imread

    if _context.verbose:
        print("loading image", filename)
    image = imread(filename)
    variable_name = make_variable_name(filename)
    _context.variables[variable_name] = image
    return "The image is now stored as " + variable_name


@_context.tools.append
@tool
def load_csv(filename: str):
    """Useful for loading a csv file and storing its as pandas DataFrame under a given variable name."""
    from pandas import read_csv

    if _context.verbose:
        print("loading csv", filename)
    df = read_csv(filename)

    variable_name = make_variable_name(filename)
    _context.variables[variable_name] = df
    return "The csv file is now stored as " + variable_name


@_context.tools.append
@tool
def list_tools():
    """Lists all available tools"""

    return "\n".join(list([t.name for t in _context.tools]))



@_context.tools.append
@tool
def list_dataframes():
    """Lists all available dataframes"""
    from ._utilities import is_dataframe

    return "\n".join(list([v for v in _context.variables.keys() if is_dataframe(_context.variables[v])]))


@_context.tools.append
@tool
def list_images():
    """Lists all available images"""
    from ._utilities import is_image

    return "\n".join(list([v for v in _context.variables.keys() if is_image(_context.variables[v])]))


