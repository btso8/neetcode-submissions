from collections import defaultdict
from typing import List
import heapq

class Twitter:

    def __init__(self):
        self.count = 0
        self.tweet_map = defaultdict(list)
        self.follow_map = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_map[userId].append([self.count, tweetId])
        if len(self.tweet_map[userId]) > 10:
            self.tweet_map[userId].pop(0)
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        result = []
        min_heap = []
        self.follow_map[userId].add(userId)
        for followeeId in self.follow_map[userId]:
            if followeeId in self.tweet_map:
                index = len(self.tweet_map[followeeId]) - 1
                count, tweetId = self.tweet_map[followeeId][index]
                heapq.heappush(min_heap, [count, tweetId, followeeId, index - 1])
        while min_heap and len(result) < 10:
            count, tweetId, followeeId, index = heapq.heappop(min_heap)
            result.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweet_map[followeeId][index]
                heapq.heappush(min_heap, [count, tweetId, followeeId, index - 1])
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId != followerId:
            self.follow_map[followerId].discard(followeeId)