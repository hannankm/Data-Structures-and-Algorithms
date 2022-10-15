class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        position={c:i for i,c in enumerate(s)}
        
        result=[]
        index=-1
        size=1
        for i,c in enumerate(s):
            index= max(index, position[c])
            if i==index:
                result.append(size)
                size=1
            else:
                size+=1
        return result
