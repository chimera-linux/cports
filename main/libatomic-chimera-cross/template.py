pkgname = "libatomic-chimera-cross"
pkgver = "0.90.0"
pkgrel = 1
build_style = "makefile"
makedepends = ["musl-cross"]
depends = ["musl-cross"]
pkgdesc = "Libatomic for cross-compiling"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://github.com/chimera-linux/libatomic-chimera"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "fccbd8c0ef7fd473275f835b3fca9275fb27a0c196cdcdff1f6d14ab12ed3a53"
# crosstoolchain
options = ["!cross", "!check", "!lto", "brokenlinks", "empty"]

_targetlist = ["aarch64", "ppc64le", "ppc64", "ppc", "x86_64", "riscv64"]
_targets = list(filter(lambda p: p != self.profile().arch, _targetlist))


def post_extract(self):
    self.mkdir("build")
    for f in self.cwd.iterdir():
        if f.name == "build":
            continue
        self.cp(f, "build")


def do_build(self):
    for an in _targets:
        with self.profile(an) as pf:
            at = pf.triplet
            with self.stamp(f"{an}_build"):
                self.cp("build", f"build-{an}", recursive=True)
                self.make.build(
                    [
                        f"CC=clang -target {at} --sysroot /usr/{at}",
                        "PREFIX=/usr",
                        "CFLAGS=" + self.get_cflags(shell=True),
                        "LDFLAGS=--unwindlib=none -nostdlib "
                        + self.get_ldflags(shell=True),
                        "AR=" + self.tools["AR"],
                    ],
                    wrksrc=self.chroot_cwd / f"build-{an}",
                )


def do_install(self):
    for an in _targets:
        with self.profile(an) as pf:
            at = pf.triplet
            self.install_dir(f"usr/{at}/usr/lib")
            self.install_link("usr/lib", f"usr/{at}/lib")
            self.make.install(
                [
                    "PREFIX=/usr",
                    "DESTDIR=" + str(self.chroot_destdir / "usr" / at),
                ],
                default_args=False,
                wrksrc=self.chroot_cwd / f"build-{an}",
            )


def _gen_crossp(an, at):
    cond = an in _targets

    @subpackage(f"libatomic-chimera-cross-{an}-static", cond)
    def _subp_static(self):
        self.pkgdesc = f"{pkgdesc} (static {an} support)"
        self.depends = [f"libatomic-chimera-cross-{an}={pkgver}-r{pkgrel}"]
        return [f"usr/{at}/usr/lib/libatomic.a"]

    @subpackage(f"libatomic-chimera-cross-{an}", cond)
    def _subp(self):
        self.pkgdesc = f"{pkgdesc} ({an} support)"
        self.depends = [f"clang-rt-crt-cross-{an}"]
        self.options = [
            "!scanshlibs",
            "!scanrundeps",
            "!splitstatic",
            "foreignelf",
        ]
        return [f"usr/{at}"]

    if cond:
        depends.append(f"libatomic-chimera-cross-{an}")


for _an in _targetlist:
    with self.profile(_an) as _pf:
        _gen_crossp(_an, _pf.triplet)


@subpackage("libatomic-chimera-cross-static")
def _static(self):
    self.options = ["empty"]
    self.pkgdesc = f"{pkgdesc} (static)"
    self.depends = []
    for an in _targets:
        self.depends.append(
            f"libatomic-chimera-cross-{an}-static={pkgver}-r{pkgrel}"
        )

    return []
