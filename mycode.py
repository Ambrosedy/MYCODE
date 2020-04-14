import numpy as np 
import pdb
import copy

class Solution:

    def __init__(self):
        self.data = self.loadfile("test_data.txt")
        self.dic = {}
        self.roads = []
        self.three = []
        self.four = []
        pass

    def loadfile(self,filename):
        return np.loadtxt(filename,dtype=np.uint32, delimiter=',')

    '''
        把只进行转账或收款的人剔除，剩余2603条数据
    '''
    def process_one(self):
        data0 = set([self.data[i][0] for i in range(self.data.shape[0])])
        data1 = set([self.data[i][1] for i in range(self.data.shape[0])])
        #求交集
        lis = data0&data1
        del_list = []
        for i in range(self.data.shape[0]):
            if (self.data[i][0] not in lis)or(self.data[i][1] not in lis):
                del_list.append(i)
        self.data = np.delete(self.data,del_list,axis=0)
        
        pass

    def createDic(self):
        self.process_one()
        #print(self.data.shape)
        for item in self.data:
            if self.dic.get(item[0])==None:
                self.dic[item[0]] = [item[1]]
            else:
                self.dic[item[0]].append(item[1])
        #sorted(self.dic.keys())
        #print("DIC:",self.dic)
    def findPath(self,v,path):

        lis = self.dic.get(v)
        if(lis==None):
            return
        for i in lis:
            temp = copy.copy(path)
            if i==path[0] and len(temp)<8:
                if len(temp)>2:
                    self.roads.append(temp)
                continue
            elif len(temp)>7:
                continue
            else:
                temp.append(i)
                self.findPath(i,temp)
    
        
    def allpaths(self):
        for i in self.dic.keys():
            path = [i]
            self.findPath(i,path)
        pass


    #列表数据归一化乘以权重，使用sorted(data,key=lambda item:func(item),reserve=true)排序

    def func(self,item):
        num=i=0
        Max = max(item)
        Min = min(item)
        l = Max - Min
        for j in item:
            v = (j-Min)/l
            num += v*np.power(10,i)
            i+=1
        return num
    
    def Sort(self):
        self.roads = sorted(self.roads,key=lambda item:self.func(item),reverse=False)


    def writeFile(self):
        self.Sort()
        num = len(self.roads)
        with open("output.txt",'w') as fw:
            fw.write("%s\n"%str(num))
            for item in self.roads:
                st = ""
                for j in item:
                    st+=str(j)+','
                fw.write('%s\n'%st[:-1])
        fw.close()

if __name__ == "__main__":
    s = Solution()
    s.createDic()
    
    #print(s.dic)
    #pdb.set_trace()
    #s.findPath(145,[145])
    s.allpaths()
    s.writeFile()


