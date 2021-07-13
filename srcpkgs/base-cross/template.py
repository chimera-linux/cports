pkgname = "base-cross"
version = "0.1"
revision = 0
depends = ["clang-rt-cross", "musl-cross", "libcxx-cross"]
short_desc = "Base metapackage for cross-compiling"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Public Domain"
homepage = "https://chimera-linux.org"

_targets = ["aarch64", "ppc64le", "x86_64"]

def do_fetch(self):
    pass

def do_install(self):
    pass

def _gen_crossp(an):
    from cbuild import cpu

    @subpackage(f"base-cross-{an}", cpu.target() != an)
    def _subp(self):
        self.short_desc = f"{short_desc} - {an}"
        self.depends = [
            f"clang-rt-cross-{an}",
            f"musl-cross-{an}",
            f"libcxx-cross-{an}"
        ]
        return []
    if cpu.target() != an:
        depends.append(f"base-cross-{an}={version}-r{revision}")

for an in _targets:
    _gen_crossp(an)
