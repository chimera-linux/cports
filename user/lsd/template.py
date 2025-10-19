pkgname = "lsd"
pkgver = "1.2.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["libgit2-devel", "rust-std"]
checkdepends = ["git"]
pkgdesc = "Alternative to ls command"
license = "Apache-2.0"
url = "https://github.com/lsd-rs/lsd"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "dae8d43087686a4a1de0584922608e9cbab00727d0f72e4aa487860a9cbfeefa"


def pre_prepare(self):
    # the version that is in there is busted on loongarch
    self.do(
        "cargo",
        "update",
        "--package",
        "libc",
        "--precise",
        "0.2.170",
        allow_network=True,
    )


def post_install(self):
    self.install_completion(next(self.find("target/", "lsd.bash")), "bash")
    self.install_completion(next(self.find("target/", "_lsd")), "zsh")
    self.install_completion(next(self.find("target/", "lsd.fish")), "fish")
