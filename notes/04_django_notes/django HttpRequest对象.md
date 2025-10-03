## The `HttpRequest` Object:

When a user's browser sends a request to your Django application, Django creates an `HttpRequest` object. This object encapsulates all the information about the incoming request, such as:

- **HTTP Method:** `request.method` (e.g., 'GET', 'POST', 'PUT', 'DELETE').
- **Request Data:**
  - `request.GET`: A dictionary-like object containing all GET parameters (query string data).
  - `request.POST`: A dictionary-like object containing all POST parameters (form data).
  - `request.body`: The raw HTTP request body, useful for handling non-form data like JSON.
- **Files:** `request.FILES`: A dictionary-like object containing uploaded files.
- **User Information:** `request.user`: An `AUTH_USER_MODEL` instance representing the currently logged-in user (if using Django's authentication system).
- **Session Data:** `request.session`: A dictionary-like object for storing session-specific data.
- **Headers:** `request.headers`: A dictionary-like object containing all HTTP headers sent with the request.
- **Path Information:**
  - `request.path`: The full path to the requested page (e.g., `/articles/2025/`).
  - `request.path_info`: Same as `request.path`, but always uses the URL-decoded path.
- **Host Information:** `request.META`: A dictionary containing all available HTTP headers and other environment variables.