pkgname = "rdfind"
pkgver = "1.8.0"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "libtool"]
makedepends = ["nettle-devel"]
pkgdesc = "Duplicate file finder"
license = "GPL-2.0-or-later"
url = "https://rdfind.pauldreik.se"
source = f"https://rdfind.pauldreik.se/rdfind-{pkgver}.tar.gz"
sha256 = "0a2d0d32002cc2dc0134ee7b649bcc811ecfb2f8d9f672aa476a851152e7af35"
hardening = ["vis", "cfi"]
# linuxisms in testsuite
options = ["!check"]
