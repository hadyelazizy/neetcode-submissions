class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hash_={}

        

        for string in strs:

            pattern=str(sorted(string))
            if pattern not in hash_:

                hash_[pattern]=[string]
            
            else:

                hash_[pattern].append(string)
        
        return list(hash_.values())

