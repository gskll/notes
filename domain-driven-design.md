# Domain driven design

- strategic design
- easier if application is designed with DDD in mind
- subdomain refers to subject area in which we're building the application
- should be the same naming as the business - ubiquitous naming

- e.g. netflix: video streaming (core domain), billing, recommendations etc.

- subdomains should be worked out as a group exercise - needs to be representative of business
- iterative process, might have to break domains down and each subdomain has bounded context

- e.g. users are customers, viewers etc.

- each element is an entity

- context map defines interactions between different subdomains
- e.g. video quality in video streaming domain needs to map to subscriber level in billing domain
- create an anti-corruption layer that maps this for us

- tactical design
- refine domains
  - entities linked to real-world counterparts: mutable
  - entities can have several value-objects: don't have to be unique but immutable
  - only set values in constructor - they are an object
- aggregate: made up of several entities/value-objects: represents a transactional boundary e.g. order
