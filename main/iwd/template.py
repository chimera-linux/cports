pkgname = "iwd"
pkgver = "2.12"
pkgrel = 1
build_style = "gnu_configure"
configure_args = [
    # junk cflags that redefine FORTIFY
    "--disable-optimization",
    "--disable-systemd-service",
    "--enable-dbus-policy",
    "--enable-wired",
    "--enable-pie",
]
make_cmd = "gmake"
make_check_wrapper = ["dbus-run-session"]
hostmakedepends = ["gmake", "pkgconf", "python-docutils", "automake", "libtool"]
# TODO: look into porting to libedit later
# iwd's usage of readline is very fucky and we don't wanna break it
makedepends = ["readline-devel", "dbus-devel", "linux-headers"]
checkdepends = ["python", "dbus"]
depends = ["dbus", "resolvconf"]
pkgdesc = "Wireless daemon that replaces wpa_supplicant"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://iwd.wiki.kernel.org"
source = f"$(KERNEL_SITE)/network/wireless/{pkgname}-{pkgver}.tar.xz"
sha256 = "6b71a78c1e1a0200c6b0097efe0f4055a76f445c0e17cdd6225d89538d7dc35e"
tool_flags = {
    "CFLAGS": ["-Wno-unknown-warning-option", "-Wno-duplicate-decl-specifier"]
}
# FIXME cfi (tests fail)
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_service(self.files_path / "iwd")
    self.install_service(self.files_path / "ead")
    self.install_file(self.files_path / "iwd.conf", "usr/lib/tmpfiles.d")

    self.install_dir("etc/iwd", empty=True)
