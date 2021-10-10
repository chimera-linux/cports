pkgname = "musl-cross"
pkgver = "1.2.2"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--prefix=/usr", "--disable-gcc-wrapper"]
hostmakedepends = ["gmake"]
makedepends = ["clang-rt-crt-cross"]
depends = ["clang-rt-crt-cross"]
make_cmd = "gmake"
pkgdesc = "Musl C library (cross-compiling)"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "http://www.musl-libc.org/"
source = f"http://www.musl-libc.org/releases/musl-{pkgver}.tar.gz"
sha256 = "9b969322012d796dc23dda27a35866034fa67d8fb67e0e2c45c913c3d43219dd"
options = ["!cross", "!check", "!lint"]

# segfaults otherwise
hardening = ["!scp"]

_targets = list(filter(
    lambda p: p != current.build_profile.arch,
    ["aarch64", "ppc64le", "ppc64", "x86_64", "riscv64"]
))

def do_configure(self):
    for an in _targets:
        with self.profile(an):
            at = self.build_profile.short_triplet
            # musl build dir
            self.mkdir(f"build-{an}", parents = True)
            # configure musl
            with self.stamp(f"{an}_configure") as s:
                s.check()
                self.do(
                    self.chroot_cwd / "configure",
                    configure_args + ["--host=" + at],
                    wrksrc = f"build-{an}",
                    env = {
                        "CC": "clang -target " + at
                    }
                )

def do_build(self):
    for an in _targets:
        with self.profile(an):
            self.mkdir(f"build-{an}", parents = True)
            with self.stamp(f"{an}_build") as s:
                s.check()
                self.make.build(wrksrc = self.chroot_cwd / f"build-{an}")

def do_install(self):
    for an in _targets:
        with self.profile(an):
            at = self.build_profile.short_triplet
            self.install_dir(f"usr/{at}/usr/lib")
            self.install_link("usr/lib", f"usr/{at}/lib")
            self.make.install([
                "DESTDIR=" + str(self.chroot_destdir / "usr" / at)
            ], default_args = False, wrksrc = self.chroot_cwd / f"build-{an}")
            self.rm(self.destdir / f"usr/{at}/lib")

def _gen_crossp(an, at):
    @subpackage(f"musl-cross-{an}")
    def _subp(self):
        self.pkgdesc = f"{pkgdesc} ({an} support)"
        self.depends = [f"clang-rt-crt-cross-{an}"]
        return [f"usr/{at}"]
    depends.append(f"musl-cross-{an}")

for an in _targets:
    with current.profile(an):
        _gen_crossp(an, current.build_profile.short_triplet)
