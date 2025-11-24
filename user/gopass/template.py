pkgname = "gopass"
pkgver = "1.15.18"
pkgrel = 1
build_style = "go"
hostmakedepends = ["go"]
checkdepends = ["git", "gnupg"]
pkgdesc = "Pass-compatible password manager with more features"
license = "MIT"
url = "https://www.gopass.pw"
source = (
    f"https://github.com/gopasspw/gopass/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "46b197fd6d72305203bf342a88931a25366b7066801c0151ea01c2a4efed2f79"
# needs initialising git config
options = ["!check"]


def post_install(self):
    self.install_man("gopass.1")
    self.install_license("LICENSE")
    self.install_completion("bash.completion", "bash")
    self.install_completion("zsh.completion", "zsh")
    self.install_completion("fish.completion", "fish")
