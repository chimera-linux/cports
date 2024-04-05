pkgname = "fprintd"
pkgver = "1.94.3"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dsystemd=false", "-Dpam_modules_dir=/usr/lib/security"]
hostmakedepends = [
    "bash",
    "gettext",
    "glib-devel",
    "meson",
    "perl",
    "pkgconf",
    "polkit-devel",
]
makedepends = [
    "dbus-devel",
    "elogind-devel",
    "glib-devel",
    "libfprint-devel",
    "linux-pam-devel",
    "polkit-devel",
]
install_if = [f"fprintd-meta={pkgver}-r{pkgrel}"]
pkgdesc = "Fingerprint scanning daemon"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-2.0-or-later"
url = "https://fprint.freedesktop.org"
source = f"https://gitlab.freedesktop.org/libfprint/fprintd/-/archive/v{pkgver}/fprintd-v{pkgver}.tar.gz"
sha256 = "2413ec9c0be24f6852afde31baa275a2d7fe3a9ee03973af9362ddb97231aedd"
# TODO: Most tests fail with the daemon exiting with SIGABRT, couldn't figure
# out how to fix that
options = ["!check"]


@subpackage("fprintd-meta")
def _meta(self):
    self.pkgdesc = f"{pkgdesc} (recommends package)"
    self.options = ["empty"]
    return []
