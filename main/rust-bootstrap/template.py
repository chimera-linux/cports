pkgname = "rust-bootstrap"
pkgver = "1.78.0"
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
            "b5fd51dc2805651031d20184cbbd25bb9adcc52007541436c00a0106bcdef5ff",
            "5b847a8e188663865637565285423eed074ed7fc46713eecfc1a34fe32fd0d7d",
        ]
    case "ppc64le":
        sha256 = [
            "ff4bd8bc445ed623858c68f11ed1d00955d9c78ddf386d42bcc5edf7fb8d27ec",
            "13fe38b4b2da39765714b86326b5a824c19508341a3731bae1eceb236c1ef7f4",
        ]
    case "ppc64":
        sha256 = [
            "7d1685640f483cd5cfd5f16ddde9e92d636d94aea18e44f359a88bcba0d42215",
            "4925417c203970487f7f667fbe11b87716600b48c3c29973862ddf70e5711e17",
        ]
    case "riscv64":
        sha256 = [
            "73200d28375909a190d72e38bd40664769497e95b25ae8c5051e81919fb173ef",
            "d90b6f06fafa43cb81c9fce405f6485043ef182ca11658637c7e869de8d7f200",
        ]
    case "x86_64":
        sha256 = [
            "da4899d11761fb78f31f1efacbb0ea3aa04616b8b4ec26c2ab1e0e89c2b9668a",
            "73c5d860f32a5b8db5fd730c4e6ca2b28c44300d958a49fd2890c982424a4181",
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
