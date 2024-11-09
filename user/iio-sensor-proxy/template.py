pkgname = "iio-sensor-proxy"
pkgver = "3.5"
pkgrel = 0
build_style = "meson"
configure_args = ["--libexecdir=lib"]
hostmakedepends = ["meson", "pkgconf"]
makedepends = [
    "glib-devel",
    "libgudev-devel",
    "linux-headers",
    "polkit-devel",
    "udev-devel",
]
pkgdesc = "D-Bus proxy for IIO sensors"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "GPL-3.0-only"
url = "https://gitlab.freedesktop.org/hadess/iio-sensor-proxy"
source = f"{url}/-/archive/{pkgver}/iio-sensor-proxy-{pkgver}.tar.gz"
sha256 = "8689425f2287626a95d95b1e1e5b62e497d09dd08cf411084ed22166d4a49da5"


def post_install(self):
    self.install_service(self.files_path / "iio-sensor-proxy")
