pkgname = "restic"
pkgver = "0.17.1"
pkgrel = 1
build_style = "go"
make_build_args = [f"-ldflags=-X main.version=v{pkgver}", "./cmd/restic"]
hostmakedepends = ["go"]
pkgdesc = "Backup tool"
maintainer = "triallax <triallax@tutanota.com>"
license = "BSD-2-Clause"
url = "https://restic.net"
source = f"https://github.com/restic/restic/releases/download/v{pkgver}/restic-{pkgver}.tar.gz"
sha256 = "cba3a5759690d11dae4b5620c44f56be17a5688e32c9856776db8a9a93d6d59a"
# fails in bwrap chroot
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
    self.install_man("doc/man/*.1", glob=True)

    self.install_completion("doc/zsh-completion.zsh", "zsh")
    self.install_completion("doc/bash-completion.sh", "bash")
    self.install_completion("doc/fish-completion.fish", "fish")
