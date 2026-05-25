pkgname = "rsync"
pkgver = "3.4.3"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--libexecdir=/usr/libexec",  # TODO switch libexec
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
    "linux-headers",
    "lz4-devel",
    "openssl3-devel",
    "popt-devel",
    "xxhash-devel",
    "zlib-ng-compat-devel",
    "zstd-devel",
]
checkdepends = ["python"]
pkgdesc = "Fast incremental file transfer tool"
license = "GPL-3.0-only"
url = "https://rsync.samba.org"
source = f"https://www.samba.org/ftp/rsync/src/rsync-{pkgver}.tar.gz"
sha256 = "c72e63ca3021cbc80ba86ec30102773f4c5631fbc492b52e773b3958f82a53d3"
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
