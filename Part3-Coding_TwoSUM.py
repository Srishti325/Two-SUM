
# coding: utf-8

# In[4]:


class Solution:
    def twosum(self, lst, target):
        dict = {}
        for i in range(0, len(lst)):
            val = lst[i]
            if (target - val) in dict:
                return [dict[target - val], i]
            
            dict[val] = i + 1


lst = [2, 7, 11, 15]
target = 22
s = Solution()
print(s.twosum(lst, target))

