READY FOR RENDER DEPLOYMENT

1. Upload this project's CONTENTS to a GitHub repository.
2. On Render, create a Web Service or Blueprint from that repository.
3. Render will use render.yaml automatically if you choose Blueprint.
4. After the first deploy, open your public .onrender.com URL.

IMPORTANT LIMITATION OF THIS SIMPLE VERSION:
- The existing SQLite database and product images are included so your current website can go live quickly.
- On Render's ephemeral filesystem, new admin changes and new uploads may not persist permanently after a restart/redeploy.
- For a permanent production shop, move the database to PostgreSQL and uploaded images to persistent cloud storage.

CUSTOM DOMAIN:
After buying a domain, connect it in Render and add the domain to ALLOWED_HOSTS and CSRF_TRUSTED_ORIGINS if required.
