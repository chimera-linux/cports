pkgname = "tio"
pkgver = "3.3"
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
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-2.0-or-later"
url = "https://github.com/tio/tio"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "4865f778905477e6768650f46270044543e487dbf2b23629b32569663804e455"
