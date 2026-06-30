# Introduction

Article URL: https://support.optisigns.com/hc/en-us/articles/4414552808467-Introduction
Article ID: 4414552808467
Last Updated: 2025-09-02T20:25:47Z

The OptiSigns API is organized around GraphQL. GraphQL is a query language for API, it provides a complete and understandable description of the data in API, gives clients the power to ask for exactly what they need and nothing more, makes it easier to evolve APIs over time, and enables powerful developer tools.

### Why GraphQL

#### Only one API endpoint

GraphQL APIs are organized in terms of types and fields, not endpoints. Access the full capabilities of your data from a single endpoint. GraphQL uses types to ensure Apps only ask for what’s possible and provide clear and helpful errors. Apps can use types to avoid writing manual parsing code.

#### Get many resources in a single request

GraphQL queries access not just the properties of one resource but also smoothly follow references between them. While typical REST APIs require loading from multiple URLs, GraphQL APIs get all the data your app needs in a single request. Apps using GraphQL can be quick even on slow mobile network connections.

#### No over-fetching and under-fetching

Send a GraphQL query to your API and get exactly what you need, nothing more and nothing less. GraphQL queries always return predictable results. Apps using GraphQL are fast and stable because they control the data they get, not the server.

#### No Versioning

New fields and types can be added to GraphQL API without impacting existing queries. Aging fields can be deprecated and hidden from tools. By using a single evolving version, GraphQL APIs give apps continuous access to new features and encourage cleaner, more maintainable server code.

### OptiSigns API endpoint

The GraphQL API can be accessed using the endpoint.

[https://graphql-gateway.optisigns.com](https://graphql-gateway.optisigns.com/)

We also offer a web-based GraphQL IDE to access our API.  
<https://graphql-gateway.optisigns.com/graphql>

**Next Article - [Generate and Manage API Key](https://support.optisigns.com/hc/en-us/articles/4414563797139-Generate-Manage-OptiSigns-API-Key)**
