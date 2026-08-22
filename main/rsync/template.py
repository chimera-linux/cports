pkgname = "rsync"
pkgver = "3.5.0"
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
checkdepends = ["bash", "python"]
pkgdesc = "Fast incremental file transfer tool"
license = "GPL-3.0-only"
url = "https://rsync.samba.org"
source = f"https://www.samba.org/ftp/rsync/src/rsync-{pkgver}.tar.gz"
sha256 = "c7ffd1ef653e99540f661e47cb00b7f9cad1ee6b972399b16f93d672656e0d33"
tool_flags = {
    # ipv6 on musl: https://bugzilla.samba.org/show_bug.cgi?id=10715
    "CFLAGS": ["-DINET6"]
}
# FIXME int: crashes in match_sums (match.c) after a while in partial mode
hardening = ["vis", "cfi", "!int"]
options = ["etcfiles"]

if self.profile().arch == "x86_64":
    configure_args += ["--enable-roll-simd"]


def post_extract(self):
    self.rm("testsuite/misc-coverage_test.py")
    self.rm("testsuite/rrsync-backup-dir-inband-pivot_test.py")
    self.rm("testsuite/rrsync-pull-delivers-content_test.py")
    self.rm("testsuite/scanner-argv-bounds_test.py")
    # chgrp/setgid fails: previously rm'd so keep up the tradition
    self.rm("testsuite/chgrp_test.py")
    self.rm("testsuite/daemon-groupmap-wild_test.py")
    self.rm("testsuite/dir-sgid_test.py")
    self.rm("testsuite/ownership-depth_test.py")
    self.rm("testsuite/protected-regular_test.py")
    self.rm("testsuite/skiplist-spec_test.py")


def post_install(self):
    self.install_file(self.files_path / "rsyncd.conf", "etc")
    self.install_file(
        self.files_path / "rsyncd.sh", "usr/lib", mode=0o755, name="rsyncd"
    )
    self.install_service(self.files_path / "rsyncd")

    self.install_bin("support/nameconvert")
    self.install_bin("support/json-rsync-version")
    self.install_bin("support/rsyncstats")
