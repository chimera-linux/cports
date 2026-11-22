pkgname = "mangobar"
pkgver = "0.2.3"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson",
    "pkgconf",
    "wayland-devel",
]
makedepends = [
    "alsa-lib-devel",
    "cjson-devel",
    "elogind-devel",
    "fcft-devel",
    "gdk-pixbuf-devel",
    "libpulse-devel",
    "libxkbcommon-devel",
    "pango-devel",
    "udev-devel",
    "wayland-protocols",
]
pkgdesc = "Wayland status bar built for MangoWM"
license = "GPL-3.0-or-later"
url = "https://github.com/mangowm/mangobar"
source = (
    f"https://github.com/mangowm/mangobar/archive/refs/tags/{pkgver}.tar.gz"
)
sha256 = "9b919191d112e6a6b1a77245ceb81df6a82b203bcf0e7d015d822ca2c531ae8e"


def post_install(self):
    self.install_license("LICENSE")
