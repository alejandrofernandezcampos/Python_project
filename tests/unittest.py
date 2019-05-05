# Unittests:

import pytest
from ie_pandas import DataFrame


def test_sum_data_frame_list(self):

    df_cl = DataFrame()
    x = {
        "a": [9, 2, 5, 8],
        "b": [True, False, False, True],
        "c": ["rasds", "sdsd", "cds", "sd"],
        "d": [1.4, 1.5, 3.6, 1.1, 1.3],
    }
    y = df_cl(x)

    expected_output = [np.sum(x["a"]), np.sum(x["d"])]

    output = y.sum()

    assert output == expected_output