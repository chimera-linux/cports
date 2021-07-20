pkgname = "bsdpatch"
version = "0.99.1"
revision = 0
build_style = "gnu_makefile"
short_desc = "The patch(1) utility from FreeBSD"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
homepage = "https://github.com/chimera-linux/bsdpatch"
distfiles = [f"https://github.com/chimera-linux/bsdpatch/archive/refs/tags/v{version}.tar.gz"]
checksum = ["ad031c86b23ed776697f77f1a3348cd7129835965d4ee9966bc50e65c97703e8"]

options = ["bootstrap"]
