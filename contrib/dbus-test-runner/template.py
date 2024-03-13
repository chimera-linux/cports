pkgname = "dbus-test-runner"
pkgver = "19.04.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-static"]
make_cmd = "gmake"
hostmakedepends = [
    "autoconf",
    "automake",
    "gmake",
    "intltool",
    "libtool",
    "pkgconf",
]
makedepends = [
    "dbus",
    "gettext-devel",
    "glib-devel",
    "glibmm-devel",
]
checkdepends = ["bash", "python-dbusmock"]
pkgdesc = (
    "Little utility to test a couple of executables under a new DBus session"
)
maintainer = "avgwst <avgwst@tutanota.de>"
license = "GPL-3.0-or-later"
url = "https://launchpad.net/dbus-test-runner"
source = f"{url}/{pkgver[:pkgver.rfind('.')]}/{pkgver}/+download/{pkgname}-{pkgver}.tar.gz"
sha256 = "645a32fbd909baf2c01438f0cbda29dc9cd01a7aba5504c45610d88e8a57cb76"


@subpackage("dbus-test-runner-devel")
def _devel(self):
    return self.default_devel()
