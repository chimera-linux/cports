pkgname = "bsdsed"
pkgver = "0.99.2"
pkgrel = 0
build_style = "makefile"
pkgdesc = "The sed(1) utility from FreeBSD"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://github.com/chimera-linux/bsdsed"
sources = [f"https://github.com/chimera-linux/bsdsed/archive/refs/tags/v{pkgver}.tar.gz"]
sha256 = ["4e2e5df15c3f9c0594f4ba1b9d243c5e7aa87abac8721716635bb872eef46229"]

options = ["bootstrap", "!check"]
