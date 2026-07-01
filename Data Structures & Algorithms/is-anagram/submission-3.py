class Solution:
    
    def isAnagram(self, s: str, t: str) -> bool:

        sorted_s=sorted(s)        
        sorted_t=sorted(t)

        s_hashmap={}
        t_hashmap={}

        for s in sorted_s:

            if s not in s_hashmap:
                s_hashmap[s]=1
            else:
                s_hashmap[s]=s_hashmap[s]+1

        for t in sorted_t:

            if t not in t_hashmap:
                t_hashmap[t]=1
            else:
                t_hashmap[t]=t_hashmap[t]+1

        

        for letter in s_hashmap.keys():

            if letter not in t_hashmap:
                return False
            
            if s_hashmap[letter] != t_hashmap[letter]:
                return False
        

        for letter in t_hashmap.keys():

            if letter not in s_hashmap:
                return False

        return True
        
