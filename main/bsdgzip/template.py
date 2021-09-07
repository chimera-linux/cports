pkgname = "bsdgzip"
version = "0.99.3"
revision = 0
build_style = "gnu_makefile"
hostmakedepends = ["pkgconf"]
makedepends = ["musl-fts-devel", "liblzma-devel", "zlib-devel", "bzip2-devel"]
short_desc = "The gzip(1) suite of utilities from FreeBSD"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
homepage = "https://github.com/chimera-linux/bsdgzip"
distfiles = [f"https://github.com/chimera-linux/{pkgname}/archive/refs/tags/v{version}.tar.gz"]
checksum = ["61b24e5573694b28f1266f38bc6859ba72eb35e48dc95bfbe37572ca120f9fe4"]

options = ["bootstrap"]
