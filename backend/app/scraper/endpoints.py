# app/scraper/endpoints.py

class XEndpoints:
    GUEST_TOKEN = "https://api.twitter.com/1.1/guest/activate.json"
    USER_TWEETS = "https://api.twitter.com/graphql/-VgD2gH5L1jZtLQQF1YhCg/UserTweets"
    USER_BY_SCREEN_NAME = "https://api.twitter.com/graphql/kS5xS3WtPpXKH5fDc8nA2A/UserByScreenName"
    FOLLOWERS = "https://api.twitter.com/graphql/fV9CTtiQ4CXBHIgG1vIJ7g/Followers"
    MENTIONS = "https://api.twitter.com/graphql/6d3FbLcFh5BKQaF8eC5kLQ/Mentions"
    TWEET_DETAIL = "https://api.twitter.com/graphql/tzDFDmFmZBGUsj0I8y9gDg/TweetDetail"