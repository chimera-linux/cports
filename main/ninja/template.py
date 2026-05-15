pkgname = "ninja"
pkgver = "1.13.2"
pkgrel = 0
hostmakedepends = ["python"]
pkgdesc = "Small build system with a focus on speed"
license = "Apache-2.0"
url = "https://ninja-build.org"
source = f"https://github.com/ninja-build/ninja/archive/v{pkgver}.tar.gz"
sha256 = "974d6b2f4eeefa25625d34da3cb36bdcebe7fbce40f4c16ac0835fd1c0cbae17"
# Cycle: ninja -> gtest -> ninja
options = ["!check"]


def configure(self):
    self.do("python", "configure.py", "--bootstrap")


def build(self):
    self.do("python", "configure.py")


def install(self):
    self.install_bin("ninja")
    for shell in ["bash", "zsh"]:
        self.install_completion(f"misc/{shell}-completion", shell)
