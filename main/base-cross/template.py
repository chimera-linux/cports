pkgname = "base-cross"
version = "0.1"
revision = 0
depends = ["clang-rt-cross", "musl-cross", "libcxx-cross"]
pkgdesc = "Base metapackage for cross-compiling"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Public Domain"
homepage = "https://chimera-linux.org"
options = ["!cross"]

_targets = list(filter(
    lambda p: p != current.build_profile.arch,
    ["aarch64", "ppc64le", "ppc64", "x86_64", "riscv64"]
))

def do_fetch(self):
    pass

def do_install(self):
    for an in _targets:
        with self.profile(an):
            at = self.build_profile.short_triplet
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
        self.pkgdesc = f"{pkgdesc} - {an}"
        self.depends = [
            f"clang-rt-cross-{an}",
            f"musl-cross-{an}",
            f"libcxx-cross-{an}",
            f"kernel-libc-headers-cross-{an}",
        ]
        return [f"usr/bin/{at}-*", f"usr/lib/ccache/bin/{at}-*"]
    depends.append(f"base-cross-{an}={version}-r{revision}")

for an in _targets:
    with current.profile(an):
        at = current.build_profile.short_triplet
    _gen_crossp(an, at)
