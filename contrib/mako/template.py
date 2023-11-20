pkgname = "mako"
pkgver = "1.8.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dbash-completions=true",
    "-Dfish-completions=true",
    "-Dzsh-completions=true",
]
hostmakedepends = [
    "meson",
    "pkgconf",
    "scdoc",
]
makedepends = [
    "basu-devel",
    "cairo-devel",
    "gdk-pixbuf-devel",
    "linux-headers",
    "pango-devel",
    "wayland-devel",
    "wayland-protocols",
]
depends = ["jq"]
pkgdesc = "Lightweight notification daemon for Wayland"
maintainer = "Umar Getagazov <umar@handlerug.me>"
license = "MIT"
url = "https://wayland.emersion.fr/mako"
source = f"https://github.com/emersion/mako/releases/download/v{pkgver}/mako-{pkgver}.tar.gz"
sha256 = "f20ff74925d6876fc243c49cb45cdb849afd55611aa1640471020d191823e3bb"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")
