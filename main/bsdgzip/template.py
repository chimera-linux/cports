pkgname = "bsdgzip"
pkgver = "0.99.3"
pkgrel = 0
build_style = "makefile"
hostmakedepends = ["pkgconf"]
makedepends = ["musl-fts-devel", "liblzma-devel", "zlib-devel", "libbz2-devel"]
pkgdesc = "The gzip(1) suite of utilities from FreeBSD"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://github.com/chimera-linux/bsdgzip"
sources = [f"https://github.com/chimera-linux/{pkgname}/archive/refs/tags/v{pkgver}.tar.gz"]
sha256 = ["61b24e5573694b28f1266f38bc6859ba72eb35e48dc95bfbe37572ca120f9fe4"]

options = ["bootstrap", "!check", "!lint"]
