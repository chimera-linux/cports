pkgname = "llvm-clang-mingw-w64"
pkgver = "23.1.6"
_llvmver = pkgver[0:2]
pkgrel = 1
build_style = "meta"
depends = [f"llvm{_llvmver}-clang-mingw-w64"]
renames = ["clang-mingw-w64"]
pkgdesc = "Clang metapackage for Windows development"
license = "custom:meta"
url = "https://chimera-linux.org"

_targets = ["x86_64", "i686", "armv7", "aarch64"]


def install(self):
    for an in _targets:
        at = an + "-w64-mingw32"
        # convenient cross symlinks
        self.install_dir("usr/bin")
        for binf in [
            "clang",
            "clang++",
            "clang-cpp",
            "cc",
            "c++",
            "ld",
            "ld.lld",
        ]:
            self.install_link(f"usr/bin/{at}-{binf}", f"{at}-{binf}-{_llvmver}")
        # ccache cross symlinks
        self.install_dir("usr/lib/ccache/bin")
        self.install_link(
            f"usr/lib/ccache/bin/{at}-clang", "../../../bin/ccache"
        )
        self.install_link(
            f"usr/lib/ccache/bin/{at}-clang++", "../../../bin/ccache"
        )
        self.install_link(f"usr/lib/ccache/bin/{at}-cc", "../../../bin/ccache")
        self.install_link(f"usr/lib/ccache/bin/{at}-c++", "../../../bin/ccache")


def _gen(an):
    at = an + "-w64-mingw32"

    @subpackage(f"llvm-clang-mingw-w64-{an}")
    def _(self):
        self.subdesc = f"{an} support"
        self.depends = [f"llvm{_llvmver}-clang-mingw-w64-{an}"]
        self.renames = [f"clang-mingw-w64-{an}"]
        self.options = ["brokenlinks"]

        return [
            f"usr/bin/{at}-*",
            f"usr/lib/ccache/bin/{at}-*",
        ]

    depends.append(self.with_pkgver(f"llvm-clang-mingw-w64-{an}"))


for _an in _targets:
    _gen(_an)
