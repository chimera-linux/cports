pkgname = "hare-adwaita"
pkgver = "0.1.0"
pkgrel = 0
build_style = "makefile"
makedepends = [
    "at-spi2-core-devel",
    "hare-gi",
    "libadwaita-devel",
]
pkgdesc = "Hare bindings to libadwaita"
license = "MPL-2.0"
url = "https://git.sr.ht/~sircmpwn/hare-adwaita"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "6fe9fa62cc840893fbac3f42111ecd4a53fff7a58aeb9246bfca9e5caa582133"
# no tests
options = ["!check"]
