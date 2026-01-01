pkgname = "shadow"
pkgver = "4.17.2"
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
# out of tree is broken with libsubid
make_dir = "."
makedepends = ["acl-devel", "linux-pam-devel", "linux-headers"]
depends = ["linux-pam", "base-shells"]
# self-trigger
triggers = ["/usr/share/shadow"]
pkgdesc = "Shadow password file utilities"
license = "BSD-3-Clause"
url = "https://github.com/shadow-maint/shadow"
source = f"{url}/releases/download/{pkgver}/shadow-{pkgver}.tar.xz"
sha256 = "a21cf0d34bffc4314cede01cff258689174fab30ca494ae8f45784d3d56c9849"
file_modes = {
    "usr/bin/chage": ("root", "root", 0o4755),
    "usr/bin/chfn": ("root", "root", 0o4755),
    "usr/bin/chsh": ("root", "root", 0o4755),
    "usr/bin/expiry": ("root", "root", 0o4755),
    "usr/bin/gpasswd": ("root", "root", 0o4755),
    "usr/bin/newgidmap": ("root", "root", 0o4755),
    "usr/bin/newuidmap": ("root", "root", 0o4755),
    "usr/bin/newgrp": ("root", "root", 0o4755),
    "usr/bin/passwd": ("root", "root", 0o4755),
    "usr/bin/sg": ("root", "root", 0o4755),
    "usr/bin/su": ("root", "root", 0o4755),
    "+usr/share/shadow": ("root", "root", 0o755, True),
}
hardening = ["!vis", "!cfi"]
# messes with filesystem
options = ["!check"]


def pre_install(self):
    # shadow force-installs into sbin regardless of configure
    self.install_dir("usr/bin")
    self.install_link("usr/sbin", "bin")


def post_install(self):
    self.uninstall("usr/sbin")

    # do not install pam files supplied with shadow
    self.uninstall("etc/pam.d")

    # install our own pam files
    for f in ["chage", "chfn", "chsh", "login", "su", "passwd"]:
        self.install_file(self.files_path / f"{f}.pam", "usr/lib/pam.d", name=f)

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
        self.install_file(
            self.destdir / "usr/lib/pam.d/chage", "usr/lib/pam.d", name=f
        )

    # defaults for useradd
    self.install_file(
        self.files_path / "default.useradd", "etc/default", name="useradd"
    )

    # links
    for mp in [
        "endspent",
        "fgetspent",
        "fgetspent_r",
        "getspent",
        "getspent_r",
        "getspnam_r",
        "lckpwdf",
        "putspent",
        "setspent",
        "sgetspent",
        "sgetspent_r",
        "ulckpwdf",
    ]:
        self.install_link(f"usr/share/man/man3/{mp}.3", "getspnam.3")

    self.install_license(self.files_path / "LICENSE")


@subpackage("shadow-devel")
def _(self):
    return self.default_devel()
