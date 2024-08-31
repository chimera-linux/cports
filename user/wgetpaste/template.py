pkgname = "wgetpaste"
pkgver = "2.34"
pkgrel = 1
depends = ["bash", "wget2"]
pkgdesc = "Command-line interface to various paste-bins"
maintainer = "jabuxas <jabuxas@proton.me>"
license = "MIT"
url = "https://github.com/zlin/wgetpaste"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "097b77440460365976f8f66e99b0150c8a9527307f6ecade1db6b60a0bfad781"


def install(self):
    self.install_bin("wgetpaste")
    self.install_completion("_wgetpaste", "zsh")
    self.install_license("LICENSE")
