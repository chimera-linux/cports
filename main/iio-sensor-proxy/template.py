pkgname = "iio-sensor-proxy"
pkgver = "3.6"
pkgrel = 0
build_style = "meson"
configure_args = [
    "--libexecdir=/usr/lib",  # XXX drop libexec
    "-Dsystemdsystemunitdir=",
    "-Dgeoclue-user=_geoclue",
    "-Dtests=true",
]
hostmakedepends = ["meson", "pkgconf"]
makedepends = [
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
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-3.0-or-later"
url = "https://gitlab.freedesktop.org/hadess/iio-sensor-proxy"
source = f"{url}/-/archive/{pkgver}/iio-sensor-proxy-{pkgver}.tar.gz"
sha256 = "387cffea8b55d3087b199975cf3e00f2405d4dfe4a9bfb311b396e6473c67a96"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_service(self.files_path / "iio-sensor-proxy")


@subpackage("iio-sensor-proxy-meta")
def _(self):
    self.subdesc = "recommends package"
    self.options = ["empty"]
    return []
