pkgname = "rust-bootstrap"
pkgver = "1.81.0"
pkgrel = 0
# satisfy revdeps
makedepends = ["zlib-ng-compat", "ncurses-libs", "zstd"]
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
            "1049cc9db0895949c01df8bf2b44ced311d6c5d2f218b543f5d261ec4b61af91",
            "ae3bfc27b76616ab890fc80b8fe91db21954ac5d211abff433f24458ddbe8d2d",
        ]
    case "ppc64le":
        sha256 = [
            "2c9233a72ee828d2b51990143f3794a45cf6421a1cd80d227794ddbe5c5e0e1e",
            "cb56e314ba4e51d0fe3e07f5a5f409e4bb9aa01d8fdc5199694da872a0ba6b7b",
        ]
    case "ppc64":
        sha256 = [
            "c76fc940ac590a990b816732d961a9bd09af2eb7e6354b234942af2f5a950c1c",
            "35c0ec8348533a2be56bade3ea5232dd56603638be3a3499435341b34322a72c",
        ]
    case "riscv64":
        sha256 = [
            "462438bb07d89ea155de71931cf3f15d87191a57e3ecfce7abceffda354fce8a",
            "81619a8faf9d5e61c279839e1b9b8eb0de54c099a379c10967e70dc62e11b4ed",
        ]
    case "x86_64":
        sha256 = [
            "b240882540a7ed0dc63f435fd75dda7ad5239fb9862d4bef4587bc0f518ccfe0",
            "2304dbb63ed9d6ace3a715794d43c8588be3c988c7eff36143488ad09ebefd35",
        ]
    case _:
        broken = f"not yet built for {self.profile().arch}"


def install(self):
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
