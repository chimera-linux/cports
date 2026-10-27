pkgname = "mingw-w64-pkg-config"
pkgver = "1.0.0"
pkgrel = 0
depends = ["cmd:pkg-config!pkgconf"]
pkgdesc = "Support pkg-config script for Windows development"
license = "Zlib"
url = "http://pkg-config.freedesktop.org"

source = [
    "!https://github.com/Martchus/PKGBUILDs/raw/a7036fac2108701dab2afa277d5d8eade63b708c/pkg-config/mingw-w64/mingw-pkgconfig.sh",
]
sha256 = [
    "44d34883ea310396b88e25a1b20f0bb9c96d0ba4bf2501690ebfd4f8a31dc34b",
]

# TODO implement proper conditional patching of mingw-pkgconfig.sh for arbitrary arch target. kinda like in arch PKGBUILD: @TRIPLE@ in the source file is substituted for a given architecture target
# _targets = ["x86_64", "i686", "aarch64", "armv7"]
_targets = ["x86_64"]


def post_patch(self):
    self.cp(self.files_path / "configure.sh", self.cwd)
    (self.cwd / "configure.sh").chmod(0o755)
    self.cp(self.sources_path / "mingw-pkgconfig.sh", self.cwd)


def configure(self):
    for an in _targets:
        at = an + "-w64-mingw32"
        self.do("./configure.sh", f"{at}")


def install(self):
    for an in _targets:
        at = an + "-w64-mingw32"
        self.install_bin(
            self.cwd / "mingw-pkgconfig.sh",
            name=f"{at}-pkg-config",
        )
