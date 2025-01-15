pkgname = "rsync"
pkgver = "3.4.0"
pkgrel = 1
build_style = "gnu_configure"
configure_args = [
    "--with-rrsync",
    "--with-included-popt=no",
    "--with-included-zlib=no",
    "--disable-md2man",
]
# breaks when regened
configure_gen = []
# otherwise manpages don't get installed
make_dir = "."
hostmakedepends = ["perl"]
makedepends = [
    "acl-devel",
    "lz4-devel",
    "openssl-devel",
    "popt-devel",
    "xxhash-devel",
    "zlib-ng-compat-devel",
    "zstd-devel",
]
pkgdesc = "Fast incremental file transfer tool"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-only"
url = "https://rsync.samba.org"
source = f"https://www.samba.org/ftp/rsync/src/rsync-{pkgver}.tar.gz"
sha256 = "8e942f95a44226a012fe822faffa6c7fc38c34047add3a0c941e9bc8b8b93aa4"
# FIXME int: crashes in match_sums (match.c) after a while in partial mode
hardening = ["vis", "cfi", "!int"]

tool_flags = {
    # ipv6 on musl: https://bugzilla.samba.org/show_bug.cgi?id=10715
    "CFLAGS": ["-DINET6"]
}

if self.profile().arch == "x86_64":
    configure_args += ["--enable-roll-simd"]


def post_extract(self):
    self.rm("testsuite/chgrp.test")


def post_install(self):
    self.install_file(self.files_path / "rsyncd.conf", "etc")
    self.install_file(
        self.files_path / "rsyncd.sh", "usr/libexec", mode=0o755, name="rsyncd"
    )
    self.install_service(self.files_path / "rsyncd")

    self.install_bin("support/nameconvert")
    self.install_bin("support/json-rsync-version")
    self.install_bin("support/rsyncstats")
