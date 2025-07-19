pkgname = "lf"
pkgver = "36"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Terminal file manager"
license = "MIT"
url = "https://github.com/gokcehan/lf"
source = f"{url}/archive/refs/tags/r{pkgver}.tar.gz"
sha256 = "478be3cfae12322273985f443496a511b444ebbd5d5bbec05f7eddaa9b098968"


def post_install(self):
    self.install_license("LICENSE")
    self.install_file("lf.desktop", "usr/share/applications")
    self.install_man("lf.1")
    with self.pushd("etc"):
        self.install_completion("lf.zsh", "zsh")
        self.install_completion("lf.bash", "bash")
        self.install_completion("lf.fish", "fish")
        self.install_completion("lf.nu", "nushell")
