#!/bin/bash
# Variables
DB_NAME="tech_care_africa"
DB_USER="tech_care_user"
DB_PASSWORD="12345678"
# Execute PostgreSQL commands
sudo -u postgres psql <<EOF
CREATE DATABASE $DB_NAME;
CREATE USER $DB_USER WITH PASSWORD '$DB_PASSWORD';
GRANT ALL PRIVILEGES ON DATABASE $DB_NAME TO $DB_USER;
\q
EOF

echo "Database setup completed successfully."
