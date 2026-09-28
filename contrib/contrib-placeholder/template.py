pkgname = "contrib-placeholder"
pkgver = "4.20.69"
pkgrel = 0
build_style = "meta"
# prevent installation
depends = ["virtual:meta:do-not-use!base-files"]
pkgdesc = "Contrib repository placeholder, do not install"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:meta"
url = "https://chimera-linux.org"


@subpackage("contrib-placeholder-dbg")
def _(self):
    self.depends = ["virtual:meta:do-not-use!base-files"]
    return []
