pkgname = "base-core"
pkgver = "0.1"
pkgrel = 0
build_style = "meta"
depends = [
    "base-minimal", "ncurses", "mksh", "file", "less", "eudev", "kmod", "kbd",
]
pkgdesc = "Common Chimera packages for most deployments"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:meta"
url = "https://chimera-linux.org"

# TODO:
#
# - man-pages, mandoc
# - filesystem tools (e2fsprogs, xfsprogs, btrfs-progs, f2fs-tools, dosfstools)
# - pciutils
# - iproute2, iputils, iw, traceroute, (dhcpcd?)
# - openssh
# - sudo or doas
