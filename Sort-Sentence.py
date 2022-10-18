class Solution:
    def sortSentence(self, s: str) -> str:
        words= s.split(" ")
        sentence=""   
        for i in range(len(words)):
            min=i
            for j in range(i+1, len(words)):
                if words[min][-1]> words[j][-1]:
                    min=j
            if i!=min:
                words[min], words[i]=words[i],words[min]
            sentence+= words[i][:-1] + ' '
            
        return sentence[:-1]
