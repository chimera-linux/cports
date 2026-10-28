pkgname = "mingw-w64-configure"
pkgver = "0.1"
pkgrel = 0
depends = []
pkgdesc = "GNU Configure script wrapper for Windows development"
license = "GPL-1.0-only"
url = "https://www.mingw-w64.org"

source = [
    "!https://github.com/Martchus/PKGBUILDs/raw/a7036fac2108701dab2afa277d5d8eade63b708c/configure/mingw-w64/mingw-configure.sh"
]
sha256 = ["802c5524bddacd3b4a3f4817a788a293d323a7ea390256ccbd2614274d3d686e"]
options = ["empty"]
_targets = ["x86_64", "i686", "aarch64", "armv7"]


def pre_patch(self):
    self.cp(self.sources_path / "mingw-configure.sh", self.cwd)


def post_patch(self):
    self.cp(self.files_path / "set_target_arch.sh", self.cwd)
    (self.cwd / "set_target_arch.sh").chmod(0o755)


def build(self):
    for an in _targets:
        at = an + "-w64-mingw32"
        self.do("./set_target_arch.sh", f"{at}")


def install(self):
    for an in _targets:
        at = an + "-w64-mingw32"
        self.install_bin("mingw-configure.sh", name=f"{at}-configure")


def _gen(an):
    at = an + "-w64-mingw32"

    @subpackage(f"mingw-w64-configure-{an}")
    def _(self):
        self.subdesc = f"{an} support"
        # target specific LIBDIR should be present otherwise why would you even need this wrapper
        self.depends = [
            f"clang-mingw-w64-{an}",
            f"mingw-w64-pkg-config-{an}",
            "mingw-w64-environment",
        ]
        return [f"usr/bin/{at}-configure"]

    depends.append(self.with_pkgver(f"mingw-w64-configure-{an}"))


for _an in _targets:
    _gen(_an)
