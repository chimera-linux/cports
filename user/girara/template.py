pkgname = "girara"
pkgver = "2026.07.18"
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
sha256 = "d7255635776a45d42d1e555aa425ab96caf23755442474cf240cbac966d8502f"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("girara-devel")
def _(self):
    return self.default_devel()
