pkgname = "chezmoi"
pkgver = "2.52.0"
pkgrel = 1
build_style = "go"
make_build_args = [
    f"-ldflags=-X main.version={pkgver} -X 'main.builtBy=Chimera Linux'",
]
hostmakedepends = ["go"]
checkdepends = ["gmake"]
go_build_tags = ["noembeddocs", "noupgrade"]
pkgdesc = "Dotfiles manager"
maintainer = "triallax <triallax@tutanota.com>"
license = "MIT"
url = "https://chezmoi.io"
source = f"https://github.com/twpayne/chezmoi/archive/v{pkgver}.tar.gz"
sha256 = "dd0a739825a0d194fec3bedced5969ad02880f72abb00e6ea834f250fe4eda09"


def do_check(self):
    from cbuild.util import golang

    self.do("gmake", "test", env=golang.get_go_env(self))


def post_install(self):
    self.install_license("LICENSE")

    with self.pushd("completions"):
        self.install_completion("chezmoi-completion.bash", "bash")
        self.install_completion("chezmoi.fish", "fish")
        self.install_completion("chezmoi.zsh", "zsh")
