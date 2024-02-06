pkgname = "restic"
pkgver = "0.16.4"
pkgrel = 0
build_style = "go"
make_build_args = ["./cmd/restic"]
hostmakedepends = ["go"]
pkgdesc = "Backup solution written in Go"
maintainer = "triallax <triallax@tutanota.com>"
license = "BSD-2-Clause"
url = "https://restic.net"
source = f"https://github.com/restic/restic/releases/download/v{pkgver}/restic-{pkgver}.tar.gz"
sha256 = "d736a57972bb7ee3398cf6b45f30e5455d51266f5305987534b45a4ef505f965"
options = ["!debug"]


def post_install(self):
    self.install_license("LICENSE")
    self.install_man("doc/man/*.1", glob=True)

    self.install_completion("doc/zsh-completion.zsh", "zsh")
    self.install_completion("doc/bash-completion.sh", "bash")
    self.install_completion("doc/fish-completion.fish", "fish")
