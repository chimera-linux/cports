pkgname = "dragon"
pkgver = "1.2.0"
pkgrel = 0
build_style = "makefile"
hostmakedepends = ["pkgconf"]
makedepends = ["gtk+3-devel", "fontconfig-devel"]
pkgdesc = "Drag and drop source/target for X"
license = "GPL-3.0-or-later"
url = "https://github.com/mwh/dragon"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "9bda28e96d715c759c8a1db754bdfde5e7d83671e13cd25a892f6b5e29357994"
# no tests
options = ["!check"]
