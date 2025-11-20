# Video Walkthrough Script

## Introduction (0:00 - 0:30)

"Hi everyone! Today I'm going to walk you through TinyLink, a complete full-stack URL shortener application I built using React and Django. This is a production-ready project that includes everything from the backend API to the frontend UI, complete with testing and deployment instructions.

Let me show you what we've built."

## Project Overview (0:30 - 1:00)

"TinyLink is a bit.ly clone that allows users to create short links, track clicks, and manage their URLs through a clean web interface. The tech stack includes:

- React with functional components and hooks for the frontend
- Django REST API for the backend
- SQLite for local development, PostgreSQL for production
- Tailwind CSS for styling
- Deployed on Vercel and Render

Let me demonstrate the functionality first, then we'll dive into the code."

## Demo (1:00 - 2:30)

[Show the running application]

"Here's the dashboard where users can create new short links. I can enter a target URL and optionally specify a custom code, or let the system generate one automatically.

Once created, the link appears in the table with its stats. I can copy the short URL, view detailed statistics, or delete links.

Let me create a link and show the redirect functionality."

[Create a link, copy URL, paste in new tab to show redirect]

"The redirect increments the click count and updates the timestamp. Let me show the stats page for this link."

[Navigate to stats page]

"Here we can see all the detailed information about the link."

## Backend Architecture (2:30 - 4:00)

"Now let's look at the backend. We're using Django with a simple Link model that stores the code, target URL, clicks, and timestamps.

The views handle all the API endpoints: creating links, listing them, getting stats, deleting, and the redirect logic.

I included proper validation for URLs and codes, and the redirect view increments the click counter."

[Show models.py, views.py, urls.py]

## Frontend Architecture (4:00 - 5:30)

"The frontend is built with React. The main components are:

- Dashboard: Shows the form and links table
- LinkForm: For creating new links
- Table: Displays links with actions
- Stats: Detailed view for individual links

We're using React Router for navigation and Axios for API calls. Tailwind CSS provides clean, responsive styling."

[Show components, api.js, App.js]

## Testing (5:30 - 6:00)

"I included comprehensive backend tests that cover all the API endpoints and functionality. You can run them with 'python manage.py test'."

[Show tests.py]

## Deployment (6:00 - 7:00)

"For deployment, the backend goes to Render/Railway with PostgreSQL, and the frontend to Vercel/Netlify. I included detailed instructions in the DEPLOYMENT.md file."

[Show deployment file briefly]

## Conclusion (7:00 - 7:30)

"This project demonstrates a complete full-stack application with modern technologies, proper architecture, testing, and deployment. The code is clean, well-documented, and production-ready.

Thanks for watching! Check out the README for setup instructions and feel free to use this as a starting point for your own projects."