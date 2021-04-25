import pandas as pd
import numpy as np

#
# Parser for the tables
#

class ServiceOrderDataParser:

  def __init__(self):
    self.df_iw73 = pd.read_excel("Data/iw73_example.xlsx")
    self.df_ncr = pd.read_excel("Data/ncrdb.xlsx")
    self.df_cji3 = pd.read_excel("Data/zps_cji3_all.xlsx")

    # DATA PREPROCESSING
    # Drop the empty columns
    self.df_iw73.dropna(how="all", axis=1, inplace=True)
    self.df_ncr.dropna(how="all", axis=1, inplace=True)
    self.df_cji3.dropna(how="all", axis=1, inplace=True)

    # Get rid of no Service order number ones
    df_cji3 = self.df_cji3[self.df_cji3["Object type"] != "WBS"]
    df_cji3 = df_cji3[:-1]

    df_cji3['Object'] = df_cji3['Object'].astype(int)

    # update the iw73 table by TECO and REL
    # 1 == TECO, 0 == Not Complete
    self.df_iw73["System status"] = np.where(self.df_iw73["System status"].str.contains("TECO"), 1, 0)

  def join_tables(self):
    pd.merge(self.df_cji3, self.df_iw73, left_on="Object", right_on="Order")