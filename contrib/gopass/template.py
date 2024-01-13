pkgname = "gopass"
pkgver = "1.15.11"
pkgrel = 1
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Pass-compatible password manager with more features"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "MIT"
url = "https://www.gopass.pw"
source = (
    f"https://github.com/gopasspw/gopass/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "f85610a4f114125bd21e1100d6a2970c7ab76f09a7e094aa6be378018979eb56"
options = ["!debug"]


def post_install(self):
    self.install_man("gopass.1")
    self.install_license("LICENSE")
    self.install_completion("bash.completion", "bash")
    self.install_completion("zsh.completion", "zsh")
    self.install_completion("fish.completion", "fish")
