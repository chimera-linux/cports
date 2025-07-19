pkgname = "exfatprogs"
pkgver = "1.2.9"
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
sha256 = "a9d2722a4190a6d4080df6a447498886cc566ae22bb721e3405bb82f423d51d1"
