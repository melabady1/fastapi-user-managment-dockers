# Microservice Authentication Application with Nginx Proxy

## Sample Users
- Username: `auser`, Password: `apassword`, Role: `auser`
- Username: `buser`, Password: `bpassword`, Role: `buser`
- Username: `admin`, Password: `adpassword`, Role: `admin`

## Service Endpoints
- Authentication: `http://localhost:8080/auth/`
  - Login: `POST /login`
  - Signup: `POST /signup`

- Service A: `http://localhost:8080/service-a/`
  - Accessible by 'auser' and 'admin' roles

- Service B: `http://localhost:8080/service-b/`
  - Accessible by 'buser' and 'admin' roles

## Running the Application
1. Ensure Docker and Docker Compose are installed
2. Run `docker-compose up --build`

## Testing
1. First, get a token by logging in via the auth service
2. Use the token in the Authorization header for other services
   - Header: `Authorization: Bearer <token>`

## Workflow Example
1. Login with `auser1`:
```bash
curl -X POST "http://localhost:8080/auth/login" \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -d "username=auser1&password=auser1pass"
```

2. Use the token to access Service A:
```bash
curl -X GET "http://localhost:8080/service-a/" \
     -H "Authorization: Bearer <token_from_login>"
```