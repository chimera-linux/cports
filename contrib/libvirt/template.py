pkgname = "libvirt"
pkgver = "10.3.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dattr=enabled",
    "-Dblkid=enabled",
    "-Dcapng=enabled",
    "-Dcurl=enabled",
    "-Ddriver_qemu=enabled",
    "-Ddriver_secrets=enabled",
    "-Dfirewalld=enabled",
    "-Dfirewalld_zone=enabled",
    "-Dfuse=enabled",
    "-Dlibiscsi=enabled",
    "-Dlibnl=enabled",
    "-Dlibssh2=enabled",
    "-Dno_git=true",
    "-Dnumactl=enabled",
    "-Dpackager=Chimera Linux",
    "-Dpciaccess=enabled",
    "-Dstorage_dir=enabled",
    "-Dstorage_disk=enabled",
    "-Dstorage_fs=enabled",
    "-Dstorage_lvm=enabled",
    "-Dstorage_mpath=enabled",
    "-Dstorage_scsi=enabled",
    "-Dstorage_zfs=enabled",
    "-Dudev=enabled",
    "-Dyajl=enabled",
    f"-Dpackager_version={pkgver}",
    "-Dqemu_user=_libvirt-qemu",
    "-Dqemu_group=_libvirt-qemu",
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
checkdepends = [
    "pahole",
    "python-black",
    "python-flake8",
    "python-pytest",
]
depends = [
    "dnsmasq",
]
pkgdesc = "API, daemon, and management tool for virtualization"
maintainer = "cesorious <cesorious@gmail.com>"
license = "LGPL-2.1-only"
url = "https://libvirt.org"
source = f"https://download.libvirt.org/libvirt-{pkgver}.tar.xz"
sha256 = "2af5a50b6b1027822b6344e35080fa78cc8266f821a3ae6f8f372f18dd049018"


def post_install(self):
    self.rm(self.destdir / "usr/lib/sysusers.d/libvirt-qemu.conf")
    self.rm(self.destdir / "usr/lib/sysctl.d/60-qemu-postcopy-migration.conf")
    self.install_file(
        self.files_path / "sysusers.conf",
        "usr/lib/sysusers.d",
        name="libvirt.conf",
    )

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


@subpackage("libvirt-firewalld")
def _firewalld(self):
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}", "firewalld"]
    self.depends = ["iptables-nft"]
    self.pkgdesc = f"{pkgdesc} (firewalld zones and policies)"
    return ["usr/lib/firewalld"]
