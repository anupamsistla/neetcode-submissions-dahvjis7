class Twitter:

    def __init__(self):
        self.count = 0
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -=1

    def getNewsFeed(self, userId: int) -> List[int]:
        self.followMap[userId].add(userId)

        minHeap = []
        res = []

        for follower in self.followMap[userId]:
            if self.tweetMap[follower]:
                index = len(self.tweetMap[follower])-1
                count, tweetId = self.tweetMap[follower][index]
                minHeap.append([count, tweetId, follower, index-1])

        heapq.heapify(minHeap)

        while minHeap and len(res) < 10:
            count, tweetId, follower, index = heapq.heappop(minHeap)
            res.append(tweetId)

            if index >= 0:
                count, tweetId = self.tweetMap[follower][index]
                heapq.heappush(minHeap, [count, tweetId, follower, index-1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
            # O(1) operation