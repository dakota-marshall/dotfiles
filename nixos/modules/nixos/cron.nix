{ config, pkgs, ... }:
{

    systemd.timers."minecraft-rclone" = {
      wantedBy = [ "timers.target" ];
        timerConfig = {
          OnCalendar = "daily";
          Persistent = true;
          Unit = "minecraft-rclone.service";
        };
    };

    systemd.services."minecraft-rclone" = {
      script = ''
        BACKUP_DIR="/home/dmarshall/containers/minecraft/vanilla/data/backups"
        NTFY_URL="https://ntfy.sh/dmarshall-minecraft-backups-2716892"
        # This isnt a public repo and isnt storing anything sensitive, so I really dont care about this password 
        export BORG_PASSPHRASE="Underpaid-Tilt-Duplex1-Magnesium-Seltzer"

        ${pkgs.curl}/bin/curl -d "Starting Minecraft Backups..." $NTFY_URL
        ${pkgs.borgbackup}/bin/borg create $BACKUP_DIR::$(date +'%F-%H:%M') /home/dmarshall/containers/minecraft/vanilla/data/world

        # Trim Backups
        ${pkgs.borgbackup}/bin/borg prune \
            --keep-daily 7 \
            --keep-monthly 1 \
            $BACKUP_DIR
        ${pkgs.borgbackup}/bin/borg compact $BACKUP_DIR

        # Sync backups
        ${pkgs.rclone}/bin/rclone sync -v \
            $BACKUP_DIR \
            b2-drive:dk-rclone-drive/minecraft/stank_redux/backups \
            --log-file=/home/dmarshall/containers/minecraft/vanilla/rclone-logs.log || curl -d "Rsync Failed" $NTFY_URL
        ${pkgs.curl}/bin/curl -d "Minecraft Backups Finished" $NTFY_URL
      '';
      serviceConfig = {
        Type = "oneshot";
        User = "dmarshall";
      };
    };

}
