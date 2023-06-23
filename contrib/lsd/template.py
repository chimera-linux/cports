pkgname = "lsd"
pkgver = "0.23.1"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo"]
makedepends = ["rust"]
pkgdesc = "Next gen ls command"
maintainer = "aurelia <git@elia.garden>"
license = "Apache-2.0"
url = "https://github.com/lsd-rs/lsd"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "9698919689178cc095f39dcb6a8a41ce32d5a1283e6fe62755e9a861232c307d"


def post_install(self):
    self.install_completion(next(self.find("target/", "lsd.bash")), "bash")
    self.install_completion(next(self.find("target/", "_lsd")), "zsh")
    self.install_completion(next(self.find("target/", "lsd.fish")), "fish")
