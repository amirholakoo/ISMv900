#!/bin/bash

# Add the backup task to crontab
(crontab -l 2>/dev/null; echo "*/15 * * * * /home/admin/backup_database.sh") | crontab -

echo "Backup task has been scheduled to run every 15 minutes"
echo "To check if it's installed, you can run: crontab -l"
echo "To monitor backups, check: /media/admin/BACKUP1404/database_backups/backup_log.txt"
