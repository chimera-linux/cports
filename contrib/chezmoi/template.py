pkgname = "chezmoi"
pkgver = "2.47.2"
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
sha256 = "b5289f22341318a2fb4f42cffc7b819ed43ae59e85d40f2daa3f4b2ea070fae3"
# debug: fails to split on powerpc
# check: needs network access
options = ["!debug", "!check"]


def post_install(self):
    self.install_license("LICENSE")

    with self.pushd("completions"):
        self.install_completion("chezmoi-completion.bash", "bash")
        self.install_completion("chezmoi.fish", "fish")
        self.install_completion("chezmoi.zsh", "zsh")
