#!/bin/bash
# Utilizator separat, doar SFTP, închis în /srv/partner (fără acces la /opt/beestyle, root sau secrete).
# Rulare (de pe laptop): ssh -i ~/.ssh/beestyle_ed25519 root@89.37.212.245 'bash -s' < tools/partner-sftp-setup.sh
# Idempotent. Nu atinge Caddy, Docker sau fișierele beestyle. Dacă sshd -t pică, restaurează configul.
set -euo pipefail

PUBKEY='ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIPNmxJFsDJ7fb7oeJlX7y/LJ6xGldm3ve0dtQ9NRbCqs edgar@DESKTOP-7FQT2T2'
U=partner
BASE=/srv/partner

id "$U" >/dev/null 2>&1 || useradd --system --home-dir "$BASE" --shell /usr/sbin/nologin "$U"
mkdir -p "$BASE/site"
chown root:root "$BASE"; chmod 755 "$BASE"          # cerință chroot: rădăcina aparține lui root
chown "$U":"$U" "$BASE/site"; chmod 755 "$BASE/site"
[ -f "$BASE/site/index.html" ] || echo '<!doctype html><title>In curand</title><p>In curand.' > "$BASE/site/index.html"
chown "$U":"$U" "$BASE/site/index.html"

# cheia stă într-un fișier deținut de root, utilizatorul nu și-o poate modifica
mkdir -p /etc/ssh/authorized_keys.d
echo "$PUBKEY" > /etc/ssh/authorized_keys.d/$U
chown root:root /etc/ssh/authorized_keys.d/$U; chmod 644 /etc/ssh/authorized_keys.d/$U

CFG=/etc/ssh/sshd_config
if ! grep -q '^# BEGIN partner-sftp' "$CFG"; then
  if grep -q '^Match ' "$CFG"; then echo "Există deja Match în $CFG, opresc."; exit 1; fi
  cp -a "$CFG" "$CFG.bak-partner-$(date +%F-%H%M)"
  cat >> "$CFG" <<EOF

# BEGIN partner-sftp
Match User $U
    ChrootDirectory $BASE
    ForceCommand internal-sftp
    AuthorizedKeysFile /etc/ssh/authorized_keys.d/$U
    PasswordAuthentication no
    AllowTcpForwarding no
    X11Forwarding no
    PermitTTY no
# END partner-sftp
EOF
  if ! sshd -t; then
    echo "sshd -t a eșuat, restaurez."; cp -a "$(ls -t $CFG.bak-partner-* | head -1)" "$CFG"; exit 1
  fi
  systemctl reload ssh 2>/dev/null || systemctl reload sshd
fi
echo "OK: $U, doar SFTP, în $BASE/site"
sshd -T -C user=$U,host=x,addr=127.0.0.1 | grep -E '^(chrootdirectory|forcecommand|authorizedkeysfile|passwordauthentication) '
