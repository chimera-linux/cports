pkgname = "enlightenment"
pkgver = "0.25.4"
pkgrel = 1
build_style = "meson"
configure_args = [
    "-Dpam=true",
    "-Dwl=true",
    "-Dsystemd=false",
]
hostmakedepends = [
    "meson",
    "pkgconf",
    "gettext-tiny",
    "efl",
    "xwayland",
    "wayland-progs",
]
makedepends = [
    "gettext-tiny-devel",
    "efl-devel",
    "mesa-devel",
    "wayland-devel",
    "wayland-protocols",
    "libxkbcommon-devel",
    "linux-pam-devel",
    "libexif-devel",
    "bluez-devel",
    "xkeyboard-config",
]
depends = [
    "desktop-file-utils",
    "hicolor-icon-theme",
    "xkeyboard-config",
    "elogind",
]
pkgdesc = "Enlightenment desktop shell"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://enlightenment.org"
source = f"http://download.enlightenment.org/rel/apps/{pkgname}/{pkgname}-{pkgver}.tar.xz"
sha256 = "56db5d206b821b9a8831d26e713e410ac70b2255a6f43fcdf7c01eefde23b7a2"
suid_files = [
    "usr/lib/enlightenment/utils/enlightenment_ckpasswd",
    "usr/lib/enlightenment/utils/enlightenment_system",
    "usr/lib/enlightenment/utils/enlightenment_sys",
]
# FIXME int: janky codebase
hardening = ["!int"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("enlightenment-devel")
def _devel(self):
    self.depends += [f"enlightenment={pkgver}-r{pkgrel}"]

    return self.default_devel()
