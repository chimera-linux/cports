pkgname = "wsdd-native"
pkgver = "1.26"
pkgrel = 0
build_style = "cmake"
configure_args = [
    # external.cmake (bundled in the prefetch tarball) sets
    # FETCHCONTENT_SOURCE_DIR_<NAME> for every dependency, bypassing
    # find_package() even where WSDDN_PREFER_SYSTEM_* is set. -U undoes
    # that override only for the deps we want resolved against the system.
    "-C",
    "../external/external.cmake",
    "-U",
    "FETCHCONTENT_SOURCE_DIR_FMT",
    "-U",
    "FETCHCONTENT_SOURCE_DIR_LIBXML2",
    "-U",
    "FETCHCONTENT_SOURCE_DIR_SPDLOG",
    "-U",
    "FETCHCONTENT_SOURCE_DIR_TOMLPLUSPLUS",
    "-DWSDDN_PREFER_SYSTEM_FMT=ON",
    "-DWSDDN_PREFER_SYSTEM_LIBXML2=ON",
    "-DWSDDN_PREFER_SYSTEM_SPDLOG=ON",
    "-DWSDDN_PREFER_SYSTEM_TOMLPLUSPLUS=ON",
    "-DWSDDN_WITH_SYSTEMD=no",
]
hostmakedepends = ["cmake", "ninja"]
makedepends = [
    "dinit-chimera",
    "fmt-devel",
    "libxml2-devel",
    "linux-headers",
    "spdlog-devel",
    "tomlplusplus-devel",
]
pkgdesc = (
    "WS-Discovery daemon to make your machine visible in Windows Network view"
)
license = "BSD-3-Clause"
url = "https://github.com/gershnik/wsdd-native"
source = (
    f"{url}/releases/download/v{pkgver}/wsddn-src-prefetch-{pkgver}.tar.bz2"
)
sha256 = "b81f28af31257488f820e6eebc312460d821350cd3dde597a89c3fef1a8cd220"


def post_install(self):
    self.install_file(
        "installers/wsddn.conf",
        "usr/share/examples/wsdd-native",
        template={
            "RELOAD_INSTRUCTIONS": "# dinitctl signal HUP wsdd-native",
            "SAMPLE_IFACE_NAME": "eth0",
        },
        pattern=r"\{(\w+)\}",
    )
    self.install_file(
        "config/firewalls/etc/ufw/applications.d/wsddn",
        "usr/lib/ufw/applications.d",
    )
    self.install_file(
        "Acknowledgements.md",
        "usr/share/doc/wsdd-native",
    )
    self.install_service(self.files_path / "wsdd-native")
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_license("LICENSE")
