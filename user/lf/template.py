pkgname = "lf"
pkgver = "41"
pkgrel = 0
build_style = "go"
make_build_args = [f"-ldflags=-X main.gVersion={pkgver}"]
hostmakedepends = ["go"]
pkgdesc = "Terminal file manager"
license = "MIT"
url = "https://github.com/gokcehan/lf"
source = f"{url}/archive/refs/tags/r{pkgver}.tar.gz"
sha256 = "55c556d53b5541d5f8691f1309a0166a7a0d8e06cb051c3030c2cd7d8abc6789"


def post_install(self):
    self.install_license("LICENSE")
    self.install_file("lf.desktop", "usr/share/applications")
    self.install_man("lf.1")
    with self.pushd("etc"):
        self.install_completion("lf.zsh", "zsh")
        self.install_completion("lf.bash", "bash")
        self.install_completion("lf.fish", "fish")
        self.install_completion("lf.nu", "nushell")
