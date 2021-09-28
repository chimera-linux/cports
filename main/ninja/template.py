pkgname = "ninja"
pkgver = "1.10.2"
pkgrel = 0
hostmakedepends = ["python"]
pkgdesc = "Small build system with a focus on speed"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
homepage = "https://ninja-build.org"
sources = [f"https://github.com/ninja-build/ninja/archive/v{pkgver}.tar.gz"]
sha256 = ["ce35865411f0490368a8fc383f29071de6690cbadc27704734978221f25e2bed"]

options = ["!check"]

def do_configure(self):
    self.do("python", ["configure.py", "--bootstrap"])

def do_build(self):
    self.do("python", ["configure.py"])

# FIXME: docs, completions
def do_install(self):
    self.install_bin("ninja")
