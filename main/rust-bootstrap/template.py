pkgname = "rust-bootstrap"
pkgver = "1.66.0"
pkgrel = 0
# satisfy revdeps
makedepends = ["zlib", "ncurses-libs"]
# overlapping files
depends = ["!rust"]
pkgdesc = "Rust programming language bootstrap toolchain"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT OR Apache-2.0"
url = "https://rust-lang.org"
_urlb = "https://repo.chimera-linux.org/distfiles"
source = [
    f"{_urlb}/rustc-{pkgver}-{self.profile().triplet}.tar.xz",
    f"{_urlb}/rust-std-{pkgver}-{self.profile().triplet}.tar.xz"
]
options = ["!strip"]

match self.profile().arch:
    case "aarch64":
        sha256 = [
            "0224bb80495ddb86e77db084c8425e2dd7153d6680709d47666fb41b7dabbbcd",
            "ac33f13bf08f6165cdbade253096a9d8d41b5d56bac2b6b74cce89111721d79f",
        ]
    case "ppc64le":
        sha256 = [
            "7c47dfac7d552c4683ab7cb28975593ca047065cafddc0e3fd97d56e734ac4fc",
            "2d3eb8b9cd99b768199b2a3bcce471a162860f0ca12e8c24efb9d3b61771e8f4",
        ]
    case "riscv64":
        sha256 = [
            "919733032cf83153fefa9771edaf2035ac9048fd2d998e3be2862a16b52c174b",
            "78b0d9db21c0a0118507b142c09e705c2129c1b599a95146d83bc95dd12666c7",
        ]
    case "x86_64":
        sha256 = [
            "069ec95ffca0a7ac671acde54ee34ea83382e7acfa322c1860f67c217017f45b",
            "076ccd4a1bc1a6d261f51d409da1b4247418b4d10502602ec5361125c4ea9704",
        ]
    case _:
        broken = f"not yet built for {self.profile().arch}"

def do_install(self):
    for d in self.cwd.iterdir():
        self.do(
            self.chroot_cwd / d.name / "install.sh", "--prefix=/usr",
            f"--destdir={self.chroot_destdir}",
            wrksrc = d.name
        )
    # remove rust copies of llvm tools
    trip = self.profile().triplet
    for f in (self.destdir / f"usr/lib/rustlib/{trip}/bin").glob("rust-ll*"):
        f.unlink()
