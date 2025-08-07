pkgname = "restic"
pkgver = "0.18.0"
pkgrel = 4
build_style = "go"
make_build_args = [f"-ldflags=-X main.version=v{pkgver}", "./cmd/restic"]
hostmakedepends = ["go"]
pkgdesc = "Backup tool"
license = "BSD-2-Clause"
url = "https://restic.net"
source = f"https://github.com/restic/restic/releases/download/v{pkgver}/restic-{pkgver}.tar.gz"
sha256 = "fc068d7fdd80dd6a968b57128d736b8c6147aa23bcba584c925eb73832f6523e"
# fails in bwrap chroot
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
    self.install_man("doc/man/*.1", glob=True)

    self.install_completion("doc/zsh-completion.zsh", "zsh")
    self.install_completion("doc/bash-completion.sh", "bash")
    self.install_completion("doc/fish-completion.fish", "fish")
