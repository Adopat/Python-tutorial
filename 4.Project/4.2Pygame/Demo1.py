# 字符串动画效果
import random
value = "你长得真特么帅气！"
result = """
<body>
<style>
body{
    font-size:13pt;
    white-space:pre;
}
</style>
"""
def getcolor():
    colors = ['1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    color = ''
    for i in range(6):
        color += colors[random.randint(0,14)]
    return color
spcing = 1
left = 1
right = 50
for i in range(1000):

    if (i<50) or (i>=570 and i<600):
        result += "<font color='{}'>{}</font><br/>".format(getcolor(),value)
    elif (i>=50 and i<120) or (i>=190 and i<260) or (i>=330 and i<400):
        spcing +=1
        temp = '{:^{display_width}}'.format(value,display_width=spcing)
        result += "<font color='{}'>{}</font><br/>".format(getcolor(), temp)
    elif (i>=120 and i<190) or (i>=260 and i<330) or (i>=400 and i<470):
        spcing -=1
        temp = '{:^{display_width}}'.format(value,display_width=spcing)
        result += "<font color='{}'>{}</font><br/>".format(getcolor(), temp)
    elif i>=470 and i<520:
        right -=1
        left +=1
        temp = '{:^{display_width}} {:<{display_right}}'.format(value[0:4],value[4:],display_width=left,display_right=right)
        result += "<font color='{}'>{}</font><br/>".format(getcolor(), temp)
    elif i>=520 and i<570:
        right +=1
        left -=1
        temp = '{:^{display_width}} {:<{display_right}}'.format(value[0:4], value[4:], display_width=left,display_right=right)
        result += "<font color='{}'>{}</font><br/>".format(getcolor(), temp)
    elif i>=600 and i<1000:
        for align,text in zip('^<>^<>^<>',value):
            temp = '{:{fill}{align}{width}}'.format(text,fill='',align=align,width=random.randint(0,50))
            result += "<font color='{}'>{}</font><br/>".format(getcolor(), temp)
    # elif i>=470 and i<520:
    #     right -=1
    #     left +=1
    #     temp = '{:{display_width}}{:<}'
result +='</body>'
with open("anime.html", 'w') as f:
    f.write(result)
