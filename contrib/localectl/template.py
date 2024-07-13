pkgname = "localectl"
pkgver = "1.0.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson",
    "gobject-introspection",
    "pkgconf",
]
depends = [
    "glib",
]
pkgdesc = "Control the system locale and keyboard layout settings"
maintainer = "Gnarwhal <git.aspect893@passmail.net>"
license = "GPL-3.0-or-later"
url = "https://github.com/Gnarwhal/localectl-chimera"
source = f"https://github.com/Gnarwhal/localectl-chimera/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "852869f8711e32885250b286e0df99d2e53b76a6f30cce0e74ea1a1b91ee23df"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")
