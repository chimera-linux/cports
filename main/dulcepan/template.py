pkgname = "dulcepan"
pkgver = "1.0.3"
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
license = "GPL-3.0-only"
url = "https://codeberg.org/vyivel/dulcepan"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "022a57335326b89b9ccc1efb98f043c7ad50fc3dcc14e1d0a220fae8d5efdf6d"
hardening = ["vis", "cfi"]
