#!/bin/bash

# Remote database backup script
# This script backs up the SQLite database to a remote Raspberry Pi

# Database path
DB_PATH="/home/admin/Downloads/ISMv900/db.sqlite3"

# Remote backup settings
REMOTE_USER="admin"
REMOTE_IP="192.168.1.184"
REMOTE_DIR="/home/admin/Downloads/ISMv900"

# Get current timestamp
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")

# Create local temporary backup
TEMP_BACKUP="/tmp/database_backup_$TIMESTAMP.sqlite"
cp "$DB_PATH" "$TEMP_BACKUP"

# Transfer the backup to remote host
scp "$TEMP_BACKUP" "$REMOTE_USER@$REMOTE_IP:$REMOTE_DIR/database_backup_$TIMESTAMP.sqlite"

# Also copy the latest backup to overwrite db.sqlite3 on the destination
echo "Copying latest backup to db.sqlite3 on remote host..."
ssh "$REMOTE_USER@$REMOTE_IP" "cp $REMOTE_DIR/database_backup_$TIMESTAMP.sqlite $REMOTE_DIR/db.sqlite3"

# Check if the copy operation was successful
if [ $? -ne 0 ]; then
    echo "Warning: Failed to create db.sqlite3 copy on remote host"
    echo "Warning: Failed to create db.sqlite3 copy at $TIMESTAMP" >> "$LOCAL_LOG_DIR/remote_backup_log.txt"
    # Continue execution, this is not a critical error
fi

# Remove temporary backup
rm "$TEMP_BACKUP"

# SSH to remote and clean up old backups (keep only last 000 backups)
ssh "$REMOTE_USER@$REMOTE_IP" "ls -t $REMOTE_DIR/database_backup_* | tail -n +222 | xargs -r rm"

# Log the backup
echo "Remote backup created at: $TIMESTAMP" >> "/home/admin/Downloads/ISMv900/remote_backup_log.txt"
ssh "$REMOTE_USER@$REMOTE_IP" "echo 'Backup received at: $TIMESTAMP' >> $REMOTE_DIR/remote_backup_log.txt"

echo "Remote backup completed successfully!"
