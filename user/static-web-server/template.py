pkgname = "static-web-server"
pkgver = "2.40.1"
pkgrel = 0
build_style = "cargo"
# We patch Cargo.toml and Cargo.lock
prepare_after_patch = True
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["rust-std", "zstd-devel"]
pkgdesc = "Web server for static files serving"
license = "MIT OR Apache-2.0"
url = "https://github.com/static-web-server/static-web-server"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "db6ee202a926452d278c14872083744a67ec31710db5fd71e00e551ee0955eb4"
# generates completions using host binary
options = ["!cross"]


def post_build(self):
    self.do(
        f"target/{self.profile().triplet}/release/static-web-server",
        "generate",
        "generated",
    )


def install(self):
    self.install_bin(
        f"target/{self.profile().triplet}/release/static-web-server"
    )
    self.install_license("LICENSE-MIT")
    with self.pushd("generated/completions"):
        self.install_completion("static-web-server.bash", "bash")
        self.install_completion("static-web-server.fish", "fish")
        self.install_completion("_static-web-server", "zsh")
        self.install_completion("static-web-server.nu", "nushell")
    self.install_man("generated/man/static-web-server.1")
