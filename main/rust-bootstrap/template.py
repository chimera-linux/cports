pkgname = "rust-bootstrap"
pkgver = "1.88.0"
pkgrel = 0
# satisfy revdeps
makedepends = ["zlib-ng-compat", "ncurses-libs", "zstd"]
# overlapping files
depends = ["!rust"]
pkgdesc = "Rust programming language bootstrap toolchain"
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
            "b4d100f5cdf86f9fd6571b9cec7df7358b8886da76f4a4fbce2fa7ec418776ab",
            "8177b2cb1ff75a882cba27ce9edead78b907696ac0c602d93d7484cc34f10f5b",
        ]
    case "loongarch64":
        sha256 = [
            "ea416c46066562f3d2558e8bcb8104a6ebc8829583f5af9f5de940d2d88be6d8",
            "b157fd911fcd8b24eadfe6ecbecdde17eda9776e67fcec34b44179eefc08df6a",
        ]
    case "ppc64le":
        sha256 = [
            "8cdfd3e4cc8510cb09cbd013373f26af0a5ca22c6690ff26072dcc90144027fd",
            "c4a8aa092b0dced816779cf3eceb0a41f9590d657a70c442c722418a4abaf966",
        ]
    case "ppc64":
        sha256 = [
            "8d592d9aaef29ca141f08a19ac759bef437df97180314f5c20ac7afb48ac7ed9",
            "4dc20d21a64d8e58a241e133bdd4b842f3ec8af3267440ddeb34c1c0f563325e",
        ]
    case "ppc":
        sha256 = [
            "b7ac9ddbbd809da7cfa0c23dae4a14806bc4f62349c81f143ace2473d89f8e3b",
            "12dd0563682a72b336964f4fb2793ffbb5bd71f4809cdced44be1b5a7bc973b1",
        ]
    case "riscv64":
        sha256 = [
            "9fa7bb602f4a9bd30702059936487338040b1a5319d3d3efbe7925eab5b19437",
            "dcb0bf6ddb3d82142933e10ffd106e585ccda908638836d36feda5c592cd052d",
        ]
    case "x86_64":
        sha256 = [
            "c6e5815140ae9328307ad87dd35da41e2f053bb2d446b421a3fd1731581d71f7",
            "f0b663f73c32d625028d41bfb61e24b7ccf56d3bc2816aaa88bc34dd46f9f3b4",
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
    self.uninstall(f"usr/lib/rustlib/{trip}/bin")
    # licenses
    self.install_license(f"rustc-{pkgver}-{self.profile().triplet}/LICENSE-MIT")
