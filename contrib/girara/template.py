pkgname = "girara"
pkgver = "0.4.4"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "doxygen",
    "gettext",
    "meson",
    "pkgconf",
]
makedepends = [
    "check-devel",
    "glib-devel",
    "gtk+3-devel",
    "json-glib-devel",
    "libnotify-devel",
]
checkdepends = ["xserver-xorg-xvfb"]
pkgdesc = "GTK+ user interface library with a focus on simplicity"
maintainer = "ttyyls <contact@behri.org>"
license = "Zlib"
url = "https://pwmt.org/projects/girara"
source = f"{url}/download/girara-{pkgver}.tar.xz"
sha256 = "a321079b3cda000d16d978e8609fb631381f54d7596e7218aaba05c6f4b8bac1"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("girara-devel")
def _(self):
    return self.default_devel()
