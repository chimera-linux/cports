pkgname = "shadow"
pkgver = "4.9"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-shared", "--disable-static", "--with-libpam", "--with-acl",
    "--with-attr", "--without-su", "--without-selinux", "--disable-nls",
    "--enable-subordinate-ids", "--disable-account-tools-setuid"
]
make_cmd = "gmake"
# out of tree is broken with libsubid
make_dir = "."
hostmakedepends = ["gmake"]
makedepends = ["acl-devel", "linux-pam-devel", "linux-headers"]
depends = ["linux-pam"]
pkgdesc = "Shadow password file utilities"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://github.com/shadow-maint/shadow"
source = f"{url}/releases/download/v{pkgver}/shadow-{pkgver}.tar.xz"
sha256 = "feec1f2ce9c1b62798afd35a7d1b04cefdfa3a0a30ff3e75d6965ba8978c9144"
suid_files = [
    "usr/bin/chage",
    "usr/bin/expiry",
    "usr/bin/gpasswd",
    "usr/bin/newgidmap",
    "usr/bin/newuidmap",
    "usr/bin/passwd",
    "usr/bin/sg",
]
# messes with filesystem
options = ["!check"]

def pre_install(self):
    # shadow force-installs into sbin regardless of configure
    self.install_dir("usr/bin")
    self.install_link("bin", "usr/sbin")

def post_install(self):
    self.rm(self.destdir / "usr/sbin", force = True)

    # do not install pam files supplied with shadow
    self.rm(self.destdir / "etc/pam.d", recursive = True, force = True)

    # install our own pam files
    for f in ["chage", "passwd"]:
        self.install_file(self.files_path / f"{f}.pam", "etc/pam.d", name = f)

    for f in [
        "chpasswd", "chgpasswd", "groupadd", "groupdel", "groupmems",
        "groupmod", "newusers", "useradd", "userdel", "usermod"
    ]:
        self.install_file(
            self.destdir / "etc/pam.d/chage", f"etc/pam.d", name = f
        )

    # default login.defs
    self.rm(self.destdir / "etc/login.defs")
    self.install_file(self.files_path / "login.defs", "etc")

    # defaults for useradd
    self.install_file(
        self.files_path / "default.useradd", "etc/default", name = "useradd"
    )

    # install daily cron job
    self.install_file(
        self.files_path / "shadow.cron-daily", "etc/cron.daily",
        name = "shadow"
    )

    # remove utilities provided by util-linux and others
    for f in [
        "groups", "sg", "login", "chsh", "chfn", "nologin", "logoutd",
        "vipw", "vigr"
    ]:
        self.rm(self.destdir / f"usr/bin/{f}")

    self.mv(self.destdir / "usr/bin/newgrp", self.destdir / "usr/bin/sg")

    for f in (self.destdir / "usr/share/man").rglob("*.[18]"):
        match f.name:
            case "chsh.1" | "chfn.1" | "login.1" | "newgrp.1" | "su.1":
                f.unlink()
            case "logoutd.8" | "nologin.8" | "vigr.8" | "vipw.8":
                f.unlink()
            case _:
                pass

    self.install_license(self.files_path / "LICENSE")
