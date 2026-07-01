class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        hasht={}



        for n in nums:

            if n not in hasht:

                hasht[n]=1
            else:
                hasht[n]=hasht[n]+1
        
        arr=[]

        for number,count in hasht.items():
            arr.append([count, number])
        
        arr.sort()


        result=[]
        
        while(len(result)<k):
            result.append(arr.pop()[1])



        return result




