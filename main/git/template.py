pkgname = "git"
pkgver = "2.44.0"
pkgrel = 0
hostmakedepends = [
    "gmake",
    "asciidoc",
    "gettext",
    "perl",
    "pkgconf",
    "xmlto",
    "tk",
]
makedepends = [
    "libcurl-devel",
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
pkgdesc = "Fast, distributed version control system"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only"
url = "https://git-scm.com"
source = f"https://www.kernel.org/pub/software/scm/{pkgname}/{pkgname}-{pkgver}.tar.xz"
sha256 = "e358738dcb5b5ea340ce900a0015c03ae86e804e7ff64e47aa4631ddee681de3"
hardening = ["!cfi"]  # TODO
# missing checkdepends
options = ["!check"]


def do_configure(self):
    with open(self.cwd / "config.mak", "w") as cf:
        cf.write(
            f"""
prefix = /usr
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
DEFAULT_TEST_TARGET = prove
GIT_PROVE_OPTS = {self.make_jobs}
HOST_CPU = {self.profile().arch}
export GIT_SKIP_TESTS=t9604.2
"""
        )


def do_build(self):
    cmd = ["gmake", f"-j{self.make_jobs}"]
    self.do(*cmd)
    self.do(*cmd, "-C", "Documentation", "man")
    self.do(*cmd, "-C", "contrib/contacts", "all", "git-contacts.1")
    self.do(*cmd, "-C", "contrib/diff-highlight", "all")
    self.do(*cmd, "-C", "contrib/subtree", "all", "man")
    self.do(*cmd, "-C", "contrib/credential/libsecret", "all")


def do_check(self):
    self.do("gmake", "test")
    self.do("gmake", "-C", "contrib/diff-highlight", "test")
    self.do("gmake", "-C", "contrib/subtree", "test")


def do_install(self):
    ddir = f"DESTDIR={self.chroot_destdir}"
    self.do("gmake", "install", "install-doc", ddir)
    self.do("gmake", "-C", "contrib/contacts", "install", "install-man", ddir)
    self.do("gmake", "-C", "contrib/subtree", "install", "install-man", ddir)
    # no install target
    self.install_file(
        "contrib/credential/libsecret/git-credential-libsecret",
        "usr/libexec/git-core",
        mode=0o755,
    )

    # remove cvs for now
    self.rm(self.destdir / "usr/bin/git-cvsserver")
    self.rm(self.destdir / "usr/libexec/git-core/git-cvsexportcommit")
    self.rm(self.destdir / "usr/libexec/git-core/git-cvsimport")
    self.rm(self.destdir / "usr/libexec/git-core/git-cvsserver")
    self.rm(self.destdir / "usr/share/man/man1/git-cvsexportcommit.1")
    self.rm(self.destdir / "usr/share/man/man1/git-cvsimport.1")
    self.rm(self.destdir / "usr/share/man/man1/git-cvsserver.1")
    self.rm(self.destdir / "usr/share/man/man7/gitcvs-migration.7")

    self.install_completion("contrib/completion/git-completion.bash", "bash")
    self.install_file("contrib/completion/git-prompt.sh", "usr/share/git")

    self.install_bin("contrib/diff-highlight/diff-highlight")
    self.install_file(
        "contrib/diff-highlight/README",
        "usr/share/doc/git",
        name="diff-highlight",
    )

    self.install_file(
        "contrib/git-jump/git-jump", "usr/libexec/git-core", mode=0o755
    )
    self.install_file(
        "contrib/git-jump/README", "usr/share/doc/git", name="git-jump"
    )

    # hardlink
    p = self.destdir / "usr/libexec/git-core/git-citool"
    self.rm(p)
    p.symlink_to("git-gui")

    # register shells
    self.install_shell("/usr/bin/git-shell")


@subpackage("gitk")
def _gitk(self):
    self.depends += [f"{pkgname}={pkgver}-r{pkgrel}", "tk"]
    self.pkgdesc = "Git repository browser"
    self.license = "GPL-2.0-or-later"
    return ["usr/bin/gitk", "usr/share/gitk", "usr/share/man/man1/gitk.1"]


@subpackage("git-gui")
def _gui(self):
    self.depends += [f"{pkgname}={pkgver}-r{pkgrel}", "tk"]
    self.pkgdesc = f"{pkgdesc} (GUI tool)"
    self.license = "GPL-2.0-or-later"
    return [
        "usr/libexec/git-core/git-gui*",
        "usr/libexec/git-core/git-citool",
        "usr/share/man/man1/git-gui.1",
        "usr/share/man/man1/git-citool.1",
        "usr/share/git-gui",
    ]


@subpackage("git-credential-libsecret")
def _libsecret(self):
    self.depends += [f"{pkgname}={pkgver}-r{pkgrel}"]
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}", "libsecret"]
    self.pkgdesc = "Git libsecret credential helper"

    return ["usr/libexec/git-core/git-credential-libsecret"]


@subpackage("git-scalar")
def _scalar(self):
    self.depends += [f"{pkgname}={pkgver}-r{pkgrel}"]
    self.pkgdesc = "Git scalar monorepo tool"

    return [
        "usr/bin/scalar",
        "usr/libexec/git-core/scalar",
    ]


@subpackage("git-svn")
def _svn(self):
    self.pkgdesc = f"{pkgdesc} (Subversion support)"
    self.depends += [
        f"{pkgname}={pkgver}-r{pkgrel}",
        # hack to work around cross-category dependency
        # won't be installable without contrib enabled (that's fine)
        "virtual:subversion-perl!base-files",
        "perl-termreadkey",
    ]
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}", "subversion"]

    return [
        "usr/share/perl5/vendor_perl/Git/SVN*",
        "usr/libexec/git-core/git-svn",
        "usr/share/man/man1/git-svn.1",
    ]
