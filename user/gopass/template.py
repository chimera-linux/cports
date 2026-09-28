pkgname = "gopass"
pkgver = "1.17.3"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
checkdepends = ["git", "gnupg"]
pkgdesc = "Pass-compatible password manager with more features"
license = "MIT"
url = "https://www.gopass.pw"
source = (
    f"https://github.com/gopasspw/gopass/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "ed7f594a23893c99f027927fb15c4d8d5a7f27f9e351decee3530f7ad22a0386"
# needs initialising git config
options = ["!check"]


def post_install(self):
    self.install_man("gopass.1")
    self.install_license("LICENSE")
    self.install_completion("bash.completion", "bash")
    self.install_completion("zsh.completion", "zsh")
    self.install_completion("fish.completion", "fish")
