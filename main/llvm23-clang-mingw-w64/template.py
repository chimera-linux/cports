pkgname = "llvm23-clang-mingw-w64"
pkgver = "23.1.6"
_llvm_majver = pkgver[0:2]
pkgrel = 0
build_style = "meta"
depends = [
    f"llvm{_llvm_majver}-clang-rt-crt-mingw-w64",
    f"llvm{_llvm_majver}-runtimes-mingw-w64",
    "mingw-w64-crt",
    "mingw-w64-headers",
    "mingw-w64-winpthreads",
]
pkgdesc = "Clang metapackage for Windows development - 23.x"
license = "custom:meta"
url = "https://chimera-linux.org"

_targets = ["x86_64", "i686", "armv7", "aarch64"]


def install(self):
    for an in _targets:
        at = an + "-w64-mingw32"
        # convenient cross symlinks
        pfx = f"usr/lib/llvm{_llvm_majver}"
        self.install_dir("usr/bin")
        self.install_dir(f"{pfx}/bin")
        for binf in [
            "clang",
            "clang++",
            "clang-cpp",
            "cc",
            "c++",
            "ld",
            "ld.lld",
        ]:
            self.install_link(f"{pfx}/bin/{at}-{binf}", binf)
            self.install_link(
                f"usr/bin/{at}-{binf}-{_llvm_majver}",
                f"../lib/llvm{_llvm_majver}/bin/{binf}",
            )
        # ccache cross symlinks
        self.install_dir("usr/lib/ccache/bin")
        self.install_link(
            f"usr/lib/ccache/bin/{at}-clang-{_llvm_majver}",
            "../../../bin/ccache",
        )
        self.install_link(
            f"usr/lib/ccache/bin/{at}-clang++-{_llvm_majver}",
            "../../../bin/ccache",
        )
        self.install_link(
            f"usr/lib/ccache/bin/{at}-cc-{_llvm_majver}", "../../../bin/ccache"
        )
        self.install_link(
            f"usr/lib/ccache/bin/{at}-c++-{_llvm_majver}", "../../../bin/ccache"
        )


def _gen(an):
    at = an + "-w64-mingw32"

    @subpackage(f"llvm{_llvm_majver}-clang-mingw-w64-{an}")
    def _(self):
        self.subdesc = f"{an} support"
        self.depends = [
            f"llvm{_llvm_majver}-clang-rt-crt-mingw-w64-{an}",
            f"llvm{_llvm_majver}-runtimes-mingw-w64-{an}",
            f"mingw-w64-crt-{an}",
            f"mingw-w64-headers-{an}",
            f"mingw-w64-winpthreads-{an}",
        ]
        self.options = ["brokenlinks"]

        return [
            f"usr/bin/{at}*",
            f"usr/lib/llvm{_llvm_majver}/bin/{at}*",
            f"usr/lib/ccache/bin/{at}*",
        ]

    depends.append(self.with_pkgver(f"llvm{_llvm_majver}-clang-mingw-w64-{an}"))


for _an in _targets:
    _gen(_an)
