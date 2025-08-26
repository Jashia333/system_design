from tabulate import tabulate
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
        before_fill = self.current_cap
        self.fill_bucket()
        after_fill = self.current_cap
        allowed = after_fill >= req_cap
        if allowed:
            self.current_cap -= req_cap

        # Build a small table of values
        table = [
            ["Before Fill", round(before_fill, 2)],
            ["After Fill", round(after_fill, 2)],
            ["Req Cap", req_cap],
            ["Decision", "✅ Allowed" if allowed else "❌ Denied"],
            ["Remaining Cap", round(self.current_cap, 2)]
        ]
        print(tabulate(table, headers=["Metric", "Value"], tablefmt="fancy_grid"))

        return allowed
