pkgname = "astyle"
pkgver = "3.6.18"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DINSTALL_DOC=ON"]
hostmakedepends = ["cmake", "ninja"]
pkgdesc = "Source code formatter"
license = "MIT"
url = "https://gitlab.com/saalen/astyle"
source = f"{url}/-/archive/{pkgver}/astyle-{pkgver}.tar.gz"
sha256 = "3cf671a726e9b14e75fd9ad862dc6b5500f948a12700bc842e9bd4bc3a9a9915"


def post_install(self):
    self.install_license("AStyle/LICENSE.md")
    for shell in ["bash", "fish", "zsh"]:
        self.install_completion(f"AStyle/sh-completion/astyle.{shell}", shell)
