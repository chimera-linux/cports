pkgname = "girara"
pkgver = "0.4.2"
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
sha256 = "6148c089cb6eac4ec5d25e769300b9f4d52b4ce363d9c238cf7c9dea704dda95"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("girara-devel")
def _devel(self):
    return self.default_devel()
