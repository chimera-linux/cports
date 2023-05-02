pkgname = "musl-cross"
pkgver = "1.2.4"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--prefix=/usr", "--disable-gcc-wrapper"]
make_cmd = "gmake"
hostmakedepends = ["gmake"]
makedepends = ["clang-rt-crt-cross"]
depends = ["clang-rt-crt-cross"]
pkgdesc = "Musl C library for cross-compiling"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "http://www.musl-libc.org"
source = f"http://www.musl-libc.org/releases/musl-{pkgver}.tar.gz"
sha256 = "7a35eae33d5372a7c0da1188de798726f68825513b7ae3ebe97aaaa52114f039"
# mirrors musl
hardening = ["!scp"]
# crosstoolchain
options = ["!cross", "!check", "!lto", "brokenlinks"]

_targetlist = ["aarch64", "ppc64le", "ppc64", "x86_64", "riscv64"]
_targets = list(filter(lambda p: p != self.profile().arch, _targetlist))

def do_configure(self):
    for an in _targets:
        with self.profile(an) as pf:
            at = pf.triplet
            # musl build dir
            self.mkdir(f"build-{an}", parents = True)
            # configure musl
            with self.stamp(f"{an}_configure") as s:
                s.check()
                self.do(
                    self.chroot_cwd / "configure",
                    *configure_args, "--host=" + at,
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
        with self.profile(an) as pf:
            at = pf.triplet
            self.install_dir(f"usr/{at}/usr/lib")
            self.install_link("usr/lib", f"usr/{at}/lib")
            self.make.install([
                "DESTDIR=" + str(self.chroot_destdir / "usr" / at)
            ], default_args = False, wrksrc = self.chroot_cwd / f"build-{an}")
            self.rm(self.destdir / f"usr/{at}/lib")

def _gen_crossp(an, at):
    cond = an in _targets

    @subpackage(f"musl-cross-{an}-static", cond)
    def _subp(self):
        self.pkgdesc = f"{pkgdesc} (static {an} support)"
        self.depends = [f"musl-cross-{an}={pkgver}-r{pkgrel}"]
        return [f"usr/{at}/usr/lib/libc.a"]

    @subpackage(f"musl-cross-{an}", cond)
    def _subp(self):
        self.pkgdesc = f"{pkgdesc} ({an} support)"
        self.depends = [f"clang-rt-crt-cross-{an}"]
        self.options = [
            "!scanshlibs", "!scanrundeps", "!splitstatic", "foreignelf"
        ]
        return [f"usr/{at}"]

    if cond:
        depends.append(f"musl-cross-{an}")

for an in _targetlist:
    with self.profile(an) as pf:
        _gen_crossp(an, pf.triplet)

@subpackage("musl-cross-static")
def _static(self):
    self.build_style = "meta"
    self.pkgdesc = f"{pkgdesc} (static)"
    self.depends = []
    for an in _targets:
        self.depends.append(f"musl-cross-{an}-static={pkgver}-r{pkgrel}")

    return []
