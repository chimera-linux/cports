pkgname = "ninja"
pkgver = "1.12.1"
pkgrel = 0
hostmakedepends = ["python"]
pkgdesc = "Small build system with a focus on speed"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://ninja-build.org"
source = f"https://github.com/ninja-build/ninja/archive/v{pkgver}.tar.gz"
sha256 = "821bdff48a3f683bc4bb3b6f0b5fe7b2d647cf65d52aeb63328c91a6c6df285a"
# Cycle: ninja -> gtest -> ninja
options = ["!check"]


def configure(self):
    self.do("python", "configure.py", "--bootstrap")


def build(self):
    self.do("python", "configure.py")


def install(self):
    self.install_bin("ninja")
    self.install_file(
        "misc/bash-completion",
        "usr/share/bash-completion/completions",
        name="ninja",
    )
    self.install_file(
        "misc/zsh-completion", "usr/share/zsh/site-functions", name="_ninja"
    )
