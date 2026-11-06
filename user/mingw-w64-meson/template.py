pkgname = "mingw-w64-meson"
pkgver = "0.1"
pkgrel = 1
makedepends = [
    "gmake",
    "python",
]
depends = []
pkgdesc = "Meson wrapper for Windows development"
license = "GPL-2.0-or-later"
url = "https://www.mingw-w64.org"
source = [
    "!https://github.com/Martchus/PKGBUILDs/raw/a7036fac2108701dab2afa277d5d8eade63b708c/meson/mingw-w64-clang-aarch64/toolchain_generator.py",
    "!https://github.com/Martchus/PKGBUILDs/raw/a7036fac2108701dab2afa277d5d8eade63b708c/meson/mingw-w64/meson-mingw-wrapper",
]
sha256 = [
    "d7465adfe25418281620c2abc8f0d7349a884a62b3be44a0bc3742184b5763ce",
    "2defbbb1f43e13815b2a8a8327bd14aad175219eb4ff9935d5bf9d46b9f8728a",
]
options = ["empty"]

_targets = ["x86_64", "i686", "aarch64", "armv7"]


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
    for an in _targets:
        at = an + "-w64-mingw32"
        # in order to be able to pass linker flags to clang when cross compiling the fuse-ld has to be specified directly
        # see: https://github.com/mstorsjo/llvm-mingw/issues/379#issuecomment-1798016620
        _cross_clang_flags = f"-fuse-ld=lld -target {at}"
        self.do(
            "make",
            f"toolchain-{at}.meson",
            env={
                "CFLAGS": _cross_clang_flags,
                "CXXFLAGS": _cross_clang_flags,
                "LDFLAGS": "",
            },
        )


def install(self):
    self.install_bin("toolchain_generator.py", name="meson-cross-file-gen")
    self.install_dir("usr/share/mingw")
    for an in _targets:
        at = an + "-w64-mingw32"
        self.install_file(f"toolchain-{at}.meson", "usr/share/mingw")
        self.install_bin(f"{at}-meson")


@subpackage("mingw-w64-meson-toolchain-generator")
def _(self):
    self.depends = ["python"]
    self.subdesc = "Meson toolchain file generator script"

    return ["usr/bin/meson-cross-file-gen"]


def _gen(an):
    at = an + "-w64-mingw32"

    @subpackage(f"mingw-w64-meson-{an}")
    def _(self):
        self.subdesc = f"{an} support"
        self.depends = [
            "meson",
            f"clang-mingw-w64-{an}",
            f"mingw-w64-pkg-config-{an}",
        ]
        return [
            f"usr/share/mingw/toolchain-{at}.meson",
            f"usr/bin/{at}-meson",
        ]

    depends.append(self.with_pkgver(f"mingw-w64-meson-{an}"))


for _an in _targets:
    _gen(_an)
