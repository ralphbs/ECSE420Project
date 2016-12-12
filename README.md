# ECSE420Project

## To run data fetching
Make sure both node and npm are installed on your machines.

Clone the repository:

```
git clone https://github.com/ralphbs/ECSE420Project
```

Go to the directory:

```
cd ECSE420Project
```

Install dependencies:

```
npm install
```

Run REST API program:

```
node search.js
```

OR

Run Stream API program:

```
node stream.js
```

To filter tweets using certain parameters, check out https://dev.twitter.com/rest/reference/get/search/tweets that displays all the options you can have in the request.

## How to run data processing

Compress the streamed data file into ```log.tar.gz``` file. Place the tar.gz file in the root folder.
Navigate to data processing folder:
```
cd data_processing
```

Run ```feature_extract.py``` with appropriate flags. For example, to process the first 500 tweets only:
```
mpiexec -np 4 python feature_extract.py -l 500
```

OR, to process all tweets

```
mpiexec -np 4 python feature_extract.py -l 0
```

For running on multiple hosts, to generate a list of workable hosts, run from root directory

```
python running_hosts.py
```

Available hosts will be generated in ```AvailableHosts.txt``` and can be used as the host file to run feature extract file

```
mpiexec --hostfile ../AvailableHosts.txt python feature_extract.py -l 0
```
