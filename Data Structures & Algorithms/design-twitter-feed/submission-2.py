class Twitter:

    def __init__(self):
        self._following = {}
        self._posts = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        print(f'userId {userId} posts tweetId {tweetId}')
        self._posts[userId] = self._posts.get(userId, [])+[tweetId]

    def getNewsFeed(self, userId: int) -> List[int]:
        self._posts[userId] = self._posts.get(userId, [])
        self._following[userId] = self._following.get(userId, set())

        feed = self._posts[userId].copy()
        for followee in self._following[userId]:
            if followee is userId: continue
            feed.extend(self._posts[followee])
        feed.sort(reverse=True)

        print(f'{userId} {self._following[userId]} {self._posts[userId]}')
        return feed[:10]

    def follow(self, followerId: int, followeeId: int) -> None:
        print(f'followerId {followerId} follows followeeId {followeeId}')
        if followerId not in self._following:
            self._following[followerId] = set()
        self._following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        print(f'followerId {followerId} unfollows followeeId {followeeId}')
        if followerId not in self._following: 
            return
        self._following[followerId].discard(followeeId)
