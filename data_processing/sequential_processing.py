import sys
import json
import time
import tarfile
import textblob

class SentimentCounter(object):
    def __init__(self):
        super(SentimentCounter, self).__init__()

        self.sentiment_sum = 0
        self.sentences_count = 0

    def process_data(self, data):
            sentiment = textblob.TextBlob(data['text']).sentiment
            self.sentiment_sum += sentiment.polarity
            self.sentences_count += 1

    def summarize(self):
            print "Sum is {0} and count is {1}. On average it is {2}.".format(self.sentiment_sum, self.sentences_count, self.sentiment_sum / float(self.sentences_count))

if __name__ == "__main__":
    with open("../log.txt") as f:
        lines = f.readlines()
    count = 0
    counter = SentimentCounter()
    start = time.time()
    for line in lines:
        count += 1
        new_line = json.loads(line)
        print "Process is reading line {0}".format(count)
        counter.process_data(new_line)
            
    counter.summarize()
    print "Took %s second." % (time.time() - start)