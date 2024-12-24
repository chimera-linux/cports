pkgname = "iio-sensor-proxy"
pkgver = "3.5"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dsystemdsystemunitdir=/usr/lib/systemd/system"]
hostmakedepends = ["meson", "pkgconf"]
makedepends = [
    "udev-devel",
    "glib-devel",
    "libgudev-devel",
    "polkit-devel",
    "linux-headers",
]
pkgdesc = "Proxies sensor devices to applications through D-Bus"
maintainer = "etj <evan@d2evs.net>"
license = "GPL-3.0-only"
url = "https://gitlab.freedesktop.org/hadess/iio-sensor-proxy"
source = f"{url}/-/archive/{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "8689425f2287626a95d95b1e1e5b62e497d09dd08cf411084ed22166d4a49da5"


def post_install(self):
    self.uninstall("usr/lib/systemd")
    self.install_service(self.files_path / "iio-sensor-proxy")
