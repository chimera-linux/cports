pkgname = "git-extras"
pkgver = "7.1.0"
pkgrel = 0
depends = ["git", "bash"]
pkgdesc = "Extra Git utilities"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://github.com/tj/git-extras"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "e5c855361d2f1ec1be6ee601247153d9c8c04a221949b6ec3903b32fa736f542"


def do_install(self):
    self.install_files("bin", "usr")
    self.install_man("man/*.1", glob=True)
    self.install_completion("etc/bash_completion.sh", "bash")
    self.install_completion("etc/git-extras-completion.zsh", "zsh")
    self.install_completion("etc/git-extras.fish", "fish")
    self.install_license("LICENSE")
