pkgname = "exfatprogs"
pkgver = "1.2.2"
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
source = f"{url}/releases/download/{pkgver}/exfatprogs-{pkgver}.tar.xz"
sha256 = "61d517231f8ec177eeb5955fd6edb89748d3f88ba412c48bcb32741b430e359a"
