pkgname = "chroot-git"
version = "2.31.1"
revision = 1
bootstrap = True
wrksrc = f"git-{version}"
build_style = "gnu_configure"
configure_args = [
    "--without-curl", "--without-openssl",
    "--without-python", "--without-expat",
    "--without-tcltk",
    "ac_cv_lib_curl_curl_global_init=no",
    "ac_cv_lib_expat_XML_ParserCreate=no"
]
make_check_target = "test"
makedepends = ["zlib-devel"]
short_desc = "GIT Tree History Storage Tool -- for xbps-src use"
maintainer = "Enno Boland <gottox@voidlinux.org>"
license = "GPL-2.0-only"
homepage = "https://git-scm.com/"
distfiles = [
    f"https://www.kernel.org/pub/software/scm/git/git-{version}.tar.xz"
]
checksum = ["9f61417a44d5b954a5012b6f34e526a3336dcf5dd720e2bb7ada92ad8b3d6680"]

if not current.bootstrapping:
    hostmakedepends = ["perl", "tar"]

def pre_configure(self):
    from cbuild.core import paths
    if self.bootstrapping:
        self.configure_args += [
            "--with-zlib", paths.masterdir() / "usr"
        ]

def post_configure(self):
    with open(self.abs_wrksrc / "config.mak", "w") as f:
        f.write("""
CC_LD_DYNPATH=-L
NO_INSTALL_HARDLINKS=Yes
NO_GETTEXT=Yes
""")

def do_install(self):
    import os

    self.make.install([
        "DESTDIR=" + str(self.chroot_wrksrc / "build-tmp")
    ], default_args = False)
    # remove unneeded stuff
    os.rename(
        self.abs_wrksrc / "build-tmp/usr/bin/git",
        self.abs_wrksrc / "build-tmp/usr/bin/chroot-git"
    )
    self.install_bin("build-tmp/usr/bin/chroot-git")
