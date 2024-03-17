pkgname = "delta"
pkgver = "0.17.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo", "pkgconf"]
makedepends = [
    "libgit2-devel",
    "oniguruma-devel",
    "rust-std",
]
checkdepends = ["git"]
pkgdesc = "Syntax-highlighting pager for git, diff, and grep output"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://github.com/dandavison/delta"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "1abd21587bcc1f2ef0cd342784ce990da9978bc345578e45506419e0952de714"


def do_prepare(self):
    # we patch the lockfile so vendor after patch
    pass


def post_patch(self):
    from cbuild.util import cargo

    self.cargo.vendor()
    cargo.setup_vendor(self)


def post_install(self):
    self.install_license("LICENSE")
    self.install_completion("etc/completion/completion.bash", "bash")
    self.install_completion("etc/completion/completion.fish", "fish")
    self.install_completion("etc/completion/completion.zsh", "zsh")
