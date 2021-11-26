pkgname = "git"
pkgver = "2.34.1"
pkgrel = 0
make_cmd = "gmake"
make_check_target = "test"
hostmakedepends = [
    "gmake", "asciidoc", "gettext-tiny", "perl", "pkgconf", "xmlto", "tk"
]
makedepends = [
    "libcurl-devel", "pcre2-devel", "tk-devel", "libexpat-devel"
]
depends = [
    "ca-certificates", "perl-authen-sasl", "perl-mime-tools",
    "perl-net-smtp-ssl"
]
pkgdesc = "Fast, distributed version control system"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only"
url = "https://git-scm.com"
source = f"https://www.kernel.org/pub/software/scm/{pkgname}/{pkgname}-{pkgver}.tar.xz"
sha256 = "3a0755dd1cfab71a24dd96df3498c29cd0acd13b04f3d08bf933e81286db802c"
# missing checkdepends
options = ["!check"]

def init_configure(self):
    from cbuild.util import make

    self.make = make.Make(self)

def do_configure(self):
    with open(self.cwd / "config.mak", "w") as cf:
        cf.write(f"""
prefix = /usr
CC = {self.get_tool("CC")}
AR = {self.get_tool("AR")}
TAR = tar
CFLAGS = {self.get_cflags(shell = True)}
LDFLAGS = {self.get_ldflags(shell = True)}
USE_LIBPCRE2 = Yes
NO_INSTALL_HARDLINKS = Yes
ICONV_OMITS_BOM = Yes
NO_REGEX = Yes
INSTALLDIRS = vendor
perllibdir = /usr/share/perl5/vendor_perl
PYTHON_PATH = /usr/bin/python
DEFAULT_TEST_TARGET = prove
GIT_PROVE_OPTS = {self.make_jobs}
HOST_CPU = {self.profile().arch}
export GIT_SKIP_TESTS=t9604.2
""")

def do_build(self):
    self.make.build()
    self.make.invoke(None, ["-C", "Documentation", "man"])
    self.make.invoke(None, ["-C", "contrib/contacts", "all", "git-contacts.1"])
    self.make.invoke(None, ["-C", "contrib/diff-highlight", "all"])
    self.make.invoke(None, ["-C", "contrib/subtree", "all", "man"])

def do_check(self):
    self.make.check()
    self.make.invoke(None, ["-C", "contrib/diff-highlight", "test"])
    self.make.invoke(None, ["-C", "contrib/subtree", "test"])

def do_install(self):
    self.make.install(["install-doc"])
    self.make.invoke(None, [
        "-C", "contrib/contacts", "DESTDIR=" + str(self.chroot_destdir),
        "install", "install-man"
    ])
    self.make.invoke(None, [
        "-C", "contrib/subtree", "DESTDIR=" + str(self.chroot_destdir),
        "install", "install-man"
    ])

    # remove cvs for now
    self.rm(self.destdir / "usr/bin/git-cvsserver")
    self.rm(self.destdir / "usr/libexec/git-core/git-cvsexportcommit")
    self.rm(self.destdir / "usr/libexec/git-core/git-cvsimport")
    self.rm(self.destdir / "usr/libexec/git-core/git-cvsserver")
    self.rm(self.destdir / "usr/share/man/man1/git-cvsexportcommit.1")
    self.rm(self.destdir / "usr/share/man/man1/git-cvsimport.1")
    self.rm(self.destdir / "usr/share/man/man1/git-cvsserver.1")
    self.rm(self.destdir / "usr/share/man/man7/gitcvs-migration.7")
    # remove svn for now
    self.rm(self.destdir / "usr/libexec/git-core/git-svn")
    self.rm(self.destdir / "usr/share/man/man1/git-svn.1")
    self.rm(
        self.destdir / "usr/share/perl5/vendor_perl/Git/SVN", recursive = True
    )
    self.rm(self.destdir / "usr/share/perl5/vendor_perl/Git/SVN.pm")

    self.install_file(
        "contrib/completion/git-completion.bash",
        "usr/share/bash-completion/completions",
        name = "git"
    )
    self.install_file(
        "contrib/completion/git-prompt.sh",
        "usr/share/git"
    )

    self.install_bin("contrib/diff-highlight/diff-highlight")
    self.install_file(
        "contrib/diff-highlight/README", "usr/share/doc/git",
        name = "diff-highlight"
    )

    self.install_file(
        "contrib/git-jump/git-jump", "usr/libexec/git-core", mode = 0o755
    )
    self.install_file(
        "contrib/git-jump/README", "usr/share/doc/git",
        name = "git-jump"
    )

    # hardlink
    p = self.destdir / "usr/libexec/git-core/git-citool"
    self.rm(p)
    p.symlink_to("git-gui")

    # register shells
    self.install_shell("/usr/bin/git-shell")

@subpackage("gitk")
def _gitk(self):
    self.depends += [f"git={pkgver}-r{pkgrel}", "tk"]
    self.pkgdesc = "Git repository browser"
    self.license = "GPL-2.0-or-later"
    return ["usr/bin/gitk", "usr/share/gitk", "usr/share/man/man1/gitk.1"]

@subpackage("git-gui")
def _gui(self):
    self.depends += [f"git={pkgver}-r{pkgrel}", "tk"]
    self.pkgdesc = f"{pkgdesc} (GUI tool)"
    self.license = "GPL-2.0-or-later"
    return [
        "usr/libexec/git-core/git-gui*",
        "usr/libexec/git-core/git-citool",
        "usr/share/man/man1/git-gui.1",
        "usr/share/man/man1/git-citool.1",
        "usr/share/git-gui"
    ]
