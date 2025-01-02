pkgname = "gnu-getopt"
pkgver = "0.0.1"
pkgrel = 0
build_style = "makefile"
pkgdesc = "GNU getopt compatibility package for musl"
maintainer = "roastveg <louis@hamptonsoftworks.com>"
license = "BSD-4-Clause AND ISC"
url = "https://github.com/sabotage-linux/gnu-getopt"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "52eefa6973d05cab92cfc76ab83b3cde4654b91564e97983b26020792694cb5c"
# no check target
options = ["!lto", "!check", "!distlicense"]


def install(self):
    self.install_file("gnu_getopt.h", "usr/include")
    self.install_lib("libgnu_getopt.a")
