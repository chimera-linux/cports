pkgname = "vaultwarden"
pkgver = "1.34.1"
_webver = "2025.6.0"
pkgrel = 0
build_style = "cargo"
make_build_args = [
    "--no-default-features",
    "--features=sqlite,postgresql",
]
make_check_args = [*make_build_args]
hostmakedepends = [
    "cargo-auditable",
    "pkgconf",
]
makedepends = [
    "openssl3-devel",
    "postgresql16-client-devel",
    "rust-std",
    "sqlite-devel",
]
pkgdesc = "Bitwarden compatible server"
license = "AGPL-3.0-or-later"
url = "https://github.com/dani-garcia/vaultwarden"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "c416ab8e563357823b11192bda46d78aae5457bdec8a6051e765d5897c98321a"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/vaultwarden")
    self.install_license("LICENSE.txt")
    self.install_file(".env.template", "etc/default", name="vaultwarden")
    self.install_service("^/vaultwarden")
    self.install_tmpfiles("^/tmpfiles.conf")
    self.install_sysusers("^/sysusers.conf")
