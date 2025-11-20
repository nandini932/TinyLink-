# TinyLink

A full-stack URL shortener application built with React and Django.

## Features

- Create short links with custom or auto-generated codes
- Redirect to original URLs with click tracking
- View detailed statistics for each link
- Clean, responsive UI with search and filtering
- REST API backend with proper validation

## Tech Stack

- **Frontend**: React, React Router, Tailwind CSS, Axios
- **Backend**: Django, SQLite/PostgreSQL
- **Deployment**: Vercel/Netlify (Frontend), Render/Railway/Heroku (Backend)

## API Documentation

### Health Check
- **GET** `/healthz`
- Returns: `{"ok": true, "version": "1.0"}`

### Create Short Link
- **POST** `/api/links`
- Body: `{"target_url": "https://example.com", "code": "optional"}`
- Returns: `{"code": "abc123", "target_url": "...", "short_url": "..."}`

### List Links
- **GET** `/api/links`
- Returns: Array of link objects with stats

### Get Link Stats
- **GET** `/api/links/:code`
- Returns: Detailed link information

### Delete Link
- **DELETE** `/api/links/:code`
- Returns: `{"message": "Link deleted"}`

### Redirect
- **GET** `/:code`
- Redirects to original URL (302) and increments click count

## Running Locally

### Prerequisites
- Python 3.8+
- Node.js 16+
- npm or yarn

### Backend Setup

```bash
cd backend
python -m venv venv
# On Windows: venv\Scripts\activate
# On macOS/Linux: source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py test  # Run tests
python manage.py runserver
```

### Frontend Setup

```bash
cd frontend
npm install
cp .env.example .env
npm start
```

Visit `http://localhost:3000` for the frontend and `http://localhost:8000` for the backend API.

## Deployment

See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed deployment instructions.

## Project Structure

```
tinylink/
├── backend/
│   ├── tinylink/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── ...
│   ├── links/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── tests.py
│   │   └── ...
│   ├── requirements.txt
│   └── .env.example
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── api.js
│   │   └── ...
│   ├── package.json
│   └── .env.example
├── DEPLOYMENT.md
└── README.md
```

## Architecture

- **Backend**: Django handles all business logic, URL validation, code generation, and database operations
- **Frontend**: React provides a modern SPA interface for link management
- **Database**: SQLite for development, PostgreSQL for production
- **API**: RESTful endpoints with proper HTTP status codes and JSON responses

## Testing

Backend tests are included and can be run with `python manage.py test`.

## Environment Variables

### Backend (.env)
- `SECRET_KEY`: Django secret key
- `DEBUG`: Set to False in production
- `ALLOWED_HOSTS`: Comma-separated allowed hosts
- `DATABASE_URL`: PostgreSQL connection string (production)
- `CORS_ALLOWED_ORIGINS`: Frontend URLs for CORS

### Frontend (.env)
- `REACT_APP_API_BASE`: Backend API URL

## Screenshots

[Dashboard showing links table and creation form]

[Link stats page with detailed information]

## License

MIT License - feel free to use this project for learning or production."# TinyLink-" 
"# TinyLink-" 
"# TinyLink-" 
