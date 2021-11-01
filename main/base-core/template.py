pkgname = "base-core"
pkgver = "0.1"
pkgrel = 0
build_style = "meta"
depends = [
    "base-minimal", "ncurses", "mksh", "file", "less", "eudev", "kmod",
    "kbd", "mandoc", "man-pages", "e2fsprogs", "xfsprogs", "btrfs-progs",
    "dosfstools", "iputils", "iproute2", "traceroute", "iw", "pciutils",
]
pkgdesc = "Common Chimera packages for most deployments"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:meta"
url = "https://chimera-linux.org"
