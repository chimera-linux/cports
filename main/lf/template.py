pkgname = "lf"
pkgver = "33"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Terminal file manager"
maintainer = "Subhaditya Nath <sn03.general@gmail.com>"
license = "MIT"
url = "https://github.com/gokcehan/lf"
source = f"{url}/archive/refs/tags/r{pkgver}.tar.gz"
sha256 = "045565197a9c12a14514b85c153dae4ee1bcd3b4313d60aec5004239d8d785a0"


def post_install(self):
    self.install_license("LICENSE")
    self.install_file("lf.desktop", "usr/share/applications")
    self.install_man("lf.1")
    with self.pushd("etc"):
        self.install_completion("lf.zsh", "zsh")
        self.install_completion("lf.bash", "bash")
        self.install_completion("lf.fish", "fish")
        self.install_completion("lf.nu", "nushell")
