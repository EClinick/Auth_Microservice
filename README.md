# Authentication Microservice

A microservice that handles user authentication including registration, login, and profile updates.

## API Contract

### Base URL 
```
http://127.0.0.1:3001
```

## How to request the microservice
### Endpoints

#### 1. Register User
**Request:**
- Method: `POST`
- Endpoint: `/auth/register`
- Content-Type: `application/json`
- Body:
```json
{
    "first_name": "John",
    "last_name": "Doe",
    "email": "john@example.com",
    "password": "securepassword123"
}
```

**Response:**
- Success (201):
```json
{
    "message": "User registered successfully"
}
```
- Error (400):
```json
{
    "error": "Email already registered"
}
```

#### 2. Login
**Request:**
- Method: `POST`
- Endpoint: `/auth/login`
- Content-Type: `application/json`
- Body:
```json
{
    "email": "john@example.com",
    "password": "securepassword123"
}
```

**Response:**
- Success (200):
```json
{
    "token": "eyJhbGciOiJIUzI1...",
    "user": {
        "user_id": 1,
        "first_name": "John",
        "last_name": "Doe",
        "email": "john@example.com"
    }
}
```
- Error (401):
```json
{
    "error": "Invalid credentials"
}
```

#### 3. Update Profile
**Request:**
- Method: `PUT`
- Endpoint: `/auth/update-profile`
- Headers: 
  - `Authorization: Bearer <token>`
- Content-Type: `application/json`
- Body:
```json
{
    "first_name": "John",
    "last_name": "Smith",
    "email": "john@example.com",
    "old_password": "currentpassword",
    "new_password": "newpassword123"  // Optional
}
```

**Response:**
- Success (200):
```json
{
    "message": "Profile updated successfully",
    "user": {
        "user_id": 1,
        "first_name": "John",
        "last_name": "Smith",
        "email": "john@example.com"
    }
}
```
- Error (401):
```json
{
    "error": "Current password is incorrect"
}
```

### Example Implementation

Here's how to make requests to the microservice using Python's requests library:

```python
import requests

BASE_URL = 'http://127.0.0.1:3001'

# Register a new user
response = requests.post(f'{BASE_URL}/auth/register', json={
    "first_name": "John",
    "last_name": "Doe",
    "email": "john@example.com",
    "password": "securepassword123"
})

# Login
response = requests.post(f'{BASE_URL}/auth/login', json={
    "email": "john@example.com",
    "password": "securepassword123"
})
token = response.json()['token']

# Update profile (requires auth token)
headers = {'Authorization': f'Bearer {token}'}
response = requests.put(
    f'{BASE_URL}/auth/update-profile',
    headers=headers,
    json={
        "first_name": "John",
        "last_name": "Smith",
        "email": "john@example.com",
        "old_password": "securepassword123"
    }
)
```

## UML Sequence Diagram
![Diagram](image/diagram.png)

```
sequenceDiagram
    participant C as Client
    participant A as Auth Service
    participant DB as Database

    %% Registration Flow
    C->>+A: POST /auth/register
    A->>DB: Check if email exists
    DB-->>A: Result
    A->>A: Hash password
    A->>DB: Save user
    A-->>-C: 201 Success / 400 Error

    %% Login Flow
    C->>+A: POST /auth/login
    A->>DB: Get user by email
    DB-->>A: User data
    A->>A: Verify password
    A->>A: Generate JWT
    A-->>-C: 200 + Token / 401 Error

    %% Update Profile Flow
    C->>+A: PUT /auth/update-profile
    Note over C,A: Include Bearer Token
    A->>A: Verify JWT
    A->>DB: Get user
    DB-->>A: User data
    A->>A: Verify old password
    A->>DB: Update user data
    A-->>-C: 200 Success / 401 Error
```

## Mitigation Plan

### Implementation Details
- **Implemented for**: Emmanuel Acheampong
- **Status**: Complete and functional
- **Repository** - teammate retrieves service from GitHub: [[Your GitHub Repository URL](https://github.com/EClinick/Auth_Microservice)]

### Access Instructions
1. Clone the repository from GitHub
2. Install dependencies:
```bash
pip install -r auth_service/app/requirements.txt
```
3. Set up environment variables in `.env`:
```
DB_URL=postgresql://[username]:[password]@localhost:5432/[dbname]
SECRET_KEY=[your-secret-key]
```
4. Run the service:
```bash
python auth_service/run.py
```

### Support and Availability
- Available for support: 12-6PM EST on weekdays
- Contact methods:
  - GitHub Issues
  - Discord group chat
- **Important**: Please report any issues within 24 hours of encountering them

### Troubleshooting
If you cannot access the microservice:
1. Verify PostgreSQL is running and accessible
2. Check environment variables are properly set
3. Ensure port 3001 is available
4. Contact me during support hours for immediate assistance

### Assumptions and Dependencies
- Requires PostgreSQL database
- Python 3.12+ recommended
- Port 3001 must be available
- Assumes JWT token-based authentication
- Requires proper CORS configuration if accessing from different origin

### Backup Plan
If the microservice is completely inaccessible:
1. Use the provided example responses to mock the API responses
2. Implement basic local authentication as temporary solution
3. Contact me immediately for emergency support and resolution timeline
```

