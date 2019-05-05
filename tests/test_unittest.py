# Unittests:

import pytest
import numpy as np
from ie_pandas import DataFrame


def test_sum_data_frame_list():

    x = {
        "a": [9, 2, 5, 8],
        "b": [True, False, False, True],
        "c": ["rasds", "sdsd", "cds", "sd"],
        "d": [1.4, 1.5, 3.6, 1.1, 1.3],
    }
    df_cl = DataFrame(x)
    

    expected_output_sum = [np.sum(x["a"]), np.sum(x["d"])]

    output_sum = df_cl.sum()
    
    assert output_sum == expected_output_sum

    
    
def test_median_data_frame_list():

    x = {
        "a": [9, 2, 5, 8],
        "b": [True, False, False, True],
        "c": ["rasds", "sdsd", "cds", "sd"],
        "d": [1.4, 1.5, 3.6, 1.1, 1.3],
    }
    df_cl = DataFrame(x)

    expected_output_median = [np.median(x["a"]), np.median(x["d"])]

    output_median = df_cl.median()

    assert output_median == expected_output_median


def test_median_data_frame_array():

    y = {
        "a": np.array([9, 2, 5, 8]),
        "b": np.array([True, False, False, True]),
        "c": np.array(["rasds", "sdsd", "cds", "sd"]),
        "d": np.array([1.4, 1.5, 3.6, 1.1, 1.3]),
    }
    df_cl_y = DataFrame(y)

    expected_output_median = [np.median(y["a"]), np.median(y["d"])]

    output_median = df_cl.median()
    
    assert output_median == expected_output_median


