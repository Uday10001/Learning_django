# Render Deployment Guide

## Files Created/Modified for Production

### New Files:
1. **requirements.txt** - Python dependencies
2. **.env.example** - Environment variables template
3. **build.sh** - Build script for Render
4. **gunicorn_config.py** - Gunicorn WSGI server configuration
5. **render.yaml** - Render deployment configuration
6. **.gitignore** - Files to exclude from version control

### Modified Files:
1. **my_pro/settings.py** - Production settings with environment variables
2. **my_pro/wsgi.py** - WhiteNoise middleware added

---

## Deployment Steps on Render

### 1. **Prepare Your Repository**
```bash
git init
git add .
git commit -m "Prepare for Render deployment"
git push origin main
```

### 2. **Create a PostgreSQL Database on Render**
- Go to [Render Dashboard](https://dashboard.render.com/)
- Click "New" → "PostgreSQL"
- Name: `django-db`
- Region: Choose your region
- Database: `django_db`
- User: `postgres`
- Copy the Internal Database URL

### 3. **Create a Web Service**
- Click "New" → "Web Service"
- Select your GitHub repository
- **Name:** `django-app`
- **Environment:** Python 3.11
- **Build Command:** `./build.sh`
- **Start Command:** `gunicorn -c gunicorn_config.py my_pro.wsgi:application`
- **Plan:** Free (or paid)

### 4. **Set Environment Variables**
In the Render dashboard, add these environment variables:

```
SECRET_KEY=<generate a new secret key>
DEBUG=False
ALLOWED_HOSTS=yourdomain.onrender.com,localhost
DATABASE_URL=<copy from PostgreSQL service>
```

**Generate a new SECRET_KEY:**
```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

### 5. **Deploy**
- Click "Deploy"
- Check the logs to ensure migration and static file collection complete
- Your app will be live at `https://django-app.onrender.com`

---

## Important Notes

- **SECRET_KEY**: Must be kept secret - use a new one for production
- **Database**: SQLite (db.sqlite3) won't work on Render. Use PostgreSQL.
- **Static Files**: WhiteNoise handles serving static files automatically
- **Media Files**: For user uploads, configure Render Disks or use cloud storage (AWS S3)
- **Build Time**: Free tier may take longer to build
- **Sleeping**: Free web services sleep after 15 minutes of inactivity

---

## Troubleshooting

### Static Files Not Loading
- Ensure `./build.sh` completes successfully
- Check `STATIC_ROOT` and `STATIC_URL` in settings.py

### Database Connection Error
- Verify `DATABASE_URL` is correct
- Run migrations: `python manage.py migrate`

### Application Crashes
- Check Render logs for specific errors
- Ensure all dependencies are in requirements.txt

---

## Local Testing Before Deployment

Test the production build locally:

```bash
# Install dependencies
pip install -r requirements.txt

# Set environment variables
set DEBUG=False
set SECRET_KEY=test-key-123
set DATABASE_URL=sqlite:///db.sqlite3
set ALLOWED_HOSTS=localhost,127.0.0.1

# Run migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Run with gunicorn
gunicorn -c gunicorn_config.py my_pro.wsgi:application
```
