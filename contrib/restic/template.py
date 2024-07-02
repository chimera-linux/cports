pkgname = "restic"
pkgver = "0.16.5"
pkgrel = 1
build_style = "go"
make_build_args = [f"-ldflags=-X main.version=v{pkgver}", "./cmd/restic"]
hostmakedepends = ["go"]
pkgdesc = "Backup tool"
maintainer = "triallax <triallax@tutanota.com>"
license = "BSD-2-Clause"
url = "https://restic.net"
source = f"https://github.com/restic/restic/releases/download/v{pkgver}/restic-{pkgver}.tar.gz"
sha256 = "2e8a57f0d1d2b90d67253d1287159dc467bdb7f3b385be2db39e7213b44672be"
# debug: fails to split on powerpc
# check: fails in bwrap chroot
options = ["!debug", "!check"]


def post_install(self):
    self.install_license("LICENSE")
    self.install_man("doc/man/*.1", glob=True)

    self.install_completion("doc/zsh-completion.zsh", "zsh")
    self.install_completion("doc/bash-completion.sh", "bash")
    self.install_completion("doc/fish-completion.fish", "fish")
