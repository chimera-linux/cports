pkgname = "lsd"
pkgver = "1.1.5"
pkgrel = 3
build_style = "cargo"
prepare_after_patch = True
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["libgit2-devel", "rust-std"]
checkdepends = ["git"]
pkgdesc = "Alternative to ls command"
maintainer = "aurelia <git@elia.garden>"
license = "Apache-2.0"
url = "https://github.com/lsd-rs/lsd"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "120935c7e98f9b64488fde39987154a6a5b2236cb65ae847917012adf5e122d1"


def post_install(self):
    self.install_completion(next(self.find("target/", "lsd.bash")), "bash")
    self.install_completion(next(self.find("target/", "_lsd")), "zsh")
    self.install_completion(next(self.find("target/", "lsd.fish")), "fish")
