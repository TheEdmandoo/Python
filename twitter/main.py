   # Import required modules
import twitter, datetime 

file = open("/Users/EdwardHart/Library/Application Support/Google/Chrome/Default/Current Session")
history = file.read()

startindex = history.rfind("http")
endindex = history.find(chr(0), startindex)

website = history[startindex:endindex]

print(history[startindex:endindex])

   # Load in my keys and secrets from the credentials file into a list (array)
file = open("TwitterCredentials.txt")
cred = file.readline().strip().split(',')

   # Create a new API wrapper, passing in my credentials one at a time
api = twitter.Api(consumer_key=cred[0],consumer_secret=cred[1],
                  access_token_key=cred[2],access_token_secret=cred[3])

   # Find out what time it is now (in Coordinated Universal Time)
timestamp = datetime.datetime.utcnow()

   # Post status update and get the response from Twitter
response = api.PostUpdate("Looking at " + website)

    #Print out response text (should be the status update if everything worked)
print("Status updated to: " + response.text)


