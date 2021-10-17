pkgname = "base-cross"
pkgver = "0.1"
pkgrel = 0
build_style = "meta"
depends = ["clang-rt-cross", "musl-cross", "libcxx-cross"]
pkgdesc = "Base metapackage for cross-compiling"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:meta"
url = "https://chimera-linux.org"
options = ["!cross", "brokenlinks"]

_targets = list(filter(
    lambda p: p != current.profile().arch,
    ["aarch64", "ppc64le", "ppc64", "x86_64", "riscv64"]
))

def do_install(self):
    for an in _targets:
        with self.profile(an) as pf:
            at = pf.short_triplet
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
        self.install_link(
            "../../../bin/ccache", f"usr/lib/ccache/bin/{at}-cc"
        )
        self.install_link(
            "../../../bin/ccache", f"usr/lib/ccache/bin/{at}-c++"
        )
    pass

def _gen_crossp(an, at):
    @subpackage(f"base-cross-{an}")
    def _subp(self):
        self.pkgdesc = f"{pkgdesc} ({an} support)"
        self.depends = [
            f"clang-rt-cross-{an}",
            f"musl-cross-{an}",
            f"libcxx-cross-{an}",
            f"kernel-libc-headers-cross-{an}",
        ]
        return [f"usr/bin/{at}-*", f"usr/lib/ccache/bin/{at}-*"]
    depends.append(f"base-cross-{an}={pkgver}-r{pkgrel}")

for an in _targets:
    with current.profile(an) as pf:
        at = pf.short_triplet
    _gen_crossp(an, at)
