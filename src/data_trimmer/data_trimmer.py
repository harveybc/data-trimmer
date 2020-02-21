# -*- coding: utf-8 -*-
"""
This File contains the DataTrimmer class. To run this script uncomment or add the following lines in the
[options.entry_points] section in setup.cfg:

    console_scripts =
         data-trimmer = data_trimmer.data_trimmer:run

Then run `python setup.py install` which will install the command `data-trimmer`
inside your current environment.
Besides console scripts, the header (i.e. until _logger...) of this file can
also be used as template for Python modules.

TODO: VERIFICAR

"""

import argparse
import sys
import logging

from data_trimmer import __version__

__author__ = "Harvey Bastidas"
__copyright__ = "Harvey Bastidas"
__license__ = "mit"

_logger = logging.getLogger(__name__)


class  DataTrimmer(Preprocessor):
    """ The Data Trimmer preprocessor class """
    
    def __init__(self):
    """ Constructor using same parameters as base class """
      super().__init__()

      self.from_start = 0
      """ number of rows to remove from start (ignored if auto_trim) """
      self.from_end = 0
      """ number of rows to remove from end (ignored if auto_trim) """
      self.remove_columns = False
      """ removes constant columns """
      self.auto_trim = True      
      """ trims the constant columns and trims all rows with consecutive zeroes from start and end.  """
        
  def parse_args(args):
      """ Parse command line parameters

      Args:
        args ([str]): command line parameters as list of strings

      Returns:
        :obj:`argparse.Namespace`: command line parameters namespace
      """
      parser = argparse.ArgumentParser(
          description="Dataset Trimmer: trims constant columns and consecutive zero rows from the end and the start of a dataset.")
      parser.add_argument(
          "--version",
          action="version",
          version="preprocessor {ver}".format(ver=__version__))
      parser.add_argument(
          "--from_start",
          help="number of rows to remove from start (ignored if auto_trim)",
          type=int,
          metavar="INT")
      parser.add_argument(
          "-v",
          "--verbose",
          dest="loglevel",
          help="set loglevel to INFO",
          action="store_const",
          const=logging.INFO)
      parser.add_argument(
          "-vv",
          "--very-verbose",
          dest="loglevel",
          help="set loglevel to DEBUG",
          action="store_const",
          const=logging.DEBUG)
      return parser.parse_args(args)

def run():
    """ Entry point for console_scripts """
    data_trimmer = DataTrimmer()
    data_trimmer.main(sys.argv[1:])


if __name__ == "__main__":
    run()
