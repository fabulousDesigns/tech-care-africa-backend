#!/bin/bash

# Base dir
base_dir="tech_care_africa"

# Create the directories
mkdir -p $base_dir/app/models
mkdir -p $base_dir/app/schemas
mkdir -p $base_dir/app/api
mkdir -p $base_dir/app/db

# files
touch $base_dir/app/__init__.py
touch $base_dir/app/main.py
touch $base_dir/app/models/__init__.py
touch $base_dir/app/models/customer.py
touch $base_dir/app/models/order.py
touch $base_dir/app/schemas/__init__.py
touch $base_dir/app/schemas/customer.py
touch $base_dir/app/schemas/order.py
touch $base_dir/app/api/__init__.py
touch $base_dir/app/api/customers.py
touch $base_dir/app/api/orders.py
touch $base_dir/app/db/__init__.py
touch $base_dir/app/db/database.py

echo "Project Structure bootstrapped successfully."
