pkgname = "mako"
pkgver = "1.10.0"
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
sha256 = "a72543f7b92568a0c3c45a5c0e3487ced65c18003eecd9b7d017a6464e7cef82"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")
