pkgname = "bzip3"
pkgver = "1.3.2"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "autoconf",
    "automake",
    "libtool",
    "pkgconf",
]
pkgdesc = "Better and stronger spiritual successor to BZip2"
maintainer = "psykose <alice@ayaya.dev>"
license = "LGPL-3.0-or-later AND Apache-2.0"
url = "https://github.com/kspalaiologos/bzip3"
source = f"https://github.com/kspalaiologos/bzip3/releases/download/{pkgver}/bzip3-{pkgver}.tar.zst"
sha256 = "3f611a6862783fa6c430fff10614d6e66e0fda27ba063603d12e5306c4a901e7"
hardening = ["vis", "cfi"]


@subpackage("libbzip3")
def _libs(self):
    return self.default_libs()


@subpackage("libbzip3-devel")
def _devel(self):
    return self.default_devel()
