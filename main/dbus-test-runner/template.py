pkgname = "dbus-test-runner"
pkgver = "19.04.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-static"]
hostmakedepends = [
    "automake",
    "gettext-devel",
    "intltool",
    "libtool",
    "pkgconf",
]
makedepends = [
    "glib-devel",
]
depends = ["dbus"]
checkdepends = ["bash", "dbus", "python-dbusmock"]
pkgdesc = "Test executables under a new DBus session"
maintainer = "avgwst <avgwst@tutanota.de>"
license = "GPL-3.0-only"
url = "https://launchpad.net/dbus-test-runner"
source = f"{url}/{pkgver[: pkgver.rfind('.')]}/{pkgver}/+download/dbus-test-runner-{pkgver}.tar.gz"
sha256 = "645a32fbd909baf2c01438f0cbda29dc9cd01a7aba5504c45610d88e8a57cb76"


@subpackage("dbus-test-runner-devel")
def _(self):
    return self.default_devel()
