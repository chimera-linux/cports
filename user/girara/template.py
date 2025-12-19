pkgname = "girara"
pkgver = "0.4.5"
pkgrel = 1
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
license = "Zlib"
url = "https://pwmt.org/projects/girara"
source = f"{url}/download/girara-{pkgver}.tar.xz"
sha256 = "6b7f7993f82796854d5036572b879ffaaf7e0b619d12abdb318ce14757bdda91"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("girara-devel")
def _(self):
    return self.default_devel()
