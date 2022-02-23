# # 字符串索引 从0 开始
# s = "Hello Python"
# print(s)
# print(s[0])  # 'H'
# print(s[1])  # 'e'
# print(s[-1])  # 'n'
# # 字符串切片
# s = "Hello Python"
# print(s[0:2])  # 'He'
# print(s[:])  # 'Hello Python'
# print(s[:-1])  # 'Hello Pytho'
# print(s[::-1])  # 'nohtyP olleH 字符串反转'
# # 字符串中的引号 单引号 双引号 三引号
# print('单引号')
# # 字符串中有单引号外层应该使用双引号
# print("He said : 'OK, I will go now'")
# # 字符串中有双引号外层应该使用单引号
# print('He said : "OK, I will go now"')
# # 定义的字符串中既有单引号又有双引号应该使用三引号
# print('''He said : 'OK, "I will go now"''')
# # 其中三引号可以 直接写内容有多行 的字符串
# print("""
# 刘总：
#    您好！
#    您发的货我们已经收到，明天就把余款付清。
#
#                祝： 商祺。
#                小徐
#                2016-06-12
# """)
# # 格式化字符串方法
# #  1.format方法
# #  2.%
# #  3. f—string
#
#
# # 字符串拼接 使用加号
# print('hello' + ' world')
# # 获取字符串长度
# print(len('hello world'))
# # 字符串查找替换
# str1 = "hello world"
# print(str1.find('l'))
# # find方法没有找到返回-1
# print(str1.find('aaa'))
# # index方法没有找到会报错
# # print(str1.index('aaa'))
# # 字符串分割和连接 split() 默认使用空格进行分割
# print(str1.split())
# print(','.join('hahhah'))
# print('\n'.join(['hello', 'world']))
# 字符串截取
# 字符串填充
# 字符串大小写转换
# import PySimpleGUI as sg
# import zipfile
# import os
#
# folder = sg.popup_get_folder('请选择要压缩的文件夹')
# zip_path = sg.popup_get_file(
#     '请选择要保存的压缩包位置',
#     save_as=True,
#     default_extension='zip',
#     file_types=(('压缩包', '.zip'),)
# )
#
# with zipfile.ZipFile(zip_path, 'w') as zipobj:
#     for file in os.scandir(folder):
#         zipobj.write(file.path, file.path.replace(folder, '.'))
#
# zip_size = os.stat(zip_path).st_size // 1024
# sg.popup(f'压缩包体积大小为：{zip_size} KB')

from PIL import Image as img
# import tkinter
# import pygeoip
#
#
# class FindLocation(object):
#     def __init__(self):
#         self.gi = pygeoip.GeoIP("./GeoLiteCity.dat")
#         # 创建主窗口,用于容纳其它组件
#         self.root = tkinter.Tk()
#         # 给主窗口设置标题内容
#         self.root.title("全球定位ip位置(离线版)")
#         # 创建一个输入框,并设置尺寸
#         self.ip_input = tkinter.Entry(self.root, width=30)
#
#         # 创建一个回显列表
#         self.display_info = tkinter.Listbox(self.root, width=50)
#
#         # 创建一个查询结果的按钮
#         self.result_button = tkinter.Button(self.root, command=self.find_position, text="查询")
#
#     # 完成布局
#     def gui_arrang(self):
#         self.ip_input.pack()
#         self.display_info.pack()
#         self.result_button.pack()
#
#     # 根据ip查找地理位置
#     def find_position(self):
#         # 获取输入信息
#         self.ip_addr = self.ip_input.get()
#         aim = self.gi.record_by_name(self.ip_addr)
#         # 为了避免非法值,导致程序崩溃,有兴趣可以用正则写一下具体的规则,我为了便于新手理解,减少代码量,就直接粗放的过滤了
#         try:
#
#             # 获取目标城市
#             city = aim["city"]
#             # 获取目标国家
#             country = aim["country_name"]
#             # 获取目标地区
#             region_code = aim["region_code"]
#             # 获取目标经度
#             longitude = aim["longitude"]
#             # 获取目标纬度
#             latitude = aim["latitude"]
#         except:
#             pass
#
#         # 创建临时列表
#         the_ip_info = ["所在纬度:" + str(latitude), "所在经度:" + str(longitude), "地域代号:" + str(region_code),
#                        "所在城市:" + str(city), "所在国家或地区:" + str(country), "需要查询的ip:" + str(self.ip_addr)]
#         # 清空回显列表可见部分,类似clear命令
#         for item in range(10):
#             self.display_info.insert(0, "")
#
#         # 为回显列表赋值
#         for item in the_ip_info:
#             self.display_info.insert(0, item)
#         # 这里的返回值,没啥用,就是为了好看
#         return the_ip_info
#
#
# def main():
#     # 初始化对象
#     FL = FindLocation()
#     # 进行布局
#     FL.gui_arrang()
#     # 主程序执行
#     tkinter.mainloop()
#     pass
#
#
# if __name__ == "__main__":
#     main()
from PIL import Image as img
# from tkinter import *
# from tkinter.filedialog import *
#
#
# def GUI_app():
#     app = Tk()
#     Label(app, text='压缩小程序', font=('Arial', 20, 'bold')).pack()
#     Listbox(app, name='listbox', bg='#f2f2f2').pack(fill=BOTH, expand=True)
#     Button(app, text='打开路径', command="open_path").pack()
#     Button(app, text='开始压缩').pack()
#     app.geometry('300x400')
#     return app
#
#
# def open_path():
#     filename = askopenfilenames()
#
#
# def main():
#     app = GUI_app()
#     app.mainloop()
#
#
# if __name__ == "__main__":
#     main()
import PySimpleGUI as sg
# 获取文件路径
# path = sg.popup_get_file("请选择文件")
# path = sg.popup_get_folder("请选择目录")
# print(path)
# 保存文件
import PySimpleGUI as sg
from hashlib import sha1
import os
import pandas as pd
import threading
import time

THREAD_EVENT = '-THREAD-'

cp = sg.cprint


def the_thread(window):
    """
    The thread that communicates with the application through the window's events.

    Once a second wakes and sends a new event and associated value to the window
    """
    i = 0
    while True:
        time.sleep(1)
        window.write_event_value('-THREAD-', (
            threading.current_thread().name, i))  # Data sent is a tuple of thread name and counter
        cp('This is cheating from the thread', c='white on green')
        i += 1


def gui():
    layout = [
        [sg.Text('你选择的文件夹是:', font=("宋体", 10)), sg.Text('', key='text1', size=(50, 1), font=("宋体", 10))],
        [sg.Text('程序运行记录', justification='center')],
        [sg.Output(size=(70, 20), font=("宋体", 10))],
        # [sg.FolderBrowse('打开文件夹', key='folder', target='text1'), sg.Button('重命名'), sg.Button('关闭程序')]
        [sg.FileBrowse('打开文件', key='folder', target='text1'), sg.Button('转换'), sg.Button('关闭程序')]
    ]

    window = sg.Window('实验室数据转换工具', layout, font=("宋体", 15), default_element_size=(50, 1))

    while True:
        event, values = window.read()
        if event in (None, '关闭', '关闭程序'):  # 如果用户关闭窗口或点击`关闭`
            break
        if event == THREAD_EVENT:
            cp(f'Data from the thread ', colors='white on purple', end='')
            cp(f'{values[THREAD_EVENT]}', colors='white on red')
        if event == '转换':
            # if values['folder']:
            #     print('{0}正在重命名原文件为hash值{0}'.format('*' * 10))
            #     mult_rename(values['folder'])
            #     print('{0}重命名完毕{0}'.format('*' * 10))
            # else:
            #     print('请先选择文件夹')
            print("=======================转换开始====================")
            start = time.time()
            path = (values['folder'])
            result = read_file(path)
            df_origin = result[0]
            df_filter = result[1]
            listCycle = sorted(result[3])
            df_record = result[2][
                ['循环号', '总充电容量(mAh)', '总放电容量(mAh)', '充电容量(mAh)', '放电容量(mAh)', '充电能量(mWh)', '放电能量(mWh)', '充电比容量(mAh/g)',
                 '放电比容量(mAh/g)', '充电比能量(mWh/g)', '放电比能量(mWh/g)',
                 '充电平均电压(V)', '放电平均电压(V)', '容量保持率']]

            # df_origin = read_file(path)[0]
            # df_filter = read_file(path)[1]
            # listCycle = sorted(read_file(path)[3])
            # df_record = read_file(path)[2][
            #     ['循环号', '总充电容量(mAh)', '总放电容量(mAh)', '充电容量(mAh)', '放电容量(mAh)', '充电能量(mWh)', '放电能量(mWh)', '充电比容量(mAh/g)',
            #      '放电比容量(mAh/g)', '充电比能量(mWh/g)', '放电比能量(mWh/g)',
            #      '充电平均电压(V)', '放电平均电压(V)', '容量保持率']]
            df_filter_test = clean_data(df_filter, listCycle)
            df_discharge_recharge = get_temperature(df_origin)
            df_voltage_result = get_voltage(df_origin)
            get_result(df_voltage_result, df_discharge_recharge, df_filter_test, df_record, path)
            # print(values['folder'])
            # df_path = pd.read_excel(path)
            # # # df_path
            # df_path['GUI'] = 6666
            # df_path.to_excel('E:\\开发文档\\202202\\实验室数据\\GUI_TEST.xlsx')
            end = time.time()
            print('程序执行成功!!!,转换耗时%.2f秒' % (end - start))
            end = time.time()
    window.close()


# 1.定义读取数据方法，缩小数据范围供后续数据清洗
def read_file(path):
    df_origin = pd.read_excel(path, sheet_name='Record', header=1)
    df_max = df_origin.groupby(['循环号', '工步号', '工步类型'], as_index=False).agg({'数据序号': 'max'})
    df_min = df_origin.groupby(['循环号', '工步号', '工步类型'], as_index=False).agg({'数据序号': 'min'})
    df_max_min = df_min.append(df_max).sort_values('数据序号')
    df_filter = pd.merge(df_origin, df_max_min, on=['数据序号', '循环号', '工步号', '工步类型'], how='inner')
    df_record = pd.read_excel(path, sheet_name='Cycle', header=1)
    listCycle = df_record['循环号'].drop_duplicates().values.tolist()
    return df_origin, df_filter, df_record, listCycle


# 2.清洗其他电压
def clean_data(df_filter, listCycle):
    df_filter_test = df_filter[['设备编号', '循环号', '数据序号', '工步号', '工步类型', 'CellVolt1(0x3f/mV)'
        , 'CellVolt2(0x3e/mV)', 'gTemperature(0x08/)',
                                'RSOC(0x0d/%)',
                                'FullChgCap(0x10/mAh)',
                                'SOH(0x4f/)',
                                'CELL1BALTIME(0x44/)',
                                'CELL2BALTIME(0x44/)',
                                'QMAX1(0x44/)',
                                'QMAX2(0x44/)']]
    # 迭代DataFrame 比较上下行，给需要的数据打标记
    df_filter_test = df_filter_test.copy()
    df_filter_test['循环开始搁置末端电压1'] = 0
    df_filter_test['循环开始搁置末端电压2'] = 0
    df_filter_test['恒流充电开始电压1'] = 0
    df_filter_test['恒流充电开始电压2'] = 0
    df_filter_test['恒压充电末端电压1'] = 0
    df_filter_test['恒压充电末端电压2'] = 0
    # 增加
    # 'RSOC(0x0d/%)',
    # 'FullChgCap(0x10/mAh)',
    # 'SOH(0x4f/)',
    # 'CELL1BALTIME(0x44/)',
    # 'CELL2BALTIME(0x44/)',
    # 'QMAX1(0x44/)',
    # 'QMAX2(0x44/)'
    df_filter_test['恒压充电末端电压_RSO'] = 0
    df_filter_test['恒压充电末端电压_Full'] = 0
    df_filter_test['恒压充电末端电压_SOH'] = 0
    df_filter_test['恒压充电末端电压_CELL1B'] = 0
    df_filter_test['恒压充电末端电压_CELL2B'] = 0
    df_filter_test['恒压充电末端电压_QMAX1'] = 0
    df_filter_test['恒压充电末端电压_QMAX2'] = 0

    df_filter_test['搁置末端电压1'] = 0
    df_filter_test['搁置末端电压2'] = 0
    df_filter_test['恒流放电开始电压1'] = 0
    df_filter_test['恒流放电开始电压2'] = 0
    df_filter_test['恒流放电结束电压1'] = 0
    df_filter_test['恒流放电结束电压2'] = 0
    # 增加
    # 'RSOC(0x0d/%)',
    # 'FullChgCap(0x10/mAh)',
    # 'SOH(0x4f/)',
    # 'CELL1BALTIME(0x44/)',
    # 'CELL2BALTIME(0x44/)',
    # 'QMAX1(0x44/)',
    # 'QMAX2(0x44/)'
    df_filter_test['恒流放电结束电压_RSO'] = 0
    df_filter_test['恒流放电结束电压_Full'] = 0
    df_filter_test['恒流放电结束电压_SOH'] = 0
    df_filter_test['恒流放电结束电压_CELL1B'] = 0
    df_filter_test['恒流放电结束电压_CELL2B'] = 0
    df_filter_test['恒流放电结束电压_QMAX1'] = 0
    df_filter_test['恒流放电结束电压_QMAX2'] = 0

    df_filter_test['循环结束搁置末端电压1'] = 0
    df_filter_test['循环结束搁置末端电压2'] = 0
    for i in range(listCycle[0], listCycle[-1]):
        for index, row in df_filter_test.iterrows():
            if (df_filter_test.loc[index, :]['循环号'] == i):
                if (df_filter_test.loc[index, :]['工步类型'] == '恒压充电' and df_filter_test.loc[index - 1, :][
                    '工步类型'] == '恒压充电'
                        and df_filter_test.loc[index + 1, :]['工步类型'] == '搁置'):
                    df_filter_test.loc[index, '恒压充电末端电压1'] = row['CellVolt1(0x3f/mV)']
                    df_filter_test.loc[index, '恒压充电末端电压2'] = row['CellVolt2(0x3e/mV)']
                    df_filter_test.loc[index, '恒压充电末端电压_RSO'] = row['RSOC(0x0d/%)']
                    df_filter_test.loc[index, '恒压充电末端电压_Full'] = row['FullChgCap(0x10/mAh)']
                    df_filter_test.loc[index, '恒压充电末端电压_SOH'] = row['SOH(0x4f/)']
                    df_filter_test.loc[index, '恒压充电末端电压_CELL1B'] = row['CELL1BALTIME(0x44/)']
                    df_filter_test.loc[index, '恒压充电末端电压_CELL2B'] = row['CELL2BALTIME(0x44/)']
                    df_filter_test.loc[index, '恒压充电末端电压_QMAX1'] = row['QMAX1(0x44/)']
                    df_filter_test.loc[index, '恒压充电末端电压_QMAX2'] = row['QMAX2(0x44/)']
                elif (df_filter_test.loc[index, :]['工步类型'] == '恒流充电' and df_filter_test.loc[index - 1, :][
                    '工步类型'] == '搁置'
                      and df_filter_test.loc[index + 1, :]['工步类型'] == '恒流充电'):
                    df_filter_test.loc[index, '恒流充电开始电压1'] = row['CellVolt1(0x3f/mV)']
                    df_filter_test.loc[index, '恒流充电开始电压2'] = row['CellVolt2(0x3e/mV)']
                    df_filter_test.loc[index, '循环开始搁置末端电压1'] = row['CellVolt1(0x3f/mV)']
                    df_filter_test.loc[index, '循环开始搁置末端电压2'] = row['CellVolt2(0x3e/mV)']
                    df_filter_test.loc[index - 1, '循环结束搁置末端电压1'] = row['CellVolt1(0x3f/mV)']
                    df_filter_test.loc[index - 1, '循环结束搁置末端电压2'] = row['CellVolt2(0x3e/mV)']
                elif (df_filter_test.loc[index, :]['工步类型'] == '搁置' and df_filter_test.loc[index - 1, :]['工步类型'] == '搁置'
                      and df_filter_test.loc[index + 1, :]['工步类型'] == '恒流放电'):
                    df_filter_test.loc[index, '搁置末端电压1'] = row['CellVolt1(0x3f/mV)']
                    df_filter_test.loc[index, '搁置末端电压2'] = row['CellVolt2(0x3e/mV)']
                elif (df_filter_test.loc[index, :]['工步类型'] == '恒流放电' and df_filter_test.loc[index - 1, :][
                    '工步类型'] == '搁置'
                      and df_filter_test.loc[index + 1, :]['工步类型'] == '恒流放电'):
                    df_filter_test.loc[index, '恒流放电开始电压1'] = row['CellVolt1(0x3f/mV)']
                    df_filter_test.loc[index, '恒流放电开始电压2'] = row['CellVolt2(0x3e/mV)']
                elif (df_filter_test.loc[index, :]['工步类型'] == '恒流放电' and df_filter_test.loc[index - 1, :][
                    '工步类型'] == '恒流放电'
                      and df_filter_test.loc[index + 1, :]['工步类型'] == '搁置'):
                    df_filter_test.loc[index, '恒流放电结束电压1'] = row['CellVolt1(0x3f/mV)']
                    df_filter_test.loc[index, '恒流放电结束电压2'] = row['CellVolt2(0x3e/mV)']
                    df_filter_test.loc[index, '恒流放电结束电压_RSO'] = row['RSOC(0x0d/%)']
                    df_filter_test.loc[index, '恒流放电结束电压_Full'] = row['FullChgCap(0x10/mAh)']
                    df_filter_test.loc[index, '恒流放电结束电压_SOH'] = row['SOH(0x4f/)']
                    df_filter_test.loc[index, '恒流放电结束电压_CELL1B'] = row['CELL1BALTIME(0x44/)']
                    df_filter_test.loc[index, '恒流放电结束电压_CELL2B'] = row['CELL2BALTIME(0x44/)']
                    df_filter_test.loc[index, '恒流放电结束电压_QMAX1'] = row['QMAX1(0x44/)']
                    df_filter_test.loc[index, '恒流放电结束电压_QMAX2'] = row['QMAX2(0x44/)']
    df_filter_test = df_filter_test.groupby('循环号').agg({'循环开始搁置末端电压1': sum, '循环开始搁置末端电压2': sum,
                                                        '恒流充电开始电压1': sum, '恒流充电开始电压2': sum,
                                                        '恒压充电末端电压1': sum, '恒压充电末端电压2': sum,
                                                        '搁置末端电压1': sum, '搁置末端电压2': sum,
                                                        '恒流放电开始电压1': sum, '恒流放电开始电压2': sum,
                                                        '恒流放电结束电压1': sum, '恒流放电结束电压2': sum,
                                                        '循环结束搁置末端电压1': sum, '循环结束搁置末端电压2': sum,
                                                        '恒压充电末端电压_RSO': sum, '恒流放电结束电压_RSO': sum,
                                                        '恒压充电末端电压_Full': sum, '恒流放电结束电压_Full': sum,
                                                        '恒压充电末端电压_SOH': sum, '恒流放电结束电压_SOH': sum,
                                                        '恒压充电末端电压_CELL1B': sum, '恒流放电结束电压_CELL1B': sum,
                                                        '恒压充电末端电压_CELL2B': sum, '恒流放电结束电压_CELL2B': sum,
                                                        '恒压充电末端电压_QMAX1': sum, '恒流放电结束电压_QMAX1': sum,
                                                        '恒压充电末端电压_QMAX2': sum, '恒流放电结束电压_QMAX2': sum}
                                                       )
    return df_filter_test


# 3.获取循环号内充电的最高温度和放电的最高温度 获取循环号内的最高温度
def get_temperature(df_origin):
    df_discharge = df_origin[df_origin['工步类型'].str.contains('放电')].groupby('循环号').agg({'gTemperature(0x08/)': max})
    # 充电最高温度
    df_recharge = df_origin[df_origin['工步类型'].str.contains('充电')].groupby('循环号').agg({'gTemperature(0x08/)': max})
    # 充电放电 合并
    df_discharge_recharge = pd.merge(df_discharge, df_recharge, on='循环号', suffixes=('_放电', '_充电'), how='right')
    return df_discharge_recharge


# 4.获取恒压充电 和 恒流充电最大点压差
def get_voltage(df_origin):
    # 获取恒压充电 恒流冲电最大点压差
    df_voltage = df_origin[['循环号', '工步类型', 'CellVolt1(0x3f/mV)', 'CellVolt2(0x3e/mV)']]
    df_voltage = df_voltage.copy()
    df_voltage['差值'] = (df_voltage['CellVolt1(0x3f/mV)'] - df_voltage['CellVolt2(0x3e/mV)']).abs()
    # 过滤恒流充电和恒压充电数据
    df_voltage1 = df_voltage[df_voltage['工步类型'].str.contains('充电')].drop_duplicates(subset=['循环号', '工步类型',
                                                                                            'CellVolt1(0x3f/mV)',
                                                                                            'CellVolt2(0x3e/mV)', '差值'
                                                                                            ], keep='last',
                                                                                    inplace=False)
    df_voltage2 = df_voltage[df_voltage['工步类型'].str.contains('充电')].groupby(['循环号', '工步类型']).agg({'差值': max})
    df_voltage_result = pd.merge(df_voltage1, df_voltage2, on=['循环号', '工步类型', '差值']).drop_duplicates(
        subset=['循环号', '工步类型', '差值'], keep='last', inplace=False)
    df_voltage_result['CellVolt1(0x3f/mV)'] = df_voltage_result['CellVolt1(0x3f/mV)'].astype(str)
    df_voltage_result['CellVolt2(0x3e/mV)'] = df_voltage_result['CellVolt2(0x3e/mV)'].astype(str)
    df_voltage_result['差值'] = df_voltage_result['差值'].astype(str)
    # 字符串拼接
    df_voltage_result['电芯Cell1-电芯Cell2'] = df_voltage_result['CellVolt1(0x3f/mV)'].str.cat(
        [df_voltage_result['CellVolt2(0x3e/mV)']], sep='-')
    df_voltage_result['电芯Cell1-电芯Cell2'] = df_voltage_result['电芯Cell1-电芯Cell2'].str.cat([df_voltage_result['工步类型']],
                                                                                        sep=' ')

    def concat_func(x):
        return pd.Series({
            '差值': ';'.join(x['差值'].unique()),
            '电芯Cell1-电芯Cell2': ';'.join(x['电芯Cell1-电芯Cell2'].unique())
        }
        )

    # 分组聚合+拼接
    df_voltage_result = df_voltage_result.groupby(df_voltage_result['循环号']).apply(concat_func)
    return df_voltage_result


# 5.获取最终结果 拼接结果集，列改名
def get_result(df_voltage_result, df_discharge_recharge, df_filter_test, df_record, path):
    final_result1 = pd.merge(df_voltage_result, df_discharge_recharge, on='循环号', how='left')
    final_result2 = pd.merge(df_filter_test, df_record, on='循环号', how='left')
    final_result = pd.merge(final_result2, final_result1, on='循环号', how='left')
    filename = os.path.basename(path).replace('.xlsx', '')
    result_sheet_name = filename[:4]
    final_result = final_result.copy()
    final_result['批次号'] = filename

    final_result['电压手工填'] = ''
    final_result['内阻手工填'] = ''
    final_result['厚度手工填'] = ''
    final_result['初始电压手工填_Cell1'] = ''
    final_result['初始电压手工填_Cell2'] = ''
    final_result = final_result[['批次号',
                                 '循环号',
                                 '初始电压手工填_Cell1',
                                 '初始电压手工填_Cell2',
                                 '循环开始搁置末端电压1',
                                 '循环开始搁置末端电压2',
                                 '恒流充电开始电压1',
                                 '恒流充电开始电压2',
                                 '恒压充电末端电压1',
                                 '恒压充电末端电压2',
                                 '搁置末端电压1',
                                 '搁置末端电压2',
                                 '恒流放电开始电压1',
                                 '恒流放电开始电压2',
                                 '恒流放电结束电压1',
                                 '恒流放电结束电压2',
                                 '循环结束搁置末端电压1',
                                 '循环结束搁置末端电压2',
                                 '差值',
                                 '电芯Cell1-电芯Cell2',
                                 '恒压充电末端电压_RSO',
                                 '恒流放电结束电压_RSO',
                                 '恒压充电末端电压_Full',
                                 '恒流放电结束电压_Full',
                                 '恒压充电末端电压_SOH',
                                 '恒流放电结束电压_SOH',
                                 'gTemperature(0x08/)_充电',
                                 'gTemperature(0x08/)_放电',
                                 '恒压充电末端电压_CELL1B',
                                 '恒流放电结束电压_CELL1B',
                                 '恒压充电末端电压_CELL2B',
                                 '恒流放电结束电压_CELL2B',
                                 '恒压充电末端电压_QMAX1',
                                 '恒流放电结束电压_QMAX1',
                                 '恒压充电末端电压_QMAX2',
                                 '恒流放电结束电压_QMAX2',
                                 '总充电容量(mAh)',
                                 '总放电容量(mAh)',
                                 '充电容量(mAh)',
                                 '放电容量(mAh)',
                                 '充电能量(mWh)',
                                 '放电能量(mWh)',
                                 '充电比容量(mAh/g)',
                                 '放电比容量(mAh/g)',
                                 '充电比能量(mWh/g)',
                                 '放电比能量(mWh/g)',
                                 '充电平均电压(V)',
                                 '放电平均电压(V)',
                                 '容量保持率',
                                 '电压手工填',
                                 '内阻手工填',
                                 '厚度手工填'
                                 ]]
    final_result = final_result.rename(columns={'批次号': '批次', '循环开始搁置末端电压1': '循环开始搁置末端电压_Cell1',
                                                '循环开始搁置末端电压2': '循环开始搁置末端电压_Cell2',
                                                '恒流充电开始电压1': '搁置后恒流充电开始电压_Cell1',
                                                '恒流充电开始电压2': '搁置后恒流充电开始电压_Cell2',
                                                '恒压充电末端电压1': '搁置前恒压充电开始电压_Cell1',
                                                '恒压充电末端电压2': '搁置前恒压充电开始电压_Cell2',
                                                '搁置末端电压1': '搁置末端电压_cell1',
                                                '搁置末端电压2': '搁置末端电压_cell2',
                                                '恒流放电开始电压1': '搁置后恒流放电开始电压_Cell1',
                                                '恒流放电开始电压2': '搁置后恒流放电开始电压_Cell2',
                                                '恒流放电结束电压1': '搁置前恒流放电结束电压_Cell1',
                                                '恒流放电结束电压2': '搁置前恒流放电结束电压_Cell2',
                                                '循环结束搁置末端电压1': '循环结束搁置末端电压_Cell1',
                                                '循环结束搁置末端电压2': '循环结束搁置末端电压_Cell2',
                                                '差值': '电芯压差最大点电压_Delta',
                                                '电芯Cell1-电芯Cell2': '电芯压差最大点电压_Cell1_Cell2',
                                                'gTemperature(0x08/)_充电': 'gTemperature(0x08/)_充电最高温度',
                                                'gTemperature(0x08/)_放电': 'gTemperature(0x08/)_放电最高温度'
                                                })
    final_result.to_excel('E:\\开发文档\\202202\\实验室数据\\下载数据格式_新威_20220214.xlsx', sheet_name=result_sheet_name)


def main():
    gui()


if __name__ == '__main__':
    main()
