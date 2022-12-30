class MyCalendar:
    '''
    where n is the input
    time - O(n)
    space - O(n)
    '''
    def __init__(self):
        self.calendar = []

    def book(self, start: int, end: int) -> bool:
        l, r = 0, len(self.calendar)

        while l < r:
            mid = l + (r-l)//2
            if self.calendar[mid][0] <= start:
                l = mid + 1
            else:
                r = mid
            
        if self.intersect(l, start, end):
            return False
        else:
            self.calendar.insert(l, [start, end])
            return True
            
    def intersect(self, idx, start, end):
        return ((self.calendar[idx-1][1] > start if idx >= 1 else False) or 
                (self.calendar[idx][0] < end if idx < len(self.calendar) else False))


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)