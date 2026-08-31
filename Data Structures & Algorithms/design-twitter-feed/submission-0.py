from collections import defaultdict

class Twitter:

    def __init__(self):
        self.userTweets = defaultdict(list)
        self.followerMap = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.userTweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets = []
        
        tweets.extend(self.userTweets[userId])

        for followeeId in self.followerMap[userId]:
            if followeeId not in self.userTweets:
                continue
            else:
                tweets.extend(self.userTweets[followeeId])

        tweets.sort(key=lambda x: x[0], reverse=True)

        return [tweetId for _, tweetId in tweets[:10]]
        
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followerMap[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followerMap[followerId].discard(followeeId)
        
