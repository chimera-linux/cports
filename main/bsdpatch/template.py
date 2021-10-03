pkgname = "bsdpatch"
pkgver = "0.99.1"
pkgrel = 0
build_style = "makefile"
pkgdesc = "The patch(1) utility from FreeBSD"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://github.com/chimera-linux/bsdpatch"
sources = [f"https://github.com/chimera-linux/bsdpatch/archive/refs/tags/v{pkgver}.tar.gz"]
sha256 = ["ad031c86b23ed776697f77f1a3348cd7129835965d4ee9966bc50e65c97703e8"]

options = ["bootstrap", "!check", "!lint", "!spdx"]
