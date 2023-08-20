# Django Q and ManyToMany Bug Report Repo

Repro instructions:
1. Clone this repo
2. `pip install -r requirements.txt`
3. `./manage.py migrate`
4. `./manage.py loaddata sample`
5. `./manage.py run_test`

Sample output from test:

```
Expect 2 results to match this query:
<QuerySet [<Test: Test object (1)>, <Test: Test object (2)>]>

Expect 3 unique (4 total, one duplicate) results to match this query:
<QuerySet [<Test: Test object (1)>, <Test: Test object (2)>, <Test: Test object (1)>, <Test: Test object (3)>]>

Expect 1 result to match this query:
<QuerySet []>

Expect 1 result to match this query:
<QuerySet [<Test: Test object (1)>]>

Expect 1 result to match this query:
<QuerySet []>
```
