pkgname = "qdiskinfo"
pkgver = "0.3"
pkgrel = 1
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "ninja",
]
makedepends = ["qt6-qtbase-devel"]
depends = [
    "qt6-qtsvg",
    "smartmontools",
]
pkgdesc = "Frontend for smartctl to display SMART data"
maintainer = "cassiofb-dev <contact@cassiofernando.com>"
license = "GPL-3.0-only"
url = "https://github.com/edisionnano/QDiskInfo"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "f9829a488ff08395e14f953d41a85dac9c91714fdd34bc9a76a46fe761511209"
