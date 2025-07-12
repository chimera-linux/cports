pkgname = "gomplate"
pkgver = "4.3.3"
pkgrel = 0
build_style = "go"
make_build_args = [
    "-ldflags",
    f"-X github.com/hairyhenderson/gomplate/v4/version.Version=v{pkgver}",
    "./cmd/gomplate",
]
# skipped tests require internet connection
make_check_args = [
    "-skip",
    "ExampleRenderer_datasources|TestDatasources_Blob_S3Datasource|TestDatasources_Blob_S3Directory|TestDatasources_Consul|TestDatasources_GitDatasource|TestDatasources_GitFileDatasource|TestDatasources_GitHTTPDatasource|TestDatasources_VaultEc2|TestDatasources_VaultIAM|TestDatasources_Vault_AppRoleAuth|TestDatasources_Vault_DynamicAuth|TestDatasources_Vault_List|TestDatasources_Vault_ListKVv2|TestDatasources_Vault_ReadKVv2|TestDatasources_Vault_TokenAuth|TestDatasources_Vault_UserPassAuth|TestInputDir_RespectsUlimit|TestLookupCNAME|TestLookupIP|TestLookupSRV|TestLookupTXT",
    "./...",
]
hostmakedepends = ["go"]
depends = ["ca-certificates"]
pkgdesc = "Template renderer with datasources"
license = "MIT"
url = "https://github.com/hairyhenderson/gomplate"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "d15c66230d72bdc13b0155f28d391c55cac45b7fdbe1ff4a73db8ee263471a3d"


def post_install(self):
    self.install_license("LICENSE")
