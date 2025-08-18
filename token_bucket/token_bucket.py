class my_bucket:
    def __init__(self,capacity,drop_rate):
        self.capacity=capacity
        self.drop_rate=drop_rate

    def allow_req(self):
        if self.capacity>=1:
            self.capacity-=1
            return True
        return False
        
