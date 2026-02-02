pkgname = "girara"
pkgver = "2026.02.04"
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
license = "Zlib"
url = "https://pwmt.org/projects/girara"
source = f"{url}/download/girara-{pkgver}.tar.xz"
sha256 = "342eca8108bd05a2275e3eacb18107fa3170fa89a12c77e541a5f111f7bba56d"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("girara-devel")
def _(self):
    return self.default_devel()
