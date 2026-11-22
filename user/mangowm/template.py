pkgname = "mangowm"
pkgver = "0.18.6"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson",
    "pkgconf",
    "wayland-devel",
]
makedepends = [
    "cjson-devel",
    "pango-devel",
    "pcre2-devel",
    "scenefx-devel",
    "wlroots0.20-devel",
]
depends = ["xwayland"]
pkgdesc = "Dwl-based wayland compositor using scenefx"
license = "GPL-3.0-or-later"
url = "https://github.com/mangowm/mango"
source = f"https://github.com/mangowm/mango/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "3018b593e48a1ea71247ec10ab898f1186687fa1e225863f360e3f04cf0520df"
options = ["etcfiles"]


def post_install(self):
    self.install_license("LICENSE")
