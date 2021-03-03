from bdshare import get_current_trade_data
import sys
from prettytable import PrettyTable
t = PrettyTable(['\33[33m'+'Name', 'LTP', 'High','Low', 'YCP','Change(%)','Trade','Volume'+'\033[0m'])

if (sys.argv[1]=='--add'):
    name = open("stocklist.txt", "w")
    addline=''
    for newstock in sys.argv[2:]:
        addline = addline + ','+ newstock
    name.write(addline)
    name.close()
    print("***The stocks have been added in the list***")
    quit() 

stock=open("stocklist.txt","r")
kolla = stock.read().split(',')
pad = kolla if sys.argv[1] == '--n' else sys.argv

for stck in pad[1:]:
    df = get_current_trade_data(stck)
    ltp = str(df['ltp']).split()[1]
    High = str(df['high']).split()[1]
    low = str(df['low']).split()[1]
    ycp= str(df['ycp']).split()[1]
    Change= "{:.2f}".format((float(ltp)-float(ycp))*100/float(ycp))
    change= '\033[91m'+str(Change)+'\033[0m' if float(Change)<= 0 else '\033[32m'+str(Change)+'\033[0m'
    Trade=str(df['trade']).split()[1]
    Volume=str(df['volume']).split()[1]
    t.add_row([stck, ltp, High , low, ycp, change, Trade, Volume])
print(t)
