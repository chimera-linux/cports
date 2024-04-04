pkgname = "tio"
pkgver = "2.7"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson",
    "pkgconf",
]
makedepends = [
    "bash-completion",
    "inih-devel",
    "linux-headers",
]
pkgdesc = "Terminal Serial I/O tool"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-2.0-or-later"
url = "https://github.com/tio/tio"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "c1fb02f953a9a1f37a2077dd7030afbb99ace10a8c6204a810f2e662ecd43fe4"
