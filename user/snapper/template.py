pkgname = "snapper"
pkgver = "0.12.1"
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
    "pkgconf",
    "slibtool",
    "libxslt-progs",
]
makedepends = [
    "acl-devel",
    "boost-devel",
    "btrfs-progs-devel",
    "dbus-devel",
    "e2fsprogs-devel",
    "json-c-devel",
    "libxml2-devel",
    "linux-pam-devel",
    "ncurses-libtinfo-devel",
    "util-linux-mount-devel",
]
pkgdesc = "Filesystem snapshot manager"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-2.0-only"
url = "https://github.com/openSUSE/snapper"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "eec9de03c8c224ac06e0b2970fde4c37cf89f848b4b49c904e8ee00bb7c3aff3"


def post_install(self):
    self.install_file("data/sysconfig.snapper", "etc/snapper", name="snapper")
    self.install_service(self.files_path / "snapper")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.uninstall("usr/lib/snapper/testsuite")
    self.uninstall("usr/lib/snapper/systemd-helper")


@subpackage("snapper-devel")
def _(self):
    return self.default_devel()
