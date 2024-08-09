pkgname = "dulcepan"
pkgver = "1.0.1"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson",
    "pkgconf",
    "wayland-progs",
]
makedepends = [
    "cairo-devel",
    "libsfdo-devel",
    "libspng-devel",
    "libxkbcommon-devel",
    "linux-headers",
    "pixman-devel",
    "wayland-devel",
    "wayland-protocols",
]
pkgdesc = "Screenshot tool for wlroots compositors"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-3.0-only"
url = "https://codeberg.org/vyivel/dulcepan"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "39f9ed1334198a021dfbf0dbfbaf4992b99462ef563314bec11e3d27519ea75b"
hardening = ["vis", "cfi"]
