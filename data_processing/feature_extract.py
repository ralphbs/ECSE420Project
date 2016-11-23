import sys
import json
import time
import tarfile
import argparse
import textblob

DATA_FILE = '../log.tar.gz'

from mpi4py import MPI
comm = MPI.COMM_WORLD
nprocs = comm.Get_size()
rank = comm.Get_rank()

class SentimentCounter(object):
    def __init__(self):
        super(SentimentCounter, self).__init__()

        self.sentiment_sum = 0
        self.sentences_count = 0

    def process_data(self, data, index):
        if nprocs == 1 or index % nprocs == rank:
            sentiment = textblob.TextBlob(data['text']).sentiment
            self.sentiment_sum += sentiment.polarity
            self.sentences_count += 1

    def summarize(self):
        if rank == 0:
            for i in xrange(1, nprocs):
                received = comm.recv(source = i, tag = i)
                self.sentiment_sum += received[0]
                self.sentences_count += received[1]

            print "Sum is {0} and count is {1}. On average it is {2}.".format(self.sentiment_sum, self.sentences_count, self.sentiment_sum / float(self.sentences_count))
        else:
            comm.send((self.sentiment_sum, self.sentences_count), dest = 0, tag = rank)



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = 'Compress the logged data.')
    parser.add_argument('-f', '--input', dest = 'input_file', default = DATA_FILE, help = 'Input data file')
    parser.add_argument('-l', '--limit', dest = 'limit', default = 500, help = 'Limit number of lines to process. 0 to process everything.', type = int)
    args = parser.parse_args()

    tar = tarfile.open("../log.tar.gz", "r:gz")
    for member in tar.getmembers():
        f = tar.extractfile(member)
        count = 0

        counter = SentimentCounter()

        lines = f.readlines()
        start = time.time()
        for line in lines:
            count += 1

            new_data = json.loads(line)
            counter.process_data(new_data, count - 1)

            if count == args.limit and args.limit != 0:
                break

        counter.summarize()
        if rank == 0:
            print "Took %s second." % (time.time() - start)
