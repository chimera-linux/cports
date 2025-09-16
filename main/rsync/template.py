pkgname = "rsync"
pkgver = "3.4.1"
pkgrel = 0
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
    "dinit-chimera",
    "lz4-devel",
    "openssl3-devel",
    "popt-devel",
    "xxhash-devel",
    "zlib-ng-compat-devel",
    "zstd-devel",
]
pkgdesc = "Fast incremental file transfer tool"
license = "GPL-3.0-only"
url = "https://rsync.samba.org"
source = f"https://www.samba.org/ftp/rsync/src/rsync-{pkgver}.tar.gz"
sha256 = "2924bcb3a1ed8b551fc101f740b9f0fe0a202b115027647cf69850d65fd88c52"
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
