pkgname = "base-cross"
pkgver = "0.1"
pkgrel = 0
build_style = "meta"
depends = [
    "clang-rt-cross",
    "musl-cross",
    "libatomic-chimera-cross",
    "libcxx-cross",
    "fortify-headers",
]
pkgdesc = "Base metapackage for cross-compiling"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:meta"
url = "https://chimera-linux.org"
options = ["!cross"]

_targetlist = ["aarch64", "ppc64le", "ppc64", "x86_64", "riscv64"]
_targets = list(filter(lambda p: p != self.profile().arch, _targetlist))


def do_install(self):
    for an in _targets:
        with self.profile(an) as pf:
            at = pf.triplet
        # convenient cross symlinks
        self.install_dir("usr/bin")
        self.install_link("clang", f"usr/bin/{at}-clang")
        self.install_link("clang++", f"usr/bin/{at}-clang++")
        self.install_link("clang-cpp", f"usr/bin/{at}-clang-cpp")
        self.install_link("cc", f"usr/bin/{at}-cc")
        self.install_link("c++", f"usr/bin/{at}-c++")
        self.install_link("ld", f"usr/bin/{at}-ld")
        self.install_link("ld.lld", f"usr/bin/{at}-ld.lld")
        # ccache cross symlinks
        self.install_dir("usr/lib/ccache/bin")
        self.install_link(
            "../../../bin/ccache", f"usr/lib/ccache/bin/{at}-clang"
        )
        self.install_link(
            "../../../bin/ccache", f"usr/lib/ccache/bin/{at}-clang++"
        )
        self.install_link("../../../bin/ccache", f"usr/lib/ccache/bin/{at}-cc")
        self.install_link("../../../bin/ccache", f"usr/lib/ccache/bin/{at}-c++")
        # arch config file
        with open(self.destdir / f"usr/bin/{at}.cfg", "w") as cf:
            cf.write(f"--sysroot /usr/{at}\n")
        # symlink fortify headers
        self.install_dir(f"usr/{at}/usr/include")
        self.install_link(
            "../../../include/fortify", f"usr/{at}/usr/include/fortify"
        )


for an in _targetlist:

    @subpackage(f"base-cross-{an}")
    def _subp(self):
        self.pkgdesc = f"{pkgdesc} ({an} support)"
        self.depends = [
            f"clang-rt-cross-{an}",
            f"musl-cross-{an}",
            f"libatomic-chimera-cross-{an}",
            f"libcxx-cross-{an}",
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
        depends.append(f"base-cross-{an}={pkgver}-r{pkgrel}")
