pkgname = "rust-bootstrap"
pkgver = "1.98.0"
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
            "1f8421c308388d303df934466052b29c432642360b6303fd2eee998a39ad942b",
            "df657f16571fd1367922de2400c5074cc46ceb374fea344f1d9f17e825de2762",
        ]
    case "loongarch64":
        sha256 = [
            "071a31f0a473e0ccb2a91255cc813f0534c7b6d0cb5882e4dea1280f43152b71",
            "1982f620d0e0d891ad81e795e8077fd2ddbaa44f2b22ec3077a0666cca58c68e",
        ]
    case "ppc64le":
        sha256 = [
            "298c058b440deca0280652f26279c8c2d0d4b1fd30cf9c8e9a909e473e85acf0",
            "51a88e3ed800672bbcd0747ee51fbecf351bc3691658e06cf648defd1317f6ea",
        ]
    case "riscv64":
        sha256 = [
            "77d56de5b7044b1769a0481c1dc6da4e5f08aabaea56b846aec6951bcbbf3c1d",
            "9c58f305e1f48ba166a418bb14644edf23a34557375c33732036384ecea30ae3",
        ]
    case "x86_64":
        sha256 = [
            "46ef59712cd92db8dde26fe5b6128227bc052b78bcf1f4f428e3022d225812f2",
            "9f2670e49ad55a589dd295e5f1b2c2009e3477b633fd147f421876137dd48c5d",
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
