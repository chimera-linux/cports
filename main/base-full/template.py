pkgname = "base-full"
pkgver = "0.1"
pkgrel = 0
build_style = "meta"
depends = [
    "base-core", "nano", "initramfs-tools", "openssh", "opendoas",
    "ethtool", "dhcpcd",
]
pkgdesc = "Chimera base package for bare metal and virtual machines"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:meta"
url = "https://chimera-linux.org"

# TODO:
#
# - f2fs-tools
# - usbutils
# - elogind
# - wpa_supplicant or iwd
# - firmware (wifi etc)
# - kernel
