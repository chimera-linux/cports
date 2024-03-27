pkgname = "libvirt"
pkgver = "10.0.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dblkid=enabled",
    "-Ddriver_secrets=enabled",
    "-Dpackager=Chimera Linux",
    "-Dstorage_dir=enabled",
    "-Dstorage_disk=enabled",
    "-Dstorage_fs=enabled",
    "-Dstorage_lvm=enabled",
    "-Dstorage_mpath=enabled",
    "-Dstorage_scsi=enabled",
    "-Dstorage_zfs=enabled",
    f"-Dpackager_version={pkgver}",
]
hostmakedepends = [
    "libxml2-progs",
    "lvm2",  # buildtime check
    "meson",
    "mkfs",  # buildtime check
    "mount",  # buildtime check
    "perl",
    "pkgconf",
    "python-docutils",
    "xsltproc",
]
makedepends = [
    "acl-devel",
    "attr-devel",
    "bash-completion",
    "device-mapper-devel",
    "fuse-devel",
    "glib-devel",
    "gnutls-devel",
    "libcap-ng-devel",
    "libcurl-devel",
    "libiscsi-devel",
    "libnl-devel",
    "libnuma-devel",
    "libpcap-devel",
    "libpciaccess-devel",
    "libsasl-devel",
    "libssh-devel",
    "libssh2-devel",
    "libtirpc-devel",
    "libxml2-devel",
    "linux-headers",
    "parted-devel",
    "polkit-devel",
    "readline-devel",
    "udev-devel",
    "yajl-devel",
]
pkgdesc = "API, daemon, and management tool for virtualization"
maintainer = "Nova <froggo8311@proton.me>"
license = "LGPL-2.1-only"
url = "https://libvirt.org"
source = f"https://download.libvirt.org/libvirt-{pkgver}.tar.xz"
sha256 = "8ba2e72ec8bdd2418554a1474c42c35704c30174b7611eaf9a16544b71bcf00a"


def post_install(self):
    self.install_service(self.files_path / "libvirtd")
    for service in [
        "ch",
        "interface",
        "lock",
        "log",
        "lxc",
        "network",
        "nodedev",
        "nwfilter",
        "proxy",
        "qemu",
        "secret",
        "storage",
        "vbox",
    ]:
        self.install_service(self.files_path / f"virt{service}d")


@subpackage("libvirt-devel")
def _devel(self):
    return self.default_devel()
