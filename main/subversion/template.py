# TODO: service
pkgname = "subversion"
pkgver = "1.14.5"
pkgrel = 1
build_style = "gnu_configure"
configure_args = [
    "--config-cache",
    "--with-editor=vi",
    "--with-gnome-keyring",
    "--disable-javahl",
    "--disable-mod-activation",
    "--disable-static",
]
configure_gen = ["./autogen.sh", "--release"]
make_dir = "."
make_build_target = "all"
make_build_args = ["swig-pl-lib", "tools"]
make_install_args = [
    "-j1",
    "install-swig-pl-lib",
    "install-tools",
    "toolsdir=/usr/bin",
]
hostmakedepends = [
    "automake",
    "gettext",
    "libtool",
    "nasm",
    "perl",
    "pkgconf",
    "python",
    "swig",
]
makedepends = [
    "apr-util-devel",
    "file-devel",
    "libsasl-devel",
    "libsecret-devel",
    "lz4-devel",
    "serf-devel",
    "sqlite-devel",
    "utf8proc-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "Centralized version control system"
license = "Apache-2.0"
url = "https://subversion.apache.org"
source = (
    f"https://archive.apache.org/dist/subversion/subversion-{pkgver}.tar.gz"
)
sha256 = "cd143fe8fdb1cd506c438eef1c772a2e87e1519e6b0be3fcd54a8c59e9022390"
# not even once also nobody cares L
options = ["!cross", "!check"]


def post_build(self):
    self.do(
        "perl", "Makefile.PL", wrksrc="subversion/bindings/swig/perl/native"
    )
    self.do(
        "make",
        "-j1",
        "-C",
        "subversion/bindings/swig/perl/native",
        "LD_RUN_PATH=/usr/lib",
        "EXTRALIBS=-lapr-1",
    )


def post_install(self):
    self.do(
        "make",
        "pure_vendor_install",
        "-C",
        "subversion/bindings/swig/perl/native",
        f"PERL_INSTALL_ROOT={self.chroot_destdir}",
    )
    self.rename("usr/share/pkgconfig", "usr/lib/pkgconfig", relative=False)
    # bash completions
    self.install_completion("tools/client-side/bash_completion", "bash", "svn")
    for f in [
        "svnadmin",
        "svndumpfilter",
        "svnlook",
        "svnsync",
        "svnversion",
    ]:
        self.install_link(f"usr/share/bash-completion/completions/{f}", "svn")
    # remove these, conflicts
    self.uninstall("usr/bin/diff*", glob=True)


@subpackage("subversion-gnome-keyring")
def _(self):
    self.subdesc = "GNOME keyring integration"
    self.install_if = [self.parent, "gnome-keyring"]

    return ["usr/lib/libsvn_auth_gnome_keyring*.so.*"]


@subpackage("subversion-tools")
def _(self):
    self.subdesc = "extra tools"

    return [
        "usr/bin/fsfs-*",
        "usr/bin/svn-*",
        "usr/bin/svnauthz*",
        "usr/bin/svnconflict",
        "usr/bin/svnmover",
        "usr/bin/svnraisetreeconflict",
        "usr/bin/x509-parser",
    ]


@subpackage("subversion-perl")
def _(self):
    self.subdesc = "Perl bindings"
    self.depends += ["perl"]

    return [
        "usr/lib/libsvn_swig_perl-1.so.*",
        "usr/lib/perl5",
        "usr/share/man/man3/SVN::*",
    ]


@subpackage("subversion-libs")
def _(self):
    return self.default_libs()


@subpackage("subversion-devel")
def _(self):
    return self.default_devel()
