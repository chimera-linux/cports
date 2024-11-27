pkgname = "playerctl"
pkgver = "2.4.1"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dgtk-doc=false"]
hostmakedepends = [
    "gobject-introspection",
    "meson",
    "pkgconf",
]
makedepends = ["glib-devel"]
pkgdesc = "MPRIS media player CLI tool"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "LGPL-3.0-or-later"
url = "https://github.com/altdesktop/playerctl"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "75957ad5071956f563542c7557af16a57e40b4a7f66bc9b6373d022ec5eef548"


@subpackage("playerctl-devel")
def _(self):
    return self.default_devel()


@subpackage("playerctl-libs")
def _(self):
    return self.default_libs()
