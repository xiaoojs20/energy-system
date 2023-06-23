import sys
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from streamlit.web import cli as stcli
import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import atexit



def show_map():
    st.title('Electric Vehicle Charging Station in Xiamen')

    st.write('## Reality Map')
    st.write('在谷歌地图中查看厦门市电动车充电站')
    st.image('resource/Xiamen_map.png')

    st.write('## Simulation Map')
    st.write('下图中红色的点就代表电动车充电站')
    df_powerStation = pd.read_csv("data/charging_station/Xiamen_Charging_Station.csv")
    latitude_list = df_powerStation['Latitude'].tolist()
    longtitude_list = df_powerStation['Longitude'].tolist()
    altitude_list = df_powerStation['Altitude'].tolist()
    df = pd.DataFrame(
        {'lat': latitude_list,
        'lon':longtitude_list}
        )
    st.map(df)

    st.write('## Detailed Information')
    st.write('各充电站信息均来源于Google Map')
    st.dataframe(df_powerStation)

    st.write('## Weighted Directed Graph')
    # 创建一个带权有向图
    G = nx.DiGraph()
    G.add_edge('A', 'B', weight=4)
    G.add_edge('B', 'C', weight=2)
    G.add_edge('C', 'A', weight=3)

    # 绘制图像
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    # 在Streamlit中显示图像
    st.pyplot(plt)


# 添加侧边栏
st.sidebar.title('Navigation')
navigation = ['README', 'EV Charging Station Map','Power Prediction']
page = st.sidebar.radio('Go to', navigation)

# 根据用户选择的选项展示不同的页面
if page == navigation[0]:
    st.title('Welcome to this project')
    st.write('You can run this project by this command.')
    st.code('stramlit run webAPP.py')
    # 读取Markdown文件内容
    with open('README.md', 'r', encoding='utf-8') as f:
        markdown_text = f.read()
    st.markdown(markdown_text)

elif page == navigation[1]:
    show_map()

elif page == navigation[2]:
    st.title("Power Prediction for Power Stations")
    # 读取Weibull.csv文件
    windSpeed = pd.read_csv('data/Weibull.csv', header=None)

    # dtype怎么转换为float64
    train_predict = pd.read_csv('data/train_predict.csv', header=None)
    test_predict = pd.read_csv('data/test_predict.csv', header=None)
    
    PowerStationNum = 5
    # 展示每一行数据的折线图
    for i in range(PowerStationNum):
        st.write(f'## Power Station {i+1}')
        plt.plot(range(len(windSpeed.iloc[i])),windSpeed.iloc[i],label='true')
        plt.plot(range(len(train_predict.iloc[i])),train_predict.iloc[i],label='train_predict')
        plt.plot(range(6000, 6000+len(test_predict.iloc[i])),test_predict.iloc[i],label='test_predict')
        plt.legend()
        plt.xlabel('Time/(per 10s)')
        plt.ylabel('Wind Speed/(p.u.)')
        plt.title(f'Power Station {i+1}')
        # st.pyplot()
        st.pyplot(plt.gcf())
        plt.clf()  # 清除之前的图像



