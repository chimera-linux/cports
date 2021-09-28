pkgname = "perl"
version = "5.32.1"
revision = 0
_perl_cross_version = "1.3.5"
build_style = "gnu_configure"
make_cmd = "gmake"
hostmakedepends = ["gmake", "less"]
makedepends = ["zlib-devel", "bzip2-devel"]
depends = ["less"]
checkdepends = ["iana-etc", "perl-AnyEvent", "perl-Test-Pod", "procps-ng"]
short_desc = "Practical Extraction and Report Language"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Artistic=1.0-Perl, GPL=1.0-or-later"
homepage = "https://www.perl.org"
sources = [
    f"https://www.cpan.org/src/5.0/perl-{version}.tar.gz",
    f"https://github.com/arsv/perl-cross/releases/download/{_perl_cross_version}/perl-cross-{_perl_cross_version}.tar.gz"
]
sha256 = [
    "03b693901cd8ae807231b1787798cf1f2e0b8a56218d07b7da44f784a7caeb2c",
    "91c66f6b2b99fccfd4fee14660b677380b0c98f9456359e91449798c2ad2ef25"
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

options = ["!check"]

# Before updating this package to a new major version, run ${FILESDIR}/provides.pl
# against ${wrksrc} to find the list of built in packages.

provides = [
    "perl-Archive-Tar=2.36-r1",
    "perl-Attribute-Handlers=1.01-r1",
    "perl-AutoLoader=5.74-r1",
    "perl-CPAN=2.27-r1",
    "perl-CPAN-Meta=2.150010-r1",
    "perl-CPAN-Meta-Requirements=2.140-r1",
    "perl-CPAN-Meta-YAML=0.018-r1",
    "perl-Carp=1.50-r1",
    "perl-Compress-Raw-Bzip2=2.093-r1",
    "perl-Compress-Raw-Zlib=2.093-r1",
    "perl-Config-Perl-V=0.32-r1",
    "perl-Data-Dumper=2.174.01-r1",
    "perl-Devel-PPPort=3.57-r1",
    "perl-Devel-SelfStubber=1.06-r1",
    "perl-Digest=1.17.01-r1",
    "perl-Digest-MD5=2.55.01-r1",
    "perl-Digest-SHA=6.02-r1",
    "perl-Dumpvalue=1.21-r1",
    "perl-Encode=3.06-r1",
    "perl-Env=1.04-r1",
    "perl-Exporter=5.74-r1",
    "perl-ExtUtils-CBuilder=0.280234-r1",
    "perl-ExtUtils-Constant=0.25-r1",
    "perl-ExtUtils-Install=2.14-r1",
    "perl-ExtUtils-MakeMaker=7.44-r1",
    "perl-ExtUtils-Manifest=1.72-r1",
    "perl-ExtUtils-ParseXS=3.40-r1",
    "perl-File-Fetch=0.56-r1",
    "perl-File-Path=2.16-r1",
    "perl-File-Temp=0.2309-r1",
    "perl-Filter-Simple=0.96-r1",
    "perl-Filter-Util-Call=1.59-r1",
    "perl-FindBin=1.51-r1",
    "perl-Getopt-Long=2.51-r1",
    "perl-HTTP-Tiny=0.076-r1",
    "perl-I18N-Collate=1.02-r1",
    "perl-I18N-LangTags=0.44-r1",
    "perl-IO=1.43-r1",
    "perl-IO-Compress=2.093-r1",
    "perl-IO-Socket-IP=0.39-r1",
    "perl-IO-Zlib=1.10-r1",
    "perl-IPC-Cmd=1.04-r1",
    "perl-IPC-SysV=2.07-r1",
    "perl-JSON-PP=4.04-r1",
    "perl-Locale-Maketext=1.29-r1",
    "perl-Locale-Maketext-Simple=0.21.01-r1",
    "perl-MIME-Base64=3.15-r1",
    "perl-Math-BigInt=1.999818-r1",
    "perl-Math-BigInt-FastCalc=0.5009-r1",
    "perl-Math-BigRat=0.2614-r1",
    "perl-Math-Complex=1.59.01-r1",
    "perl-Memoize=1.03.01-r1",
    "perl-Module-CoreList=5.20210123-r1",
    "perl-Module-Load=0.34-r1",
    "perl-Module-Load-Conditional=0.70-r1",
    "perl-Module-Loaded=0.08-r1",
    "perl-Module-Metadata=1.000037-r1",
    "perl-NEXT=0.67.01-r1",
    "perl-Net-Ping=2.72-r1",
    "perl-Params-Check=0.38-r1",
    "perl-PathTools=3.78-r1",
    "perl-Perl-OSType=1.010-r1",
    "perl-PerlIO-via-QuotedPrint=0.08-r1",
    "perl-Pod-Checker=1.73-r1",
    "perl-Pod-Escapes=1.07-r1",
    "perl-Pod-Perldoc=3.2801-r1",
    "perl-Pod-Simple=3.40-r1",
    "perl-Pod-Usage=1.69-r1",
    "perl-Safe=2.41.01-r1",
    "perl-Scalar-List-Utils=1.55-r1",
    "perl-Search-Dict=1.07-r1",
    "perl-SelfLoader=1.26-r1",
    "perl-Socket=2.029-r1",
    "perl-Storable=3.21-r1",
    "perl-Sys-Syslog=0.36-r1",
    "perl-Term-ANSIColor=5.01-r1",
    "perl-Term-Cap=1.17-r1",
    "perl-Term-Complete=1.403-r1",
    "perl-Term-ReadLine=1.17-r1",
    "perl-Test=1.31-r1",
    "perl-Test-Harness=3.42-r1",
    "perl-Test-Simple=1.302175-r1",
    "perl-Text-Abbrev=1.02-r1",
    "perl-Text-Balanced=2.03-r1",
    "perl-Text-ParseWords=3.30-r1",
    "perl-Text-Tabs-2013.0523-r1",
    "perl-Thread-Queue=3.14-r1",
    "perl-Thread-Semaphore=2.13-r1",
    "perl-Tie-File=1.06-r1",
    "perl-Tie-RefHash=1.39-r1",
    "perl-Time-HiRes=1.9764-r1",
    "perl-Time-Local=1.28-r1",
    "perl-Time-Piece=1.3401-r1",
    "perl-Unicode-Collate=1.27-r1",
    "perl-Unicode-Normalize=1.27-r1",
    "perl-Win32=0.53-r1",
    "perl-Win32API-File=0.1203.01-r1",
    "perl-XSLoader=0.30-r1",
    "perl-autodie=2.32-r1",
    "perl-autouse=1.11-r1",
    "perl-base=2.27-r1",
    "perl-bignum=0.51-r1",
    "perl-constant=1.33-r1",
    "perl-encoding-warnings=0.13-r1",
    "perl-experimental=0.020-r1",
    "perl-if=0.0608-r1",
    "perl-lib=0.65-r1",
    "perl-libnet=3.11-r1",
    "perl-parent=0.238-r1",
    "perl-perlfaq=5.20200523-r1",
    "perl-podlators=5.008-r1",
    "perl-threads=2.25-r1",
    "perl-threads-shared=1.61-r1",
    "perl-version=0.9924-r1",
]

def pre_patch(self):
    for f in (self.cwd / f"perl-{version}").iterdir():
        self.mv(f, ".")

    for f in (self.cwd / f"perl-cross-{_perl_cross_version}").iterdir():
        if f.name == "utils":
            self.mv(f / "Makefile", "utils")
            f.rmdir()
            continue
        self.mv(f, ".")

def init_configure(self):
    from cbuild.util import make

    self.make = make.Make(self, wrksrc = ".")

    self.env["HOSTCFLAGS"] = "-D_GNU_SOURCE"

    self.tools["LD"] = self.tools["CC"]

    # to prevent perl buildsystem from invoking bmake
    self.env["MAKE"] = self.make.get_command()

def do_configure(self):
    cargs = [
        "--prefix=/usr",
        "-Dusethreads", "-Duseshrplib", "-Dusesoname", "-Dusevendorprefix",
        "-Dprefix=/usr", "-Dvendorprefix=/usr",
        "-Dprivlib=/usr/share/perl5/core_perl",
        "-Darchlib=/usr/lib/perl5/core_perl",
        "-Dsitelib=/usr/share/perl5/site_perl",
        "-Dsitearch=/usr/lib/perl5/site_perl",
        "-Dvendorlib=/usr/share/perl5/vendor_perl",
        "-Dvendorarch=/usr/lib/perl5/vendor_perl",
        "-Dscriptdir=/usr/bin", "-Dvendorscript=/usr/bin",
        "-Dinc_version_list=none", "-Dman1ext=1p", "-Dman3ext=3p",
        "-Dman1dir=/usr/share/man/man1",
        "-Dman3dir=/usr/share/man/man3",
        "-Dd_sockaddr_in6=define",
    ]

    if self.cross_build:
        cargs.append("--target=" + self.build_profile.short_triplet)

    cfl = self.get_cflags(shell = True)
    lfl = self.get_ldflags(shell = True)

    cargs.append("-Dcccdlflags=-fPIC")
    cargs.append("-Doptimize=-Wall " + cfl)
    cargs.append("-Dccflags=" + cfl)
    cargs.append("-Dlddlflags=-shared " + lfl)
    cargs.append("-Dldflags=" + lfl)
    cargs.append("-Dperl_static_inline=static __inline__")
    cargs.append("-Dd_static_inline")

    self.do(self.chroot_cwd / "configure", cargs)

def do_check(self):
    from cbuild.util import make

    self.env["TEST_JOBS"] = str(make.jobs())

    self.make.invoke("test")

def post_install(self):
    for f in (self.destdir / "usr/share").rglob("*"):
        if f.is_file() and not f.is_symlink():
            f.chmod(0o644)

    for f in (self.destdir / "usr/lib").rglob("*"):
        if f.is_file() and not f.is_symlink():
            f.chmod(0o644)

    self.install_link("perl", "usr/bin/perl" + version)

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
