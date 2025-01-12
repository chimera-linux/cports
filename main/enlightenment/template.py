pkgname = "enlightenment"
pkgver = "0.27.0"
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
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://enlightenment.org"
source = f"http://download.enlightenment.org/rel/apps/enlightenment/enlightenment-{pkgver}.tar.xz"
sha256 = "5b66b914c6d90a916b3fe66b5ff70a9fd912088aa6399bdde1b3a505aae50331"
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


def post_install(self):
    self.install_license("COPYING")


@subpackage("enlightenment-devel")
def _(self):
    self.depends += [self.parent]

    return self.default_devel()
