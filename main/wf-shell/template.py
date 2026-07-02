pkgname = "wf-shell"
pkgver = "0.10.0"
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
sha256 = "49a7fc861849051a3be5de353e3d7442a37170c990a3ffd8d83b67a369edca93"


def post_install(self):
    self.install_license("LICENSE")
