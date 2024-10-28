pkgname = "restic"
pkgver = "0.17.2"
pkgrel = 0
build_style = "go"
make_build_args = [f"-ldflags=-X main.version=v{pkgver}", "./cmd/restic"]
hostmakedepends = ["go"]
pkgdesc = "Backup tool"
maintainer = "triallax <triallax@tutanota.com>"
license = "BSD-2-Clause"
url = "https://restic.net"
source = f"https://github.com/restic/restic/releases/download/v{pkgver}/restic-{pkgver}.tar.gz"
sha256 = "ac52843c40bc9b520bb8dbbbaeda6afec7a35c59753b8cbf11348dd734896ed1"
# fails in bwrap chroot
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
    self.install_man("doc/man/*.1", glob=True)

    self.install_completion("doc/zsh-completion.zsh", "zsh")
    self.install_completion("doc/bash-completion.sh", "bash")
    self.install_completion("doc/fish-completion.fish", "fish")
