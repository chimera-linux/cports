pkgname = "exfatprogs"
pkgver = "1.3.2"
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
sha256 = "4b3e198a2b879da52254f9d4a68accff8001b7b4e5c1860d47ad232e03a2a2d0"
