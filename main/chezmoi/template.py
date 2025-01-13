pkgname = "chezmoi"
pkgver = "2.58.0"
pkgrel = 0
build_style = "go"
make_build_args = [
    f"-ldflags=-X main.version={pkgver} -X 'main.builtBy=Chimera Linux'",
]
hostmakedepends = ["go"]
checkdepends = ["gnupg"]
go_build_tags = ["noembeddocs", "noupgrade"]
pkgdesc = "Dotfiles manager"
maintainer = "triallax <triallax@tutanota.com>"
license = "MIT"
url = "https://chezmoi.io"
source = f"https://github.com/twpayne/chezmoi/archive/v{pkgver}.tar.gz"
sha256 = "50ac56d7e0624c5b1df2f451fbdec5c46e0e381476e8f2212669840de0d42984"


def check(self):
    from cbuild.util import golang

    self.do("make", "test", env=golang.get_go_env(self))


def post_install(self):
    self.install_license("LICENSE")

    with self.pushd("completions"):
        self.install_completion("chezmoi-completion.bash", "bash")
        self.install_completion("chezmoi.fish", "fish")
        self.install_completion("chezmoi.zsh", "zsh")
