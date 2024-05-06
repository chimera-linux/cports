pkgname = "ninja"
pkgver = "1.12.0"
pkgrel = 1
hostmakedepends = ["python"]
pkgdesc = "Small build system with a focus on speed"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://ninja-build.org"
source = f"https://github.com/ninja-build/ninja/archive/v{pkgver}.tar.gz"
sha256 = "8b2c86cd483dc7fcb7975c5ec7329135d210099a89bc7db0590a07b0bbfe49a5"
# Cycle: ninja -> gtest -> ninja
options = ["!check"]


def do_configure(self):
    self.do("python", "configure.py", "--bootstrap")


def do_build(self):
    self.do("python", "configure.py")


def do_install(self):
    self.install_bin("ninja")
    self.install_file(
        "misc/bash-completion",
        "usr/share/bash-completion/completions",
        name="ninja",
    )
    self.install_file(
        "misc/zsh-completion", "usr/share/zsh/site-functions", name="_ninja"
    )
