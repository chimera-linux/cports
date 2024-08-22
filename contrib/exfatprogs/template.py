pkgname = "exfatprogs"
pkgver = "1.2.5"
pkgrel = 0
build_style = "gnu_configure"
make_dir = "."
hostmakedepends = [
    "automake",
    "slibtool",
]
makedepends = ["linux-headers"]
pkgdesc = "ExFAT filesystem utilities"
maintainer = "Val Packett <val@packett.cool>"
license = "GPL-2.0-only"
url = "https://github.com/exfatprogs/exfatprogs"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "ce638f06b15b3553307d244f13c64bdbd52a73460e383a5aa5d60d84a58d51b0"
