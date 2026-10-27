pkgname = "mingw-w64-meson"
pkgver = "1.0.0"
pkgrel = 0
makedepends = ["python", "gmake"]
depends = ["meson", "mingw-w64-pkg-config", "clang-mingw-w64-x86_64"]
pkgdesc = "Meson wrapper for MinGW"
license = "GPL-2.0-or-later"
url = "https://fedoraproject.org/wiki/MinGW"
source = [
    "!https://github.com/Martchus/PKGBUILDs/raw/a7036fac2108701dab2afa277d5d8eade63b708c/meson/mingw-w64-clang-aarch64/toolchain_generator.py",
    "!https://github.com/Martchus/PKGBUILDs/raw/a7036fac2108701dab2afa277d5d8eade63b708c/meson/mingw-w64/meson-mingw-wrapper",
]
sha256 = [
    "d7465adfe25418281620c2abc8f0d7349a884a62b3be44a0bc3742184b5763ce",
    "2defbbb1f43e13815b2a8a8327bd14aad175219eb4ff9935d5bf9d46b9f8728a",
]

# TODO
# _targets = ["x86_64", "i686", "aarch64", "armv7"]
_targets = [
    "x86_64",
]


def pre_patch(self):
    self.cp(
        self.sources_path / "toolchain_generator.py",
        self.cwd,
    )


def post_patch(self):
    self.cp(self.files_path / "configure.sh", self.cwd)
    (self.cwd / "configure.sh").chmod(0o755)
    self.cp(self.sources_path / "meson-mingw-wrapper", self.cwd)


def configure(self):
    for an in _targets:
        at = an + "-w64-mingw32"
        self.do("./configure.sh", f"{at}")


def build(self):
    self.do("make")


def install(self):
    self.install_bin(
        "toolchain_generator.py", name="meson-cross-file-generator"
    )
    self.install_dir("usr/share/mingw")
    for an in _targets:
        at = an + "-w64-mingw32"
        self.install_file(self.cwd / f"toolchain-{at}.meson", "usr/share/mingw")
        self.install_bin(f"{at}-meson")
