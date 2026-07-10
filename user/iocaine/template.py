pkgname = "iocaine"
pkgver = "3.5.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = [
    "dinit-chimera",
    "gmp-devel",
    "iptables-devel",
    "jansson-devel",
    "libmnl-devel",
    "libnftnl-devel",
    "nftables-devel",
    "rust-std",
    "zstd-devel",
]
pkgdesc = "LLM crawler abuse defense mechanism"
license = "MIT"
url = "https://iocaine.madhouse-project.org"
source = f"https://git.madhouse-project.org/iocaine/iocaine/archive/iocaine-{pkgver}.tar.gz"
sha256 = "d0acb7019238c4b7cb163a999dacbe4919ab0cc1380c1c39e79b6b7e108d6f1b"

if self.profile().wordsize == 32:
    broken = "atomic64"


def install(self):
    self.install_license("LICENSES/MIT.txt")
    self.install_bin(f"target/{self.profile().triplet}/release/iocaine")
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_service(self.files_path / "iocaine")
