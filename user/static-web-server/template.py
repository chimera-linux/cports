pkgname = "static-web-server"
pkgver = "2.32.2"
pkgrel = 0
build_style = "cargo"
# We patch Cargo.toml and Cargo.lock
prepare_after_patch = True
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["zstd-devel", "libgit2-devel"]
pkgdesc = "Web server for static files serving"
maintainer = "Jan Christian Grünhage <jan.christian@gruenhage.xyz>"
license = "MIT OR Apache-2.0"
url = "https://github.com/static-web-server/static-web-server"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "191a014f2f30fa145fbac727fb930e2a7063f3c27b8e72f33c21a8814969a641"
# generates completions using host binary
options = ["!cross"]


def post_build(self):
    self.do(
        f"target/{self.profile().triplet}/release/static-web-server",
        "generate",
        "generated",
    )


def post_install(self):
    self.install_license("LICENSE-MIT")
    with self.pushd("generated/completions"):
        self.install_completion("static-web-server.bash", "bash")
        self.install_completion("static-web-server.fish", "fish")
        self.install_completion("_static-web-server", "zsh")
        self.install_completion("static-web-server.nu", "nushell")
    self.install_man("generated/man/static-web-server.1")
