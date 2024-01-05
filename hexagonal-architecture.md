# hexagonal architecture

- traditional architecture similar to MVC - 3 layers: presentation, logic, data

- hexagonal architecture: we have a port for every input/output to an application
  - uses ports and adapters on different services
  - to 'plug-and-play' different parts without re-writing
  - e.g. change database
- instead of calling the database, we have a generic read/write method
- application doesn't care whether saving to database, file system or queue
- code for actually communicating inside adapter
- inputs are 'driving' (primary) our application and outputs are 'driven' (secondary) by our application

- pros:
  - testing as decoupled
  - maintainability
  - flexibility
- cons:
  - complexity
  - complex running locally
  - performance considerations
