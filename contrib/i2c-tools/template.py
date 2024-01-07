pkgname = "i2c-tools"
pkgver = "4.3"
pkgrel = 1
build_style = "makefile"
make_cmd = "gmake"
make_build_args = ["EXTRA=py-smbus"]
make_install_args = ["sbindir=/usr/bin"] + make_build_args
hostmakedepends = ["gmake", "python", "python-setuptools"]
makedepends = ["linux-headers", "python-devel"]
depends = ["perl"]
pkgdesc = "Heterogeneous set of I2C tools and I2C library for Linux"
maintainer = "Subhaditya Nath <sn03.general@gmail.com>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later AND GPL-2.0-only"
url = "https://git.kernel.org/pub/scm/utils/i2c-tools/i2c-tools.git"
source = f"https://mirrors.edge.kernel.org/pub/software/utils/i2c-tools/i2c-tools-{pkgver}.tar.xz"
sha256 = "1f899e43603184fac32f34d72498fc737952dbc9c97a8dd9467fadfdf4600cf9"
# no tests
options = ["!check"]


# LGPL-2.1-or-later
@subpackage("i2c-tools-devel")
def _devel(self):
    return self.default_devel()


# GPL-2.0-only
@subpackage("python-smbus")
def _python(self):
    self.pkgdesc = "Python bindings for Linux SMBus access through i2c-dev"
    return ["usr/lib/python3*"]
