# https://leetcode.com/problems/logger-rate-limiter/

class Logger:

    def __init__(self):
        self.logs = {}
        self.gap = 10
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.logs.keys():
            self.logs[message] = timestamp + self.gap
            return True
        else:
            if timestamp < self.logs[message]:
                return False
            else:
                self.logs[message] = timestamp + self.gap
                return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)