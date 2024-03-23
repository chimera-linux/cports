pkgname = "lsd"
pkgver = "1.1.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo", "pkgconf"]
makedepends = ["libgit2-devel", "rust-std"]
checkdepends = ["git"]
pkgdesc = "Next gen ls command"
maintainer = "aurelia <git@elia.garden>"
license = "Apache-2.0"
url = "https://github.com/lsd-rs/lsd"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "4bbd180deeef2674e55724bb4297ee0442bea956e36f9c4cd2fcca4e82bb4026"


def post_install(self):
    self.install_completion(next(self.find("target/", "lsd.bash")), "bash")
    self.install_completion(next(self.find("target/", "_lsd")), "zsh")
    self.install_completion(next(self.find("target/", "lsd.fish")), "fish")
