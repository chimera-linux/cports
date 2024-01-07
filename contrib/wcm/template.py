pkgname = "wcm"
pkgver = "0.8.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "glib-devel",
    "meson",
    "pkgconf",
    "wayland-progs",
]
makedepends = [
    "gtk+3-devel",
    "gtkmm3.0-devel",
    "libxml2-devel",
    "wayfire-devel",
    "wayland-protocols",
    "wf-config-devel",
]
pkgdesc = "Wayfire Config Manager"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://wayfire.org"
source = f"https://github.com/WayfireWM/wcm/releases/download/v{pkgver}/wcm-{pkgver}.tar.xz"
sha256 = "61aef3ceab7f5c16966462c42d98bd0580d45b346a86d029df3e625b9bc13bba"
# vis breaks symbols
hardening = ["!vis"]


def post_install(self):
    self.install_license("LICENSE")
