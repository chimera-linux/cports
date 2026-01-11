pkgname = "perl"
pkgver = "5.42.0"
pkgrel = 0
_perl_cross_ver = "1.6.4"
build_style = "gnu_configure"
configure_gen = []
make_dir = "."
make_check_target = "test"
make_check_env = {"PERL_BUILD_PACKAGING": "1"}
makedepends = ["zlib-ng-compat-devel", "bzip2-devel"]
checkdepends = ["perl-AnyEvent", "perl-Test-Pod", "procps"]
pkgdesc = "Practical Extraction and Report Language"
license = "Artistic-1.0-Perl OR GPL-1.0-or-later"
url = "https://www.perl.org"
source = [
    f"https://www.cpan.org/src/5.0/perl-{pkgver}.tar.gz",
    f"https://github.com/arsv/perl-cross/releases/download/{_perl_cross_ver}/perl-cross-{_perl_cross_ver}.tar.gz",
]
sha256 = [
    "e093ef184d7f9a1b9797e2465296f55510adb6dab8842b0c3ed53329663096dc",
    "b6202173b0a8a43fb312867d85a8cd33527f3f234b1b6e591cdaa9895c9920c7",
]
# prevent a massive log dump
tool_flags = {
    "CFLAGS": [
        "-Wno-compound-token-split-by-macro",
        "-DNO_POSIX_2008_LOCALE",
        "-D_GNU_SOURCE",
        # https://github.com/llvm/llvm-project/issues/152241
        "-fno-strict-aliasing",
    ],
    "LDFLAGS": ["-Wl,-z,stack-size=2097152", "-pthread"],
}
env = {
    "HOSTCFLAGS": "-D_GNU_SOURCE",
}
# FIXME int; available ubsan patch does not help (e.g. automake fails to run)
hardening = ["!int"]
# check is cyclic: depends on perl modules
options = ["!check"]


def pre_patch(self):
    for f in (self.cwd / f"perl-{pkgver}").iterdir():
        self.mv(f, ".")

    for f in (self.cwd / f"perl-cross-{_perl_cross_ver}").iterdir():
        if f.name == "utils":
            self.mv(f / "Makefile", "utils")
            f.rmdir()
            continue
        self.mv(f, ".")


def init_configure(self):
    self.tools["LD"] = self.tools["CC"]


def configure(self):
    cargs = [
        "--prefix=/usr",
        "-Dusethreads",
        # this has to come after the above or cross breaks
        # don't ask questions!
        "--host-use-threads",
        "-Duseshrplib",
        "-Dusesoname",
        "-Dusevendorprefix",
        "-Dprefix=/usr",
        "-Dvendorprefix=/usr",
        "-Dprivlib=/usr/share/perl5/core_perl",
        "-Darchlib=/usr/lib/perl5/core_perl",
        "-Dsitelib=/usr/share/perl5/site_perl",
        "-Dsitearch=/usr/lib/perl5/site_perl",
        "-Dvendorlib=/usr/share/perl5/vendor_perl",
        "-Dvendorarch=/usr/lib/perl5/vendor_perl",
        "-Dscriptdir=/usr/bin",
        "-Dvendorscript=/usr/bin",
        "-Dinc_version_list=none",
        "-Dman1ext=1p",
        "-Dman3ext=3p",
        "-Dman1dir=/usr/share/man/man1",
        "-Dman3dir=/usr/share/man/man3",
        "-Dd_sockaddr_in6=define",
    ]

    if self.profile().cross:
        cargs.append("--target=" + self.profile().triplet)

    cfl = self.get_cflags(shell=True)
    lfl = self.get_ldflags(shell=True)

    cargs.append("-Dcccdlflags=-fPIC")
    cargs.append("-Doptimize=-Wall " + cfl)
    cargs.append("-Dccflags=" + cfl)
    cargs.append("-Dlddlflags=-shared " + lfl)
    cargs.append("-Dldflags=" + lfl)
    cargs.append("-Dperl_static_inline=static __inline__")
    cargs.append("-Dd_static_inline")

    self.do(self.chroot_cwd / "configure", *cargs)


def init_check(self):
    self.make_check_env["TEST_JOBS"] = str(self.make_jobs)


def post_install(self):
    for f in (self.destdir / "usr/share").rglob("*"):
        if f.is_file() and not f.is_symlink():
            f.chmod(0o644)

    for f in (self.destdir / "usr/lib").rglob("*"):
        if f.is_file() and not f.is_symlink():
            f.chmod(0o644)

    self.install_link(f"usr/bin/perl{pkgver}", "perl")

    # remove all pod files except those under
    # /usr/share/perl5/core_perl/pod/ (FS#16488)
    for f in (self.destdir / "usr/share/perl5/core_perl").glob("*.pod"):
        f.unlink()

    for d in (self.destdir / "usr/share/perl5/core_perl").iterdir():
        if not d.is_dir() or d.name == "pod":
            continue
        for f in d.rglob("*.pod"):
            f.unlink()

    for f in (self.destdir / "usr/lib").rglob("*.pod"):
        f.unlink()

    for f in self.destdir.rglob(".packlist"):
        f.unlink()

    # convert hardlinks
    hf = self.destdir / "usr/share/man/man1/perlthanks.1p"
    hf.unlink()
    hf.symlink_to("perlbug.1p")
    hf = self.destdir / "usr/bin/perlthanks"
    hf.unlink()
    hf.symlink_to("perlbug")
