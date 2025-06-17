# import pandas as pd
# import numpy as np

# # 读取Excel数据
# df = pd.read_excel("c:/Users/11428/Downloads/pdos_data.xlsx", sheet_name="Sheet1")
# energy = df["能量(eV)"].values
# d_up = df[["d1_up", "d2_up", "d3_up", "d4_up", "d5_up"]].values
# d_down = df[["d1_down", "d2_down", "d3_down", "d4_down", "d5_down"]].values

# # 定义积分函数
# def calculate_integral(orbits, energy_values, e_min, e_max):
#     mask = (energy_values >= e_min) & (energy_values <= e_max)
#     return np.trapz(orbits[mask], x=energy_values[mask])

# # 设定能量范围
# e_min, e_max = -5, 5  # 可替换为实际范围

# # 计算自旋向上目标轨道和全部轨道
# up_target = np.sum(d_up[:, [0, 1, 4]], axis=1)
# S_up_target = calculate_integral(up_target, energy, e_min, e_max)
# S_up_all = calculate_integral(np.sum(d_up, axis=1), energy, e_min, e_max)

# # 计算自旋向下目标轨道和全部轨道
# down_target = np.sum(d_down[:, [0, 1, 4]], axis=1)
# S_down_target = calculate_integral(down_target, energy, e_min, e_max)
# S_down_all = calculate_integral(np.sum(d_down, axis=1), energy, e_min, e_max)

# # 计算占比
# total_target = S_up_target + S_down_target
# total_all = S_up_all + S_down_all
# percentage = (total_target / total_all) * 100
# print(f"占比：{percentage:.2f}%")

# import pandas as pd
# import numpy as np

# def calculate_pdos_ratios(file_path, sheet_name='Sheet1', energy_range=(-5, 5)):
#     """
#     计算PDOS数据中各轨道的占比
    
#     参数:
#     file_path (str): Excel文件路径
#     sheet_name (str): 工作表名称
#     energy_range (tuple): 能量积分范围 (e_min, e_max)
    
#     返回:
#     dict: 包含各轨道占比的字典
#     """
#     # 读取Excel数据
#     df = pd.read_excel(file_path, sheet_name=sheet_name)
    
#     # 提取能量列和轨道数据
#     energy = df['能量(eV)'].values
#     up_columns = ['d1_up', 'd2_up', 'd3_up', 'd4_up', 'd5_up']
#     down_columns = ['d1_down', 'd2_down', 'd3_down', 'd4_down', 'd5_down']
    
#     # 筛选能量范围内的数据
#     mask = (energy >= energy_range[0]) & (energy <= energy_range[1])
#     filtered_energy = energy[mask]
#     filtered_up = df.loc[mask, up_columns].values
#     filtered_down = df.loc[mask, down_columns].values
    
#     # 计算各轨道积分 (使用梯形法则)
#     def integrate(orbit_data):
#         return np.trapz(orbit_data, x=filtered_energy)
    
#     # 计算各轨道的积分值
#     up_integrals = np.array([integrate(filtered_up[:, i]) for i in range(5)])
#     down_integrals = np.array([integrate(filtered_down[:, i]) for i in range(5)])
    
    
#     # 计算总和
#     total_all = np.sum(up_integrals) + np.sum(down_integrals)
    
#     # 计算目标轨道的占比
#     results = {}
    
#     # 自旋向上的第1、2、5个轨道在整个d轨道中的占比
#     target_orbit_indices = [0, 1, 4]  # 第1、2、5个轨道的索引
#     for i in target_orbit_indices:
#         orbit_name = up_columns[i]
#         results[f'{orbit_name}在整个d轨道中的占比'] = (up_integrals[i] / total_all) * 100
    
#     # 自旋向下的第1、2、5个轨道在整个d轨道中的占比
#     for i in target_orbit_indices:
#         orbit_name = down_columns[i]
#         results[f'{orbit_name}在整个d轨道中的占比'] = (down_integrals[i] / total_all) * 100
    
#     # 自旋向上5个轨道总和在整个d轨道中的占比
#     results['自旋向上5个轨道总和在整个d轨道中的占比'] = (np.sum(up_integrals) / total_all) * 100
    
#     # 自旋向下5个轨道总和在整个d轨道中的占比
#     results['自旋向下5个轨道总和在整个d轨道中的占比'] = (np.sum(down_integrals) / total_all) * 100
    
#     return results

# # 示例使用
# if __name__ == "__main__":
#     file_path = "c:/Users/11428/Downloads/pdos_data.xlsx"  # 替换为实际文件路径
#     energy_range = (-5, 5)  # 替换为实际能量范围
    
#     results = calculate_pdos_ratios(file_path, energy_range=energy_range)
    
#     # 输出结果
#     print("轨道占比计算结果:")
#     for key, value in results.items():
#         print(f"{key}: {value:.2f}%")    







import pandas as pd
import numpy as np

def calculate_pdos_ratios(df, energy_range):
    """
    计算PDOS数据中各轨道的占比

    参数:
    df (DataFrame): 包含PDOS数据的DataFrame
    energy_range (tuple): 能量积分范围 (e_min, e_max)

    返回:
    dict: 包含各轨道占比的字典
    """
    # 提取能量列和轨道数据
    energy = df['能量(eV)'].values
    up_columns = ['d1_up', 'd2_up', 'd3_up', 'd4_up', 'd5_up']
    down_columns = ['d1_down', 'd2_down', 'd3_down', 'd4_down', 'd5_down']

    # 筛选能量范围内的数据
    mask = (energy >= energy_range[0]) & (energy <= energy_range[1])
    filtered_energy = energy[mask]
    filtered_up = df.loc[mask, up_columns].values
    filtered_down = df.loc[mask, down_columns].values

    # 检查是否存在负值
    negative_values_up = (filtered_up < 0).any()
    negative_values_down = (filtered_down < 0).any()
    print(f"自旋向上数据存在负值: {negative_values_up}")
    print(f"自旋向下数据存在负值: {negative_values_down}")

    # 计算各轨道积分 (使用梯形法则)
    def integrate(orbit_data):
        return np.trapz(np.abs(orbit_data), x=filtered_energy)

    # 计算各轨道的积分值
    up_integrals = np.array([integrate(filtered_up[:, i]) for i in range(5)])
    down_integrals = np.array([integrate(filtered_down[:, i]) for i in range(5)])

    # 计算总和
    total_all = np.sum(up_integrals) + np.sum(down_integrals)

    # 计算目标轨道的占比
    results = {}

    # 自旋向上的第1、2、5个轨道在整个d轨道中的占比
    target_orbit_indices = [0, 1, 4]  # 第1、2、5个轨道的索引
    for i in target_orbit_indices:
        orbit_name = up_columns[i]
        results[f'{orbit_name}在整个d轨道中的占比'] = (up_integrals[i] / total_all) * 100

    # 自旋向下的第1、2、5个轨道在整个d轨道中的占比
    for i in target_orbit_indices:
        orbit_name = down_columns[i]
        results[f'{orbit_name}在整个d轨道中的占比'] = (down_integrals[i] / total_all) * 100

    # 自旋向上5个轨道总和在整个d轨道中的占比
    results['自旋向上5个轨道总和在整个d轨道中的占比'] = (np.sum(up_integrals) / total_all) * 100

    # 自旋向下5个轨道总和在整个d轨道中的占比
    results['自旋向下5个轨道总和在整个d轨道中的占比'] = (np.sum(down_integrals) / total_all) * 100

    return results

# 读取 Excel 文件
excel_file = pd.ExcelFile('c:/Users/11428/Downloads/pdos_data.xlsx')
# 获取指定工作表中的数据
df = excel_file.parse('Sheet1')

# 找出能量列的最小值和最大值
energy_min = df['能量(eV)'].min()
energy_max = df['能量(eV)'].max()

# 定义能量范围
energy_range = (energy_min, energy_max)

results = calculate_pdos_ratios(df, energy_range)

# 输出结果
print("轨道占比计算结果:")
for key, value in results.items():
    print(f"{key}: {value:.2f}%")