pkgname = "shadow"
pkgver = "4.14.5"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-shared",
    "--enable-lastlog",
    "--disable-static",
    "--with-libpam",
    "--with-acl",
    "--with-attr",
    "--without-libbsd",
    "--without-selinux",
    "--without-nscd",
    "--disable-nls",
    "--enable-subordinate-ids",
    "--disable-account-tools-setuid",
]
configure_gen = []
make_cmd = "gmake"
# out of tree is broken with libsubid
make_dir = "."
hostmakedepends = ["gmake"]
makedepends = ["acl-devel", "linux-pam-devel", "linux-headers"]
depends = ["linux-pam", "base-shells"]
triggers = ["/var/lib/shadow"]
pkgdesc = "Shadow password file utilities"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://github.com/shadow-maint/shadow"
source = f"{url}/releases/download/{pkgver}/shadow-{pkgver}.tar.xz"
sha256 = "cba74bc7b05d89c015afe23131f9159ece38779d40a8af4cf162852e6e85ca23"
suid_files = [
    "usr/bin/chage",
    "usr/bin/chfn",
    "usr/bin/chsh",
    "usr/bin/expiry",
    "usr/bin/gpasswd",
    "usr/bin/newgidmap",
    "usr/bin/newuidmap",
    "usr/bin/newgrp",
    "usr/bin/passwd",
    "usr/bin/sg",
    "usr/bin/su",
]
hardening = ["!cfi"]  # TODO
# messes with filesystem
options = ["!check"]


def pre_install(self):
    # shadow force-installs into sbin regardless of configure
    self.install_dir("usr/bin")
    self.install_link("bin", "usr/sbin")


def post_install(self):
    self.rm(self.destdir / "usr/sbin", force=True)

    # install sulogin which is noinst
    self.install_bin("src/sulogin")
    self.install_man("man/man8/sulogin.8")

    # do not install pam files supplied with shadow
    self.rm(self.destdir / "etc/pam.d", recursive=True, force=True)

    # install our own pam files
    for f in ["chage", "chfn", "chsh", "login", "su", "passwd"]:
        self.install_file(self.files_path / f"{f}.pam", "etc/pam.d", name=f)

    for f in [
        "chpasswd",
        "chgpasswd",
        "groupadd",
        "groupdel",
        "groupmems",
        "groupmod",
        "newusers",
        "useradd",
        "userdel",
        "usermod",
    ]:
        self.install_file(self.destdir / "etc/pam.d/chage", "etc/pam.d", name=f)

    # defaults for useradd
    self.install_file(
        self.files_path / "default.useradd", "etc/default", name="useradd"
    )

    # chimerautils
    self.rm(self.destdir / "usr/bin/groups")
    self.rm(self.destdir / "usr/share/man/man1/groups.1")

    # trigger
    self.install_dir("var/lib/shadow", empty=True)

    self.install_license(self.files_path / "LICENSE")


@subpackage("shadow-devel")
def _devel(self):
    return self.default_devel()
