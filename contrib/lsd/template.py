pkgname = "lsd"
pkgver = "1.1.1"
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
sha256 = "7933e196bf7b164ea8879078f8a8e87381e0c49f71867e0036c82916199aba61"


def post_install(self):
    self.install_completion(next(self.find("target/", "lsd.bash")), "bash")
    self.install_completion(next(self.find("target/", "_lsd")), "zsh")
    self.install_completion(next(self.find("target/", "lsd.fish")), "fish")
