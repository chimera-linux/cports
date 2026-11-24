pkgname = "llvm23-clang-cross"
pkgver = "23.1.6"
_llvm_majver = pkgver[0:2]
pkgrel = 0
build_style = "meta"
depends = [
    "fortify-headers",
    "libatomic-chimera-cross",
    f"llvm{_llvm_majver}-clang-rt-cross",
    "llvm-runtimes-cross",
    "musl-cross",
]
pkgdesc = "LLVM cross-toolchain - 23.x"
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
        # arch config file
        with open(self.destdir / f"{pfx}/bin/{at}.cfg", "w") as cf:
            cf.write(f"--sysroot /usr/{at}\n")
        # symlink fortify headers
        self.install_dir(f"usr/{at}/usr/include")
        self.install_link(
            f"usr/{at}/usr/include/fortify", "../../../include/fortify"
        )


def _gen(an):
    cond = an in _targets

    @subpackage(f"llvm{_llvm_majver}-clang-cross-{an}", cond)
    def _(self):
        self.subdesc = f"{an} support"
        self.depends = [
            "fortify-headers",
            f"libatomic-chimera-cross-{an}",
            f"llvm{_llvm_majver}-clang-rt-cross",
            f"llvm-runtimes-cross-{an}",
            f"musl-cross-{an}",
        ]
        self.options = ["brokenlinks"]
        with self.rparent.use_profile(an) as pf:
            return [
                f"usr/bin/{pf.triplet}*",
                f"usr/lib/llvm{_llvm_majver}/bin/{pf.triplet}*",
                f"usr/lib/ccache/bin/{pf.triplet}*",
                f"usr/{pf.triplet}",
            ]

    if an in _targets:
        depends.append(self.with_pkgver(f"llvm{_llvm_majver}-clang-cross-{an}"))


for _an in _targetlist:
    _gen(_an)
