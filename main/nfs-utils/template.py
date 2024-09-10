pkgname = "nfs-utils"
pkgver = "2.6.4"
pkgrel = 0
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
        "cmd:nfsdcld",
        "cmd:rpc.mountd",
        "cmd:fsidd",
        "cmd:rpc.nfsd",
        "cmd:blkmapd",
        "cmd:nfsdclddb",
        "cmd:rpc.svcgssd",
        "cmd:nfsdclnts",
        "cmd:nfsref",
        "cmd:nfsdcltrack",
        "cmd:exportfs",
        "usr/libexec/dinit-nfs-server",
        "usr/libexec/dinit-proc-fs-nfsd",
        "man:exports.5",
        "man:mountd.8",
        "man:nfsd.8",
        "man:svcgssd.8",
    ]


@subpackage("nfs-utils-devel")
def _(self):
    return self.default_devel()


@subpackage("nfs-utils-libs")
def _(self):
    self.pkgdesc = f"{pkgdesc} (libraries)"

    return ["usr/lib/libnfsidmap.so.*", "usr/lib/libnfsidmap"]
