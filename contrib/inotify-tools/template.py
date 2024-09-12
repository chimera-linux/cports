pkgname = "inotify-tools"
pkgver = "4.23.9.0"
pkgrel = 1
build_style = "gnu_configure"
makedepends = ["automake", "slibtool"]
pkgdesc = "Command-line interface to inotify"
maintainer = "c7s <c7s@kasku.net>"
license = "GPL-2.0-only"
url = "https://github.com/inotify-tools/inotify-tools"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "1dfa33f80b6797ce2f6c01f454fd486d30be4dca1b0c5c2ea9ba3c30a5c39855"


@subpackage("inotify-tools-devel")
def _(self):
    return self.default_devel()
