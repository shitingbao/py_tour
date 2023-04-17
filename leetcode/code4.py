class Solution(object):
    def countDaysTogether(self, arriveAlice, leaveAlice, arriveBob, leaveBob):
        if arriveAlice < leaveBob and leaveAlice < arriveBob:
            return 0

        if arriveBob > arriveAlice and leaveAlice > leaveBob:
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
        if start[0] == stop[0]:
            return stop[1]-start[1]+1
        print(start, stop)
        return 0


su = Solution()
su.countDaysTogether("08-15", "08-18", "09-16", "09-19")
su.countDaysTogether("08-15", "09-18", "08-16", "08-19")
su.countDaysTogether("08-17", "08-18", "08-16", "09-19")
su.countDaysTogether("08-15", "09-18", "08-16", "09-19")
su.countDaysTogether("08-15", "09-18", "08-14", "09-16")
