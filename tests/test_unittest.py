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
    

    expected_output = [np.sum(x["a"]), np.sum(x["d"])]

    output = df_cl.sum()

    assert output == expected_output