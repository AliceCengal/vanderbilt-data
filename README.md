Vanderbilt Places Data Repository
---------------------------------
This is a separate repository to store the location and places data that we have
gathered so far in the development of the Guide app. The intention is that by separating
the app from the data we could:

- Update the app and data independently of each other, so there would be no merging headache.

- Allow separate teams to work on improving each entities. The database can be managed and
  improved by non-programmers, while the seemingly class CR critically endangered programmers
  can focus on the programming task.
  
- Allow easier reuse of the data by future projects.

- Generize the Guide app for institutions other than Vanderbilt simply by swapping the source
  URL of the data.

Usage
-----

Download the data using this pattern: "https://raw.github.com/AliceCengal/vanderbilt-data/master/{TABLE}.json"
where {TABLE} is one of {nodes, places, tours}
