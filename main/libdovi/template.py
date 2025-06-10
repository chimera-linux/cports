pkgname = "libdovi"
pkgver = "3.3.2"
pkgrel = 0
build_style = "cargo"
hostmakedepends = [
    "cargo-auditable",
    "cargo-c",
    "pkgconf",
]
makedepends = ["rust-std"]
pkgdesc = "Library to read & write Dolby Vision metadata"
license = "MIT"
url = "https://github.com/quietvoid/dovi_tool"
source = f"{url}/archive/refs/tags/libdovi-{pkgver}.tar.gz"
sha256 = "8ccb1922d7dbb57bc4f2c15c10b90c462f7a5f292efe317c116db923728dd3f1"
# literally one test lol
options = ["!check"]


def prepare(self):
    self.cargo.vendor(args=["--manifest-path", "dolby_vision/Cargo.toml"])


def build(self):
    self.cargo.cbuild(args=["--manifest-path", "dolby_vision/Cargo.toml"])


def check(self):
    self.cargo.check(args=["--manifest-path", "dolby_vision/Cargo.toml"])


def install(self):
    self.cargo.cinstall(wrksrc="dolby_vision")
    self.install_license("LICENSE")


@subpackage("libdovi-devel")
def _(self):
    return self.default_devel()
