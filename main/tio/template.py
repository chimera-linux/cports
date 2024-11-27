pkgname = "tio"
pkgver = "3.7"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson",
    "pkgconf",
]
makedepends = [
    "bash-completion",
    "glib-devel",
    "linux-headers",
    "lua5.4-devel",
]
pkgdesc = "Terminal Serial I/O tool"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://github.com/tio/tio"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "9e39b57f38a5648b87b436e66edc54103e1deee23d78a8c5a097f314967cc326"
