```
sudo chmod -R 755 frontend/

chmod +x /home/admin/Downloads/ISMv900/fix_cron_permissions.sh
/home/admin/Downloads/ISMv900/fix_cron_permissions.sh

./setup_backup_task.sh


chmod +x /home/admin/Dowmloads/ISMv900/setup_remote_backup.sh
chmod +x /home/admin/Dowmloads/ISMv900/remote_backup_database.sh

./setup_remote_backup.sh

crontab -e

*/5 * * * * /home/admin/Dowmloads/ISMv900/remote_backup_database.sh

*/15 * * * * /home/admin/Dowmloads/ISMv900/backup_database.sh

```
