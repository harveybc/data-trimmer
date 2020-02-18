# -*- coding: utf-8 -*-

import pytest
from data_trimmer.data_trimmer import trim_data

__author__ = "Harvey Bastidas"
__copyright__ = "Harvey Bastidas"
__license__ = "mit"

# get the number of rows and columns of the test dataset
rows_d, cols_d = get_size_csv(test_file)

# test code: C02T01
def test_trim_rows():
    # perform trimming using the function trim_data(test_file, out_file, auto_trim=true, column_trim=true, from_start=0, from_end=0)
    rows_t, cols_t = rowstrim_data(test_file, out_file, false, false, 10, 10)

    # get the number of rows and cols from out_file
    rows_o, cols_o = getsizecsv(out_file)

    # assert if the new == old - trimmed
    assert (rows_o + cols_o) == (rows_d + cols_d) - (rows_t + cols_t)
    