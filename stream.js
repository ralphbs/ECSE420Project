var Twitter = require('twit');

var twitter = new Twitter({
	consumer_key: 'fbwLlRZcz4lM1AxtjMlJJ5wca',
	consumer_secret: 'M3SKxFhrUQA1ohFtYbjrrO3EhFaadhfQ5VAAL205iwxMlQ2dMB',
	access_token: '792977116941914112-hkYWIP3LomFASEYrzp2gnaYKpxSGUDS',
	access_token_secret: 'uRiuIlAQVujcN8sn1UpHRrigqBk4Gt5DimEuZWljXJNBv'
});


var stream = twitter.stream('statuses/filter', { track: 'donald trump', language: 'en' })
 
stream.on('tweet', function (tweet) {
  console.log(tweet);
})