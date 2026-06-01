class Twitter:

    class User:
        def __init__(self, userId):
            self.userId = userId
            self.following = set()
            self.tweets = set()

    class Tweet:
        def __init__(self, userId, tweetId, time):
            self.userId = userId
            self.tweetId = tweetId
            self.time = time


    def __init__(self):
        self.users = {}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        user = self.users.get(userId, self.User(userId))
        self.users[userId] = user
        user.tweets.add(self.Tweet(userId, tweetId, self.time))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets = {}
        user = self.users[userId]
        following = user.following
        following.add(userId)

        for id in following:
            user = self.users[id]
            for tweet in user.tweets:
                tweets[tweet.time] = tweet.tweetId
        
        tweetTimes = list(tweets.keys())

        heapq.heapify_max(tweetTimes)

        retVal = []

        for i in range(10):
            if tweetTimes:
                t = heapq.heappop_max(tweetTimes)
                retVal.append(tweets[t])

        return retVal


    def follow(self, followerId: int, followeeId: int) -> None:
        user = self.users.get(followerId, self.User(followerId))
        self.users[followerId] = user
        user.following.add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        user = self.users[followerId]
        user.following.discard(followeeId)
        
