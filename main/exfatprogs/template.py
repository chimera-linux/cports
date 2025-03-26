pkgname = "exfatprogs"
pkgver = "1.2.8"
pkgrel = 0
build_style = "gnu_configure"
make_dir = "."
hostmakedepends = [
    "automake",
    "slibtool",
]
makedepends = ["linux-headers"]
pkgdesc = "ExFAT filesystem utilities"
license = "GPL-2.0-only"
url = "https://github.com/exfatprogs/exfatprogs"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "33ecb1c5d6bccb2f09925291bce918785269270b11a349bc45c8008b76de7e31"
