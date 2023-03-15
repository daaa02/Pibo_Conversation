import os, subprocess
import random
import numpy as np
import pandas as pd


class Schedule():
    
    def __init__(self):
        self.sbj = ['의사소통', '사회성', '인지', '근육']
        self.init_development = [2.0, 2.0, 3.0, 2.0]
        self.init_preference = [1.0, 3.0, 2.0, 2.0] # 구글 시트에 고정해두기            


    def init_data(self):        
        
        # 기초 정보 수집
        self.init_development = np.asarray(self.init_development, dtype=float)
        self.init_preference = np.asarray(self.init_preference, dtype=float)
        
        print("init_data:", self.init_development, self.init_preference)        
        
        # 첫째날 스케줄 결정
        # 가중치 계산: 1/발달검사 + (선호도*0.5) 
        result = []
        for i in range(len(self.init_development)):
            cal = (np.reciprocal(self.init_development[i]) * 1.0) + (self.init_preference[i] * 0.5)
            result.append(cal)
            
        print("init_result", result)
        
        # 가중치 계산 결과
        act = {self.sbj[0] : result[0], self.sbj[1] : result[1], self.sbj[2] : result[2], self.sbj[3] : result[3]}
        
        # 내림차순으로 정렬
        init_activities = []
        act1 = sorted(act.items(), key=lambda x: x[1], reverse=True)
        for k in range(len(act1)):
            init_activities.append(act1[k][0])
        
        print("init:", init_activities, "\n")
        
        return init_activities        


    def update(self, new_preference):
        
        now_preference = [self.init_preference[i] + new_preference[i] for i in range(len(self.init_preference))]        
        # print('\nupdate_preference: ', now_preference)
        
        for i in range(len(self.init_preference)):
            if self.init_preference[i] - now_preference[i] >= 1:
                now_preference[i] = 0.9
                
        print('\ninit_preference:', self.init_preference)
        print('update_preference:', now_preference)
        
        result = []
        for i in range(len(self.init_preference)):
            cal = (np.reciprocal(self.init_development[i]) * 1.0) + (now_preference[i] * 1.5)
            result.append(cal)
            
        print("update_result:", result)
        
         # 가중치 계산 결과
        act = {self.sbj[0] : result[0], self.sbj[1] : result[1], self.sbj[2] : result[2], self.sbj[3] : result[3]}
        
        # 내림차순으로 정렬
        activities = []
        act1 = sorted(act.items(), key=lambda x: x[1], reverse=True)
        for k in range(len(act1)):
            activities.append(act1[k][0])
        
        print("update_activites:", activities, "\n")
        
        return activities