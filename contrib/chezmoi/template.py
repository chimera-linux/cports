pkgname = "chezmoi"
pkgver = "2.47.0"
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
sha256 = "1a7fe26f787a5f5b0bcfbba03de0769a1da56608561783d72a1e1bab865e915d"
options = ["!debug"]


def post_install(self):
    self.install_license("LICENSE")

    with self.pushd("completions"):
        self.install_completion("chezmoi-completion.bash", "bash")
        self.install_completion("chezmoi.fish", "fish")
        self.install_completion("chezmoi.zsh", "zsh")
