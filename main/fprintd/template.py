pkgname = "fprintd"
pkgver = "1.94.2"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dsystemd=false", "-Dpam_modules_dir=/usr/lib/security"]
hostmakedepends = ["bash", "gettext", "meson", "perl", "pkgconf"]
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
sha256 = "79f422378162be60935ec4ecd14e845e297d36b62385659721319bb514d23e77"
# TODO: Most tests fail with the daemon exiting with SIGABRT, couldn't figure
# out how to fix that
options = ["!check"]


@subpackage("fprintd-meta")
def _meta(self):
    self.pkgdesc = f"{pkgdesc} (recommends package)"
    self.options = ["empty"]
    return []
