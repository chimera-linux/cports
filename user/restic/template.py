pkgname = "restic"
pkgver = "0.18.1"
pkgrel = 3
build_style = "go"
make_build_args = [f"-ldflags=-X main.version=v{pkgver}", "./cmd/restic"]
hostmakedepends = ["go"]
pkgdesc = "Backup tool"
license = "BSD-2-Clause"
url = "https://restic.net"
source = f"https://github.com/restic/restic/releases/download/v{pkgver}/restic-{pkgver}.tar.gz"
sha256 = "4b8e2b6cb20e9707e14b9b9d92ddb6f2e913523754e1f123e2e6f3321e67f7ca"
# fails in bwrap chroot
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
    self.install_man("doc/man/*.1", glob=True)

    self.install_completion("doc/zsh-completion.zsh", "zsh")
    self.install_completion("doc/bash-completion.sh", "bash")
    self.install_completion("doc/fish-completion.fish", "fish")
