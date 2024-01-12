pkgname = "chezmoi"
pkgver = "2.44.0"
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
source = f"https://github.com/twpayne/{pkgname}/archive/v{pkgver}.tar.gz"
sha256 = "04aef3ea8cdbb01dea55fbd1292f9269d791b13774d7b75749a3e4cd505914bd"
options = ["!debug"]


def post_install(self):
    self.install_license("LICENSE")

    with self.pushd("completions"):
        self.install_completion("chezmoi-completion.bash", "bash")
        self.install_completion("chezmoi.fish", "fish")
        self.install_completion("chezmoi.zsh", "zsh")
