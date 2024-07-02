pkgname = "dulcepan"
pkgver = "1.0.0"
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
sha256 = "5125c4c082f3551f611f3e2cf09e98f51767447a82a68ceed41f35169fdede43"
hardening = ["vis", "cfi"]
