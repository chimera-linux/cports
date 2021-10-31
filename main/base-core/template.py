pkgname = "base-core"
pkgver = "0.1"
pkgrel = 0
build_style = "meta"
depends = [
    "base-minimal", "ncurses", "mksh", "file", "less", "eudev", "kmod", "kbd",
    "mandoc", "man-pages", "e2fsprogs", "xfsprogs", "btrfs-progs",
]
pkgdesc = "Common Chimera packages for most deployments"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:meta"
url = "https://chimera-linux.org"

# TODO:
#
# - filesystem tools (f2fs-tools, dosfstools)
# - pciutils
# - iproute2, iputils, iw, traceroute, (dhcpcd?)
# - openssh
