pkgname = "git"
pkgver = "2.48.0"
pkgrel = 0
hostmakedepends = [
    "asciidoc",
    "gettext",
    "perl",
    "pkgconf",
    "tk",
    "xmlto",
]
makedepends = [
    "curl-devel",
    "libexpat-devel",
    "libsecret-devel",
    "pcre2-devel",
    "tk-devel",
]
depends = [
    "ca-certificates",
    "perl-authen-sasl",
    "perl-mime-tools",
    "perl-net-smtp-ssl",
]
checkdepends = ["gnupg"]
pkgdesc = "Fast, distributed version control system"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only"
url = "https://git-scm.com"
source = f"https://www.kernel.org/pub/software/scm/git/git-{pkgver}.tar.xz"
sha256 = "4803b809c42696b3b8cce6b0ba6de26febe1197f853daf930a484db93c1ad0d5"
hardening = ["!vis", "!cfi"]


def configure(self):
    with open(self.cwd / "config.mak", "w") as cf:
        cf.write(
            f"""
prefix = /usr
gitexecdir = /usr/lib/git-core
CC = {self.get_tool("CC")}
AR = {self.get_tool("AR")}
TAR = tar
CFLAGS = {self.get_cflags(shell=True)}
LDFLAGS = {self.get_ldflags(shell=True)}
USE_LIBPCRE2 = Yes
NO_INSTALL_HARDLINKS = Yes
ICONV_OMITS_BOM = Yes
NO_REGEX = Yes
INSTALLDIRS = vendor
INSTALL_SYMLINKS = 1
perllibdir = /usr/share/perl5/vendor_perl
PYTHON_PATH = /usr/bin/python
DEFAULT_TEST_TARGET=prove
GIT_PROVE_OPTS=--jobs={self.make_jobs}
HOST_CPU = {self.profile().arch}
# FIXME: figure out why these fail
export GIT_SKIP_TESTS=t4201 t4301 t7008 t7003
"""
        )


def build(self):
    cmd = ["make", f"-j{self.make_jobs}"]
    self.do(*cmd)
    self.do(*cmd, "-C", "Documentation", "man")
    self.do(*cmd, "-C", "contrib/contacts", "all", "git-contacts.1")
    self.do(*cmd, "-C", "contrib/diff-highlight", "all")
    self.do(*cmd, "-C", "contrib/subtree", "all", "man")
    self.do(*cmd, "-C", "contrib/credential/libsecret", "all")


def check(self):
    self.do("make", "test")
    self.do("make", "-C", "contrib/diff-highlight", "test")
    self.do("make", "-C", "contrib/subtree", "test")


def install(self):
    ddir = f"DESTDIR={self.chroot_destdir}"
    self.do("make", "install", "install-doc", ddir)
    self.do("make", "-C", "contrib/contacts", "install", "install-man", ddir)
    self.do("make", "-C", "contrib/subtree", "install", "install-man", ddir)
    # no install target
    self.install_file(
        "contrib/credential/libsecret/git-credential-libsecret",
        "usr/lib/git-core",
        mode=0o755,
    )

    # remove cvs for now
    self.uninstall("usr/bin/git-cvsserver")
    self.uninstall("usr/lib/git-core/git-cvsexportcommit")
    self.uninstall("usr/lib/git-core/git-cvsimport")
    self.uninstall("usr/lib/git-core/git-cvsserver")
    self.uninstall("usr/share/man/man1/git-cvsexportcommit.1")
    self.uninstall("usr/share/man/man1/git-cvsimport.1")
    self.uninstall("usr/share/man/man1/git-cvsserver.1")
    self.uninstall("usr/share/man/man7/gitcvs-migration.7")

    self.install_completion("contrib/completion/git-completion.bash", "bash")
    self.install_file("contrib/completion/git-prompt.sh", "usr/share/git")

    self.install_bin("contrib/diff-highlight/diff-highlight")
    self.install_file(
        "contrib/diff-highlight/README",
        "usr/share/doc/git",
        name="diff-highlight",
    )

    self.install_file(
        "contrib/git-jump/git-jump", "usr/lib/git-core", mode=0o755
    )
    self.install_file(
        "contrib/git-jump/README", "usr/share/doc/git", name="git-jump"
    )

    # hardlink
    p = self.destdir / "usr/lib/git-core/git-citool"
    self.rm(p)
    p.symlink_to("git-gui")

    # register shells
    self.install_shell("/usr/bin/git-shell")


@subpackage("gitk")
def _(self):
    self.depends += [self.parent, "tk"]
    self.pkgdesc = "Git repository browser"
    self.license = "GPL-2.0-or-later"
    return ["usr/bin/gitk", "usr/share/gitk", "usr/share/man/man1/gitk.1"]


@subpackage("git-gui")
def _(self):
    self.depends += [self.parent, "tk"]
    self.subdesc = "GUI tool"
    self.license = "GPL-2.0-or-later"
    return [
        "usr/lib/git-core/git-gui*",
        "usr/lib/git-core/git-citool",
        "usr/share/man/man1/git-gui.1",
        "usr/share/man/man1/git-citool.1",
        "usr/share/git-gui",
    ]


@subpackage("git-credential-libsecret")
def _(self):
    self.depends += [self.parent]
    self.install_if = [self.parent, "libsecret"]
    self.pkgdesc = "Git libsecret credential helper"

    return ["usr/lib/git-core/git-credential-libsecret"]


@subpackage("git-scalar")
def _(self):
    self.depends += [self.parent]
    self.pkgdesc = "Git scalar monorepo tool"

    return [
        "usr/bin/scalar",
        "usr/lib/git-core/scalar",
    ]


@subpackage("git-svn")
def _(self):
    self.subdesc = "Subversion support"
    self.depends += [self.parent, "subversion-perl", "perl-termreadkey"]
    self.install_if = [self.parent, "subversion"]

    return [
        "usr/share/perl5/vendor_perl/Git/SVN*",
        "usr/lib/git-core/git-svn",
        "usr/share/man/man1/git-svn.1",
    ]
