pkgname = "dulcepan"
pkgver = "1.0.2"
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
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-3.0-only"
url = "https://codeberg.org/vyivel/dulcepan"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "9d21d8cef45ea965a9a3039af3e3f887808c30d423c5dc3159c40aedab7da870"
hardening = ["vis", "cfi"]
