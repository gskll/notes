# Microservices vs Monoliths

- monoliths:
  - quicker? to work on and develop, easier to integrate different app parts
  - easier to deploy
  - easier to debug
  - performance - no requests between services
  - as grows - hard to release/test/onboard
- microservices:
  - easier to maintain
  - can scale each one independently
  - each team/service can have own tech stack/development
  - issues tend to affect only one part of application - high reliability
  - unless infra issue like DNS
  - use a message queue to interact between services if no return value is necessary - rabbitMQ, aws SQS
  - service mesh: communication between services and reliability/discoverability
  - continuous deployment
  - but hard to run locally and debug
