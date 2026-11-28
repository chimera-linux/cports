pkgname = "rust-bootstrap"
pkgver = "1.99.1"
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
    f"{_urlb}/rustc-{pkgver}-{self.profile.triplet}.tar.xz",
    f"{_urlb}/rust-std-{pkgver}-{self.profile.triplet}.tar.xz",
]
options = ["!strip"]

match self.profile.arch:
    case "aarch64":
        sha256 = [
            "b38e69fc5b25b09501028cb8365e6361c21370472a3c230c40c6afdcb3eca968",
            "50d02b0c8182d88e044bff8aa451cf7329882be3eb0074949d33505b905a8a7f",
        ]
    case "loongarch64":
        sha256 = [
            "5c04df57c150d2aa05879efd79e79ee8d7f38540c0f5ccf305a6e9be8c1c8294",
            "eb4f60ca64521d26a483fb579659908dfaf858f994d6ee20036c148635bfc4bc",
        ]
    case "ppc64le":
        sha256 = [
            "61c7478abdf25df61b5d876bef8573b1ccb4230b047aae46db7fe37a3ffc0473",
            "9bb5a50c035de0d1e33e86b9df61d167babb229cec826dfbf4ba135603bbad39",
        ]
    case "riscv64":
        sha256 = [
            "e62ce3e3a5705f13c33b97d3aeb235d882139f3691b0e2ecbaeae960f79bacf2",
            "647d645862c7419e1c7ad7f5859399283ed780e8445408003f302cd88bf2c61f",
        ]
    case "x86_64":
        sha256 = [
            "b150f90e1775e51bd1f5713850aef659f925261f23b3bc2f660847a3f122de46",
            "dc42b456bfbf84330b7de5fadb893ffd346a57a8b6d2fb1e5254a257d408e99c",
        ]
    case _:
        broken = f"not yet built for {self.profile.arch}"


def install(self):
    for d in self.cwd.iterdir():
        self.do(
            self.chroot_cwd / d.name / "install.sh",
            "--prefix=/usr",
            f"--destdir={self.chroot_destdir}",
            wrksrc=d.name,
        )
    # remove rust copies of llvm tools
    trip = self.profile.triplet
    self.uninstall(f"usr/lib/rustlib/{trip}/bin")
    # whatever
    self.uninstall("usr/etc")
    # licenses
    self.install_license(f"rustc-{pkgver}-{self.profile.triplet}/LICENSE-MIT")
