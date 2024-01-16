pkgname = "chezmoi"
pkgver = "2.45.0"
pkgrel = 0
build_style = "go"
make_build_args = [
    f"-ldflags=-X main.version={pkgver} -X main.commit=v{pkgver}",
]
hostmakedepends = ["go"]
go_build_tags = ["noembeddocs", "noupgrade"]
pkgdesc = "Manage your dotfiles across multiple machines, securely"
maintainer = "triallax <triallax@tutanota.com>"
license = "MIT"
url = "https://chezmoi.io"
source = f"https://github.com/twpayne/chezmoi/archive/v{pkgver}.tar.gz"
sha256 = "4f105472a0b419c1f9bf15dc3ecc2009d98be113c87c257cf0710ce97edea714"
options = ["!debug"]


def post_install(self):
    self.install_license("LICENSE")

    with self.pushd("completions"):
        self.install_completion("chezmoi-completion.bash", "bash")
        self.install_completion("chezmoi.fish", "fish")
        self.install_completion("chezmoi.zsh", "zsh")
