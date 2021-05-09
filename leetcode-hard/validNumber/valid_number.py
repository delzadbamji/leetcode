class Solution:
    def checkE(self,lhs,rhs):
        
        try:
            
            if isinstance(int(lhs),int):
                try:
                    return isinstance(int(rhs),int)
#                 for float rhs
                except:
                    return False
            else:
                return False
            
#             float lhs
        except:
            try:
                
                if isinstance(float(lhs),float):
                    try:
                        return isinstance(int(rhs),int)
#                     for float rhs
                    except:
                        return False
                else:
                    return False
#                 for 99aE23 where 'a' is a random value
            except:
                False
    
    
    
    def isNumber(self, s: str) -> bool:
#         for --6 +-2
        if any(x in s for x in ["++","--","+-","-+"]):
            return False
        
        if s.isdigit() or s.lstrip("+-").isdigit():
            return True
        
        elif "e" in s or "E" in s:
            temp = s.split("e") if "e" in s else s.split("E")
#             for strings like e3 or 3e
            if temp[0] is '' or temp[1] is '' or len(temp)>2:
                return False
            else:
                return self.checkE(temp[0],temp[1])
            
        else:
            try:
#                 check inf,+inf,-inf,infinity
                if s.isalpha() or s.lstrip("+-").isalpha():
                    return False

                return isinstance(float(s),float)
#                 for 'abcd' '123a'
            except:
                return False
            
