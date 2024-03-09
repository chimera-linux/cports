pkgname = "nfs-utils"
pkgver = "2.6.4"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    # TODO: probably depends on mit kerberos, and at least one of the
    # dependencies (gssproxy) absolutely needs mit kerberos
    "--disable-gss",
    # TODO: ditto
    "--disable-svcgss",
    "--disable-sbin-override",
    "--disable-static",
    "--enable-junction",
    "--enable-libmount-mount",
]
make_cmd = "gmake"
make_dir = "."
hostmakedepends = [
    "automake",
    "gmake",
    "libtool",
    "pkgconf",
    "rpcsvc-proto",
]
makedepends = [
    "device-mapper-devel",
    "keyutils-devel",
    "libcap-devel",
    "libevent-devel",
    "libmount-devel",
    "libtirpc-devel",
    "libxml2-devel",
    "linux-headers",
    "musl-bsd-headers",
    "sqlite-devel",
]
depends = ["python", "rpcbind"]
pkgdesc = "Utilities for managing NFS"
maintainer = "miko <mikoxyzzz@gmail.com>"
license = "GPL-2.0-or-later"
url = "https://linux-nfs.org"
source = f"https://cdn.kernel.org/pub/linux/utils/nfs-utils/{pkgver}/nfs-utils-{pkgver}.tar.gz"
sha256 = "e41c9ac96b15b4e8b8bde05da6e072e98bcf3acd8ae8f055e4a0bd5ac2328d4c"
# FIXME
tool_flags = {"CFLAGS": ["-Wno-format-nonliteral", "-Wno-strict-prototypes"]}
file_modes = {"usr/bin/mount.nfs": ("root", "root", 0o4755)}
# vis breaks symbols
hardening = ["!vis"]
# tests require a running nfsd
options = ["!check"]


def post_install(self):
    for n in ["nfs-server", "proc-fs-nfsd", "rpc_pipefs"]:
        self.install_file(
            self.files_path / f"dinit-{n}", "usr/libexec", mode=0o755
        )
    self.install_file(
        self.files_path / "tmpfiles.conf",
        "usr/lib/tmpfiles.d",
        name="nfs-utils.conf",
    )
    self.install_file(self.files_path / "idmapd.conf", "etc")
    self.install_file("nfs.conf", "etc")
    self.install_files(self.files_path / "dinit.d", "etc")


@subpackage("nfs-utils-dinit")
def _dinit(self):
    return ["etc/dinit.d", "usr/libexec/dinit*"]


@subpackage("libnfsidmap")
def _lib(self):
    self.pkgdesc = "Library for nfsidmap(5)"

    return ["usr/lib/libnfsidmap.so.*", "usr/lib/libnfsidmap"]


@subpackage("libnfsidmap-devel")
def _libdev(self):
    self.pkgdesc = "Library for nfsidmap(5) (development files)"

    return [
        "usr/include",
        "usr/lib/libnfsidmap.*",
        "usr/lib/pkgconfig",
    ]
