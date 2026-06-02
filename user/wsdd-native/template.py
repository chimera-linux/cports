pkgname = "wsdd-native"
pkgver = "1.24"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DWSDDN_PREFER_SYSTEM_FMT=ON",
    "-DWSDDN_PREFER_SYSTEM_LIBXML2=ON",
    "-DWSDDN_PREFER_SYSTEM_SPDLOG=ON",
    "-DWSDDN_PREFER_SYSTEM_TOMLPLUSPLUS=ON",
    "-DWSDDN_WITH_SYSTEMD=no",
]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = [
    "dinit-chimera",
    "fmt-devel",
    "libxml2-devel",
    "linux-headers",
    "spdlog-devel",
    "tomlplusplus-devel",
]
pkgdesc = "WS-Discovery daemon to make Linux visible in Windows Network view"
license = "BSD-3-Clause"
url = "https://github.com/gershnik/wsdd-native"
source = [
    f"{url}/archive/refs/tags/v{pkgver}.tar.gz",
    "https://github.com/gershnik/argum/tarball/v2.9>argum-2.9.tar.gz",
    "https://github.com/gershnik/sys_string/tarball/v2.23>sys_string-2.23.tar.gz",
    "https://github.com/gershnik/intrusive_shared_ptr/tarball/v1.9>isptr-1.9.tar.gz",
    "https://github.com/gershnik/ptl/tarball/v1.7>ptl-1.7.tar.gz",
    "https://github.com/gershnik/modern-uuid/tarball/v2.2>modern-uuid-2.2.tar.gz",
    "https://github.com/ned14/outcome/tarball/v2.2.15>outcome-2.2.15.tar.gz",
    "https://downloads.sourceforge.net/asio/asio-1.36.0.tar.gz",
]
source_paths = [
    ".",
    "build/_deps/argum-src",
    "build/_deps/sys_string-src",
    "build/_deps/isptr-src",
    "build/_deps/ptl-src",
    "build/_deps/modern-uuid-src",
    "build/_deps/outcome-src",
    "build/_deps/asio-src",
]
sha256 = [
    "b1f6adb7086f2f7ce3199a1b80cd7091159b6f7e6a66266484efcd50aadcc4bb",
    "f1881d1195864475da3ed8a388b8c077bf1406b4fe788047432b63bc6c259812",
    "da94ef50659c01bc2fbc66599d9fdee9c0a0aaddcb1e6ee315f4a42ae660859c",
    "f9095609a2226f3aa6dbfcd4726a8521a56f4fd2f426b0898d92acd1f133aa6d",
    "e3efb37f71846ba7d10165bef7f62a581dd3e7c8f4ac185bb86d4069bc4ec9ed",
    "dcbf6d135957d43f304fc8f739911f9db7a31c150558ce45710031e2b3130ed3",
    "9461c08df6cfd7b887f1390df2f36db4aac196590191a24485df60778fdccfc5",
    "55d5c64e78b1bedd0004423e695c2cfc191fc71914eaaa7f042329ff99ee6155",
]


def post_install(self):
    self.install_file("installers/wsddn.conf", "usr/share/etc")
    conf = self.destdir / "usr/share/etc/wsddn.conf"
    conf.write_text(
        conf.read_text()
        .replace("{RELOAD_INSTRUCTIONS}", "# dinitctl restart wsdd-native")
        .replace("{SAMPLE_IFACE_NAME}", "eth0")
    )
    self.install_file(
        "config/firewalls/etc/ufw/applications.d/wsddn",
        "usr/lib/ufw/applications.d",
    )
    self.install_service(self.files_path / "wsdd-native")
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_license("LICENSE")
