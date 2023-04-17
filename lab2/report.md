Для gunicorn
ab -n 10 -c 2 -t 1 -v 2 http://127.0.0.1:8000/ 

Finished 6179 requests


Server Software:        gunicorn
Server Hostname:        127.0.0.1
Server Port:            8000

Document Path:          /
Document Length:        14 bytes

Concurrency Level:      2
Time taken for tests:   1.000 seconds
Complete requests:      6179
Failed requests:        0
Total transferred:      945540 bytes
HTML transferred:       86520 bytes
Requests per second:    6178.93 [#/sec] (mean)
Time per request:       0.324 [ms] (mean)
Time per request:       0.162 [ms] (mean, across all concurrent requests)
Transfer rate:          923.37 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     0    0   0.0      0       1
Waiting:        0    0   0.0      0       1
Total:          0    0   0.0      0       1

Percentage of the requests served within a certain time (ms)
  50%      0
  66%      0
  75%      0
  80%      0
  90%      0
  95%      0
  98%      0
  99%      0
 100%      1 (longest request)

Для nginx

ab -n 10 -c 2 -t 1 -v 2 http://127.0.0.1/index.html

Finished 16163 requests


Server Software:        nginx/1.22.1
Server Hostname:        127.0.0.1
Server Port:            80

Document Path:          /index.html
Document Length:        157 bytes

Concurrency Level:      2
Time taken for tests:   1.000 seconds
Complete requests:      16163
Failed requests:        0
Non-2xx responses:      16163
Total transferred:      4994367 bytes
HTML transferred:       2537591 bytes
Requests per second:    16162.84 [#/sec] (mean)
Time per request:       0.124 [ms] (mean)
Time per request:       0.062 [ms] (mean, across all concurrent requests)
Transfer rate:          4877.26 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     0    0   0.0      0       2
Waiting:        0    0   0.0      0       2
Total:          0    0   0.0      0       2

Percentage of the requests served within a certain time (ms)
  50%      0
  66%      0
  75%      0
  80%      0
  90%      0
  95%      0
  98%      0
  99%      0
 100%      2 (longest request)


