pkgname = "bat"
pkgver = "0.23.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo", "pkgconf"]
makedepends = [
    "rust-std",
    "oniguruma-devel",
    "libgit2-devel",
    "zlib-devel",
]
checkdepends = ["bash"]
pkgdesc = "Cat clone with wings"
maintainer = "aurelia <git@elia.garden>"
license = "MIT OR Apache-2.0"
url = "https://github.com/sharkdp/bat"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "30b6256bea0143caebd08256e0a605280afbbc5eef7ce692f84621eb232a9b31"


def do_prepare(self):
    # Since we update libgit2 via patch, we do not want to vendor yet
    pass


def post_patch(self):
    from cbuild.util import cargo

    self.cargo.vendor()
    cargo.setup_vendor(self)


def post_install(self):
    self.install_man(next(self.find("target/", "bat.1")))
    self.install_license("LICENSE-MIT")
    self.install_completion(next(self.find("target/", "bat.bash")), "bash")
    self.install_completion(next(self.find("target/", "bat.zsh")), "zsh")
    self.install_completion(next(self.find("target/", "bat.fish")), "fish")
