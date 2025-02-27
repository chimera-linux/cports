pkgname = "fprintd"
pkgver = "1.94.5"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dsystemd=false"]
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
install_if = [self.with_pkgver("fprintd-meta")]
pkgdesc = "Fingerprint scanning daemon"
license = "GPL-2.0-or-later"
url = "https://fprint.freedesktop.org"
source = f"https://gitlab.freedesktop.org/libfprint/fprintd/-/archive/v{pkgver}/fprintd-v{pkgver}.tar.gz"
sha256 = "a026ef34c31b25975275cc29a5e4eba2b54524769672095a5228098a08acd82c"
# TODO: Most tests fail with the daemon exiting with SIGABRT, couldn't figure
# out how to fix that
options = ["!check"]


@subpackage("fprintd-meta")
def _(self):
    self.subdesc = "recommends package"
    self.options = ["empty"]
    return []
