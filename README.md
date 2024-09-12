# :arrow_up: Level Launch :rocket:
Crowdfunding Back End
Created by Afira Zulkifli

## Planning:
### Concept/Name
{{ Include a short description of your website concept here. }}

### Intended Audience/User Stories
{{ Who are your intended audience? How will they use the website? }}

### Front End Pages/Functionality
- {{ A page on the front end }}
    - {{ A list of dot-points showing functionality is available on this page }}
    - {{ etc }}
    - {{ etc }}
- {{ A second page available on the front end }}
    - {{ Another list of dot-points showing functionality }}
    - {{ etc }}

### API Spec
{{ Fill out the table below to define your endpoints. An example of what this might look like is shown at the bottom of the page. 

It might look messy here in the PDF, but once it's rendered it looks very neat! 

It can be helpful to keep the markdown preview open in VS Code so that you can see what you're typing more easily. }}

| URL | HTTP Method | Purpose | Purpose | Request Body | Success Response Code | Authentication/Authorisation |
| --- | ----------- | ------- | ------- | ------------ | --------------------- | ---------------------------- |
|     |             |         |         |              |                       |                              |

### DB Schema
![]( {{ ./relative/path/to/your/schema/image.png }} )

## Project Requirements
This crowdfunding project must:

- [ ] Be separated into two distinct projects: an API built using the Django Rest Framework and a website built using React. 
- [x] Have a cool name, bonus points if it includes a pun and/or missing vowels. See https://namelix.com/ for inspiration. <sup><sup>(Bonus Points are meaningless)</sup></sup>
- [ ] Have a clear target audience.
- [ ] Have user accounts. A user should have at least the following attributes:
  - [ ] Username
  - [ ] Email address
  - [ ] Password
- [ ] Ability to create a “project” to be crowdfunded which will include at least the following attributes:
  - [ ] Title
  - [ ] Owner (a user)
  - [ ] Description
  - [ ] Image
  - [ ] Target amount to fundraise
  - [ ] Whether it is currently open to accepting new supporters or not
  - [ ] When the project was created
- [ ] Ability to “pledge” to a project. A pledge should include at least the following attributes:
  - [ ] An amount
  - [ ] The project the pledge is for
  - [ ] The supporter/user (i.e. who created the pledge)
  - [ ] Whether the pledge is anonymous or not
  - [ ] A comment to go along with the pledge
- [ ] Implement suitable update/delete functionality, e.g. should a project owner be allowed to update a project description?
- [ ] Implement suitable permissions, e.g. who is allowed to delete a pledge?
- [ ] Return the relevant status codes for both successful and unsuccessful requests to the API.
- [ ] Handle failed requests gracefully (e.g. you should have a custom 404 page rather than the default error page).
- [ ] Use Token Authentication, including an endpoint to obtain a token along with the current user's details.
- [ ] Implement responsive design.

## Submission Requirements
The following should be included in this readme doc:

- [ ] A link to the deployed project.
- [ ] A screenshot of Insomnia, demonstrating a successful GET method for any endpoint.
- [ ] A screenshot of Insomnia, demonstrating a successful POST method for any endpoint.
- [ ] A screenshot of Insomnia, demonstrating a token being returned.
- [ ] Step by step instructions for how to register a new user and create a new project (i.e. endpoints and body data).
- [ ] Your refined API specification and Database Schema.