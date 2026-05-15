pkgname = "rust-bootstrap"
pkgver = "1.94.1"
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
            "4eba2273b053c45c9b07679ff6c396a97502a7b12defe9dbf18f3e99c8dfef1f",
            "29c3a06838003399a819528366f1dbe09231ae995dcfcb4ab0378a3367337d2e",
        ]
    case "loongarch64":
        sha256 = [
            "a7526f0908555b48796a1b5362c71d12e1099b30ed96fb25e6432ee62d62519a",
            "cd3da285b605010b6acefea8debbe6a39ab3c8067a0475f7c0d46fcc92fb26ae",
        ]
    case "ppc64le":
        sha256 = [
            "6bf285265729f4bed996614ac528ada4da7a97fc56cce219b50406edd8b9bbc1",
            "bae9c744366cf74a3ebdcc8ee6a4435bd9731ae78ccba6c1c339381c973a7d5d",
        ]
    case "ppc64":
        sha256 = [
            "4594921821fbb8fbb882b771c857a34ed9958786ddc41d44ac9f6b448e5033fa",
            "b8b09d6c94355674aa25ee7326af88f66400509a46be233f6323b13968d84e96",
        ]
    case "ppc":
        sha256 = [
            "e7608902dd1ebb56bfa520274970a6ea145e58d9ed3950c61eb3bd4ac050139f",
            "2a1ece44bb0bf133f7b636f138e3611b9636aa516af327a32028b0b02cedac78",
        ]
    case "riscv64":
        sha256 = [
            "18da00479f89fd19a31416ac54e8dcdbbecdd90663bb4b433e08c4e0a5b76e41",
            "261bf4c5f48cb945feb4699a030001424c75239dcfaddb3c3a5b7d8acb8f18a8",
        ]
    case "x86_64":
        sha256 = [
            "45b0b6a05839f8a37dee99d7b5b414deca153c31ed4cc0a85713f58baa3cb0c1",
            "e53829f1291417192b3c7655ff5c7bc1fcd28e72e6bd503c955e7a6c0da8846e",
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
    # whatever
    self.uninstall("usr/etc")
    # licenses
    self.install_license(f"rustc-{pkgver}-{self.profile().triplet}/LICENSE-MIT")
