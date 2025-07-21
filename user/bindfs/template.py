pkgname = "bindfs"
pkgver = "1.18.1"
pkgrel = 0
build_style = "gnu_configure"
make_dir = "."
hostmakedepends = [
    "automake",
    "pkgconf",
    "slibtool",
]
makedepends = [
    "fuse-devel",
    "linux-headers",
]
checkdepends = ["ruby"]
pkgdesc = "Bind mounts altering permission bits"
license = "GPL-2.0-or-later"
url = "https://bindfs.org"
source = f"{url}/downloads/bindfs-{pkgver}.tar.gz"
sha256 = "2a7064d993a5f255c52d72385ef14e349c131bc44195766e2173428e06d279fd"
# Some tests must be run as root, and some tests only work as non-root
options = ["!check"]
