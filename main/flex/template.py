pkgname = "flex"
version = "2.6.4"
revision = 0
build_style = "gnu_configure"
configure_args = ["--disable-bootstrap", "--disable-shared"]
hostmakedepends = ["byacc", "bsdm4"]
makedepends = ["byacc", "bsdm4"]
depends = ["byacc", f"libfl-devel={version}-r{revision}", "bsdm4"]
short_desc = "Fast Lexical Analyzer"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:flex"
homepage = "https://github.com/westes/flex"
distfiles = [f"https://github.com/westes/{pkgname}/releases/download/v{version}/{pkgname}-{version}.tar.gz"]
checksum = ["e87aae032bf07c26f85ac0ed3250998c37621d95f8bd748b31f15b33c45ee995"]

options = ["!check"]

# Required to enable the definition of reallocarray() in stdlib.h
CFLAGS = ["-D_GNU_SOURCE"]

def post_install(self):
    self.install_link("flex", "usr/bin/lex")
    self.install_license("COPYING")

@subpackage("libfl-devel")
def _devel(self):
    self.short_desc = short_desc + " - development files"

    return ["usr/include", "usr/lib/*.a"]
