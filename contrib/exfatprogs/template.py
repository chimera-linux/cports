pkgname = "exfatprogs"
pkgver = "1.2.4"
pkgrel = 0
build_style = "gnu_configure"
make_cmd = "gmake"
make_dir = "."
hostmakedepends = [
    "automake",
    "gmake",
    "libtool",
]
makedepends = ["linux-headers"]
pkgdesc = "ExFAT filesystem utilities"
maintainer = "Val Packett <val@packett.cool>"
license = "GPL-2.0-only"
url = "https://github.com/exfatprogs/exfatprogs"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "62b48bddd19c49ca0ebef44a836856be1917531717d6c1d600e026fe1af95a78"
