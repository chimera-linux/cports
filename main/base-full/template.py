pkgname = "base-full"
pkgver = "0.2"
pkgrel = 1
build_style = "meta"
depends = [
    "base-core",
    "base-locale",
    "nano",
    "initramfs-tools",
    "openssh",
    "syslog-ng",
    "rfkill",
    "zramctl",
    "opendoas",
    "ethtool",
    "dhcpcd",
    "usbutils",
    "f2fs-tools",
    "fdisk",
    "elogind-meta",
    "dbus",
    "iwd",
    "chrony",
    "console-setup",
    "turnstile",
    "chimera-artwork",
    # firmware for all
    "base-firmware-linux",
]
pkgdesc = "Chimera base package for bare metal and virtual machines"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:meta"
url = "https://chimera-linux.org"

match self.profile().arch:
    case "x86_64":
        # intel audio firmware
        depends += ["base-firmware-sof"]
    case "ppc64" | "ppc":
        # ppc mac disk tools
        depends += ["hfsutils", "mac-fdisk"]
