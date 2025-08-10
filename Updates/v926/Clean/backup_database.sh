#!/bin/bash

# Directory where your SQLite database is located
DB_PATH="/home/admin/Downloads/ISMv900/db.sqlite3"  # You'll need to replace this with your actual database path

# Backup directory on USB
BACKUP_DIR="/media/admin/BACKUP404/database_backups"

# Create backup directory if it doesn't exist
mkdir -p "$BACKUP_DIR"

# Get current timestamp
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")

# Create backup with timestamp
cp "$DB_PATH" "$BACKUP_DIR/database_backup_$TIMESTAMP.sqlite3"

# Keep only last 111 backups
ls -t "$BACKUP_DIR"/database_backup_* | tail -n +288 | xargs -r rm

# Log the backup
echo "Backup created at: $TIMESTAMP" >> "$BACKUP_DIR/backup_log.txt"
