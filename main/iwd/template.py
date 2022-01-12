pkgname = "iwd"
pkgver = "1.19"
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
depends = ["dbus"]
pkgdesc = "Wireless daemon that replaces wpa_supplicant"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://iwd.wiki.kernel.org"
source = f"$(KERNEL_SITE)/network/wireless/{pkgname}-{pkgver}.tar.xz"
sha256 = "dd65a8795f6127fb1b9e29f2092686b0590a0d3738c2b90c792ccd320deaf966"
tool_flags = {"CFLAGS": [
    "-Wno-unknown-warning-option", "-Wno-duplicate-decl-specifier"
]}

def post_install(self):
    self.install_service(self.files_path / "iwd")
    self.install_service(self.files_path / "ead")

    self.install_dir("etc/iwd")
    (self.destdir / "etc/iwd/.empty").touch(mode = 0o644)
