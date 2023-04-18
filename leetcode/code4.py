class Solution(object):
    def countDaysTogether(self, arriveAlice, leaveAlice, arriveBob, leaveBob):
        if arriveAlice > leaveBob or leaveAlice < arriveBob:
            return 0
        if arriveBob >= arriveAlice and leaveAlice >= leaveBob:
            return self.getDay(arriveBob, leaveBob)
        if arriveAlice > arriveBob and leaveBob > leaveAlice:
            return self.getDay(arriveAlice, leaveAlice)
        if arriveAlice > arriveBob and leaveAlice > leaveBob:
            return self.getDay(arriveAlice, leaveBob)
        if arriveBob > arriveAlice and leaveBob > leaveAlice:
            return self.getDay(arriveBob, leaveAlice)

    def getDay(self, startDay, stopDay):
        day = {}
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        for (idx, month) in enumerate(months):
            day[idx+1] = month
        start = startDay.split("-")
        stop = stopDay.split("-")
        startNum0, startNum1 = int(start[0]), int(start[1])
        stoptNum0, stopNum1 = int(stop[0]), int(stop[1])
        if startNum0 == stoptNum0:
            return stopNum1 - startNum1 + 1
        sum = day[startNum0] - startNum1 + 1 + stopNum1
        for idx in range(startNum0 + 1, stoptNum0):
            # print(startNum0, stoptNum0, idx, day[idx])
            sum += day[idx]
        return sum


su = Solution()
print(su.countDaysTogether("03-05", "07-14", "04-14", "09-21"))
print(su.countDaysTogether("03-05", "07-14", "07-14", "09-21"))
print(su.countDaysTogether("01-01", "12-31", "01-01", "12-31"))
