# mentorship-matching-api

An API that matches mentees to mentors using a weighted scoring system.

I did workstudy with a mentorship cohort that paired incoming students with upperclassmen, by reading each individual application and matching them manually. This API automates the process of matching mentees to mentors. 

## Running it

```
pip install -r requirements.txt
python app.py
```
The server runs at `http://127.0.0.1:5000`.

## Endpoints

- `GET /mentees` - list all mentees
- `POST /mentees` - add a mentee
- `GET /mentors` - list all mentors
- `POST /mentors` - add a mentor
- `GET /matches` - run matching, return pairings

## Example requests

Add a mentee:

```
curl -X POST http://127.0.0.1:5000/mentees \
-H "Content-Type: application/json" \
-d '{"id":"1","name":"Mindy","major":"EECS","subjects":["python","java"],"skills":["3d printing","robotics"],"interests":["hiking","reading"]}'
```

Add a mentor with capacity 1:

```
curl -X POST http://127.0.0.1:5000/mentors \
  -H "Content-Type: application/json" \
  -d '{"id":"3","name":"Maddy","major":"EECS","subjects":["python","html"],"skills":["robotics"],"interests":["hiking","painting"],"capacity":1}'
```

Get matches:

```
curl http://127.0.0.1:5000/matches
```

```json
[{"mentee": "Mindy", "mentor": "Maddy", "score": 67.5}]
```

On Windows PowerShell, use `Invoke-RestMethod` instead:

```powershell
Invoke-RestMethod -Uri http://127.0.0.1:5000/mentees -Method Post -ContentType "application/json" -Body '{"id":"1","name":"Mindy","major":"EECS","subjects":["python","java"],"skills":["3d printing","robotics"],"interests":["hiking","reading"]}'
```

## How scoring works

Each pair is scored out of 100:

| Criterion | Weight |
|---|---|
| Major | 35 |
| Subjects | 25 |
| Skills | 25 |
| Interests | 15 |

The scoring for major is all-or-nothing, so if the mentor and the mentee do not share a major, they do not receive those points. The other three criteria produce a fraction between 0 and 1, multiplied by their weight.

That fraction divides shared items by **the number of items the mentee listed** - not by the union of both lists. The score answers "how much of what this mentee wants does this mentor cover?" Using the union would penalize mentors with broad interest lists, which is backwards for a program that exists to serve mentees. 

Mentors have a capacity limit and stop being eligible once they have reached the limit.

## Limitations

- **Greedy assignment.** Mentees are processed in list order, and each takes the best mentor still available. This can waste a strong pairing: if mentee A scores 67.5 with a mentor, and mentee B scores 100 with the same mentor, A goes first and B is left unmatched. 
- **In-memory storage.** Data is lost when the server restarts. 
- **No authentication or input validation.** A malformed request will raise a `KeyError` rather than returning a useful error. 

## Tests
```
python -m pytest
```



