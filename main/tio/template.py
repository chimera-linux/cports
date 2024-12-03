pkgname = "tio"
pkgver = "3.8"
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
sha256 = "c0e68c96f28a5b4daaf94eba31b066853efd1f1ea396c75a6cc168f2e95cdea3"
