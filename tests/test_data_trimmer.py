# -*- coding: utf-8 -*-

import pytest
import csv 
import sys
sys.path.append('c:\\Users\\HarveyD\\Dropbox\\preprocessor\\src\\')
from data_trimmer.data_trimmer import DataTrimmer 
from test_preprocessor import TestPreprocessor 


__author__ = "Harvey Bastidas"
__copyright__ = "Harvey Bastidas"
__license__ = "mit"

class  TestDataTrimmer(TestPreprocessor): 
    """ Component Tests
    """
    
    def __init__(self):
        """ Component Tests Constructor """
        conf=None
        conf.input_file = "test_input.csv"
        conf.output_file = "test_output.csv"
        conf.input_config_file = "in_config.csv"
        conf.output_config_file = "out_config.csv"
        super().__init__(conf)
        """ Use parent class attributes and test data as parameters for parent class constructor """
        self.dt = DataTrimmer(conf)
        """ Data trimmer object """

    def test_C02T01_trim_fixed_rows(self):
        """ Trims a configurable number of rows from the start or end of the input dataset by using the trim_fixed_rows method. Execute trimmer with from_start=10, from_end=10. """
        rows_t, cols_t = self.dt.trim_fixed_rows(10, 10)
        # get the number of rows and cols from out_file
        rows_o, cols_o = self.get_size_csv(self.output_file)
        # assert if the new == old - trimmed
        assert (rows_o + cols_o) == (self.rows_d + self.cols_d) - (rows_t + cols_t)
        
    def test_C02T02_trim_columns(self):
        """ Trims all the constant columns by using the trim_columns method. Execute trimmer with remove_colums = true. """
        rows_t, cols_t = self.dt.trim_columns()
        # get the number of rows and cols from out_file
        rows_o, cols_o = self.get_size_csv(self.output_file)
        # assert if the new == old - trimmed
        assert (rows_o + cols_o) == (self.rows_d  + self.cols_d) - (rows_t + cols_t)

    def test_C02T03_trim_auto(self):
        """ Trims all the constant columns and trims all rows with consecutive zeroes from start and end by using the trim_auto method. Execute trimmer with auto_trim = true.  """
        rows_t, cols_t = self.dt.trim_auto()
        # get the number of rows and cols from out_file
        rows_o, cols_o = self.get_size_csv(self.output_file)
        # assert if the new == old - trimmed
        assert (rows_o + cols_o) == (self.rows_d  + self.cols_d) - (rows_t + cols_t)