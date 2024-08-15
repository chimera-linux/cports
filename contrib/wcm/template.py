pkgname = "wcm"
pkgver = "0.8.0"
pkgrel = 1
build_style = "meson"
configure_args = ["-Denable_wdisplays=false"]
hostmakedepends = [
    "meson",
    "pkgconf",
    "wayland-progs",
]
makedepends = [
    "gtkmm3.0-devel",
    "libxkbcommon-devel",
    "libxml2-devel",
    "wayfire-devel",
    "wayland-protocols",
    "wf-config-devel",
]
depends = ["cmd:wdisplays!wdisplays"]
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
