import time

class my_bucket:
    def __init__(self, current_cap, drop_rate):
        self.cap = float(current_cap)        # maximum capacity
        self.current_cap = float(current_cap)  # current tokens
        self.drop_rate = float(drop_rate)    # tokens per second
        self.check_time = time.monotonic()   # monotonic is better for elapsed time

    def fill_bucket(self):
        now = time.monotonic()
        elapsed = now - self.check_time
        if elapsed > 0:
            self.current_cap = min(self.cap, self.current_cap + elapsed * self.drop_rate)
            self.check_time = now

    def allow_req(self, req_cap=1):
        self.fill_bucket()
        req_cap = float(req_cap)
        if self.current_cap >= req_cap:
            self.current_cap -= req_cap
            return True
        return False
