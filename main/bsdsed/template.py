pkgname = "bsdsed"
version = "0.99.2"
revision = 0
build_style = "gnu_makefile"
short_desc = "The sed(1) utility from FreeBSD"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
homepage = "https://github.com/chimera-linux/bsdsed"
distfiles = [f"https://github.com/chimera-linux/bsdsed/archive/refs/tags/v{version}.tar.gz"]
checksum = ["4e2e5df15c3f9c0594f4ba1b9d243c5e7aa87abac8721716635bb872eef46229"]

options = ["bootstrap", "!check"]
