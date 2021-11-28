pkgname = "dash"
pkgver = "0.5.11.5"
pkgrel = 0
build_style = "gnu_configure"
pkgdesc = "POSIX-compliant Unix shell, much smaller than GNU bash"
maintainer = "q66 <daniel@octaforge.org>"
license = "BSD-3-Clause"
url = "http://gondor.apana.org.au/~herbert/dash"
source = f"http://gondor.apana.org.au/~herbert/dash/files/{pkgname}-{pkgver}.tar.gz"
sha256 = "db778110891f7937985f29bf23410fe1c5d669502760f584e54e0e7b29e123bd"
# enabling LTO results in crash on ctrl-c
options = ["bootstrap", "!lto"]

def post_install(self):
    self.install_license("COPYING")
    self.install_link("dash", "usr/bin/sh")
    # register shells
    self.install_shell("/usr/bin/dash", "/usr/bin/sh")
