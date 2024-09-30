pkgname = "snapper"
pkgver = "0.11.2"
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
    "xsltproc",
]
makedepends = [
    "acl-devel",
    "boost-devel",
    "dbus-devel",
    "e2fsprogs-devel",
    "json-c-devel",
    "libbtrfs-devel",
    "libbtrfsutil-devel",
    "libmount-devel",
    "libxml2-devel",
    "linux-pam-devel",
    "ncurses-libtinfo-devel",
]
pkgdesc = "Filesystem snapshot manager"
maintainer = "tulilirockz <tulilirockz@outlook.com>"
license = "GPL-2.0-only"
url = "https://github.com/openSUSE/snapper"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "d2a33935f94f30b22aecbdfdecccf651b3616fa698aec266646a9d06043bfd6f"
patch_style = "patch"


def post_install(self):
    self.install_file("data/sysconfig.snapper", "etc/snapper", name="snapper")
    self.install_service(self.files_path / "snapper")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.uninstall("usr/lib/snapper/testsuite")
    self.uninstall("usr/lib/snapper/systemd-helper")


@subpackage("snapper-devel")
def _(self):
    return self.default_devel()
