pkgname = "wcm"
pkgver = "0.9.0"
pkgrel = 0
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
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "MIT"
url = "https://wayfire.org"
source = f"https://github.com/WayfireWM/wcm/releases/download/v{pkgver}/wcm-{pkgver}.tar.xz"
sha256 = "8c8605ccb720fb24e58f16c2e2727cd07b6754bd441c9a3f0e715548b4e7c4ae"
# vis breaks symbols
hardening = ["!vis"]


def post_install(self):
    self.install_license("LICENSE")
