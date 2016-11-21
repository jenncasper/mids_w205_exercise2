import tweepy

consumer_key = "BwLb8YNyZeePZnRZ4Waf5APwN";
#eg: consumer_key = "YisfFjiodKtojtUvW4MSEcPm";


consumer_secret = "VevClvCc5psGUgUZXxdL56exWj6Kxo694mjEspF0tSjjnwpmFY";
#eg: consumer_secret = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";

access_token = "800393487753449473-JJThcBGCNQGi7AimrsRzhY9Nj7cw6YD";
#eg: access_token = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";

access_token_secret = "9qzIbKYj9INQClBqHuLXJOAa5KjOO8FOGia1piBj1CBRO";
#eg: access_token_secret = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)



