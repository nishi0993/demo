from prometheus_client import Counter, Histogram


walks_started = Counter('walks_started', 'number of walks started')
walks_completed = Counter('walks_completed', 'number of walks completed')
invalid_walks = Counter('invalid_walks', 'number of walks attempted to be started, but invalid')

walk_distance = Histogram('walk_distance', 'distribution of distance walked', buckets=[0, 50, 200, 400, 800, 1600, 3200])