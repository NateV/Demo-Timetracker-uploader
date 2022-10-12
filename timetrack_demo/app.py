from fastapi import FastAPI, Form, Response, Cookie
from typing import Union
from fastapi.responses import HTMLResponse
from fastapi.responses import RedirectResponse


app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def root():
    return HTMLResponse("""
        <html><body>
            <p> Please <a href='/login'> login </a>.</p>
        </body></html>
            """)

@app.get("/login", response_class=HTMLResponse)
async def login():
    html_content = """<html> 
        <body>
            <h1> Login here </h1>
            <div>
                <form id="login" action="/login" method="post">
                    <div>
                    <label for="userid">User Name</label>
                    <input id="userid" name="userid"/>
                    </div>
                    <div>
                    <label for="password">Password</label>
                    <input id="password" name="password" type="password"/>
                    </div>
                    <div>
                        <button type="submit">Submit</button>
                    </div>
                </form>
            </div>
        </body>
    </html>"""
    return HTMLResponse(html_content)


@app.post("/login")
async def handleLoginForm(response: Response, userid:str = Form(), password : str = Form()):
    if userid == "test" and password == "test":
        response =  RedirectResponse("/timekeeping", status_code=303)
        response.set_cookie(key="fakesession", value="fake-cookie-session-value")
        return response
    else:
        return RedirectResponse("/login", status_code=303)

@app.get("/timekeeping", response_class=HTMLResponse)
async def timetracking_form(fakesession : Union[str, None] = Cookie(default=None)):
    if fakesession != "fake-cookie-session-value":
        return RedirectResponse("/login",status_code=403)
    html_content = """
        <html>
            <body>
                <h2> Please upload time entry here. </h2>
                <form id="timeslip" action="/timekeeping" method="post">
                    <div>
                        <label for="caseid">Case ID</label>
                        <input id="caseid" name="caseid" type="text"/>
                    </div>
                    <div>
                        <label for="date_of_service">Date of Service</label>
                        <input id="date_of_service" name="date_of_service" type="date"/>
                    </div>
                    <div>
                        <label for="caseworker">Case Worker</label>
                        <input id="caseworker" name="caseworker" type="text"/>
                    </div>
                    <div>
                        <label for="funding_code">Funding Code</label>
                        <input id="funding_code" name="funding_code" type="text"/>
                    </div>
                    <div>
                        <label for="time_spent">Time Spent</label>
                        <input id="time_spent" name="time_spent" type="text"/>
                    </div>
                    <div>
                        <label for="activity_details">Activity Details</label>
                        <input id="activity_details" name="activity_details" type="text"/>
                    </div>
                    <div>
                        <button type="submit">Submit</button>
                    </div>
                </form>
            </body>
        </html>
    """
    
    return HTMLResponse(html_content)

@app.post("/timekeeping", response_class=HTMLResponse)
async def timekeeping_create(caseid: str = Form(), date_of_service: str = Form(),
    caseworker: str = Form(), funding_code: str = Form(), time_spent: float = Form(),
    activity_details: str = Form(), fakesession : Union[str, None] = Cookie(default=None)):

    if fakesession != "fake-cookie-session-value":
        return RedirectResponse("/login",status_code=403)

    html_content = """
        <html>
            <body>
                <p> Good job! </p>
            </body>
        </html>
    """

    return HTMLResponse(html_content)
