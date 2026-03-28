pkgname = "units"
pkgver = "2.24"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "pkgconf",
]
makedepends = [
    "python",
    "readline-devel",
]
depends = [
    "python-requests",
]
pkgdesc = "Units conversion and calculation program"
license = "GPL-3.0-or-later"
url = "https://www.gnu.org/software/units"
source = f"http://ftp.gnu.org/gnu/units/units-{pkgver}.tar.gz"
sha256 = "1e502c4edfacf20b29284716c72e5ddb51a495a2365d7b03e7960494c4a0c902"
hardening = ["vis", "cfi"]
