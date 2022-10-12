# Timekeeping demo

This is a very basic demo site  for demonstrating how time tracking can  work in a case management system.  I have created this site for the  Philadelphia  social justice hackathon of October 2022.

If you are working on the hackathon challenge related to voice controlled time tracking,  then you can use this site  to show you what would be required to upload  time slip data  from a local computer to the case management system.

This site assumes there is no API  for directly uploading timeslip data to the system. Instead, our upload tool  needs to  log into the system like any human user.  Once logged in, the tool can navigate to a form for POST'ing  timeslip data that has been saved locally.

The endpoints you need to know about:

`/login`. 

A `GET`  requests to this endpoint will return a form for logging in. In the real world, it would also include a CSRF token that needs to be included in submissions to this form.

A `POST`  request to this endpoint with a username and password will redirect you. With the correct credentials ('test' and 'test' in this demo) you  will be redirected to the timekeeping page.

`/timekeeping`

You can only access this endpoint once you have successfully authenticated to `/login`. ( in this demo site, it would be very easy to fake the authentication,  but that would be cheating! And it wouldn't work in a real time tracking site.)

A `GET` request to this endpoint returns a form for submitting timeslip data.

A `POST` request with the form's required data will return a page that tells you that you successfully submitted a timeslip.



## Running this demo

Running this demo site is hopefully pretty easy if you are used to using python. Clone the code from Github and install the dependencies with `poetry install`. 

Activate the new virtual environment for the site with `poetry shell`.

Run the site with `uvicorn timetrack_demo.app:app`. It will run on port 8000 by default.

