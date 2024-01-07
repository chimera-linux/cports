pkgname = "perl"
pkgver = "5.38.2"
pkgrel = 0
_perl_cross_ver = "1.5.2"
build_style = "gnu_configure"
make_cmd = "gmake"
make_dir = "."
make_check_target = "test"
make_check_env = {"PERL_BUILD_PACKAGING": "1"}
hostmakedepends = ["gmake", "less"]
makedepends = ["zlib-devel", "bzip2-devel"]
checkdepends = ["perl-AnyEvent", "perl-Test-Pod", "procps"]
depends = ["less"]
pkgdesc = "Practical Extraction and Report Language"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Artistic-1.0-Perl OR GPL-1.0-or-later"
url = "https://www.perl.org"
source = [
    f"https://www.cpan.org/src/5.0/perl-{pkgver}.tar.gz",
    f"https://github.com/arsv/perl-cross/releases/download/{_perl_cross_ver}/perl-cross-{_perl_cross_ver}.tar.gz",
]
sha256 = [
    "a0a31534451eb7b83c7d6594a497543a54d488bc90ca00f5e34762577f40655e",
    "584dc54c48dca25e032b676a15bef377c1fed9de318b4fc140292a5dbf326e90",
]
# prevent a massive log dump
tool_flags = {
    "CFLAGS": [
        "-Wno-compound-token-split-by-macro",
        "-DNO_POSIX_2008_LOCALE",
        "-D_GNU_SOURCE",
    ],
    "LDFLAGS": ["-Wl,-z,stack-size=2097152", "-pthread"],
}
env = {
    "HOSTCFLAGS": "-D_GNU_SOURCE",
    "MAKE": "gmake",
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


def do_configure(self):
    cargs = [
        "--prefix=/usr",
        "-Dusethreads",
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

    self.install_link("perl", f"usr/bin/perl{pkgver}")

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

    import re
    import os

    cfpath = self.destdir / "usr/lib/perl5/core_perl/Config_heavy.pl"
    with open(cfpath) as ifile:
        with open(self.cwd / "Config_heavy.pl.new", "w") as ofile:
            for ln in ifile:
                ln = re.sub("-specs=.*hardened-ld", "", ln)
                ln = re.sub("-specs=.*hardened-cc1", "", ln)
                ofile.write(ln)

    cfpath.unlink()
    os.rename(self.cwd / "Config_heavy.pl.new", cfpath)
    cfpath.chmod(0o644)

    # convert hardlinks
    hf = self.destdir / "usr/share/man/man1/perlthanks.1p"
    hf.unlink()
    hf.symlink_to("perlbug.1p")
    hf = self.destdir / "usr/bin/perlthanks"
    hf.unlink()
    hf.symlink_to("perlbug")


configure_gen = []
