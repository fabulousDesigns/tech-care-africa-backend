#!/bin/bash
# Connect to the tech_care_africa database and grant permissions
sudo -u postgres psql << EOF
-- Connect to the tech_care_africa database
\c tech_care_africa

-- Grant usage on schema public to tech_care_user
GRANT USAGE ON SCHEMA public TO tech_care_user;

-- Grant all privileges on all tables in schema public to tech_care_user
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO tech_care_user;

-- Grant all privileges on all sequences in schema public to tech_care_user
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO tech_care_user;

-- Grant tech_care_user the ability to create tables in the public schema
ALTER USER tech_care_user WITH CREATEDB;

-- Make tech_care_user the owner of the public schema
ALTER SCHEMA public OWNER TO tech_care_user;
EOF
