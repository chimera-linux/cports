pkgname = "gopass"
pkgver = "1.15.14"
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
sha256 = "47a2a735fc94064c3eb53c400f15c39b543bdb01753537da39403d12dddc03ea"
# needs initialising git config
options = ["!check"]


def post_install(self):
    self.install_man("gopass.1")
    self.install_license("LICENSE")
    self.install_completion("bash.completion", "bash")
    self.install_completion("zsh.completion", "zsh")
    self.install_completion("fish.completion", "fish")
