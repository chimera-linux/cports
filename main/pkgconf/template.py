pkgname = "pkgconf"
pkgver = "1.7.3"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-shared", "--disable-static"]
checkdepends = ["kyua"]
pkgdesc = "Provides compiler and linker configuration"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "http://pkgconf.org"
sources = [f"https://sources.dereferenced.org/pkgconf/pkgconf-{pkgver}.tar.xz"]
sha256 = ["b846aea51cf696c3392a0ae58bef93e2e72f8e7073ca6ad1ed8b01c85871f9c0"]

options = ["bootstrap", "!check", "!lint", "!spdx"]

def post_install(self):
    self.install_license("COPYING")

    self.rm(self.destdir / "usr/include", recursive = True)

    self.install_link("pkgconf", "usr/bin/pkg-config")
    self.install_link("pkgconf.1", "usr/share/man/man1/pkg-config.1")
