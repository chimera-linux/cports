pkgname = "zsh-syntax-highlighting"
pkgver = "0.8.0"
pkgrel = 0
build_style = "makefile"
pkgdesc = "Syntax highlighting for zsh"
license = "BSD-3-Clause"
url = "https://github.com/zsh-users/zsh-syntax-highlighting"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "5981c19ebaab027e356fe1ee5284f7a021b89d4405cc53dc84b476c3aee9cc32"
# no tests
options = ["!check"]


def install(self):
    self.make.install(
        [
            f"SHARE_DIR={self.chroot_destdir}/usr/share/zsh/plugins/zsh-syntax-highlighting",
            f"DOC_DIR={self.chroot_destdir}/usr/share/zsh/plugins/zsh-syntax-highlighting/doc",
        ]
    )
    self.install_file(
        "zsh-syntax-highlighting.plugin.zsh",
        "usr/share/zsh/plugins/zsh-syntax-highlighting",
    )
    self.install_license("COPYING.md")
