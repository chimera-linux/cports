pkgname = "cargo-bootstrap"
pkgver = "1.59.0"
pkgrel = 0
# satisfy runtime dependencies
hostmakedepends = ["curl"]
depends = ["!cargo"]
pkgdesc = "Bootstrap binaries of Rust package manager"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT OR Apache-2.0"
url = "https://rust-lang.org"
source = f"https://ftp.octaforge.org/chimera/distfiles/cargo-{pkgver}-{self.profile().triplet}.tar.xz"
options = ["!strip"]

match self.profile().arch:
    case "aarch64":
        sha256 = "e5a30356352af17b8a4588e7aad0ba2237666938d62dbfec9d397e8029707e92"
    case "ppc64le":
        sha256 = "f5497ec82de8dd7c66d5583699697d9a940d55e765eedc7c19fe73dfd017dabd"
    case "x86_64":
        sha256 = "e2663267ceb8fa9df9c2c23333c60caadb027f59398c07eef7e94d812415f107"
    case _:
        broken = f"not yet built for {self.profile().arch}"

def do_install(self):
    self.install_bin("cargo")
    self.install_license("LICENSE-APACHE")
    self.install_license("LICENSE-MIT")
    self.install_license("LICENSE-THIRD-PARTY")
