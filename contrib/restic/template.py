pkgname = "restic"
pkgver = "0.16.2"
pkgrel = 0
build_style = "go"
make_build_args = ["./cmd/restic"]
hostmakedepends = ["go"]
pkgdesc = "Backup solution written in Go"
maintainer = "triallax <triallax@tutanota.com>"
license = "BSD-2-Clause"
url = "https://restic.net"
source = f"https://github.com/restic/restic/releases/download/v{pkgver}/restic-{pkgver}.tar.gz"
sha256 = "88165b5b89b6064df37a9964d660f40ac62db51d6536e459db9aaea6f2b2fc11"
options = ["!debug"]


def post_install(self):
    self.install_license("LICENSE")
    self.install_man("doc/man/*.1", glob=True)

    self.install_completion("doc/zsh-completion.zsh", "zsh")
    self.install_completion("doc/bash-completion.sh", "bash")
    self.install_completion("doc/fish-completion.fish", "fish")
