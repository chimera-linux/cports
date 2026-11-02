pkgname = "wf-shell"
pkgver = "0.11.0"
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
    "gtk4-layer-shell-devel",
    "gtkmm-devel",
    "inotify-tools-devel",
    "libdbusmenu-devel",
    "libpulse-devel",
    "linux-pam-devel",
    "openssl3-devel",
    "wayfire-devel",
    "wayland-protocols",
    "yyjson-devel",
]
pkgdesc = "Desktop shell for Wayfire"
license = "MIT"
url = "https://wayfire.org"
source = f"https://github.com/WayfireWM/wf-shell/releases/download/v{pkgver}/wf-shell-{pkgver}.tar.xz"
sha256 = "8ba3698a6a136cdb85a666e7b597cd183337f05edaabf072cf2f290a2ffa4a3b"
options = ["etcfiles"]


def post_install(self):
    self.rename("etc/pam.d", "usr/lib/pam.d", relative=False)
    self.install_license("LICENSE")
