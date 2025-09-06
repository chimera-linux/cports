pkgname = "enlightenment"
pkgver = "0.27.1"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dpam=true",
    "-Dwl=true",
    "-Dsystemd=false",
]
hostmakedepends = [
    "efl",
    "gettext",
    "meson",
    "pkgconf",
    "wayland-progs",
]
makedepends = [
    "bluez-devel",
    "efl-devel",
    "gettext-devel",
    "libexif-devel",
    "libxkbcommon-devel",
    "linux-pam-devel",
    "mesa-devel",
    "wayland-devel",
    "wayland-protocols",
    "xkeyboard-config",
    "xwayland-devel",
]
depends = [
    "desktop-file-utils",
    "elogind",
    "hicolor-icon-theme",
    "setxkbmap",
    "xkeyboard-config",
]
pkgdesc = "Enlightenment desktop shell"
license = "BSD-2-Clause"
url = "https://enlightenment.org"
source = f"http://download.enlightenment.org/rel/apps/enlightenment/enlightenment-{pkgver}.tar.xz"
sha256 = "b41df8771f60e3b96a1973ae566d7425c53a8339f18e54e31230218781da2fa9"
file_modes = {
    "usr/lib/enlightenment/utils/enlightenment_ckpasswd": (
        "root",
        "root",
        0o4755,
    ),
    "usr/lib/enlightenment/utils/enlightenment_system": (
        "root",
        "root",
        0o4755,
    ),
    "usr/lib/enlightenment/utils/enlightenment_sys": ("root", "root", 0o4755),
}
# FIXME int: janky codebase
hardening = ["!int"]
# FIXME lintpixmaps
options = ["!lintpixmaps"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("enlightenment-devel")
def _(self):
    self.depends += [self.parent]

    return self.default_devel()
