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
          ${pkgs.rclone}/bin/rclone sync -v --protondrive-replace-existing-draft=true \
          /home/dmarshall/containers/minecraft/vanilla/data/backups/ \
          pdrive:minecraft/stank_redux/backups \
          --log-file=/home/dmarshall/containers/minecraft/vanilla/rclone-logs.log
      '';
      serviceConfig = {
        Type = "oneshot";
        User = "dmarshall";
      };
    };

}
