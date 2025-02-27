pkgname = "rdfind"
pkgver = "1.7.0"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "libtool"]
makedepends = ["nettle-devel"]
pkgdesc = "Duplicate file finder"
license = "GPL-2.0-or-later"
url = "https://rdfind.pauldreik.se"
source = f"https://rdfind.pauldreik.se/rdfind-{pkgver}.tar.gz"
sha256 = "78c463152e1d9e4fd1bfeb83b9c92df5e7fc4c5f93c7d426fb1f7efa2be4df29"
hardening = ["vis", "cfi"]
# linuxisms in testsuite
options = ["!check"]
