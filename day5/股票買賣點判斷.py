# 利用 twstock 來進行買賣點分析
# 需要安裝套件
# pip install twstock
# pip install lxml
'''
四大買賣點為:
1.量大收紅/量大收黑
2.量縮價不跌/量縮價跌
3.三日均價由上往下/三日均價由下往上
4.三日均價大於六日均價/三日均價小於六日均價
'''
import twstock

if __name__ == '__main__':
    print('四大買賣點判斷')
    symbol = '2330'
    bfp = twstock.BestFourPoint(twstock.Stock(symbol))
    print('股票代號', symbol)
    print('\n買進理由:')
    print('量大收紅', bfp.best_buy_1())
    print('量縮價不跌', bfp.best_buy_2())
    print('三日均價由上往下', bfp.best_buy_3())
    print('三日均價大於六日均價', bfp.best_buy_4())
    print('\n賣出理由:')
    print('量大收黑', bfp.best_sell_1())
    print('量縮價跌', bfp.best_sell_2())
    print('三日均價由下往上', bfp.best_sell_3())
    print('三日均價小於六日均價', bfp.best_sell_4())