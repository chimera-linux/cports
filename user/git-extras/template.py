pkgname = "git-extras"
pkgver = "7.2.0"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
make_install_args = [
    "COMPL_DIR=$(DESTDIR)/usr/share/bash-completion/completions"
]
hostmakedepends = ["git", "gmake", "bash"]
depends = ["git", "bash"]
pkgdesc = "Extra Git utilities"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://github.com/tj/git-extras"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "f570f19b9e3407e909cb98d0536c6e0b54987404a0a053903a54b81680c347f1"
# no tests defined
options = ["!check"]


def do_build(self):
    pass


def post_install(self):
    self.install_completion("etc/git-extras-completion.zsh", "zsh")
    self.install_completion("etc/git-extras.fish", "fish")
    self.install_license("LICENSE")
