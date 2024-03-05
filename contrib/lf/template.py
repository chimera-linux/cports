pkgname = "lf"
pkgver = "31"
pkgrel = 1
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Terminal file manager"
maintainer = "Subhaditya Nath <sn03.general@gmail.com>"
license = "MIT"
url = "https://github.com/gokcehan/lf"
source = f"{url}/archive/refs/tags/r{pkgver}.tar.gz"
sha256 = "ed47fc22c58cf4f4e4116a58c500bdb9f9ccc0b89f87be09f321e8d1431226ab"


def post_install(self):
    self.install_license("LICENSE")
    self.install_file("lf.desktop", "usr/share/applications")
    self.install_man("lf.1")
    with self.pushd("etc"):
        self.install_completion("lf.zsh", "zsh")
        self.install_completion("lf.bash", "bash")
        self.install_completion("lf.fish", "fish")
