pkgname = "zsh-syntax-highlighting"
pkgver = "0.8.0"
pkgrel = 0
pkgdesc = "Fish shell like syntax highlighting for Zsh"
license = "BSD-3-Clause"
url = "https://github.com/zsh-users/zsh-syntax-highlighting"
source = f"https://github.com/zsh-users/zsh-syntax-highlighting/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "5981c19ebaab027e356fe1ee5284f7a021b89d4405cc53dc84b476c3aee9cc32"


def install(self):
    self.install_license("COPYING.md")
    self.install_files(
        ".", "usr/share/zsh/plugins", name="zsh-syntax-highlighting"
    )
