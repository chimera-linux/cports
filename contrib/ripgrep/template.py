pkgname = "ripgrep"
pkgver = "13.0.0"
pkgrel = 1
build_style = "cargo"
hostmakedepends = ["cargo", "asciidoc"]
makedepends = ["rust-std"]
pkgdesc = (
    "Tool that recursively searches the current directory for a regex pattern"
)
maintainer = "Wesley Moore <wes@wezm.net>"
license = "MIT OR Unlicense"
url = "https://github.com/BurntSushi/ripgrep"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "0fb17aaf285b3eee8ddab17b833af1e190d73de317ff9648751ab0660d763ed2"


def do_prepare(self):
    # we patch the lockfile so vendor after patch
    pass


def post_patch(self):
    from cbuild.util import cargo

    self.cargo.vendor()
    cargo.setup_vendor(self)


def post_install(self):
    self.install_license("LICENSE-MIT")
    self.install_man(next(self.find("target/", "rg.1")))
    self.install_completion(next(self.find("target/", "rg.bash")), "bash", "rg")
    self.install_completion(next(self.find("target/", "rg.fish")), "fish", "rg")
    self.install_completion("complete/_rg", "zsh", "rg")
