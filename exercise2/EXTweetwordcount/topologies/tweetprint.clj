(ns tweetprint
  (:use     [streamparse.specs])
  (:gen-class))

(defn tweetprint [options]
   [
    ;; spout configuration
    {"tweet-spout" (python-spout-spec
          options
          "spouts.tweets.Tweets"
          ["tweet"]
          :p 1
          )
    }
    ;; bolt configuration
    {"print-tweet-bolt" (python-bolt-spec
          options
          {"tweet-spout" :shuffle}
          "bolts.tweetprint.TweetPrint"
          ["word"]
          :p 2
          )
    }
  ]
)
