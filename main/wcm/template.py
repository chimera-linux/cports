pkgname = "wcm"
pkgver = "0.10.0"
pkgrel = 1
build_style = "meson"
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
license = "MIT"
url = "https://wayfire.org"
source = f"https://github.com/WayfireWM/wcm/releases/download/v{pkgver}/wcm-{pkgver}.tar.xz"
sha256 = "38b912dcaaf52f7585414b5b40a694b0706ed5570e17703bc3d07654646ba707"
# vis breaks symbols
hardening = ["!vis"]


def post_install(self):
    self.install_license("LICENSE")
