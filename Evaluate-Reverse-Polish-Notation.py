class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operand=[]
        for token in tokens:
            if token!="+" and token!="-" and token!="*" and token!="/":
                operand.append(token)
            else:
                second=int(operand.pop())
                first=int(operand.pop())
                if token=="+":
                    result=first+second
                elif token=="-":
                    result=first-second
                elif token=="*":
                    result=first*second
                else:
                    result=int(first/second)
                operand.append(result)
        return operand[-1]
