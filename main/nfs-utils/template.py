pkgname = "nfs-utils"
pkgver = "2.6.4"
pkgrel = 1
build_style = "gnu_configure"
configure_args = [
    "--disable-sbin-override",
    "--disable-static",
    "--enable-junction",
    "--enable-libmount-mount",
    "--enable-svcgss",
]
make_dir = "."
hostmakedepends = [
    "automake",
    "libtool",
    "pkgconf",
    "rpcsvc-proto",
]
makedepends = [
    "device-mapper-devel",
    "heimdal-devel",
    "heimdal-devel-static",
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
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://linux-nfs.org"
source = f"https://cdn.kernel.org/pub/linux/utils/nfs-utils/{pkgver}/nfs-utils-{pkgver}.tar.gz"
sha256 = "e41c9ac96b15b4e8b8bde05da6e072e98bcf3acd8ae8f055e4a0bd5ac2328d4c"
# FIXME
tool_flags = {"CFLAGS": ["-Wno-format-nonliteral", "-Wno-strict-prototypes"]}
file_modes = {"usr/bin/mount.nfs": ("root", "root", 0o4755)}
# tests require a running nfsd
options = ["!check"]


def post_install(self):
    # helpers
    for n in ["nfs-server", "proc-fs-nfsd", "rpc_pipefs"]:
        self.install_file(
            self.files_path / f"dinit-{n}", "usr/libexec", mode=0o755
        )
    # services
    for srv in [
        "blkmapd",
        "fsidd",
        "nfs-proc-nfsd",
        "nfs-rpc_pipefs",
        "nfs-server",
        "nfsdcld",
        "rpc.gssd",
        "rpc.idmapd",
        "rpc.mountd",
        "rpc.svcgssd",
        "rpc.statd",
    ]:
        self.install_service(self.files_path / srv)

    # managed by tmpfiles
    self.uninstall("var/lib/nfs")

    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_file(self.files_path / "idmapd.conf", "etc")
    self.install_file("nfs.conf", "etc")


@subpackage("nfs-server")
def _(self):
    self.pkgdesc = f"{pkgdesc} (server components)"
    self.depends = [self.parent]

    return [
        "etc/dinit.d/fsidd",
        "etc/dinit.d/blkmapd",
        "etc/dinit.d/nfs-server",
        "etc/dinit.d/nfsdcld",
        "etc/dinit.d/rpc.mountd",
        "etc/dinit.d/rpc.svcgssd",
        "usr/bin/nfsdcld",
        "usr/bin/rpc.mountd",
        "usr/bin/fsidd",
        "usr/bin/rpc.nfsd",
        "usr/bin/blkmapd",
        "usr/bin/nfsdclddb",
        "usr/bin/rpc.svcgssd",
        "usr/bin/nfsdclnts",
        "usr/bin/nfsref",
        "usr/bin/nfsdcltrack",
        "usr/bin/exportfs",
        "usr/libexec/dinit-nfs-server",
        "usr/libexec/dinit-proc-fs-nfsd",
        "usr/share/man/man5/exports.5",
        "usr/share/man/man8/nfsdcld.8",
        "usr/share/man/man8/*mountd.8",
        "usr/share/man/man8/*nfsd.8",
        "usr/share/man/man8/blkmapd.8",
        "usr/share/man/man8/nfsdclddb.8",
        "usr/share/man/man8/*svcgssd.8",
        "usr/share/man/man8/nfsdclnts.8",
        "usr/share/man/man8/nfsref.8",
        "usr/share/man/man8/nfsdcltrack.8",
        "usr/share/man/man8/exportfs.8",
    ]


@subpackage("nfs-utils-devel")
def _(self):
    return self.default_devel()


@subpackage("nfs-utils-libs")
def _(self):
    self.pkgdesc = f"{pkgdesc} (libraries)"

    return ["usr/lib/libnfsidmap.so.*", "usr/lib/libnfsidmap"]
