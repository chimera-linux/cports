pkgname = "snapper"
pkgver = "0.13.2"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--disable-systemd",
    "--disable-ext4",
    "--disable-bcachefs",
    "--disable-zypp",
    "--with-conf=/etc/snapper",
]
make_dir = "."
make_build_args = [
    "DOCBOOK_XSL=/usr/share/xsl-nons/docbook/manpages/docbook.xsl",
]
hostmakedepends = [
    "automake",
    "docbook-xsl-nons",
    "gettext",
    "libxslt-progs",
    "pkgconf",
    "slibtool",
]
makedepends = [
    "acl-devel",
    "boost-devel",
    "btrfs-progs-devel",
    "dbus-devel",
    "dinit-chimera",
    "json-c-devel",
    "libxml2-devel",
    "linux-pam-devel",
    "ncurses-libtinfo-devel",
    "openssl3-devel",
    "util-linux-mount-devel",
]
pkgdesc = "Filesystem snapshot manager"
license = "GPL-2.0-only"
url = "https://github.com/openSUSE/snapper"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "6cd92e2597c35801e4ad9e2b62713db42d8884ef0d9c75d522bca3fbd78b1821"
options = ["etcfiles"]


def post_install(self):
    self.install_file("data/sysconfig.snapper", "etc/snapper", name="snapper")
    self.install_service(self.files_path / "snapper")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.uninstall("usr/lib/snapper/testsuite")
    self.uninstall("usr/lib/snapper/systemd-helper")


@subpackage("snapper-devel")
def _(self):
    return self.default_devel()
