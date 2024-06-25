# URL Shortening Service

## Setup

1. Clone the repository:

    ```
    git clone https://github.com/daud6699/url_shortener.git
    cd url_shortener
    ```

2. Create a virtual environment and activate it:

    ```
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```
    pip install -r requirements.txt
    ```

4. Run the application:

    ```
    python app.py
    ```

5. The service will be available at `http://127.0.0.1:5000`.

## Endpoints

### Encode URL

- **URL:** `/encode`
- **Method:** `POST`
- **Request Body:** JSON containing the long URL, e.g., `{"url": "https://uk.indeed.com"}`
- **Response:** JSON containing the shortened URL, e.g., `{"short_url": "https://uk.indeed.com"}`

### Decode URL

- **URL:** `/decode`
- **Method:** `POST`
- **Request Body:** JSON containing the shortened URL, e.g., `{"url": "https://uk.indeed.com"}`
- **Response:** JSON containing the original long URL, e.g., `{"long_url": "https://uk.indeed.com"}`

## Running Tests

To run the tests, use the following command:

