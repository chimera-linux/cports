pkgname = "iwd"
pkgver = "2.3"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--disable-systemd-service",
    "--enable-dbus-policy",
    "--enable-wired",
    "--enable-pie",
]
make_cmd = "gmake"
make_check_wrapper = ["dbus-run-session"]
hostmakedepends = ["gmake", "pkgconf", "python-docutils"]
# TODO: look into porting to libedit later
# iwd's usage of readline is very fucky and we don't wanna break it
makedepends = ["readline-devel", "dbus-devel", "linux-headers"]
checkdepends = ["python", "dbus"]
depends = ["dbus", "openresolv"]
pkgdesc = "Wireless daemon that replaces wpa_supplicant"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://iwd.wiki.kernel.org"
source = f"$(KERNEL_SITE)/network/wireless/{pkgname}-{pkgver}.tar.xz"
sha256 = "b0506d797a8bfb88f3c3eeea5e49dcf4ee8e6cef118f57c118e587eeb377ac64"
tool_flags = {"CFLAGS": [
    "-Wno-unknown-warning-option", "-Wno-duplicate-decl-specifier"
]}
# FIXME cfi (tests fail)
hardening = ["vis", "!cfi"]

def post_install(self):
    self.install_service(self.files_path / "iwd")
    self.install_service(self.files_path / "ead")

    self.install_dir("etc/iwd", empty = True)
