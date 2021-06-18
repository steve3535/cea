from time import sleep
import redis
r = redis.Redis(host="cea_redis_1")
r.set("counter",0)

list=("\U0001f600","\U0001F923","\U0001f601","\U0001f602","\U0001f603","\U0001f604","\U0001f605","\U0001f606","\U0001f609","\U0001f60A","\U0001F970","\U0001F60D","\U0001F929","\U0001F618","\U0001F617","\U0001F61A","\U0001F619","\U0001F972","\U0001F60B","\U0001F61B","\U0001F61C","\U0001F92A","\U0001F61D","\U0001F911","\U0001F917","\U0001F92D","\U0001F92B","\U0001F914","\U0001F910","\U0001F928","\U0001F610","\U0001F611","\U0001F636","\U0001F60F","\U0001F612","\U0001F644","\U0001F637","\U0001F912","\U0001F915","\U0001F922","\U0001F92E","\U0001F927","\U0001F975","\U0001F976 ","\U0001F974","\U0001F635","\U0001F920","\U0001F973") 

while True:
  for i in range(12):
    print(list[i],end=' ',flush=True)
    sleep(0.5)
    r.incr("counter",1)
  print()

  for i in range(12):
    print(list[12+i],end=' ',flush=True)
    sleep(0.5)
    r.incr("counter",1)
  print()

  for i in range(12):
    print(list[24+i],end=' ',flush=True)
    sleep(0.5)
    r.incr("counter",1)
  print()

  for i in range(12):
    print(list[36+i],end=' ',flush=True)
    sleep(0.5)
    r.incr("counter",1)
  print()

