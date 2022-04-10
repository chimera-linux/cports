pkgname = "base-full"
pkgver = "0.1"
pkgrel = 0
build_style = "meta"
depends = [
    "base-core", "base-locale", "nano", "initramfs-tools", "openssh",
    "syslog-ng", "opendoas", "ethtool", "dhcpcd", "usbutils",
    "f2fs-tools", "elogind", "polkit", "dbus", "iwd",
    "dinit-userservd",
    "chimera-artwork",
    # firmware for all
    "firmware-linux-amd",
    "firmware-linux-nvidia",
    "firmware-linux-network",
    "firmware-wifi",
]
pkgdesc = "Chimera base package for bare metal and virtual machines"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:meta"
url = "https://chimera-linux.org"

# firmware for some
match self.profile().arch:
    case "x86_64":
        depends += ["firmware-linux-intel"]
