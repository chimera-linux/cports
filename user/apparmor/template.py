# match to libapparmor
pkgname = "apparmor"
pkgver = "5.0.2"
pkgrel = 0
build_style = "makefile"
make_env = {"USE_SYSTEM": "1"}
hostmakedepends = [
    "automake",
    "bash",
    "bison",
    "findutils",
    "flex",
    "gettext",
    "gsed",
    "libapparmor-devel",
    "linux-headers",
    "pkgconf",
    "python",
    "python-setuptools",
]
makedepends = [
    "dinit-chimera",
    "libapparmor-devel",
    "linux-headers",
    "linux-pam-devel",
    "zstd-devel",
]
depends = ["python-apparmor"]
pkgdesc = "Mandatory access control for programs"
license = "GPL-2.0-or-later"
url = "https://gitlab.com/apparmor/apparmor"
source = f"{url}/-/archive/v{pkgver}/apparmor-v{pkgver}.tar.gz"
sha256 = "bef45f228c0bde2f80d9630084e56bd8020b3fc4dfa7ee48a6aca585bb5ea0ed"
# cfi breaks apparmor_parser
hardening = ["vis", "!cfi"]
# the build system is a mess to untangle
options = ["!check", "etcfiles"]
# gsed: used to generate headers
# gfind: used to install apparmor profiles
exec_wrappers = [("/usr/bin/gsed", "sed"), ("/usr/bin/gfind", "find")]


def build(self):
    self.make.build(wrksrc="binutils")
    self.make.build(wrksrc="parser")
    self.make.build(wrksrc="profiles")
    self.make.build(wrksrc="utils")

    self.make.build(wrksrc="changehat/pam_apparmor")


def install(self):
    for proj in (
        "binutils",
        "parser",
        "profiles",
        "utils",
        "changehat/pam_apparmor",
    ):
        self.make.install(
            args=[
                f"SBINDIR=/{self.chroot_destdir}/usr/bin",
                f"USR_SBINDIR=/{self.chroot_destdir}/usr/bin",
                f"BINDIR=/{self.chroot_destdir}/usr/bin",
                f"VIM_INSTALL_PATH=/{self.chroot_destdir}/usr/share/vim/vimfiles/syntax",
                f"SECDIR=/{self.chroot_destdir}/usr/lib/security",
            ],
            wrksrc=proj,
        )

    self.install_service(self.files_path / "apparmor")
    self.install_file("init/apparmor.systemd", "usr/lib/apparmor", 0o755)
    self.install_file("init/rc.apparmor.functions", "usr/lib/apparmor", 0o755)

    # requires python tkinter
    self.uninstall("usr/bin/aa-notify")
    self.uninstall("etc/apparmor/notify.conf")


@subpackage("apparmor-extra-profiles")
def _(self):
    self.subdesc = "Extra profiles"
    return ["usr/share/apparmor/extra-profiles"]
