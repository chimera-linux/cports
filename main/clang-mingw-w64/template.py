pkgname = "clang-mingw-w64"
pkgver = "0.1"
pkgrel = 1
build_style = "meta"
depends = [
    "clang",
    "clang-rt-builtins-mingw-w64",
    "llvm-runtimes-mingw-w64",
    "mingw-w64-crt",
    "mingw-w64-headers",
    "mingw-w64-winpthreads",
]
pkgdesc = "Metapackage for Windows development"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "custom:meta"
url = "https://chimera-linux.org"

_targets = ["x86_64", "i686", "armv7", "aarch64"]


def install(self):
    self.install_dir("usr/bin")
    self.install_dir("usr/lib/ccache/bin")
    for an in _targets:
        at = an + "-w64-mingw32"
        # convenient cross symlinks
        for prog in [
            "clang",
            "clang++",
            "clang-cpp",
            "cc",
            "c++",
            "ld",
            "ld.lld",
        ]:
            self.install_link(f"usr/bin/{at}-{prog}", prog)
        # ccache cross symlinks
        for prog in ["clang", "clang++", "cc", "c++"]:
            self.install_link(
                f"usr/lib/ccache/bin/{at}-{prog}", "../../../bin/ccache"
            )


def _gen(an):
    at = an + "-w64-mingw32"

    @subpackage(f"clang-mingw-w64-{an}")
    def _(self):
        self.subdesc = f"{an} support"
        self.depends = [
            "clang",
            f"clang-rt-builtins-mingw-w64-{an}",
            f"llvm-runtimes-mingw-w64-{an}",
            f"mingw-w64-crt-{an}",
            f"mingw-w64-headers-{an}",
            f"mingw-w64-winpthreads-{an}",
        ]
        self.options = ["brokenlinks"]

        return [
            f"usr/bin/{at}-*",
            f"usr/lib/ccache/bin/{at}-*",
        ]

    depends.append(self.with_pkgver(f"clang-mingw-w64-{an}"))


for _an in _targets:
    _gen(_an)
