import pymssql
import random
import time

server = 'localhost'
user = "sa"
password = '123456'

content = [
    ['barrier/save', '添加路障','tb_Barrier'],
    ['barrier/save', '添加应急路障','tb_Barrier'],
    ['barrier/update','撤销路障','tb_Barrier'],
    ['barrier/update','撤销应急路障','tb_Barrier'],
    ['calamity/save','灾害事件','tb_Calamity'],
    ['calamity/update','结束灾害事件','tb_Calamity'],
    ['common/save','保存数据','tb_MaterialStatistics'],
    ['data/delete','删除数据','tb_CarEntry'],
    ['data/delete_pl','批量删除数据','tb_CarEntry'],
    ['data/update','更新数据','tb_CarEntry'],
    ['Dispatchinstructionlist/save','积水点/内涝处置指令','tb_DispatchInstructionList'],
    ['Dispatchinstructionlist/save','积水点处置指令','tb_DispatchInstructionList'],
    ['Dispatchinstructionlist/save','内涝处置指令','tb_DispatchInstructionList'],
    ['Dispatchinstructionlist/save', '窨井/雨量处置指令', 'tb_DispatchInstructionList'],
    ['Dispatchinstructionlist/save','窨井处置指令','tb_DispatchInstructionList'],
    ['Dispatchinstructionlist/save','雨量处置指令','tb_DispatchInstructionList'],
    ['ecinstructions/save','应急指挥指令','tb_ECinstructions'],
    ['Ecinstructions/save','应急指令反馈','tb_ECinstructions'],
    ['ecinstructions/update','结束应急指挥指令','tb_ECinstructions'],
    ['emergencycommand/save','应急指挥','tb_EmergencyCommand'],
    ['Instructionandfeedback/save','积水点反馈保存','tb_InstructionAndFeedback'],
    ['Instructionandfeedback/save','积水点协同反馈保存','tb_InstructionAndFeedback'],
    ['Instructionandfeedback/save','内涝反馈保存','tb_InstructionAndFeedback'],
    ['IntensityFormula/delete','删除暴雨强度公式','tb_IntensityFormula'],
    ['IntensityFormula/save','添加暴雨强度公式','tb_IntensityFormula'],
    ['IntensityFormula/update','修改暴雨强度公式','tb_IntensityFormula'],
    ['menu/delete','删除菜单','tb_Menu'],
    ['menu/save','添加菜单','tb_Menu'],
    ['menu/update','修改菜单','tb_Menu'],
    ['monitoringalarm/update','监测数据报警修改','tb_MonitoringAlarm'],
    ['partment/delete','删除部门','tb_Partment'],
    ['partment/save','添加部门','tb_Partment'],
    ['partment/update','修改部门','tb_Partment'],
    ['Pumpdispose/save','泵站处置指令','tb_PumpDispose'],
    ['Regionalhead/delete','修改区域负责人','tb_RegionalHead'],
    ['Regionalhead/save','添加区域负责人','tb_RegionalHead'],
    ['Regionalhead/save','修改区域负责人','tb_RegionalHead'],
    ['role/delete','删除角色权限','tb_Role'],
    ['role/save','添加角色权限','tb_Role'],
    ['role/update','修改角色权限','tb_Role'],
    ['sfscheme/update','结束方案预警','tb_SFScheme'],
    ['user/delete','删除用户','tb_Operator'],
    ['user/login','用户登录','tb_Operator'],
    ['user/logout','用户退出','tb_Operator'],
    ['user/save','用户注册','tb_Operator'],
    ['user/update','修改用户信息','tb_Operator'],
    ['WaterEvent/update','积水点/内涝解除报警','tb_WaterEvent'],
    ['Watereventfiling/delete','删除积水事件归档','tb_WaterEventfiling'],
    ['watereventfiling/save','积水事件归档','tb_WaterEventfiling'],
    ['waterwarning/save','内涝预警信号发布通知','tb_WaterWarning'],
    ['we/save','内涝预报发布','tb_WaterEvent'],
    ['we/save','处置指令','tb_DispatchInstructionList'],
    ['we/save','积水点报送','tb_WaterEvent'],
    ['we/save','内涝预报发布','tb_WaterEvent'],
    ['we/save','微信端积水点报送','tb_WaterEventwx']
]

conn = pymssql.connect(server, user, password, "zjps")
cursor = conn.cursor()
cursor.execute('SELECT * FROM tb_Operator')
uid = cursor.fetchall()
uid_list = []
for i in uid:
    uid_list.append(i[0])

action = random.choice(range(10, 26))  # 随机操作的次数10-25次
r_uid = random.choice(uid_list)  # 随机uid [1, 15, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53]

start_time = 1509465600 + 21600
end_time = 1509465600 + (22 * 3600)


def sjnr():
    rt = random.choice(range(0, len(content)))
    return content[rt]


def settime(st, ed, sj):
    rt = random.sample(range(st, ed), sj)
    return sorted(rt)


def zxcr():
    global start_time, end_time
    for i in range(0, len(uid_list)):
        uid = uid_list[i]
        sj = random.choice(range(10, 20))
        timeArr = settime(start_time, end_time, sj)
        for j in range(0, len(timeArr)):
            curTime = timeArr[j]
            curcon = sjnr()
            cursor = conn.cursor()
            sql_insert = 'insert into tb_ActionLog(userid,object,action,count,last_time,ip,descript)' \
                         ' VALUES (%s,%s,%s,%s,%s,%s,%s)'
            param = (uid, curcon[2], curcon[0], 0, curTime, "127.0.0.1", curcon[1])
            cursor.execute(sql_insert, param)
            conn.commit()

        if i == len(uid_list)-1:
            start_time = start_time+86400
            end_time = end_time+86400

            timearray = time.localtime(start_time)
            dtime = time.strftime("%Y-%m-%d %H:%M:%S", timearray)
            print(dtime)
            if start_time > 1545148800:
                pass
            else:
                zxcr()

zxcr()
conn.commit()

