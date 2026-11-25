pkgname = "llvm-clang-cross"
pkgver = "23.1.6"
_llvmver = pkgver[0:2]
pkgrel = 0
build_style = "meta"
depends = [f"llvm{_llvmver}-clang-cross"]
renames = ["base-cross"]
pkgdesc = "Clang metapackage for cross-compiling"
license = "custom:meta"
url = "https://chimera-linux.org"
options = ["!cross"]

_targetlist = [
    "aarch64",
    "armhf",
    "armv7",
    "ppc64le",
    "ppc64",
    "ppc",
    "x86_64",
    "riscv64",
    "loongarch64",
]
_targets = list(filter(lambda p: p != self.profile.arch, _targetlist))


def install(self):
    for an in _targets:
        with self.use_profile(an) as pf:
            at = pf.triplet
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
    cond = an in _targets

    @split(an, cond)
    def _(self):
        self.subdesc = f"{an} support"
        self.depends = [f"llvm{_llvmver}-clang-cross-{an}"]
        self.renames = [f"base-cross-{an}"]
        self.options = ["brokenlinks"]

        with self.rparent.use_profile(an) as pf:
            return [
                f"usr/bin/{pf.triplet}-*",
                f"usr/lib/ccache/bin/{pf.triplet}-*",
            ]

    if an in _targets:
        depends.append(self.with_pkgver(f"llvm-clang-cross-{an}"))


for _an in _targetlist:
    _gen(_an)
