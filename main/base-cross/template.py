pkgname = "base-cross"
pkgver = "0.1"
pkgrel = 4
build_style = "meta"
depends = [
    "clang-rt-cross",
    "fortify-headers",
    "libatomic-chimera-cross",
    "llvm-runtimes-cross",
    "musl-cross",
]
pkgdesc = "Base metapackage for cross-compiling"
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
_targets = list(filter(lambda p: p != self.profile().arch, _targetlist))


def install(self):
    for an in _targets:
        with self.profile(an) as pf:
            at = pf.triplet
        # convenient cross symlinks
        self.install_dir("usr/bin")
        self.install_link(f"usr/bin/{at}-clang", "clang")
        self.install_link(f"usr/bin/{at}-clang++", "clang++")
        self.install_link(f"usr/bin/{at}-clang-cpp", "clang-cpp")
        self.install_link(f"usr/bin/{at}-cc", "cc")
        self.install_link(f"usr/bin/{at}-c++", "c++")
        self.install_link(f"usr/bin/{at}-ld", "ld")
        self.install_link(f"usr/bin/{at}-ld.lld", "ld.lld")
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
        # arch config file
        with open(self.destdir / f"usr/bin/{at}.cfg", "w") as cf:
            cf.write(f"--sysroot /usr/{at}\n")
        # symlink fortify headers
        self.install_dir(f"usr/{at}/usr/include")
        self.install_link(
            f"usr/{at}/usr/include/fortify", "../../../include/fortify"
        )


def _gen(an):
    cond = an in _targets

    @subpackage(f"base-cross-{an}", cond)
    def _(self):
        self.subdesc = f"{an} support"
        self.depends = [
            f"clang-rt-cross-{an}",
            f"musl-cross-{an}",
            f"libatomic-chimera-cross-{an}",
            f"llvm-runtimes-cross-{an}",
        ]
        self.options = ["brokenlinks"]
        with self.rparent.profile(an) as pf:
            return [
                f"usr/bin/{pf.triplet}.cfg",
                f"usr/bin/{pf.triplet}-*",
                f"usr/lib/ccache/bin/{pf.triplet}-*",
                f"usr/{pf.triplet}",
            ]

    if an in _targets:
        depends.append(self.with_pkgver(f"base-cross-{an}"))


for _an in _targetlist:
    _gen(_an)
