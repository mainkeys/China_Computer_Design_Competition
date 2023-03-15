#!/usr/bin/env python
# coding: utf-8

# In[788]:


import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.ticker as ticker
import numpy as np

# pd.set_option('expand_frame_repr', False)
# pd.set_option('display.max_rows', False)
df = pd.read_csv('Energy_Transition.csv')
# print(df)
area = df.loc[:, "Country/Region"]
area = list(set(area))



# In[789]:



df = df.drop(columns=['ObjectId', 'ISO2', 'ISO3', 'Energy_Type', 'Unit', 'Source', 'CTS_Name', 'CTS_Code', 'CTS_Full_Descriptor'])
df.set_index('Country/Region', inplace = True)


df_hk = df.loc['China, P.R.: Hong Kong']
df_mainland = df.loc['China, P.R.: Mainland']
df_taiwan = df.loc['Taiwan Province of China']
df_Americas = df.loc['United States']


df_Asia = df.loc['Asia']
df_Oceania = df.loc['Oceania']
df_Africa = df.loc['Africa']
df_Europe = df.loc['Europe']
df_Americas = df.loc['Americas']
area_Continent = ['Europe','Americas','Oceania','Africa','Asia']

df_NorthernAmerica = df.loc['Northern America']
df_Latin_America = df.loc['Latin America and the Caribbean']


def Continent_single_data(_df_):
    np_single_continent = []
    group = _df_.groupby('Indicator')
    plt.rcParams['figure.figsize'] = (15, 8) # 设置画布大小，单位是inches
    for key, df in group:
        contry_name = list(set(_df_.index))[0]
        df.set_index('Technology', inplace = True)
        df = df.T[1:]
        x= list(i+1 for i in range(5))#横坐标刻度
        x_label = area_Continent
        #print(df[20:21])#提取单个国家的2020年所有能源
        df_2020 = df.loc['F2020']
        np_2020 = np.array(df_2020)
        np_single_continent.append(np_2020)
    return np_single_continent[0], np_single_continent[1]


def draw_bar_all(_df_): #所有洲所有能源柱状图对比
    group = _df_.groupby('Indicator')
    plt.rcParams['figure.figsize'] = (15, 8) # 设置画布大小，单位是inches
    for key, df in group:
        contry_name = list(set(_df_.index))[0]
        #print(contry_name)
        df.set_index('Technology', inplace = True)
        df = df.T[1:]
        #print(df)
        x= list(i+1 for i in range(5))#横坐标刻度
        x_label = area_Continent
        #print(x_label)
        print(df[20:21])#提取单个国家的2020年所有能源
        

def draw_bar(_df_):
    
    #x_label = _df_.loc['']
    group = _df_.groupby('Indicator')
    plt.rcParams['figure.figsize'] = (15, 8) # 设置画布大小，单位是inches
    flag = 1
    for key, df in group:
        contry_name = list(set(_df_.index))[0]
#         if flag==1:
#             print(key)
#             flag=0
#         else :
#             print(key) 
        df.set_index('Technology', inplace = True)
        df = df.T[1:]
        #print(df)
        x= list(i+1 for i in range(df.shape[1]))#横坐标刻度
        x_label = list(df.columns)#横坐标
        print(contry_name+ ' ' +key)
        df_2020 = df.loc['F2020']
        np_2020 = np.array(df_2020)
        #print(np_2020)
        
        
        plt.xticks(x, x_label, rotation=45)  # 绘制x刻度标签
        plt.bar(x, np_2020)  # 绘制y刻度标签
        #设置网格刻度
        #plt.grid(True,linestyle=':',color='r',alpha=0.6)
        plt.show()
    
    
    
    

def draw_single_line(_df_):   
    group = _df_.groupby('Indicator')
    plt.rcParams['figure.figsize'] = (15, 8) # 设置画布大小，单位是inches
    flag = 1
    for key, df in group:
        contry_name = list(set(_df_.index))[0]
#         if flag==1:
#             print(key)
#             flag=0
#         else :
#             print(key) 
        df.set_index('Technology', inplace = True)
        df = df.T[1:]
        
       
    
#         ColNames_List = df.columns.tolist() #提取列名转换为list 
#         print(ColNames_List,type(ColNames_List))
        
#         df_sum = pd.DataFrame()
#         fig, axs = plt.subplots(1 , 2, figsize=(10,4))
#         for i in range(df.shape[1]):
#             #print(ColNames_List[i])
#             df_single= df.loc[:, ColNames_List[i]] #提取单独列_能源类型
#             print(df_single)
#             axs[0].bar(area, df_single, width=0.4, bottom=df_sum, label= ColNames_List[i])
#             axs[0].set_ylim(0, 30000)
#             df_sum = df_sum + df_single
        
        #df = df.drop(columns=['Fossil fuels', 'Hydropower (excl. Pumped Storage)'])
        df.plot( 
             linestyle = '-', # 折线类型
             linewidth = 3, # 折线宽度
             marker = 'o', # 点的形状
             markersize = 1, # 点的大小
             markeredgecolor='black', # 点的边框色
             markerfacecolor='brown') # 点的填充色

        #plt.figure(dpi=1000,figsize=(24,8))
        tick_spacing = 1
        ax=plt.gca()
        ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
        plt.title(contry_name+' ' +key)
        #plt.show()


# In[790]:



#     fig, axs = plt.subplots(1 , 2, figsize=(10,4))
#     axs[0].bar(index, salary1, width=0.4, label= 'salary1')
#     axs[0].bar(index, salary2, width=0.4, bottom=salary1, label= 'salary2')
#     axs[0].bar(index, salary3, width=0.4, bottom=salary2+salary1, label= 'salary3')
#     axs[0].set_ylim(0, 30000)
#     axs[0].set_xticklabels(name, rotation=90)
#     axs[0].legend(loc='upper left',  shadow=True)

#     summ = salary1+salary2+salary3
#     percentage1 = salary1/summ
#     percentage2 = salary2/summ
#     percentage3 = salary3/summ

#     axs[1].bar(index, percentage1, width=0.4, label= salary1)
#     axs[1].bar(index, percentage2, width=0.4, bottom=percentage1, label= salary2)
#     axs[1].bar(index, percentage3, width=0.4, bottom=percentage1+percentage2, label= salary3)
#     axs[1].set_ylim(0,1)
#     axs[1].set_xticklabels(name, rotation=90)

#     plt.savefig('9.tiff', dpi=300)
#     plt.show()


# In[791]:



#draw_bar(df_Europe)
# draw_single_line(df_NorthernAmerica)
# draw_single_line(df_Latin_America)
# draw_single_line(df_Africa)
# draw_single_line(df_Asia)
# draw_single_line(df_mainland)
#draw_bar_all(df_Asia)

america_generation, americ2_install = Continent_single_data(df_Asia)
#print(americ2_install)
#print(Continent_single_data(df_Asia))

Europe_2020 = Continent_single_data(df_Europe)
Americas_2020 = Continent_single_data(df_Americas)
Oceania_2020 = Continent_single_data(df_Oceania)
Africa_2020 = Continent_single_data(df_Africa)
Aisa_2020 = Continent_single_data(df_Asia)
result = []


# In[ ]:





# In[ ]:





# In[ ]:




