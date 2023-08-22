pkgname = "libmspack"
pkgver = "0.11_alpha"
pkgrel = 0
build_style = "gnu_configure"
make_cmd = "gmake"
hostmakedepends = [
    "autoconf",
    "automake",
    "gmake",
    "libtool",
    "pkgconf",
]
pkgdesc = "Library for Microsoft CAB compression formats"
maintainer = "psykose <alice@ayaya.dev>"
license = "LGPL-2.1-only"
url = "https://www.cabextract.org.uk/libmspack"
source = f"https://www.cabextract.org.uk/libmspack/libmspack-{pkgver.replace('_', '')}.tar.gz"
sha256 = "70dd1fb2f0aecc36791b71a1e1840e62173079eadaa081192d1c323a0eeea21b"
# vis breaks symbols
hardening = []


@subpackage("libmspack-devel")
def _devel(self):
    return self.default_devel()
