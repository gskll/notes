# Event driven architecture

- as opposed to api architecture
- and opposed but similar to message architecture using queues etc.

- service sends event after the event has happened
- sender doesn't care what happens to event
- service that raises the event doens't rely on anything being done with that event

- event vs message?
- message like a command for a specific service
- event: no instructions just info on what happened and by who

- messages get deleted once processed, events are immutable and can't be deleted

- event broker subscribed to by other services -> pub/sub

- producer publishes events, broker decides which services get which events, consumer subscribes to events

- best used where processes can be used separately

  - auditing, async backend processes, data processing

- benefits over api arch
- decouples components
- other services can be created to subscribe to same events
- use dependency inversion, components are dependent on abstraction i.e. events being raised
- systems can scale easily without slowing down publishing service

- disadvantages
- data consistency - delay between pub and sub - can make sure have enough subscribers
- eventual consistency - data will eventually be consistent
- sometimes need to use a cache layer to avoid delays
- also duplicate messages - if service goes offline it starts from the last checkpoint
- need to make sure subscribers are idempotent - unique ids
- more complex and harder to debug
