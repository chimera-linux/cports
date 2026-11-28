pkgname = "iocaine"
pkgver = "3.6.0"
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
sha256 = "854eff515b4666d7a92c4cd79c1bef88f6224bf11f773b0af83ceed33dda0b64"

if self.profile.wordsize == 32:
    broken = "atomic64"


def install(self):
    from cbuild.util import cargo

    self.install_license("LICENSES/MIT.txt")
    self.install_bin(cargo.target_path(self, "iocaine"))
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_service(self.files_path / "iocaine")
