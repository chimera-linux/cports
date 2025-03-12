pkgname = "wf-shell"
pkgver = "0.9.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "glib-devel",
    "gobject-introspection",
    "meson",
    "pkgconf",
    "wayland-progs",
]
makedepends = [
    "alsa-lib-devel",
    "gtk-layer-shell-devel",
    "gtkmm3.0-devel",
    "libdbusmenu-devel",
    "libpulse-devel",
    "wayfire-devel",
    "wayland-protocols",
]
pkgdesc = "Desktop shell for Wayfire"
license = "MIT"
url = "https://wayfire.org"
source = f"https://github.com/WayfireWM/wf-shell/releases/download/v{pkgver}/wf-shell-{pkgver}.tar.xz"
sha256 = "c8ac529b9fa6a4f65bd430140394b6b6a486c7b2def6c22b811396612ba94bb4"


def post_install(self):
    self.install_license("LICENSE")
