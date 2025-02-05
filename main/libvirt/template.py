pkgname = "libvirt"
pkgver = "11.0.0"
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
    "perl",
    "pkgconf",
    "python-docutils",
    "util-linux-mkfs",  # buildtime check
    "util-linux-mount",  # buildtime check
    "libxslt-progs",
]
makedepends = [
    "acl-devel",
    "attr-devel",
    "bash-completion",
    "fuse-devel",
    "glib-devel",
    "gnutls-devel",
    "json-c-devel",
    "libcap-ng-devel",
    "curl-devel",
    "libiscsi-devel",
    "libnl-devel",
    "libpcap-devel",
    "libpciaccess-devel",
    "libsasl-devel",
    "libssh-devel",
    "libssh2-devel",
    "libtirpc-devel",
    "libxml2-devel",
    "linux-headers",
    "lvm2-devel",
    "numactl-devel",
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
depends = ["dinit-dbus", "dnsmasq"]
pkgdesc = "API, daemon, and management tool for virtualization"
maintainer = "cesorious <cesorious@gmail.com>"
license = "LGPL-2.1-only"
url = "https://libvirt.org"
source = f"https://download.libvirt.org/libvirt-{pkgver}.tar.xz"
sha256 = "01a176ff4042ad58cf83c09fe0925d6bc8eed0ecce1e0ee19b8ef4c1ffa3806e"

if self.profile().wordsize != 32:
    depends += ["virtiofsd-meta"]


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
