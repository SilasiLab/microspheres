"""
Author: Gavin Heidenreich
Institution: University of Ottawa
Contact: gheidenr@uottawa.ca
"""

import pandas as pd
import numpy as np
import os
from collections import defaultdict

# set base_dir to the directory containing your dataset
# in my case it was set as below
base_dir = 'ExampleDatasetGavin'

atlas_df = pd.read_excel(base_dir + os.sep + 'AMB Atlas Organization.xlsx', 'Tree Organization')

# this class has methods to generate dict objects mapping IDs to names and names to levels
class utils:
    def __init__(self, atlas_df):
        self.atlas_df = atlas_df

    def get_names(self):
        ID_to_name = defaultdict(str)

        Nx, Ny = self.atlas_df.shape

        for i in range(Nx):
            ID_to_name[self.atlas_df.iloc[i, 0]] = self.atlas_df.iloc[i, 1]

        return ID_to_name

    def get_level_lookup(self, level):
        Nx, Ny = self.atlas_df.shape

        if level == 1:
            level1 = defaultdict(int)
            level = 1
            level_col = level + 4
            for i in range(Nx):
                for j in range(level_col, Ny):
                    if pd.notna(self.atlas_df.iloc[i, j]):
                        level1[self.atlas_df.iloc[i, j]] = self.atlas_df.iloc[i, level_col]
                for j in range(5, level_col):
                    if pd.notna(self.atlas_df.iloc[i, j]):
                        level1[self.atlas_df.iloc[i, j]] = self.atlas_df.iloc[i, j]
            return level1
            
        if level == 2:
            level2 = defaultdict(int)
            level_col = level + 4
            for i in range(Nx):
                for j in range(level_col, Ny):
                    if pd.notna(self.atlas_df.iloc[i, j]):
                        level2[self.atlas_df.iloc[i, j]] = self.atlas_df.iloc[i, level_col]
                for j in range(5, level_col):
                    if pd.notna(self.atlas_df.iloc[i, j]):
                        level2[self.atlas_df.iloc[i, j]] = self.atlas_df.iloc[i, j]
            return level2

        if level == 3:
            level3 = defaultdict(int)
            level_col = level + 4
            for i in range(Nx):
                for j in range(level_col, Ny):
                    if pd.notna(self.atlas_df.iloc[i, j]):
                        level3[self.atlas_df.iloc[i, j]] = self.atlas_df.iloc[i, level_col]
                for j in range(5, level_col):
                    if pd.notna(self.atlas_df.iloc[i, j]):
                        level3[self.atlas_df.iloc[i, j]] = self.atlas_df.iloc[i, j]
            return level3

        if level == 4:
            level4 = defaultdict(int)
            level_col = level + 4
            for i in range(Nx):
                for j in range(level_col, Ny):
                    if pd.notna(self.atlas_df.iloc[i, j]):
                        level4[self.atlas_df.iloc[i, j]] = self.atlas_df.iloc[i, level_col]
                for j in range(5, level_col):
                    if pd.notna(self.atlas_df.iloc[i, j]):
                        level4[self.atlas_df.iloc[i, j]] = self.atlas_df.iloc[i, j]
            return level4

        if level == 5:
            level5 = defaultdict(int)
            level_col = level + 4
            for i in range(Nx):
                for j in range(level_col, Ny):
                    if pd.notna(self.atlas_df.iloc[i, j]):
                        level5[self.atlas_df.iloc[i, j]] = self.atlas_df.iloc[i, level_col]
                for j in range(5, level_col):
                    if pd.notna(self.atlas_df.iloc[i, j]):
                        level5[self.atlas_df.iloc[i, j]] = self.atlas_df.iloc[i, j]
            return level5

        if level == 6:
            level6 = defaultdict(int)
            level_col = level + 4
            for i in range(Nx):
                for j in range(level_col, Ny):
                    if pd.notna(self.atlas_df.iloc[i, j]):
                        level6[self.atlas_df.iloc[i, j]] = self.atlas_df.iloc[i, level_col]
                for j in range(5, level_col):
                    if pd.notna(self.atlas_df.iloc[i, j]):
                        level6[self.atlas_df.iloc[i, j]] = self.atlas_df.iloc[i, j]
            return level6

        if level == 7:
            level7 = defaultdict(int)
            level_col = level + 4
            for i in range(Nx):
                for j in range(level_col, Ny):
                    if pd.notna(self.atlas_df.iloc[i, j]):
                        level7[self.atlas_df.iloc[i, j]] = self.atlas_df.iloc[i, level_col]
                for j in range(5, level_col):
                    if pd.notna(self.atlas_df.iloc[i, j]):
                        level7[self.atlas_df.iloc[i, j]] = self.atlas_df.iloc[i, j]
            return level7

        if level == 8:
            level8 = defaultdict(int)
            level_col = level + 4
            for i in range(Nx):
                for j in range(level_col, Ny):
                    if pd.notna(self.atlas_df.iloc[i, j]):
                        level8[self.atlas_df.iloc[i, j]] = self.atlas_df.iloc[i, level_col]
                for j in range(5, level_col):
                    if pd.notna(self.atlas_df.iloc[i, j]):
                        level8[self.atlas_df.iloc[i, j]] = self.atlas_df.iloc[i, j]
            return level8

        if level == 9:
            level9 = defaultdict(int)
            level_col = level + 4
            for i in range(Nx):
                for j in range(level_col, Ny):
                    if pd.notna(self.atlas_df.iloc[i, j]):
                        level9[self.atlas_df.iloc[i, j]] = self.atlas_df.iloc[i, level_col]
                for j in range(5, level_col):
                    if pd.notna(self.atlas_df.iloc[i, j]):
                        level9[self.atlas_df.iloc[i, j]] = self.atlas_df.iloc[i, j]
            return level9

        if level == 10:
            level10 = defaultdict(int)
            level_col = level + 4
            for i in range(Nx):
                for j in range(level_col, Ny):
                    if pd.notna(self.atlas_df.iloc[i, j]):
                        level10[self.atlas_df.iloc[i, j]] = self.atlas_df.iloc[i, level_col]
                for j in range(5, level_col):
                    if pd.notna(self.atlas_df.iloc[i, j]):
                        level10[self.atlas_df.iloc[i, j]] = self.atlas_df.iloc[i, j]
            return level10

        if level == 11:
            level11 = defaultdict(int)
            level_col = level + 4
            for i in range(Nx):
                for j in range(level_col, Ny):
                    if pd.notna(self.atlas_df.iloc[i, j]):
                        level11[self.atlas_df.iloc[i, j]] = self.atlas_df.iloc[i, level_col]
                for j in range(5, level_col):
                    if pd.notna(self.atlas_df.iloc[i, j]):
                        level11[self.atlas_df.iloc[i, j]] = self.atlas_df.iloc[i, j]

            return level11

 
# this class builds our pandas dfs (one for each level)
class buildDFs:
    def __init__(self, atlas_df):
        self.atlas_df = atlas_df
        self.level1, self.level2, self.level3, self.level4, self.level5, self.level6, self.level7, self.level8, self.level9, self.level10, self.level11 = self.get_lookups(self.atlas_df)
        ut = utils(atlas_df)
        self.ID_to_name = ut.get_names()

    def get_lookups(self, atlas_df):
        level1 = defaultdict(int)
        level2 = defaultdict(int)
        level3 = defaultdict(int)
        level4 = defaultdict(int)
        level5 = defaultdict(int)
        level6 = defaultdict(int)
        level7 = defaultdict(int)
        level8 = defaultdict(int)
        level9 = defaultdict(int)
        level10 = defaultdict(int)
        level11 = defaultdict(int)

        Nx, Ny = atlas_df.shape

        level = 1
        level_col = level + 4
        for i in range(Nx):
            for j in range(level_col, Ny):
                if pd.notna(atlas_df.iloc[i, j]):
                    level1[atlas_df.iloc[i, j]] = atlas_df.iloc[i, level_col]
            for j in range(5, level_col):
                if pd.notna(self.atlas_df.iloc[i, j]):
                    level1[self.atlas_df.iloc[i, j]] = self.atlas_df.iloc[i, j]
        level += 1
        level_col = level + 4
        for i in range(Nx):
            for j in range(level_col, Ny):
                if pd.notna(atlas_df.iloc[i, j]):
                    level2[atlas_df.iloc[i, j]] = atlas_df.iloc[i, level_col]
            for j in range(5, level_col):
                if pd.notna(self.atlas_df.iloc[i, j]):
                    level2[self.atlas_df.iloc[i, j]] = self.atlas_df.iloc[i, j]
        level += 1
        level_col = level + 4
        for i in range(Nx):
            for j in range(level_col, Ny):
                if pd.notna(atlas_df.iloc[i, j]):
                    level3[atlas_df.iloc[i, j]] = atlas_df.iloc[i, level_col]
            for j in range(5, level_col):
                if pd.notna(self.atlas_df.iloc[i, j]):
                    level3[self.atlas_df.iloc[i, j]] = self.atlas_df.iloc[i, j]
        level += 1
        level_col = level + 4
        for i in range(Nx):
            for j in range(level_col, Ny):
                if pd.notna(atlas_df.iloc[i, j]):
                    level4[atlas_df.iloc[i, j]] = atlas_df.iloc[i, level_col]
            for j in range(5, level_col):
                if pd.notna(self.atlas_df.iloc[i, j]):
                    level4[self.atlas_df.iloc[i, j]] = self.atlas_df.iloc[i, j]
        level += 1
        level_col = level + 4
        for i in range(Nx):
            for j in range(level_col, Ny):
                if pd.notna(atlas_df.iloc[i, j]):
                    level5[atlas_df.iloc[i, j]] = atlas_df.iloc[i, level_col]
            for j in range(5, level_col):
                if pd.notna(self.atlas_df.iloc[i, j]):
                    level5[self.atlas_df.iloc[i, j]] = self.atlas_df.iloc[i, j]
        level += 1
        level_col = level + 4
        for i in range(Nx):
            for j in range(level_col, Ny):
                if pd.notna(atlas_df.iloc[i, j]):
                    level6[atlas_df.iloc[i, j]] = atlas_df.iloc[i, level_col]
            for j in range(5, level_col):
                if pd.notna(self.atlas_df.iloc[i, j]):
                    level6[self.atlas_df.iloc[i, j]] = self.atlas_df.iloc[i, j]
        level += 1
        level_col = level + 4
        for i in range(Nx):
            for j in range(level_col, Ny):
                if pd.notna(atlas_df.iloc[i, j]):
                    level7[atlas_df.iloc[i, j]] = atlas_df.iloc[i, level_col]
            for j in range(5, level_col):
                if pd.notna(self.atlas_df.iloc[i, j]):
                    level7[self.atlas_df.iloc[i, j]] = self.atlas_df.iloc[i, j]
        level += 1
        level_col = level + 4
        for i in range(Nx):
            for j in range(level_col, Ny):
                if pd.notna(atlas_df.iloc[i, j]):
                    level8[atlas_df.iloc[i, j]] = atlas_df.iloc[i, level_col]
            for j in range(5, level_col):
                if pd.notna(self.atlas_df.iloc[i, j]):
                    level8[self.atlas_df.iloc[i, j]] = self.atlas_df.iloc[i, j]
        level += 1
        level_col = level + 4
        for i in range(Nx):
            for j in range(level_col, Ny):
                if pd.notna(atlas_df.iloc[i, j]):
                    level9[atlas_df.iloc[i, j]] = atlas_df.iloc[i, level_col]
            for j in range(5, level_col):
                if pd.notna(self.atlas_df.iloc[i, j]):
                    level9[self.atlas_df.iloc[i, j]] = self.atlas_df.iloc[i, j]
        level += 1
        level_col = level + 4
        for i in range(Nx):
            for j in range(level_col, Ny):
                if pd.notna(atlas_df.iloc[i, j]):
                    level10[atlas_df.iloc[i, j]] = atlas_df.iloc[i, level_col]
            for j in range(5, level_col):
                if pd.notna(self.atlas_df.iloc[i, j]):
                    level10[self.atlas_df.iloc[i, j]] = self.atlas_df.iloc[i, j]
        level += 1
        level_col = level + 4
        for i in range(Nx):
            for j in range(level_col, Ny):
                if pd.notna(atlas_df.iloc[i, j]):
                    level11[atlas_df.iloc[i, j]] = atlas_df.iloc[i, level_col]
            for j in range(5, level_col):
                if pd.notna(self.atlas_df.iloc[i, j]):
                    level11[self.atlas_df.iloc[i, j]] = self.atlas_df.iloc[i, j]

        return level1, level2, level3, level4, level5, level6, level7, level8, level9, level10, level11

    def make_output_df(self, level):
        if level == 1:
            unique_regions_L = [self.ID_to_name[x] + '_L' +  '_' + str(int(x)) for x in self.atlas_df['Level 1'].dropna().unique()]
            unique_regions_R = [self.ID_to_name[x] + '_R' + '_' + str(int(x)) for x in self.atlas_df['Level 1'].dropna().unique()]
            unique_regions_1 = unique_regions_L + unique_regions_R
            unique_regions_1.sort(key=lambda x: (x.split('_')[-2], x.split('_')[0]))
            unique_regions_1 = ['Animal ID'] + unique_regions_1
            output_df_1 = pd.DataFrame()
            for i in range(len(unique_regions_1)):
                output_df_1[unique_regions_1[i]] = ''

            return output_df_1
        if level == 2:
            unique_regions_L = [self.ID_to_name[x] + '_L' + '_' + str(int(x)) for x in self.atlas_df['Level 2'].dropna().unique()]
            unique_regions_R = [self.ID_to_name[x] + '_R' + '_' + str(int(x)) for x in self.atlas_df['Level 2'].dropna().unique()]
            unique_regions_2 = unique_regions_L + unique_regions_R
            unique_regions_2.sort(key=lambda x: (x.split('_')[-2], x.split('_')[0]))
            unique_regions_2 = ['Animal ID'] + unique_regions_2
            output_df_2 = pd.DataFrame()
            for i in range(len(unique_regions_2)):
                output_df_2[unique_regions_2[i]] = ''
        
            return output_df_2
        if level == 3:
            unique_regions_L = [self.ID_to_name[x] + '_L' + '_' + str(int(x)) for x in self.atlas_df['Level 3'].dropna().unique()]
            unique_regions_R = [self.ID_to_name[x] + '_R' + '_' + str(int(x)) for x in self.atlas_df['Level 3'].dropna().unique()]
            unique_regions_3 = unique_regions_L + unique_regions_R
            unique_regions_3.sort(key=lambda x: (x.split('_')[-2], x.split('_')[0]))
            unique_regions_3 = ['Animal ID'] + unique_regions_3
            output_df_3 = pd.DataFrame()
            for i in range(len(unique_regions_3)):
                output_df_3[unique_regions_3[i]] = ''
        
            return output_df_3
        if level == 4:
            unique_regions_L = [self.ID_to_name[x] + '_L' + '_' + str(int(x)) for x in self.atlas_df['Level 4'].dropna().unique()]
            unique_regions_R = [self.ID_to_name[x] + '_R' + '_' + str(int(x)) for x in self.atlas_df['Level 4'].dropna().unique()]
            unique_regions_4 = unique_regions_L + unique_regions_R
            unique_regions_4.sort(key=lambda x: (x.split('_')[-2], x.split('_')[0]))
            unique_regions_4 = ['Animal ID'] + unique_regions_4
            output_df_4 = pd.DataFrame()
            for i in range(len(unique_regions_4)):
                output_df_4[unique_regions_4[i]] = ''
        
            return output_df_4
        if level == 5:
            unique_regions_L = [self.ID_to_name[x] + '_L' + '_' + str(int(x)) for x in self.atlas_df['Level 5'].dropna().unique()]
            unique_regions_R = [self.ID_to_name[x] + '_R' + '_' + str(int(x)) for x in self.atlas_df['Level 5'].dropna().unique()]
            unique_regions_5 = unique_regions_L + unique_regions_R
            unique_regions_5.sort(key=lambda x: (x.split('_')[-2], x.split('_')[0]))
            unique_regions_5 = ['Animal ID'] + unique_regions_5
            output_df_5 = pd.DataFrame()
            for i in range(len(unique_regions_5)):
                output_df_5[unique_regions_5[i]] = ''
        
            return output_df_5
        if level == 6:
            unique_regions_L = [self.ID_to_name[x] + '_L' + '_' + str(int(x)) for x in self.atlas_df['Level 6'].dropna().unique()]
            unique_regions_R = [self.ID_to_name[x] + '_R' + '_' + str(int(x)) for x in self.atlas_df['Level 6'].dropna().unique()]
            unique_regions_6 = unique_regions_L + unique_regions_R
            unique_regions_6.sort(key=lambda x: (x.split('_')[-2], x.split('_')[0]))
            unique_regions_6 = ['Animal ID'] + unique_regions_6
            output_df_6 = pd.DataFrame()
            for i in range(len(unique_regions_6)):
                output_df_6[unique_regions_6[i]] = ''
        
            return output_df_6
        if level == 7:
            unique_regions_L = [self.ID_to_name[x] + '_L' + '_' + str(int(x)) for x in self.atlas_df['Level 7'].dropna().unique()]
            unique_regions_R = [self.ID_to_name[x] + '_R' + '_' + str(int(x)) for x in self.atlas_df['Level 7'].dropna().unique()]
            unique_regions_7 = unique_regions_L + unique_regions_R
            unique_regions_7.sort(key=lambda x: (x.split('_')[-2], x.split('_')[0]))
            unique_regions_7 = ['Animal ID'] + unique_regions_7
            output_df_7 = pd.DataFrame()
            for i in range(len(unique_regions_7)):
                output_df_7[unique_regions_7[i]] = ''
        
            return output_df_7
        if level == 8:
            unique_regions_L = [self.ID_to_name[x] + '_L' + '_' + str(int(x)) for x in self.atlas_df['Level 8'].dropna().unique()]
            unique_regions_R = [self.ID_to_name[x] + '_R' + '_' + str(int(x)) for x in self.atlas_df['Level 8'].dropna().unique()]
            unique_regions_8 = unique_regions_L + unique_regions_R
            unique_regions_8.sort(key=lambda x: (x.split('_')[-2], x.split('_')[0]))
            unique_regions_8 = ['Animal ID'] + unique_regions_8
            output_df_8 = pd.DataFrame()
            for i in range(len(unique_regions_8)):
                output_df_8[unique_regions_8[i]] = ''
        
            return output_df_8
        if level == 9:
            unique_regions_L = [self.ID_to_name[x] + '_L' + '_' + str(int(x)) for x in self.atlas_df['Level 9'].dropna().unique()]
            unique_regions_R = [self.ID_to_name[x] + '_R' + '_' + str(int(x)) for x in self.atlas_df['Level 9'].dropna().unique()]
            unique_regions_9 = unique_regions_L + unique_regions_R
            unique_regions_9.sort(key=lambda x: (x.split('_')[-2], x.split('_')[0]))
            unique_regions_9 = ['Animal ID'] + unique_regions_9
            output_df_9 = pd.DataFrame()
            for i in range(len(unique_regions_9)):
                output_df_9[unique_regions_9[i]] = ''
        
            return output_df_9
        if level == 10:
            unique_regions_L = [self.ID_to_name[x] + '_L' + '_' + str(int(x)) for x in self.atlas_df['Level 10'].dropna().unique()]
            unique_regions_R = [self.ID_to_name[x] + '_R' + '_' + str(int(x)) for x in self.atlas_df['Level 10'].dropna().unique()]
            unique_regions_10 = unique_regions_L + unique_regions_R
            unique_regions_10.sort(key=lambda x: (x.split('_')[-2], x.split('_')[0]))
            unique_regions_10 = ['Animal ID'] + unique_regions_10
            output_df_10 = pd.DataFrame()
            for i in range(len(unique_regions_10)):
                output_df_10[unique_regions_10[i]] = ''
        
            return output_df_10
        if level == 11:
            unique_regions_L = [self.ID_to_name[x] + '_L' + '_' + str(int(x)) for x in self.atlas_df['Level 11'].dropna().unique()]
            unique_regions_R = [self.ID_to_name[x] + '_R' + '_' + str(int(x)) for x in self.atlas_df['Level 11'].dropna().unique()]
            unique_regions_11 = unique_regions_L + unique_regions_R
            unique_regions_11.sort(key=lambda x: (x.split('_')[-2], x.split('_')[0]))
            unique_regions_11 = ['Animal ID'] + unique_regions_11
            output_df_11 = pd.DataFrame()
            for i in range(len(unique_regions_11)):
                output_df_11[unique_regions_11[i]] = ''
            return output_df_11

# this class iterates over the rows of our input data and concats the rows to our output dfs
class fillDFS:
    def __init__(self, base_dir, atlas_df):
        self.atlas_df = atlas_df
        self.base_dir = base_dir
        self.mice = self.get_mice(self.base_dir)
        ut = utils(atlas_df)
        self.ID_to_name = ut.get_names()

    def get_mice(self, base_dir):        
        mice = []
        for mouse in os.listdir(base_dir):
            if os.path.isdir(base_dir + os.sep + mouse):
                mice.append(mouse)
        return mice

    def fill_df(self, mouse, hemi, level):      
        LEFT, RIGHT = False, False
        
        if hemi == 'left' or hemi == 'L' or hemi == 'l' or hemi == 'Left':
            LEFT = True
        else:
            RIGHT = True

        if LEFT:
            df_path = base_dir + os.sep + mouse + os.sep + '~Nutil OUTPUT' + os.sep + 'Left' + os.sep + 'Reports' + os.sep + mouse + '_Objects' + os.sep + mouse + '_Objects_All.csv' 
            mouse_df = pd.read_csv(df_path, delimiter=';')
        else:
            df_path = base_dir + os.sep + mouse + os.sep + '~Nutil OUTPUT' + os.sep + 'Right' + os.sep + 'Reports' + os.sep + mouse + '_Objects' + os.sep + mouse + '_Objects_All.csv' 
            mouse_df = pd.read_csv(df_path, delimiter=';')
        
        counts = mouse_df['Region ID'].value_counts().to_dict()

        leveled_counts = self.get_leveled_counts(counts, level)

        named_counts = defaultdict(int)
        for k, v in leveled_counts.items():
            if LEFT:
                named_counts[self.ID_to_name[k] + '_L' + '_' + str(int(k))] = [v]
            else:
                named_counts[self.ID_to_name[k] + '_R' + '_' + str(int(k))] = [v]

        named_counts['Animal ID'] = [mouse]
        
        return named_counts

    def combine_data(self):
        bdf = buildDFs(self.atlas_df)
        fdf = fillDFS(self.base_dir, self.atlas_df)
        level1_df = bdf.make_output_df(1)
        for mouse in self.mice:
            data = fdf.fill_df(mouse, 'L', 1)
            data.update(fdf.fill_df(mouse, 'R', 1))
            tmp_df = pd.DataFrame.from_dict(data).set_index('Animal ID')
            level1_df = pd.concat([level1_df, tmp_df], axis=0)

        level2_df = bdf.make_output_df(2)
        for mouse in self.mice:
            data = fdf.fill_df(mouse, 'L', 2)
            data.update(fdf.fill_df(mouse, 'R', 2))
            tmp_df = pd.DataFrame.from_dict(data).set_index('Animal ID')
            level2_df = pd.concat([level2_df, tmp_df], axis=0)

        level3_df = bdf.make_output_df(3)
        for mouse in self.mice:
            data = fdf.fill_df(mouse, 'L', 3)
            data.update(fdf.fill_df(mouse, 'R', 3))
            tmp_df = pd.DataFrame.from_dict(data).set_index('Animal ID')
            level3_df = pd.concat([level3_df, tmp_df], axis=0)

        level3_df = bdf.make_output_df(3)
        for mouse in self.mice:
            data = fdf.fill_df(mouse, 'L', 3)
            data.update(fdf.fill_df(mouse, 'R', 3))
            tmp_df = pd.DataFrame.from_dict(data).set_index('Animal ID')
            level3_df = pd.concat([level3_df, tmp_df], axis=0)

        level4_df = bdf.make_output_df(4)
        for mouse in self.mice:
            data = fdf.fill_df(mouse, 'L', 4)
            data.update(fdf.fill_df(mouse, 'R', 4))
            tmp_df = pd.DataFrame.from_dict(data).set_index('Animal ID')
            level4_df = pd.concat([level4_df, tmp_df], axis=0)

        level5_df = bdf.make_output_df(5)
        for mouse in self.mice:
            data = fdf.fill_df(mouse, 'L', 5)
            data.update(fdf.fill_df(mouse, 'R', 5))
            tmp_df = pd.DataFrame.from_dict(data).set_index('Animal ID')
            level5_df = pd.concat([level5_df, tmp_df], axis=0)

        level6_df = bdf.make_output_df(6)
        for mouse in self.mice:
            data = fdf.fill_df(mouse, 'L', 6)
            data.update(fdf.fill_df(mouse, 'R', 6))
            tmp_df = pd.DataFrame.from_dict(data).set_index('Animal ID')
            level6_df = pd.concat([level6_df, tmp_df], axis=0)

        level7_df = bdf.make_output_df(7)
        for mouse in self.mice:
            data = fdf.fill_df(mouse, 'L', 7)
            data.update(fdf.fill_df(mouse, 'R', 7))
            tmp_df = pd.DataFrame.from_dict(data).set_index('Animal ID')
            level7_df = pd.concat([level7_df, tmp_df], axis=0)

        level8_df = bdf.make_output_df(8)
        for mouse in self.mice:
            data = fdf.fill_df(mouse, 'L', 8)
            data.update(fdf.fill_df(mouse, 'R', 8))
            tmp_df = pd.DataFrame.from_dict(data).set_index('Animal ID')
            level8_df = pd.concat([level8_df, tmp_df], axis=0)

        level9_df = bdf.make_output_df(9)
        for mouse in self.mice:
            data = fdf.fill_df(mouse, 'L', 9)
            data.update(fdf.fill_df(mouse, 'R', 9))
            tmp_df = pd.DataFrame.from_dict(data).set_index('Animal ID')
            level9_df = pd.concat([level9_df, tmp_df], axis=0)

        level10_df = bdf.make_output_df(10)
        for mouse in self.mice:
            data = fdf.fill_df(mouse, 'L', 10)
            data.update(fdf.fill_df(mouse, 'R', 10))
            tmp_df = pd.DataFrame.from_dict(data).set_index('Animal ID')
            level10_df = pd.concat([level10_df, tmp_df], axis=0)

        level11_df = bdf.make_output_df(11)
        for mouse in self.mice:
            data = fdf.fill_df(mouse, 'L', 11)
            data.update(fdf.fill_df(mouse, 'R', 11))
            tmp_df = pd.DataFrame.from_dict(data).set_index('Animal ID')
            level11_df = pd.concat([level11_df, tmp_df], axis=0)
        
        level1_df = level1_df.drop('Animal ID', axis=1)                
        level2_df = level2_df.drop('Animal ID', axis=1)
        level3_df = level3_df.drop('Animal ID', axis=1)
        level4_df = level4_df.drop('Animal ID', axis=1)
        level5_df = level5_df.drop('Animal ID', axis=1)
        level6_df = level6_df.drop('Animal ID', axis=1)
        level7_df = level7_df.drop('Animal ID', axis=1)
        level8_df = level8_df.drop('Animal ID', axis=1)
        level9_df = level9_df.drop('Animal ID', axis=1)
        level10_df = level10_df.drop('Animal ID', axis=1)
        level11_df = level11_df.drop('Animal ID', axis=1)

        df_list = [level1_df, level2_df, level3_df, level4_df, level5_df, level6_df, level7_df, level8_df, level9_df,
                   level10_df, level11_df]

        for i in range(11):
            seen = set()
            df_cols = set(df_list[i].columns.values.tolist())
            for col_name in df_cols:
                if col_name not in seen:
                    if len(col_name.split('_')) > 2:
                        if '_R_' in col_name:
                            opposite = col_name.split('_')[0] + '_L_' + col_name.split('_')[2]
                        else:
                            opposite = col_name.split('_')[0] + '_R_' + col_name.split('_')[2]
                        seen.add(col_name)
                        seen.add(opposite)
                        if opposite not in df_list[i]:
                            df_list[i][opposite] = 0

        level1_df.columns = level1_df.columns.str.replace(' ', '_')
        level2_df.columns = level2_df.columns.str.replace(' ', '_')
        level3_df.columns = level3_df.columns.str.replace(' ', '_')
        level4_df.columns = level4_df.columns.str.replace(' ', '_')
        level5_df.columns = level5_df.columns.str.replace(' ', '_')
        level6_df.columns = level6_df.columns.str.replace(' ', '_')
        level7_df.columns = level7_df.columns.str.replace(' ', '_')
        level8_df.columns = level8_df.columns.str.replace(' ', '_')
        level9_df.columns = level9_df.columns.str.replace(' ', '_')
        level10_df.columns = level10_df.columns.str.replace(' ', '_')
        level11_df.columns = level11_df.columns.str.replace(' ', '_')

        level1_df = level1_df.fillna(0)
        level2_df = level2_df.fillna(0)
        level3_df = level3_df.fillna(0)
        level4_df = level4_df.fillna(0)
        level5_df = level5_df.fillna(0)
        level6_df = level6_df.fillna(0)
        level7_df = level7_df.fillna(0)
        level8_df = level8_df.fillna(0)
        level9_df = level9_df.fillna(0)
        level10_df = level10_df.fillna(0)
        level11_df = level11_df.fillna(0)




        level1_df.sort_index(inplace=True, axis=1, key=lambda x: x.str.lower())
        level2_df.sort_index(inplace=True, axis=1, key=lambda x: x.str.lower())
        level3_df.sort_index(inplace=True, axis=1, key=lambda x: x.str.lower())
        level4_df.sort_index(inplace=True, axis=1, key=lambda x: x.str.lower())
        level5_df.sort_index(inplace=True, axis=1, key=lambda x: x.str.lower())
        level6_df.sort_index(inplace=True, axis=1, key=lambda x: x.str.lower())
        level7_df.sort_index(inplace=True, axis=1, key=lambda x: x.str.lower())
        level8_df.sort_index(inplace=True, axis=1, key=lambda x: x.str.lower())
        level9_df.sort_index(inplace=True, axis=1, key=lambda x: x.str.lower())
        level10_df.sort_index(inplace=True, axis=1, key=lambda x: x.str.lower())
        level11_df.sort_index(inplace=True, axis=1, key=lambda x: x.str.lower())

        writer = pd.ExcelWriter('output_test_2.xlsx')
        level1_df.to_excel(writer, 'level1')
        level2_df.to_excel(writer, 'level2')
        level3_df.to_excel(writer, 'level3')
        level4_df.to_excel(writer, 'level4')
        level5_df.to_excel(writer, 'level5')
        level6_df.to_excel(writer, 'level6')
        level7_df.to_excel(writer, 'level7')
        level8_df.to_excel(writer, 'level8')
        level9_df.to_excel(writer, 'level9')
        level10_df.to_excel(writer, 'level10')
        level11_df.to_excel(writer, 'level11')

        writer.save()

    def get_leveled_counts(self, counts, level):
        ut = utils(self.atlas_df)
        level_dict = ut.get_level_lookup(level)
        
        leveled_counts = defaultdict(int)
        if level == 1:
            for k, v in counts.items():
                leveled_counts[level_dict[k]] += v
        if level == 2:
            for k, v in counts.items():
                leveled_counts[level_dict[k]] += v
        if level == 3:
            for k, v in counts.items():
                leveled_counts[level_dict[k]] += v
        if level == 4:
            for k, v in counts.items():
                leveled_counts[level_dict[k]] += v
        if level == 5:
            for k, v in counts.items():
                leveled_counts[level_dict[k]] += v
        if level == 6:
            for k, v in counts.items():
                leveled_counts[level_dict[k]] += v
        if level == 7:
            for k, v in counts.items():
                leveled_counts[level_dict[k]] += v
        if level == 8:
            for k, v in counts.items():
                leveled_counts[level_dict[k]] += v
        if level == 9:
            for k, v in counts.items():
                leveled_counts[level_dict[k]] += v
        if level == 10:
            for k, v in counts.items():
                leveled_counts[level_dict[k]] += v
        if level == 11:
            for k, v in counts.items():
                leveled_counts[level_dict[k]] += v

        return leveled_counts


def main():
    TEST = True

    if not TEST:
        fdf = fillDFS(base_dir, atlas_df)
        fdf.combine_data()
    else:
        # bdf = buildDFs(atlas_df)
        # for i in range(1, 12):
        #     print(i)
        #     df = bdf.make_output_df(i)
        #     print(df.head())
        fdf = fillDFS(base_dir, atlas_df)
        # cnts = fdf.fill_df('103615-1', 'R', 11)
        # print(cnts)
        fdf.combine_data()

        print('data cleaning done... go check for the output file')



if __name__ == '__main__':
    main()
