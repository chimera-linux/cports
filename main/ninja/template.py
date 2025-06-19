pkgname = "ninja"
pkgver = "1.13.0"
pkgrel = 0
hostmakedepends = ["python"]
pkgdesc = "Small build system with a focus on speed"
license = "Apache-2.0"
url = "https://ninja-build.org"
source = f"https://github.com/ninja-build/ninja/archive/v{pkgver}.tar.gz"
sha256 = "f08641d00099a9e40d44ec0146f841c472ae58b7e6dd517bee3945cfd923cedf"
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
