pkgname = "iio-sensor-proxy"
pkgver = "3.7"
pkgrel = 0
build_style = "meson"
configure_args = [
    "--libexecdir=/usr/lib",  # XXX drop libexec
    "-Dsystemdsystemunitdir=",
    "-Dgeoclue-user=_geoclue",
]
hostmakedepends = ["glib-devel", "meson", "pkgconf"]
makedepends = [
    "dinit-chimera",
    "glib-devel",
    "libgudev-devel",
    "linux-headers",
    "polkit-devel",
    "udev-devel",
]
checkdepends = [
    "python-dbusmock",
    "python-gobject",
    "python-psutil",
    "umockdev",
]
install_if = [f"iio-sensor-proxy-meta={pkgver}-r{pkgrel}"]
pkgdesc = "D-Bus proxy for IIO sensors"
license = "GPL-3.0-or-later"
url = "https://gitlab.freedesktop.org/hadess/iio-sensor-proxy"
source = f"{url}/-/archive/{pkgver}/iio-sensor-proxy-{pkgver}.tar.gz"
sha256 = "4d7eb0ae23506919a9a40bc1aab0e144c218be60457b3137533724814c41997b"
hardening = ["vis", "cfi"]

if not self.profile().cross:
    # don't pull in checkdepends for cross
    configure_args += ["-Dtests=true"]


def post_install(self):
    self.install_service(self.files_path / "iio-sensor-proxy")


@subpackage("iio-sensor-proxy-meta")
def _(self):
    self.subdesc = "recommends package"
    self.options = ["empty"]
    return []
