pkgname = "pkgconf"
version = "1.7.3"
revision = 0
build_style = "gnu_configure"
configure_args = ["--disable-shared", "--disable-static"]
checkdepends = ["kyua"]
short_desc = "Provides compiler and linker configuration"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
homepage = "http://pkgconf.org"
distfiles = [f"https://distfiles.dereferenced.org/pkgconf/pkgconf-{version}.tar.xz"]
checksum = ["b846aea51cf696c3392a0ae58bef93e2e72f8e7073ca6ad1ed8b01c85871f9c0"]

options = ["bootstrap"]

def post_install(self):
    self.install_license("COPYING")

    import shutil
    shutil.rmtree(self.destdir / "usr/include")

    self.install_link("pkgconf", "usr/bin/pkg-config")
    self.install_link("pkgconf.1", "usr/share/man/man1/pkg-config.1")
