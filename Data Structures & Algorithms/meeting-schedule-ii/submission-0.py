import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        # Sort by start time
        intervals.sort(key=lambda x: x.start)

        heap = []  # stores end times
        max_rooms = 0

        for meeting in intervals:
            start = meeting.start
            end = meeting.end

            # Remove all meetings that have already ended
            while heap and heap[0] <= start:
                heapq.heappop(heap)

            # Allocate room for current meeting
            heapq.heappush(heap, end)

            # Current number of rooms being used
            max_rooms = max(max_rooms, len(heap))

        return max_rooms