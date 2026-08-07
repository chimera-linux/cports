pkgname = "monero"
pkgver = "0.18.5.1"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DSTACK_TRACE=OFF", "-DARCH=default"]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "boost-devel",
    "dinit-chimera",
    "ldns-devel",
    "libexpat-devel",
    "libsodium-devel",
    "libzmq-devel",
    "miniupnpc-devel",
    "openssl3-devel",
    "readline-devel",
    "unbound-devel",
]
pkgdesc = "Digital currency"
license = "BSD-3-Clause"
url = "https://getmonero.org"
source = [
    f"https://github.com/monero-project/monero/archive/v{pkgver}.tar.gz",
    # these are the revisions for the tag, must be updated
    "https://github.com/tevador/RandomX/archive/6c4340ba4561aec9a3611c1aedf9931239777fb3.tar.gz",
    "https://github.com/Tencent/rapidjson/archive/129d19ba7f496df5e33658527a7158c79b99c21c.tar.gz",
    "https://github.com/monero-project/supercop/archive/633500ad8c8759995049ccd022107d1fa8a1bbc9.tar.gz",
    "https://github.com/trezor/trezor-common/archive/bff7fdfe436c727982cc553bdfb29a9021b423b0.tar.gz",
]
source_paths = [
    ".",
    "external/randomx",
    "external/rapidjson",
    "external/supercop",
    "external/trezor-common",
]
sha256 = [
    "66100f2f840052e6dca68b80df69b453ae076fac04d7cf20a471d1a2f4c4212c",
    "d98a8885968d736b36657fa5264786d4947c3fcf433c873802678527e6db3584",
    "44b007d419ac21b6affec58991e865ee572346ead19b73cf1c3e4e11c7a81273",
    "b973b9d8269ec4d97c3c3443f0dad96d09f72b1b30e616e0947557adbdbb03f7",
    "951f4df9dfb2466698e0b0a1b52ec27e4d6f13538ff22f1d6c0ae87f9d07c1b6",
]
# needs some manual setup
options = ["etcfiles", "!cross"]


def post_install(self):
    self.install_license("LICENSE")
    self.install_file("utils/conf/monerod.conf", "etc")
    self.install_service(self.files_path / "monerod")
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")


@subpackage("monero-devel")
def _(self):
    self.depends += [self.parent]

    return self.default_devel()
