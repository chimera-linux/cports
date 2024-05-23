pkgname = "grim"
pkgver = "1.4.1"
pkgrel = 1
build_style = "meson"
configure_args = [
    "-Dfish-completions=true",
    "-Dbash-completions=true",
]
hostmakedepends = [
    "bash-completion",
    "meson",
    "pkgconf",
    "scdoc",
]
makedepends = [
    "cairo-devel",
    "libjpeg-turbo-devel",
    "libxkbcommon-devel",
    "linux-headers",
    "wayland-devel",
    "wayland-protocols",
]
pkgdesc = "Grab images from a wayland compositor"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://sr.ht/~emersion/grim"
source = f"https://git.sr.ht/~emersion/grim/archive/v{pkgver}.tar.gz"
sha256 = "5ed8e70fcd83a7e203e92d34dbb82a1342d3f13ad98a6b0310cc97e1a9342ded"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")
