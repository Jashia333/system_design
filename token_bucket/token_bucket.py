class my_bucket:
    def __init__(self,capacity,drop_rate):
        self.capacity=capacity
        self.drop_rate=drop_rate
        

    def allow_req(self,req_cap):
        if self.capacity>=1:
            self.capacity-=req_cap
            return True
        return False
