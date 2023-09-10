pkgname = "wcm"
pkgver = "0.7.5"
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
sha256 = "4b7c847f48e80bad3448961b9900a1f4eed8df101daa033592b60dc892f253c9"
# vis breaks symbols
hardening = ["!vis"]


def post_install(self):
    self.install_license("LICENSE")
