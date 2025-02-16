pkgname = "static-web-server"
pkgver = "2.36.0"
pkgrel = 0
build_style = "cargo"
# We patch Cargo.toml and Cargo.lock
prepare_after_patch = True
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["zstd-devel", "rust-std"]
pkgdesc = "Web server for static files serving"
maintainer = "Jan Christian Grünhage <jan.christian@gruenhage.xyz>"
license = "MIT OR Apache-2.0"
url = "https://github.com/static-web-server/static-web-server"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "bb99fd25835050e9572ea4589f66b94a64d1724712a2f4881ab35f29d1d8f2a9"
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
