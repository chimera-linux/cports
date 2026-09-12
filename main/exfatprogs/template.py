pkgname = "exfatprogs"
pkgver = "1.4.3"
pkgrel = 0
build_style = "gnu_configure"
make_dir = "."
hostmakedepends = [
    "automake",
    "pkgconf",
    "slibtool",
]
makedepends = ["linux-headers", "util-linux-blkid-devel"]
pkgdesc = "ExFAT filesystem utilities"
license = "GPL-2.0-only"
url = "https://github.com/exfatprogs/exfatprogs"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "d745a0e7f97e1c36fad97148062ba4c496724e212d6075ff3129355d9054e218"
