pkgname = "rsync"
pkgver = "3.2.7"
pkgrel = 2
build_style = "gnu_configure"
configure_args = ["--with-rrsync", "--with-included-zlib=no"]
hostmakedepends = ["perl", "python-commonmark"]
makedepends = [
    "zlib-devel",
    "acl-devel",
    "popt-devel",
    "xxhash-devel",
    "lz4-devel",
    "zstd-devel",
    "openssl-devel",
]
pkgdesc = "Fast incremental file transfer tool"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-only"
url = "https://rsync.samba.org"
source = f"https://www.samba.org/ftp/rsync/src/rsync-{pkgver}.tar.gz"
sha256 = "4e7d9d3f6ed10878c58c5fb724a67dacf4b6aac7340b13e488fb2dc41346f2bb"
# FIXME int: crashes in match_sums (match.c) after a while in partial mode
hardening = ["vis", "cfi", "!int"]

tool_flags = {
    # ipv6 on musl: https://bugzilla.samba.org/show_bug.cgi?id=10715
    "CFLAGS": ["-DINET6"]
}


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


configure_gen = []
