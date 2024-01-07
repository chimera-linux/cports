pkgname = "sway"
pkgver = "1.8.1"
pkgrel = 3
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
    "wlroots-devel",
]
pkgdesc = "Wayland compositor compatible with i3"
maintainer = "flukey <flukey@vapourmail.eu>"
license = "MIT"
url = "https://swaywm.org"
source = f"https://github.com/swaywm/sway/releases/download/{pkgver}/sway-{pkgver}.tar.gz"
sha256 = "73f08fd2cf7948e8af900709efe44eae412ae11c5773960e25c9aa09f73bad41"
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
