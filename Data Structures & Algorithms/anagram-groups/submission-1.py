class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #logic 
        #make a another list where each word is sorted 
        #then make a dictionary with key being each element of strs and 
        #value as sorted key = whatever in the sorted list we created 

        result=[]
        sorted_words_list=[]

        dict1={}
        for word in strs:
            sort_word="".join(sorted(word))
            if sort_word in dict1:
                dict1[sort_word].append(word)
            else:
                dict1[sort_word]=[word]
                   
        for i in dict1.values():
            result.append(i)
        
        return result 


        