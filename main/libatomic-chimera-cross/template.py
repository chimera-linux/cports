pkgname = "libatomic-chimera-cross"
pkgver = "0.90.0"
pkgrel = 4
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


def post_extract(self):
    self.mkdir("build")
    for f in self.cwd.iterdir():
        if f.name == "build":
            continue
        self.cp(f, "build")


def build(self):
    for an in _targets:
        with self.profile(an) as pf:
            at = pf.triplet
            with self.stamp(f"{an}_build"):
                self.cp("build", f"build-{an}", recursive=True)
                eflags = []
                eldflags = ["--unwindlib=none", "-nostdlib"]
                if an == "aarch64":
                    # avoid emitting dependencies on builtins
                    eflags += ["-mno-outline-atomics"]
                cfl = self.get_cflags(shell=True, extra_flags=eflags)
                ldfl = self.get_ldflags(shell=True, extra_flags=eldflags)
                self.make.build(
                    [
                        f"CC=clang -target {at} --sysroot /usr/{at}",
                        "PREFIX=/usr",
                        f"CFLAGS={cfl}",
                        f"LDFLAGS={ldfl}",
                        "AR=" + self.tools["AR"],
                    ],
                    wrksrc=self.chroot_cwd / f"build-{an}",
                )


def install(self):
    for an in _targets:
        with self.profile(an) as pf:
            at = pf.triplet
            self.install_dir(f"usr/{at}/usr/lib")
            self.install_link(f"usr/{at}/lib", "usr/lib")
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
    def _(self):
        self.subdesc = f"static {an} support"
        self.depends = [self.with_pkgver(f"libatomic-chimera-cross-{an}")]
        return [f"usr/{at}/usr/lib/libatomic.a"]

    @subpackage(f"libatomic-chimera-cross-{an}", cond)
    def _(self):
        self.subdesc = f"{an} support"
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
def _(self):
    self.options = ["empty"]
    self.subdesc = "static"
    self.depends = []
    for an in _targets:
        self.depends.append(
            self.with_pkgver(f"libatomic-chimera-cross-{an}-static")
        )

    return []
