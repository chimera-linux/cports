pkgname = "mako"
pkgver = "1.9.0"
pkgrel = 2
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
maintainer = "Umar Getagazov <umar@handlerug.me>"
license = "MIT"
url = "https://wayland.emersion.fr/mako"
source = f"https://github.com/emersion/mako/releases/download/v{pkgver}/mako-{pkgver}.tar.gz"
sha256 = "16d821ef49acfc8503367e1a886d28b2f8578ae9ceb1a7e284888b1e32b3a337"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")
