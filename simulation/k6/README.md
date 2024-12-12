## Run
You must first install the k6 on your local machine:
https://grafana.com/docs/k6/latest/set-up/install-k6/

Then you can run the script using command below
```bash
k6 run script.js
```

## Scenarios

There are two scenarios simulated in the script:
- `random_rating`: in this scenario we use 200 virtual users to send `rate` request for random posts with
id from 1 to 1000 with random rating from 0 to 5. The goal of this scenario is to see if the system is working
properly or not. In 5 minutes we try to send requests.
- `mixed_rating`: After 5 minutes, we trigger this scenario to run. Now we use 400 virtual users with 50% chance of
sending rate request for posts with id 1 or 2 with rating of 5, and 50% chance of sending rates to random posts with random
rating score (same as first scenario). The goal is that we see how the rating changes.

If you know k6, feel free to change or update the scenarios (You can ask help from chatGPT).
