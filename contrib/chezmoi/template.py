pkgname = "chezmoi"
pkgver = "2.48.0"
pkgrel = 1
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
sha256 = "3034a37ddc21fd19e9a37297dd98a6edbf85e68f112cafef721d2512fbac13e5"
# debug: fails to split on powerpc
# check: needs network access
options = ["!debug", "!check"]


def post_install(self):
    self.install_license("LICENSE")

    with self.pushd("completions"):
        self.install_completion("chezmoi-completion.bash", "bash")
        self.install_completion("chezmoi.fish", "fish")
        self.install_completion("chezmoi.zsh", "zsh")
