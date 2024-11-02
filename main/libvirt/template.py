pkgname = "libvirt"
pkgver = "10.9.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    "--libexecdir=/usr/lib",  # XXX drop libexec
    "-Dattr=enabled",
    "-Dblkid=enabled",
    "-Dcapng=enabled",
    "-Dcurl=enabled",
    "-Ddriver_qemu=enabled",
    "-Ddriver_secrets=enabled",
    "-Dfirewalld=enabled",
    "-Dfirewalld_zone=enabled",
    "-Dfuse=enabled",
    "-Djson_c=enabled",
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
    f"-Dpackager_version={pkgver}",
    "-Dqemu_user=_libvirt-qemu",
    "-Dqemu_group=_libvirt-qemu",
    "-Duserfaultfd_sysctl=disabled",
]
hostmakedepends = [
    "gettext",
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
    "json-c-devel",
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
]
checkdepends = [
    "pahole",
    "python-black",
    "python-flake8",
    "python-pytest",
]
depends = ["dinit-dbus", "dnsmasq", "virtiofsd-meta"]
pkgdesc = "API, daemon, and management tool for virtualization"
maintainer = "cesorious <cesorious@gmail.com>"
license = "LGPL-2.1-only"
url = "https://libvirt.org"
source = f"https://download.libvirt.org/libvirt-{pkgver}.tar.xz"
sha256 = "2473db10bb9b9992c02897cef4b26ae58885ff357cea5f9ce3ec9e008f6b5b3a"


def post_install(self):
    self.uninstall("usr/lib/sysusers.d/libvirt-qemu.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_sysusers(self.files_path / "sysusers.conf")

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
def _(self):
    return self.default_devel()


@subpackage("libvirt-firewalld")
def _(self):
    self.install_if = [self.parent, "firewalld"]
    self.depends = [self.parent, "iptables-nft"]
    self.subdesc = "firewalld zones and policies"
    return ["usr/lib/firewalld"]
