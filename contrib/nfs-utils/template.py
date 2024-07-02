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
    for n in ["auth_rpcgss", "nfs-server", "proc-fs-nfsd", "rpc_pipefs"]:
        self.install_file(
            self.files_path / f"dinit-{n}", "usr/libexec", mode=0o755
        )

    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_file(self.files_path / "idmapd.conf", "etc")
    self.install_file("nfs.conf", "etc")
    self.install_files(self.files_path / "dinit.d", "etc")


@subpackage("nfs-server")
def _server(self):
    self.pkgdesc = f"{pkgdesc} (server components)"
    self.depends = [f"{pkgname}={pkgver}-r{pkgrel}"]

    return [
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


@subpackage("nfs-server-dinit")
def _server_dinit(self):
    return [
        "etc/dinit.d/fsidd",
        "etc/dinit.d/nfs-blkmap",
        "etc/dinit.d/nfs-mountd",
        "etc/dinit.d/nfs-server",
        "etc/dinit.d/nfsdcld",
        "etc/dinit.d/rpc-svcgssd",
        "usr/libexec/dinit-nfs-server",
        "usr/libexec/dinit-proc-fs-nfsd",
    ]


@subpackage("nfs-utils-devel")
def _devel(self):
    return self.default_devel()


@subpackage("nfs-utils-dinit")
def _dinit(self):
    return ["etc/dinit.d", "usr/libexec/dinit*"]


@subpackage("nfs-utils-libs")
def _lib(self):
    self.pkgdesc = f"{pkgdesc} (libraries)"

    return ["usr/lib/libnfsidmap.so.*", "usr/lib/libnfsidmap"]
