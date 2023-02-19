# Nu-Tracker-API

Welcome to the API the Nu-Tracker team built for their application!

Checkout our frontend repository for more info on the application here:
https://github.com/EricLGDev/Nu-Tracker-Frontend

The entire application can be ran using 
`flask run`

# REST API

The REST API to the app is described below.

"user_id" = user id in the database
"id" = references the specific diary entry in the database

## Signup to make an account

### Request

`POST /signup`

- Requires username, email, and password values

## Login to an account

### Request

`POST /login`

- Requires username and password
  - Bcrypt verification for password enabled

## Get diary entries
` GET /diary/<int:user_id>`
- Requires JWT access_token

## Create diary entries
` POST /diary`
- Requires JWT access_token

## Update diary entries
` PUT /diary/<int:id>`
- Requires JWT access_token

## DELETE diary entries
` GET /diary/<int:id>`
- Requires JWT access_token

