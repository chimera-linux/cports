pkgname = "mako"
pkgver = "1.11.0"
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
    "cairo-devel",
    "gdk-pixbuf-devel",
    "linux-headers",
    "pango-devel",
    "tangle-devel",
    "wayland-devel",
    "wayland-protocols",
]
depends = ["jq", "tangle-progs"]
pkgdesc = "Lightweight notification daemon for Wayland"
license = "MIT"
url = "https://wayland.emersion.fr/mako"
source = f"https://github.com/emersion/mako/releases/download/v{pkgver}/mako-{pkgver}.tar.gz"
sha256 = "e97eb5bd0dc6a9159019949f48b3db4e8781b56bd6377bd65827e1cb440a7def"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")
