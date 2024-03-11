pkgname = "sway"
pkgver = "1.9"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson",
    "pkgconf",
    "scdoc",
]
makedepends = [
    "cairo-devel",
    "gdk-pixbuf-devel",
    "json-c-devel",
    "pango-devel",
    "pcre2-devel",
    "wayland-devel",
    "wayland-protocols",
    "wlroots0.17-devel",
]
pkgdesc = "Wayland compositor compatible with i3"
maintainer = "flukey <flukey@vapourmail.eu>"
license = "MIT"
url = "https://swaywm.org"
source = f"https://github.com/swaywm/sway/releases/download/{pkgver}/sway-{pkgver}.tar.gz"
sha256 = "a63b2df8722ee595695a0ec6c84bf29a055a9767e63d8e4c07ff568cb6ee0b51"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")
    self.install_file(
        self.files_path / "sway-portals.conf", "usr/share/xdg-desktop-portal"
    )


@subpackage("sway-backgrounds")
def _backgrounds(self):
    self.pkgdesc = f"{pkgdesc} (backgrounds)"

    return ["usr/share/backgrounds"]
