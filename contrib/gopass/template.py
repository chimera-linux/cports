pkgname = "gopass"
pkgver = "1.15.13"
pkgrel = 3
build_style = "go"
hostmakedepends = ["go"]
checkdepends = ["git", "gnupg"]
pkgdesc = "Pass-compatible password manager with more features"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "MIT"
url = "https://www.gopass.pw"
source = (
    f"https://github.com/gopasspw/gopass/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "8f7ee347f517bf66a7d0760e7a5ed6c948d66737559bd04fa8da594801ed9b4f"
# debug: fails to split on powerpc
# check: needs initialising git config
options = ["!debug", "!check"]


def post_install(self):
    self.install_man("gopass.1")
    self.install_license("LICENSE")
    self.install_completion("bash.completion", "bash")
    self.install_completion("zsh.completion", "zsh")
    self.install_completion("fish.completion", "fish")
