# Crowdfunding Back End
{{ your name here }}

## Planning:
### Concept/Name
{{ Include a short description of your website concept here. }}

### Intended Audience/User Stories
{{ Who are your intended audience? How will they use the website? }}

### Front End Pages/Functionality
- Home Page
  - ### requirements first then
  - Featured kickstarters
- Create New Fundraiser Page
  - Form with fundraiser details
  - Abilities to submit
  - Nice error pages for validation
- Display Fundraiser
  - Shows all information about fundraiser
  - Show all pledges made so far

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

| URL | HTTP Method | Purpose | Request Body | Success Response Code | Authentication / Authorisation | 
| --- | ----------- | ------- | ------------ | --------------------- | ------------------ |
|/fundraisers/ | GET | Fetch all the fundraisers | N/A | 201 | None | |/ fundraisers | POST | Create a new fundraiser | JSON Payload | 201 | Any logged in user |
|/fundraisers/ | POST | Create a new fundraiser | JSON Payload | 201 | Any logged in user |
|/fundraisers/1/ | text | text | text | text | text |
|/pledges/ | GET | Fetch all the pledges | N/A | 200 | Any logged in user |
|/pledges/ | POST | Create a new pledge | JSON Payload {"fundraiser_id"} | 201 | Any logged in user |



### DB Schema
![](database.drawio.svg)

Link to deployed project: https://karolt-crowdfunding-70503c219ccc.herokuapp.com/fundraisers/

Working POST endpoint (auth-token)
![alt text](<Screenshot 2025-09-06 at 12.49.36 pm.png>)

Working GET endpoint (fundraisers)
![alt text](<Screenshot 2025-09-06 at 12.50.36 pm.png>)

Working PUT endpoint (fundraisers)
![alt text](<Screenshot 2025-09-06 at 12.47.49 pm.png>)

