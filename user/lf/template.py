pkgname = "lf"
pkgver = "39"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Terminal file manager"
license = "MIT"
url = "https://github.com/gokcehan/lf"
source = f"{url}/archive/refs/tags/r{pkgver}.tar.gz"
sha256 = "1393f86a2387534dd5321754846e0fe39df55a7345ef2b19f349eb6ae96aaaf7"


def post_install(self):
    self.install_license("LICENSE")
    self.install_file("lf.desktop", "usr/share/applications")
    self.install_man("lf.1")
    with self.pushd("etc"):
        self.install_completion("lf.zsh", "zsh")
        self.install_completion("lf.bash", "bash")
        self.install_completion("lf.fish", "fish")
        self.install_completion("lf.nu", "nushell")
