pkgname = "gopass"
pkgver = "1.15.12"
pkgrel = 0
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
sha256 = "803d779bc55aab3c1e0ade85612f287b3007cd5316a7a571314e08b015a95426"
# debug: fails to split on powerpc
# check: needs initialising git config
options = ["!debug", "!check"]


def post_install(self):
    self.install_man("gopass.1")
    self.install_license("LICENSE")
    self.install_completion("bash.completion", "bash")
    self.install_completion("zsh.completion", "zsh")
    self.install_completion("fish.completion", "fish")
