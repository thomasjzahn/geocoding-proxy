# Geocoding Proxy Service

_Thomas Zahn_

## Installation

### Requirements
* Python 3.6
* pip
* pipenv

### Install
* Clone the repo from GitHub
* Copy the `.env` file from the email into the root directory of the project
* Run `pipenv install` from the project directory
* Run the server by running `pipenv run python main.py`
* Press Ctrl+C to stop the server

## How to Use
* Server is set to localhost (127.0.0.1) on port 8000
* Using a client of choice (browser, Postman, `curl`, etc.) access the `/geocoding` endpoint with a URL (GET) parameter of `address`
* **Example:**
`http://127.0.0.1:8000/geocoding?address=425+Market+Street+San+Francisco+California`
* All API responses will contain a HTTP status code (`status`) and either `data` or `message` if the request is valid or not
* The `/geocoding` response will contain a `source` property that contains the name of the external API (Here.com or Google Maps) that was used
* GET requests to `/` will return all possible API routes
* Requests to any other URL on the server will return a 404

## Assumptions
* A production API would be behind a web server like Apache or Nginx.  For the sake of this demo, Python's HTTPServer library is used.
* Usually a production application would use a standard MVC framework like Django or Flask.
* REST API will only support GET method.
* REST API will only support JSON response.
* REST API will only support the geocode resource route.  Other routes will return a 404 response.
* Primary and Seconary Geocoding Services are set as class constants.  A production application would have these in a database or some other easy-to-manage location.
* The REST server contains simple, hard-coded routes for this example.  No dynamic routes or regex parameters are included.
* Assumed all external API responses will be over HTTPS.
* Assumed all external API responses will be GET requests.
* Assumed all external API responses will return JSON data.
* No instruction was given on how to respond when both Primary and Secondary Geocoding APIs fail or do not return a result.
* No translation is made to the lat/lng data returned from the external API; they are passed as-is.
* More robust error-checking for parsing JSON results of external services is needed.  For the sake of time, this was minimally implemented to support the standard use case.
* Credentials and Secrets (API keys, etc.) should not be committed to version control, and should be kept in a secret manager like Hashicorp Vault or AWS Parameter Store.  For the sake of this exercise, they are delivered in an `.env` file via email.


