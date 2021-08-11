pkgname = "bsdgzip"
version = "0.99.2"
revision = 0
build_style = "gnu_makefile"
hostmakedepends = ["pkgconf"]
makedepends = ["musl-fts-devel", "liblzma-devel", "zlib-devel", "bzip2-devel"]
short_desc = "The gzip(1) suite of utilities from FreeBSD"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
homepage = "https://github.com/chimera-linux/bsdgzip"
distfiles = [f"https://github.com/chimera-linux/{pkgname}/archive/refs/tags/v{version}.tar.gz"]
checksum = ["785fe89ecd03ac07fcea0682f33d35d611a397897efa537c0b00e70d86f86b2b"]

options = ["bootstrap"]
