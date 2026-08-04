pkgname = "astyle"
pkgver = "3.6.17"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DINSTALL_DOC=ON"]
hostmakedepends = ["cmake", "ninja"]
pkgdesc = "Source code formatter"
license = "MIT"
url = "https://gitlab.com/saalen/astyle"
source = f"{url}/-/archive/{pkgver}/astyle-{pkgver}.tar.gz"
sha256 = "5ca894e3d651983baa4f8a36113a948b5de66328e6cd55f08a6fba91c0ffca21"


def post_install(self):
    self.install_license("AStyle/LICENSE.md")
    for shell in ["bash", "fish", "zsh"]:
        self.install_completion(f"AStyle/sh-completion/astyle.{shell}", shell)
