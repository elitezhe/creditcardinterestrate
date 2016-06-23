"""
Python: 3.5
输入信用卡分期每期手续费费率,自动计算等效年化利率

"""

from decimal import Decimal

def CalcInterestRate(chargeRate, instalStages):
    interestPerStage = chargeRate / 100
    equiMoney = 0#等效本金
    for i in range(int(instalStages)):
        equiMoney += (i+1)/instalStages
    equiMoney /= instalStages

    return (interestPerStage * 12 / equiMoney * 100)


if __name__ == '__main__':
    print("""本程序用以计算信用卡分期手续费等价的年化利率.""")
    inputStr = input("请输入分期手续费率(无需输入百分号): [0.72]  ")
    if inputStr == '':
        chargeRate = Decimal(0.72)
    else:
        chargeRate = Decimal(inputStr)

    inputStr = input("请输入分期期数(3/6/12/24等): [12]  ")
    if inputStr == '':
        instalStages = Decimal(12)
    else:
        instalStages = Decimal(inputStr) #分期期数, 确保是整数
        instalStages = int(instalStages)
        instalStages = Decimal(instalStages)

    print("%.2f" % chargeRate)

    print("您的分期期数为%d期,每期手续费为%.2f%%:" % \
          (instalStages, chargeRate))

    print("这相当于%.3f%%的年化贷款利率!" % CalcInterestRate(chargeRate, instalStages))