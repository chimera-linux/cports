pkgname = "rust-bootstrap"
pkgver = "1.77.2"
pkgrel = 0
# satisfy revdeps
makedepends = ["zlib", "ncurses-libs", "zstd"]
# overlapping files
depends = ["!rust"]
pkgdesc = "Rust programming language bootstrap toolchain"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT OR Apache-2.0"
url = "https://rust-lang.org"
_urlb = "https://repo.chimera-linux.org/distfiles"
source = [
    f"{_urlb}/rustc-{pkgver}-{self.profile().triplet}.tar.xz",
    f"{_urlb}/rust-std-{pkgver}-{self.profile().triplet}.tar.xz",
]
options = ["!strip"]

match self.profile().arch:
    case "aarch64":
        sha256 = [
            "29fe7bf6416b41e668c28ba19e566a4ba08c3973e214e5bfdac7f5bd4dbdec42",
            "347d75f445e8a3c4730e802007d2c7d7cff414f4cd324e1d26da7685777e1bc9",
        ]
    case "ppc64le":
        sha256 = [
            "f946143e49442e3198981e925ea89cd828ea289b5fd49e8ce7431132d65bd7c5",
            "df96de2fd814fa9f7b9388e1f0a020423da7394f358cc7581a33959f7a714951",
        ]
    case "ppc64":
        sha256 = [
            "3f76a9b9233cdb25ce0ddf72dabbe00c99223abea6ab7f23de5ca0abc6b11072",
            "1e2a0f5f0f09329e53a82cd0ade6ff88525adb8243ea494cc237885d203d9bcd",
        ]
    case "riscv64":
        sha256 = [
            "1b20f6554da115f62073db15b7e10430b03ed235ded39cad1fff7c026217f065",
            "ae8b16a484fb10bba943c63771c77204f775ae044197802709a3202492a66b65",
        ]
    case "x86_64":
        sha256 = [
            "d26bdcfceaa741cabd41400f73c739ceb6d20fd99e64005c8330724bec766d27",
            "4a96c947437764448173d4e157c17fa112cfbb805ba51ff10918cff4fdb52868",
        ]
    case _:
        broken = f"not yet built for {self.profile().arch}"


def do_install(self):
    for d in self.cwd.iterdir():
        self.do(
            self.chroot_cwd / d.name / "install.sh",
            "--prefix=/usr",
            f"--destdir={self.chroot_destdir}",
            wrksrc=d.name,
        )
    # remove rust copies of llvm tools
    trip = self.profile().triplet
    for f in (self.destdir / f"usr/lib/rustlib/{trip}/bin").glob("rust-ll*"):
        f.unlink()
    # licenses
    self.install_license(f"rustc-{pkgver}-{self.profile().triplet}/LICENSE-MIT")
