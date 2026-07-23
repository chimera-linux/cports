pkgname = "rspamd"
pkgver = "4.1.2"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DCONFDIR=/etc/rspamd",
    "-DENABLE_URI_INCLUDE=ON",
    "-DRSPAMD_GROUP=_rspamd",
    "-DRSPAMD_USER=_rspamd",
    "-DSYSTEM_XXHASH=ON",
    "-DSYSTEM_ZSTD=ON",
    "-D_CAN_RUN=0",
    "-DHAVE_BUILTIN_CPU_SUPPORTS_EXITCODE=0",
    "-DHAVE_ATOMIC_BUILTINS_EXITCODE=0",
]
make_build_args = ["--target", "all", "check"]
make_check_target = "run-test"
hostmakedepends = ["cmake", "ninja", "perl", "pkgconf", "ragel"]
makedepends = [
    "dinit-chimera",
    "elfutils-devel",
    "fmt-devel",
    "glib-devel",
    "hiredis-devel",
    "icu-devel",
    "libarchive-devel",
    "libsodium-devel",
    "libunwind-devel",
    "linux-headers",
    "openssl3-devel",
    "pcre2-devel",
    "snowball-devel",
    "sqlite-devel",
    "xxhash-devel",
    "zstd-devel",
]
pkgdesc = "Spam filtering system"
license = "Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND BSL-1.0 AND CC0-1.0 AND LGPL-3.0-only AND MIT AND Zlib"
url = "https://rspamd.com"
source = f"https://github.com/rspamd/rspamd/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "f0a4cf9f036cb3bbef495f4eb50fe54ee1c1599f58896a1b6a727ec8d63b52ef"
# check may be disabled
options = ["etcfiles"]

match self.profile().arch:
    case "aarch64" | "ppc64le" | "x86_64":
        configure_args += ["-DENABLE_HYPERSCAN=ON"]
        makedepends += ["luajit-devel", "vectorscan-devel"]
    case _:
        configure_args += ["-DENABLE_LUAJIT=OFF"]
        makedepends += ["lua5.4-devel"]
        # needs cffi-lua
        options += ["!check"]


def post_patch(self):
    self.rm("contrib/hiredis", recursive=True)
    self.rm("contrib/fmt", recursive=True)
    self.mkdir("contrib/fmt/include", parents=True)
    self.ln_s(
        self.profile().sysroot / "usr/include/fmt", "contrib/fmt/include/fmt"
    )


def post_install(self):
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_service(self.files_path / "rspamd")
    self.install_license("LICENSE.md")
