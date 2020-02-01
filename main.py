from tools import Calaculation
import math

calc = Calaculation()
print('=========================================')
print('支持常用三角函数以及反函数(tan,sin,cos)\t支持括号优先级运算\n支持乘方及开方\tpi=π')
while True:
    result = calc.main(input('>>').replace('pi',str(math.pi)))
    # if len(result)>10:
    #     print('结果过长，自动四舍五入..')
    #     print(round(float(result),5))
    #
    # else:
    #     print(result)
    print(result)