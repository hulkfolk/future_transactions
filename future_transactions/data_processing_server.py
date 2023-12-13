import os
import sys
import time

import pandas as pd

from .utils import logger, load_config

# # local run
# from future_transactions.utils import logger, load_config


COL_NAMES = ['RECORD CODE', 'CLIENT TYPE', 'CLIENT NUMBER', 'ACCOUNT NUMBER', 'SUBACCOUNT NUMBER', 'OPPOSITE PARTY CODE',
             'PRODUCT GROUP CODE', 'EXCHANGE CODE', 'SYMBOL', 'EXPIRATION DATE', 'CURRENCY CODE', 'MOVEMENT CODE',
             'BUY SELL CODE', 'QUANTTTY LONG SIGN', 'QUANTITY LONG', 'QUANTITY SHORT SIGN', 'QUANTITY SHORT',
             'EXCH/BROKER FEE / DEC', 'EXCH/BROKER D C', 'EXCH/BROKER CUR CODE', 'CLEARING FEE / DEC', 'CLEARING D C', 'CLEARING CUR CODE',
             'COMMISSION FEE / DEC', 'COMMISSION D C', 'COMMISSION CUR CODE', 'TRANSACTION DATE', 'FUTURE REFERENCE',
             'TICKET NUMBER', 'EXTERNAL NUMBER', 'TRANSACTION PRICE I DEC', 'TRADER INITIALS', 'OPPOSITE TRADER ID',
             'OPEN CLOSE CODE', 'FILLER']

COL_SPECS = [(0, 3), (3, 7), (7, 11), (11, 15), (15, 19), (19, 25), (25, 27), (27, 31), (31, 37), (37, 45), (45, 48),
             (48, 50), (50, 51), (51, 52), (52, 62), (62, 63), (63, 73), (73, 85), (85, 86), (86, 89), (89, 101),
             (101, 102), (102, 105), (105, 117), (117, 118), (118, 121), (121, 129), (129, 135), (135, 141), (141, 147),
             (147, 162), (162, 168), (168, 175), (175, 176), (176, 303)]

DATA_PATH = load_config().get('data_path', '/opt/data/future_transactions')


def process_data():
    start = time.time()
    try:
        file_path = os.path.join(os.path.dirname(__file__), 'Input.txt')
    except FileNotFoundError:
        logger.exception('Input.txt does not exist!')
        return

    try:
        df = pd.read_fwf(file_path, colspecs=COL_SPECS, names=COL_NAMES)
        df['Client_Information'] = df['CLIENT TYPE'].astype(str) + "-" + df['CLIENT NUMBER'].astype(str) + "-" + \
                                   df['ACCOUNT NUMBER'].astype(str) + "-" + df['SUBACCOUNT NUMBER'].astype(str)
        df['Product_Information'] = df['EXCHANGE CODE'] + "-" + df['PRODUCT GROUP CODE'] + "-" + df['SYMBOL'] + "-" + df['EXPIRATION DATE'].astype(str)
        df['Total_Transaction_Amount'] = df['QUANTITY LONG'] - df['QUANTITY SHORT']
        df.to_csv(f'{DATA_PATH}/output.csv', columns=['Client_Information', 'Product_Information', 'Total_Transaction_Amount'])
    except:
        logger.exception('Failed to process Input.txt')
        return

    end = time.time()
    return end - start


if __name__ == '__main__':
    time_taken = process_data()
    logger.info(f'Time take to process the data: {time_taken}')
    sys.exit()

