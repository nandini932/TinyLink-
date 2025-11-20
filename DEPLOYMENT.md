# Deployment Instructions

## Backend Deployment (Django)

### Option 1: Render

1. Create a Render account at https://render.com
2. Connect your GitHub repository
3. Create a new Web Service
4. Set build command: `pip install -r requirements.txt`
5. Set start command: `python manage.py migrate && gunicorn tinylink.wsgi:application`
6. Add environment variables:
   - SECRET_KEY
   - DEBUG=False
   - ALLOWED_HOSTS=your-render-app.onrender.com
   - DATABASE_URL (from Render Postgres)
   - CORS_ALLOWED_ORIGINS=https://your-frontend-domain.com

### Option 2: Railway

1. Create a Railway account at https://railway.app
2. Connect your GitHub repository
3. Add a PostgreSQL database
4. Set environment variables as above
5. Deploy

### Option 3: Heroku

1. Install Heroku CLI
2. `heroku create`
3. Add PostgreSQL addon: `heroku addons:create heroku-postgresql:hobby-dev`
4. Set environment variables: `heroku config:set ...`
5. `git push heroku main`
6. Run migrations: `heroku run python manage.py migrate`

## Frontend Deployment (React)

### Option 1: Vercel

1. Create a Vercel account at https://vercel.com
2. Connect your GitHub repository
3. Set root directory to `frontend`
4. Add environment variable: REACT_APP_API_BASE=https://your-backend-domain.com
5. Deploy

### Option 2: Netlify

1. Create a Netlify account at https://netlify.com
2. Connect your GitHub repository
3. Set build command: `npm run build`
4. Set publish directory: `build`
5. Add environment variable: REACT_APP_API_BASE=https://your-backend-domain.com
6. Deploy

## Database Setup

For production, use PostgreSQL.

### Neon (Recommended)

1. Create account at https://neon.tech
2. Create a new project
3. Get the connection string
4. Set DATABASE_URL in backend environment

### Railway Postgres

Automatically provided when adding Postgres to Railway project.

## Environment Variables

### Backend

- SECRET_KEY: Generate a random secret key
- DEBUG: False for production
- ALLOWED_HOSTS: Comma-separated list of allowed hosts
- DATABASE_URL: PostgreSQL connection string
- CORS_ALLOWED_ORIGINS: Comma-separated list of frontend URLs

### Frontend

- REACT_APP_API_BASE: Backend API URL (e.g., https://your-backend.onrender.com)

## Post-Deployment

1. Run migrations on backend
2. Test API endpoints
3. Update frontend API_BASE if needed
4. Test full functionality