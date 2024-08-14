# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/7/21 下午11:04
# @Note     :   仅作学习使用--禁止传播，违者必究✅

"""
大家都知道，男大当婚，女大当嫁。那么女方家长要嫁女儿，当然要提出一定的条件：高：180cm以上；富：财富1千万以上；帅：是。条件从控制台输入
如果这三个条件同时满足，则：“我一定要嫁给他！”
如果三个条件有为真的情况，则：“嫁吧，比上不足，比下有余。”
如果三个条件都不满足，则：”不嫁！“
"""
high = float(input("身高(cm):"))
wealthy = float(input("存款(万):"))
face = input("长相(帅/不帅):")
if high > 180 and wealthy >= 1000 and face == "帅":
    print("我一定要嫁给他！")
elif high > 180 or wealthy >= 1000 or face == "帅":
    print("嫁吧，比上不足，比下有余")
else:
    print("不嫁！")