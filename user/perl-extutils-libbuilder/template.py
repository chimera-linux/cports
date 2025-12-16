pkgname = "perl-extutils-libbuilder"
pkgver = "0.09"
pkgrel = 0
hostmakedepends = ["perl-module-build"]
checkdepends = ["perl-test-pod"]
depends = ["perl"]
pkgdesc = "Tool to build C libraries"
license = "Artistic-1.0-Perl OR GPL-1.0-or-later"
url = "https://metacpan.org/pod/ExtUtils::LibBuilder"
source = f"$(CPAN_SITE)/ExtUtils/ExtUtils-LibBuilder-{pkgver}.tar.gz"
sha256 = "dbfac85d015874189a704fa0a2f001d13b5a0c7d89f36c06ff32d569720a6cfb"


def init_configure(self):
    # ssame as main/perl/template.py
    self.tools["LD"] = self.tools["CC"]


def configure(self):
    self.do("perl", "Build.PL")


def build(self):
    self.do("./Build")


def check(self):
    self.do("./Build", "test")


def install(self):
    self.do("./Build", "install", f"--destdir={self.chroot_destdir}")
