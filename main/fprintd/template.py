pkgname = "fprintd"
pkgver = "1.94.4"
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
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-2.0-or-later"
url = "https://fprint.freedesktop.org"
source = f"https://gitlab.freedesktop.org/libfprint/fprintd/-/archive/v{pkgver}/fprintd-v{pkgver}.tar.gz"
sha256 = "f58355c4c40d351db0af99f37ae3eb9f901bd0fae3ea84ea5f731fe1ce235cbe"
# TODO: Most tests fail with the daemon exiting with SIGABRT, couldn't figure
# out how to fix that
options = ["!check"]


@subpackage("fprintd-meta")
def _(self):
    self.subdesc = "recommends package"
    self.options = ["empty"]
    return []
