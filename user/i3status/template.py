pkgname = "i3status"
pkgver = "2.15"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dmans=true"]
hostmakedepends = ["meson", "pkgconf"]
makedepends = [
    "libconfuse-devel",
    "yajl-devel",
    "alsa-lib-devel",
    "libnl-devel",
    "libpulse-devel",
    "asciidoc",
    "xmlto",
    "perl",
]
pkgdesc = "Generates status bar to use with i3bar, dzen2 or xmobar"
maintainer = "shortcircuit <shortcircuitv@gmail.com>"
license = "BSD-3-Clause"
url = "https://github.com/i3/i3status"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "25af0dd77a5325c13890d4ee53a9205827a11c8b90f54e8a7fe2654bd0273d4b"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")
