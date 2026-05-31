# Weather app

This is a basic weather app server. This accepts a GET request with cities are a query parameter and responds with their temperature. Using this app, I will learn:

1. HTTP server basics
2. Making external API calls asynchronously
3. Batching multiple API calls using asyncio.gather
4. Retry mechanisms when a request fails
5. Basics of websocket (theory only)

## Learnings:

- Used asyncio.gather to batch the fetching of weather data. This is just like promise.all in js.
- As we use spread operator (...) in js, we have \* in python that expands a list into individual arguments.
- Used httpx.AsyncClient to make a get request. This is similar to fetch in js.
- Used FastAPI to spin up a server, routes and route handlers.
- Implemented retry mechanism along with exception handling.

## Dev

- Start the server with `fastapi dev`
- Open "http://127.0.0.1:8000/weather?cities=chennai,%20hyderabad,%20mumbai" in browser. You must see the list of cities with their temperature.
