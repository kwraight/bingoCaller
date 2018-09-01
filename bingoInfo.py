import tweepy
import random
from datetime import datetime, date, timedelta
import argparse
import sys
sys.path.insert(0, '../configs/')
import configSettings_bc as configSettings

def BingoArgs():
    ### get arguments for setting parameters
    parser = argparse.ArgumentParser(description="Arguments bingo")
    #basics
    parser.add_argument('--slot', help='which game: morn/after/even')
    parser.add_argument('--go', help='compell the call!')
    args = parser.parse_args()
    return args

def postTweet(tweet):
    api=configSettings.get_api()
    status = api.update_status(status=tweet)

bingoCalls=[
            "Kelly's Eye", "One Little Duck", "Cup of Tea", "Knock at the Door", "Man Alive", "Tom Mix",
            "Lucky 7", "Garden Gate", "Doctors Orders", "Theresa's Den", "Legs Eleven", "One Dozen",
            "Unlucky for Some", "Valentine's Day", "Young and Keen", "Sweet Sixteen", "Dancing Queen",
            "Coming of Age", "Goodbye-Teens", "One Score", "Key of the Door", "Two Little Ducks",
            "Thee and Me", "Two Dozen", "Duck and Dive", "Pick and Mix", "Gateway to Heaven", "Over Weight",
            "Rise and Shine", "Dirty Gertie", "Get up and Run", "Buckle my Shoe", "Dirty Knee",
            "Ask for More", "Jump and Jive", "Three Dozen", "More than Eleven", "Christmas Cake", "Steps",
            "Naughty Forty", "Time for Fun", "Winnie the Pooh", "Down on your Knees", "Droopy Drawers",
            "Halfway There", "Up to Tricks", "Four and Seven", "Four Dozen", "PC", "Half a Century",
            "Tweak of the Thumb", "Danny La Rue", "Stuck in the Tree", "Clean the Floor", "Snakes Alive",
            "Was she worth it", "Heinz Varieties", "Make them Wait", "Brighton Line", "Five Dozen",
            "Bakers Bun", "Turn on the Screw", "Tickle Me 63", "Red Raw", "Old Age Pension", "Clickety Click",
            "Made in Heaven", "Saving Grace", "Either Way Up", "Three Score & Ten", "Bang on the Drum",
            "Six Dozen", "Queen B", "Candy Store", "Strive & Strive", "Trombones", "Sunset Strip",
            "Heaven's Gate", "One More Time", "Eight & Blank", "Stop & Run", "Straight On Through",
            "Time for Tea", "Seven Dozen", "Staying Alive", "Between the Sticks", "Torquay in Devon",
            "Two Fat Ladies", "Nearly There", "Top of the Shop"
            ]


def main():
    args = BingoArgs()
    if args.slot==None and args.go==None:
        print "No reason to do owt. Check the arguments. exiting."
        return
    
    index=int(random.uniform(0,len(bingoCalls)-1))
    tweet="NYS"
    if args.slot!=None and "morn" in args.slot:
        tweet="Morning session. "
    elif args.slot!=None and "noon" in args.slot:
        tweet="Afternoon session. "
    elif args.slot!=None and "even" in args.slot:
        tweet="Evening session. "
    elif args.go!=None or "go" in args.slot:
        tweet="Surprise call. "

    if tweet=="NYS":
        print "no call set. exiting"
        return

    today = datetime.today()
    tweet=tweet.replace("."," on "+today.strftime('%d, %b %Y')+".")

    tweet+="Eyes down...\n"+str(index+1)+". \t"+bingoCalls[index]+", "+str(index+1)+"."
    print tweet
    postTweet(tweet)


if __name__ == "__main__":
    print "### in bingoInfo"
    main()
    print "### out bingoInfo"

