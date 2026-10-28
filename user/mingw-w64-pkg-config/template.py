pkgname = "mingw-w64-pkg-config"
pkgver = "0.1"
pkgrel = 0
depends = []
pkgdesc = "Pkgconf tool wrapper for Windows development"
license = "Zlib"
url = "http://pkg-config.freedesktop.org"

source = [
    "!https://github.com/Martchus/PKGBUILDs/raw/a7036fac2108701dab2afa277d5d8eade63b708c/pkg-config/mingw-w64/mingw-pkgconfig.sh",
]
sha256 = [
    "44d34883ea310396b88e25a1b20f0bb9c96d0ba4bf2501690ebfd4f8a31dc34b",
]
options = ["empty"]
_targets = ["x86_64", "i686", "aarch64", "armv7"]


def post_patch(self):
    self.cp(self.files_path / "set_target_arch.sh", self.cwd)
    (self.cwd / "set_target_arch.sh").chmod(0o755)
    self.cp(self.sources_path / "mingw-pkgconfig.sh", self.cwd)


def build(self):
    for an in _targets:
        at = an + "-w64-mingw32"
        self.do("./set_target_arch.sh", f"{at}")


def install(self):
    for an in _targets:
        at = an + "-w64-mingw32"
        self.install_bin("mingw-pkgconfig.sh", name=f"{at}-pkg-config")


def _gen(an):
    at = an + "-w64-mingw32"

    @subpackage(f"mingw-w64-pkg-config-{an}")
    def _(self):
        self.subdesc = f"{an} support"
        # target specific LIBDIR should be present otherwise why would you even need this wrapper
        self.depends = ["cmd:pkg-config!pkgconf", f"mingw-w64-crt-{an}"]
        return [f"usr/bin/{at}-pkg-config"]

    depends.append(self.with_pkgver(f"mingw-w64-pkg-config-{an}"))


for _an in _targets:
    _gen(_an)
