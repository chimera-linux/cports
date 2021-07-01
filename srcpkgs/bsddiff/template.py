pkgname = "bsddiff"
version = "0.99.0"
revision = 1
bootstrap = True
build_style = "meson"
short_desc = "Alternative to GNU coreutils from FreeBSD"
maintainer = "q66 <daniel@octaforge.org>"
license = "BSD-2-Clause"
homepage = "https://github.com/chimera-linux/bsdutils"
distfiles = [f"https://github.com/chimera-linux/{pkgname}/archive/refs/tags/v{version}.tar.gz"]
checksum = ["9505436bc26b7a9ba7efed7e67194f1fc21ff3b3b4c968277c96d3da25676ca1"]

if not current.bootstrapping:
    hostmakedepends = ["meson"]
