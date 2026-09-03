BACKUPS=/tmp/backup
# rm -rf $BACKUPS
python backup_oop.py sample_dir $BACKUPS -s
tree --charset ascii  $BACKUPS