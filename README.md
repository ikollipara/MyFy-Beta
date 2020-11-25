# MyFy

## Structure of Code
 * backend
    * api
        * spotify Wrapper
    * auth
 * nginx
 * web
 *docker-compose.yml

## How to run
Install Docker and run ```bash
docker-compose up -d ```
__________
## Tests
### Component & System Tests
 1. One Time Login
     * Start MyFy and navigate to homepage.
     * Login and then close the tab.
     * Reopen tab
     * PASS: If navigated to Homepage and not login page.
     * **PASSED**
 2. Token Refresh
     * Start MyFy and navigate to homepage.
     * Allow Token to expire
     * Navigate to a feature page
     * PASS: If feature works correctly.
     * **NOT IMPLEMENTED**
 3. Listening Graph Endpoint
     * Start MyFy and navigate to /api/listening_graph?genre=rock with a test access token.
     * PASS: 
        * If returned JSON at key genre contains 3 entries. 
        * If returned JSON entries are a tuple of 2 numbers.
     * **PASSED**

 4. Top Artists Endpoint
     * Start MyFy and navigate to Top Artists Page. 
     * PASS:
        * If 5 Artists are shown
        * If each artist has their own card.
        * If each card contains correct Spotify Link.
        * If each card contains a song from each artist.
     * **NOT IMPLEMENTED**

 5. Oldies Endpoint
     * Start MyFy and navigate to Oldies Page.
     * Click "Generate Oldie"
     * PASS:
        * If oldie generated is over user's oldie range (~5 years)
        * If list of songs older than 5 years is shown.
     * **NOT IMPLEMENTED**

 6. Working Reverse Proxy
     * Start MyFy and navigate to homepage.
     * Navigate to /auth
     * Navigate to /api/total_genres.
     * PASS: If not 502 error is presented.
     * **PASSED**