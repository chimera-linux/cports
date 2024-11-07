pkgname = "lf"
pkgver = "32"
pkgrel = 8
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Terminal file manager"
maintainer = "Subhaditya Nath <sn03.general@gmail.com>"
license = "MIT"
url = "https://github.com/gokcehan/lf"
source = f"{url}/archive/refs/tags/r{pkgver}.tar.gz"
sha256 = "01531e7a78d8bfbe14739072e93446d003f0e4ce12032a26671fa326b73bc911"


def post_install(self):
    self.install_license("LICENSE")
    self.install_file("lf.desktop", "usr/share/applications")
    self.install_man("lf.1")
    with self.pushd("etc"):
        self.install_completion("lf.zsh", "zsh")
        self.install_completion("lf.bash", "bash")
        self.install_completion("lf.fish", "fish")
