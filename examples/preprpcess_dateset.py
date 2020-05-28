import pandas as pd
import sys


def fmt_dt(dt):
    dt_str =  dt.strftime('%Y%m%d %H%M%S')
    dot = dt_str.find('.')
    if dot > 0:
        print(dt_str)
        tt 
        dt_str = dt_str[:dot]
    return dt_str

def main(argv):
    assert(len(argv)==2)
    in_file = argv[0]
    out_file = argv[1]
    data = pd.read_csv(in_file)
    data.index = pd.to_datetime(data['date_time'], format='%Y-%m-%d %H:%M:%S.%f')
    data = data.loc[~data.index.duplicated(keep='first')]
    data['date_time'] = data.index.to_series().apply(fmt_dt)
    # print(data.columns)
    data.drop(['tick_num', 'cum_buy_volume', 'cum_ticks', 'cum_dollar_value'],  axis=1, inplace=True)
    data.to_csv(out_file, sep=';', header =False, index=False)
    
    # 20170102 020100;1.071860;1.072060;1.071810;1.071810;0

# (ptrader) C:\git\btgym\examples>python  preprpcess_dateset.py .\data\dollar_bars_tx_20180701_20200301_1600K.csv .\data\tx_data.csv
if __name__ == "__main__":
    main(sys.argv[1:])