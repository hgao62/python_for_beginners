from typing import List, Dict, Union
import pandas as pd


TRADES = "/home/coderpad/data/clearing_firm_trades.csv"
ISIN_MAPPING = "/home/coderpad/data/isin_mapping.csv"
THEOS = "/home/coderpad/data/theos.csv"
# Can you calculate the pnl difference between ELK theos and clearing firm theos?

print(pd.read_csv(TRADES).columns)

def load_trades_from_clearing_firm() -> pd.DataFrame:
  
    df = pd.read_csv(THEOS)
    return df
def load_trades_from_internal_system() ->  pd.DataFrame:
    df = pd.read_csv(TRADES)
    return df

def load_symbol_isin_mapping() -> pd.DataFrame:
    df = pd.read_csv(ISIN_MAPPING)
    return df

def enrich_symbol(trades:pd.DataFrame, isin_symbol_mapping:pd.DataFrame) -> pd.DataFrame:
    enriched_trades = pd.merge(trades, isin_symbol_mapping, on = 'ISIN', how='left')
    return enriched_trades


def normalize_qty_column(trades:pd.DataFrame) ->pd.DataFrame:
    trades['Quantity'] = trades.apply(lambda row: row['Quantity Long'] if row['Buy Sell'] == 'BUY' else row['Quantity Short'], axis=1)
    return trades
import numpy as np
def calculate_pnl(trades:pd.DataFrame, clearing_trades:pd.DataFrame, colum_name:str) -> pd.DataFrame:
    pnl = pd.merge(trades, clearing_trades, on = 'symbol', how='inner')
    pnl['price_diff'] = pnl.apply(lambda row: row['theo']-row['Trade Price'] if row['Buy Sell'] =='BUY' else row['Trade Price']- row['theo'],axis=1)
    pnl['price_diff'] = np.where(pnl['Buy Sell'] =='BUY', pnl['theo']-pnl['Trade Price'], pnl['Trade Price']- pnl['theo'])
    pnl['pnl'] = pnl['price_diff'] * pnl['Quantity']
    pnl_by_symbol = pnl.groupby('symbol')['pnl'].sum().reset_index(name=colum_name)
    return pnl_by_symbol

def main():
    internal_trades = load_trades_from_internal_system()
    isin_symbol_mapping = load_symbol_isin_mapping()
    internal_trades = enrich_symbol(internal_trades, isin_symbol_mapping)
    clearing_firm_trades = load_trades_from_clearing_firm()
    cleaned_internal_trades = normalize_qty_column(internal_trades)
    elk_theo = clearing_firm_trades[clearing_firm_trades['source']=='ELK']
    clearing_theo = clearing_firm_trades[clearing_firm_trades['source']=='CF']
    elk_pnl = calculate_pnl(cleaned_internal_trades, elk_theo,'elk_pnl')
    clearing_pnl = calculate_pnl(cleaned_internal_trades, clearing_theo,'clearing_pnl')
    final_output = pd.merge(elk_pnl, clearing_pnl, on = 'symbol')
    return final_output
    





if __name__ == "__main__":
    '''TODO'''
    res = main()
    print(res)